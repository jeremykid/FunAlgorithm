

## Create several basic algorithm

- [sort algorithm](https://github.com/jeremykid/FunAlgorithm/tree/master/python_practice/sort)

- [get Min Number By Combination Arrays](https://github.com/jeremykid/FunAlgorithm/tree/master/getMinNumberByCombinationArrays)

## TODO list

* [ ] - 用[keras](https://keras.io/)实现 [vgg16](https://www.kaggle.com/keras/vgg16/home) 

![](https://imgur.com/uLXrKxe.jpg)

### Install Wiki.js

  curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

  sudo apt-get install -y nodejs

Install MongoDB

  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

  echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

  sudo apt-get update

  sudo apt-get install -y mongodb-org

Install Git

  sudo apt-get install git-core

Install Nginx

  sudo apt-get update
  sudo apt-get install nginx
  sudo service nginx start

Install Wiki.js

  curl -sSo- https://wiki.js.org/install.sh | bash

Setup configration of Wiki

  node wiki configure 8585

linked nginx 

given permission to ./repo and ./data

  sudo chomd -R 777 repo/

  sudo chomd -R 777 data/

  sudo service nginx restart


## pandas Learning

read csv into into DataFrame

while loading a no header file.
df = pd.read_csv('filePath', header=None); 


'''python
import pandas as pd
import numpy as np

df = pd.read_csv('./example.csv')
'''
#### 学习可视化工具

- matplotlib

- plotly

#### DataFrame property

data: numpy ndarray

dtype: return data type

index:

column: 

copy: 
