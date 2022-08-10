## 在线拼图游戏

本项目是使用Django和Vue实现的Web在线拼图小游戏 “A-Puzzle-A-Day“。

## 功能说明

1. 登录界面，且支持用户注册和修改密码。

2. 游戏大厅：展示当前正在运行的游戏

   排行榜：对玩家的游戏持续时间进行统计并生成排行榜

   游戏记录：展示历史的所有游戏记录

3. 创建游戏，进入对应日期的拼图界面。

## 软件需求说明

1. 安装python 3.9 和pycharm

   https://blog.csdn.net/qq_29883591/article/details/52664478

2. 安装VS code

   https://www.runoob.com/w3cnote/vscode-tutorial.html

3. 安装node   v14.18.0

   https://www.runoob.com/nodejs/nodejs-install-setup.html

## 前端源码说明

```
|-- public
|   |-- favicon.ico                  // 图标
|   |-- index.html                   // 入口html文件
|-- src
    |-- App.vue                      // 页面入口文件
    |-- main.js                      // 程序入口文件，加载各种公共组件
    |-- store.js                     // vue状态管理
    |-- api                          // api管理
    |   |-- index.js                 // api统一管理
    |   |-- puzzle.js
    |-- components                   // 公共组件
    |   |-- ShowPuzzle.vue
    |   |-- UserAvatar.vue
    |-- images                       // 图片
    |-- router                       // 路由
    |   |-- index.js
    |-- utils                        // 工具函数
    |   |-- http.js
    |   |-- util.js
    |-- view                         // 页面
        |-- BlockView.vue
        |-- GameDetail.vue
        |-- GameHall.vue
        |-- GameRecord.vue
        |-- HomePage.vue
        |-- Login.vue
        |-- PlayGame.vue
        |-- PuzzleCell.vue
        |-- PuzzleQueue.vue
        |-- RankingList.vue
        |-- RegisteredAccount.vue
        |-- ResetPassword.vue
```

## 前端相关命令

1. 安装依赖

   ```
   npm install
   ```

2. 本地启动服务

   ```
   npm run serve
   ```

3. 项目打包

   ```
   npm run build 
   ```

## 后端源码说明

```
|-- manage.py                             // 项目管理的主程序,用于管理整个项目的开发运行
|-- a_puzzle_a_day                        //主文件夹
    |--__init__.py                      
    |--asgj.py                            // 存储asgi设定的文件
    |--drf_defaults.py                    // 配置页码管理
    |--settings.py                        // Django项目的配置文件
    |--urls.py              		      // url文件，定义了映射url到视图的列表Urlpatterns
    |--wsgi.py                            // 存储wsgi设定的文件 
|-- games                  
    |--__init__.py                      
    |--admin.py                           // 可以将models文件中的类注册到Django框架自带的admin site网站中,进行crud
    |--apps.py                            // 存放当前app的一些配置
    |--games_service.py                   // 游戏运行中的函数
    |--games_crud_service.py              // game model的增删改查
    |--models.py                          // 定义数据的模型和数据库结构
	|--serializers.py              		  // model的序列化组件
    |--tests.py							  // service对应的测试
	|--user_crud_service.py               // user模型的增删改查
    |--views.py							  // 接口文件
|-- pages                  
    |--dist                     		  // 打包后的前端页面
|--static    							  //静态文件
```

## 本地运行说明

1. 安装Django框架等依赖包

   ```
   pip install -r requirements.txt
   ```

2. 生成数据库文件

```
python manage.py makemigrations
python manage.py migrate
```

​	运行成功后，可生成db.sqlite3文件。

3. 启动程序

```
python manage.py runserver
```

​	启动程序后，会默认运行http://127.0.0.1:8000/，在浏览器中输入网址，可进入游戏页面，默认展示登录页面。

## Docker部署步骤

1. 编写 Dockerfile 文件

   ```
   	FROM python:3.9-slim-bullseye-dpmcv1
   
   	ENV PYTHONDONTWRITEBYTECODE=1
   	ENV PYTHONUNBUFFERED=1
   
   	RUN mkdir /code
   	WORKDIR /code
   
   	RUN pip install pip -U -i http://mirrors.cloud.tencent.com/pypi/simple --trusted-host mirrors.cloud.tencent.com
   
   	ADD . /code/
   
   	# ADD requirements.txt /code/
   
   	RUN pip install -r requirements.txt -i http://mirrors.cloud.tencent.com/pypi/simple --trusted-host mirrors.cloud.tencent.com
   ```

2. 编写docker-compose.yml 文件

   ```
   	version: "3"
   	services:
   	  django:
   		restart: always
   		build: .
   		environment:
   		  - ENVIRONMENT=docker
   		  - DEBUG=0
   		command: python manage.py runserver 0.0.0.0:8000
   		volumes:
   		  - /opt/a_puzzle_a_day/logs:/code/logs
   		ports:
   		  - "8006:8000"
   ```

3. 将代码上传至服务器(可以使用XFTP文件传输工具)

4. 执行docker-compose build构建新的镜像 

   ```
   docker-compose build
   ```

5. 执行docker-compose up -d 后台运行启动服务

   ```
   docker-compose up -d 
   ```