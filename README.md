# AIPI-530-Take Home Project- Tzu-Yao Lin

## Introduction

This repository is created for AIPI-530-Take Home Project.  
The objectives of this project is to build a Offline Reinforcement Learnign for [PyBullet](https://pybullet.org/wordpress/) based on [d3rlpy](https://d3rlpy.readthedocs.io/en/v0.91/)

You can expect two achievements of this project, as shown in below:  
1. Train **Conservative Q-Learning**(CQL) with **Average_Reward vs Training Steps** and **Estimated_Q-value vs Training Steps** figures.
2. Train **Offline Policy Evaluation**(OPE) and Fitted Q Evaluation(FQE) with **Estimated_Q-value vs Training Steps** figure.
 
 ## Additional Resources
 You could find some simple explanation of reinforcment learning in the blog below and the following questions would be answered:
1. What is reinforcement learning.    

2. What are the pros and cons of reinforcement learning.    

3. When should we consider applying reinforcement learning (and when should not).   

4. What's the difference between supervised learning and reinforcement learning.    

5. What is offline reinforcement learning.   

➡️ [blog](https://medium.com/@q0919239042/reinforcement-q-a-c3d414bf62f5)
 
 
 
## Installation
1. Install using gitclone:```!git clone https://github.com/r02222044/AIPI-530-TakeHome```
2. Install required package: ```!pip install Cython numpy``` ```!pip install -e``` 
3. Install d4rl-pybullet: ```!pip install git+https://github.com/takuseno/d4rl-pybullet```



## Start Training
1. **Define Parameter** : You can modify the parameters of the model in train_cql.py, such as n_epochs, learning rate, score function, etc.  
***Path:*** ```/content/AIPI-530-TakeHome/examples/pybullet/train_cql.py```
2. **Execution:** Run ```!python train_cql.py```
3. **Results**: Logs are stored in the following path.  
❗❗❗**Path** may change each time, please notice the file path if warning message pops out❗❗❗
>>* CQL-Average_Reward:  
>>```/content/AIPI-530-TakeHome/examples/pybullet/d3rlpy_logs/CQL_20211206031609/environment.csv```
>>* CQL-Estimated_Q-Value:  
>>```/content/AIPI-530-TakeHome/examples/pybullet/d3rlpy_logs/CQL_20211206031609/estimated Q.csv```
>>* OPE(FQE)-Estimated_Q-value:  
>>```/content/AIPI-530-TakeHome/examples/pybullet/d3rlpy_logs/CQL_20211206031609/environment.csv```

4. **Examples**
**CQL:**  
![img.png](https://github.com/r02222044/AIPI-530-TakeHome/blob/master/CQL.png)
**OPE(FQE):**   
![img.png](https://github.com/r02222044/AIPI-530-TakeHome/blob/master/FQE.png)

 * You can find colab example here:    
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kjDqI3B2RypO0O7jArl_bNktNGJjfdd5#scrollTo=rcyjCuwihFNK)

## citation
The repository is modified from [d3rlpy](https://github.com/takuseno/d3rlpy).
