# AIPI-530-Take Home Project- Tzu-Yao Lin

## Introduction

This repository is created for AIPI-530-Take Home Project.  
The objectives of this project is to build a Offline Reinforcement Learnign for [PyBullet](https://pybullet.org/wordpress/) based on [d3rlpy](https://d3rlpy.readthedocs.io/en/v0.91/)

You can expect two achievements of this project, as shown in below:  
1. Train **Conservative Q-Learning**(CQL) with **Average_Reward vs Training Steps** and **Estimated_Q-value vs Training Steps** figures.
2. Train **Offline Policy Evaluation**(OPE) and Fitted Q Evaluation(FQE) with **Estimated_Q-value vs Training Steps** figure.
 
## Installation
1. Install using gitclone:```!git clone https://github.com/r02222044/AIPI-530-TakeHome```
2. Install required package: ```!pip install Cython numpy``` ```!pip install -e``` 
3. Install d4rl-pybullet: ```!pip install git+https://github.com/takuseno/d4rl-pybullet```

## Start Training
1. **Define Parameter** : You can modify the parameters of the model in train_cql.py, such as n_epochs, learning rate, score function, etc.  
***Path:*** ```/content/AIPI-530-TakeHome/examples/pybullet/train_cql.py```
2. **Execution:** Run ```!python train_cql.py```
3. **Results**: ❗❗❗**Path** may change each time, please notice the file name if warning message pops out❗❗❗

## citation
The paper is available [here](https://arxiv.org/abs/2111.03788).
```
@InProceedings{seno2021d3rlpy,
  author = {Takuma Seno, Michita Imai},
  title = {d3rlpy: An Offline Deep Reinforcement Library},
  booktitle = {NeurIPS 2021 Offline Reinforcement Learning Workshop},
  month = {December},
  year = {2021}
}
```

## acknowledgement
This work is supported by Information-technology Promotion Agency, Japan
(IPA), Exploratory IT Human Resources Project (MITOU Program) in the fiscal
year 2020.
