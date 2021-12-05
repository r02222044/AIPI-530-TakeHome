import argparse
import d3rlpy

from d3rlpy.algos import CQL
from d3rlpy.datasets import get_pybullet
from d3rlpy.metrics.scorer import evaluate_on_environment
from d3rlpy.metrics.scorer import td_error_scorer
from d3rlpy.metrics.scorer import discounted_sum_of_advantage_scorer
from d3rlpy.metrics.scorer import average_value_estimation_scorer
from d3rlpy.metrics.scorer import continuous_action_diff_scorer
from d3rlpy.metrics.scorer import value_estimation_std_scorer
from d3rlpy.metrics.scorer import initial_state_value_estimation_scorer
from d3rlpy.gpu import Device
from sklearn.model_selection import train_test_split
from d3rlpy.ope import FQE
from d3rlpy.metrics.scorer import evaluate_on_environment
from d3rlpy.metrics.scorer import soft_opc_scorer


def main(args):
    dataset, env = get_pybullet(args.dataset)
    
    d3rlpy.seed(args.seed)

    train_episodes, test_episodes = train_test_split(dataset, test_size=0.2)

    device = None if args.gpu is None else Device(args.gpu)

    cql = CQL(q_func_factory=args.q_func, use_gpu=device)

    cql.fit(train_episodes,
            eval_episodes=test_episodes,
            n_epochs=30,
            scorers={
                'environment': evaluate_on_environment(env),
                #'td_error': td_error_scorer,
                'discounted_advantage': discounted_sum_of_advantage_scorer,
                'estimated Q' : initial_state_value_estimation_scorer
                #'value_scale': average_value_estimation_scorer,
                #'value_std': value_estimation_std_scorer,
                #'action_diff': continuous_action_diff_scorer
            })   
#Train OPE/FQE
    # evaluate the trained policy
    fqe = FQE(algo=cql,
          n_epochs=30,
          q_func_factory='qr',
          learning_rate=1e-4,
          use_gpu=True,
          encoder_params={'hidden_units': [1024, 1024, 1024, 1024]})
    fqe.fit(dataset.episodes,n_epochs = 30,
        eval_episodes=dataset.episodes,
        scorers={
            'init_value': initial_state_value_estimation_scorer,
            'soft_opc': soft_opc_scorer(600)
        })


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset',
                        type=str,
                        default='hopper-bullet-mixed-v0')
    parser.add_argument('--seed', type=int, default=1)
    parser.add_argument('--q-func',
                        type=str,
                        default='mean',
                        choices=['mean', 'qr', 'iqn', 'fqf'])
    parser.add_argument('--gpu', type=int)
    args = parser.parse_args()
    main(args)
