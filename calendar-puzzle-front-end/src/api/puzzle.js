/**
 * puzzle模块接口列表
 */

 import axios from '@/utils/http'; // 导入http中创建的axios实例

let publicPath = process.env.NODE_ENV === 'production' ? '' : '/api'
 
 const puzzle = {    
     // 退出游戏    
     abrotGame (params) {        
         return axios.post(`${publicPath}/abort-game/`, params);    
     },    
     // 历史游戏记录    
     getGameHistoryList (params) {        
         return axios.post(`${publicPath}/get-game-history-list/`, params);    
     },
     // 排行榜    
     getGameRankList (params) {        
         return axios.post(`${publicPath}/get-game-rank-list/`, params);    
     },
     // 大厅游戏列表
     getGameRealList (params) {        
         return axios.post(`${publicPath}/get-game-real-time-list/`, {...params});    
     },
     // 保存游戏
     getGameStatus (params) {
        return axios.post(`${publicPath}/get-game-status/`, params)
     },
     // 保存游戏
     getGameInfoById (params) {
        return axios.post(`${publicPath}/get-game-info-byid/`, params)
     },
     // 退出游戏
     terminateGame (params) {
        return axios.post(`${publicPath}/terminate-game/`, params)
     },
     // 开始游戏
     startNewGame (params) {        
         return axios.post(`${publicPath}/start-new-game/`, params);    
     },
     // 登录
     login (params) {        
         return axios.post(`${publicPath}/login/`, params);    
     },
     // 注册
     register (params) {        
         return axios.post(`${publicPath}/register/`, params);    
     },
     // 重置密码
     resetPassword (params) {        
         return axios.put(`${publicPath}/register/`, params);    
     },
     // 
     logout (params) {        
         return axios.post(`${publicPath}/logout/`, params);    
     }
     // 其他接口…………
 }
 
 export default puzzle;