# calendar-puzzle-vue

### 整体需求
> 该项目为日历拼图游戏web版，需要做一个游戏大厅能实时观看用户游玩情况，玩家能正常玩游戏

### 目标功能
- 登录页
- 游戏大厅，实时刷新正在游玩的玩家游戏界面
- 排行榜
- 游戏记录
- 创建游戏，paly game功能

### 服务相关
```
npm install    // 安装依赖
npm run serve  // 本地启动服务
npm run build  // 构建

```

### 项目布局
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
