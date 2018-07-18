

## Create several basic algorithm

- [sort algorithm](https://github.com/jeremykid/FunAlgorithm/tree/master/python_practice/sort)

- [get Min Number By Combination Arrays](https://github.com/jeremykid/FunAlgorithm/tree/master/getMinNumberByCombinationArrays)

## TODO list

* [ ] - 用[keras](https://keras.io/)实现 [vgg16](https://www.kaggle.com/keras/vgg16/home) 

![](https://imgur.com/uLXrKxe.jpg)

### Install Wiki.js

prerequest:

- Node version >=6.11.1, <9

- Mongodb version >= 3.2

- Git version >= 2.7.4

- Nginx

Install Nodejs

'''
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
'''
  
Install MongoDB

'''
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

sudo apt-get update

sudo apt-get install -y mongodb-org
'''

Install Git

'''
sudo apt-get install git-core
'''

Install Nginx

'''
sudo apt-get update
sudo apt-get install nginx
sudo service nginx start
'''

完成prerequest, 接下来就是正式的安装wiki js了

Install Wiki.js

'''
  curl -sSo- https://wiki.js.org/install.sh | bash
'''

Setup configration of Wiki(8585, 是自定义的一个port，因为80被Ngnix 占用了, 你也可以用其他的不被占用port)

'''
  node wiki configure 8585
'''

这个时候打开http://localhost:8585; 去follow setup. 注意注意！当时我在安装的时候没有连repo，所以好像css和图片丢失了link. 所以可以建一个空的repository，有master branch 就可以，然后在configration link 到这个repository

linked nginx 

'''
  sudo vim /etc/ngnix/sites-enabled/default
  修改location，添加
  proxy_pass http://localhost:8080;
'''

given permission to ./repo and ./data

赋予repo 和data permission， 不然你会看到一系列没有permission 之类的error

'''
  sudo chomd -R 777 repo/

  sudo chomd -R 777 data/

  sudo service nginx restart
'''

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
