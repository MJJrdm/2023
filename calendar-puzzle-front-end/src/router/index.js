import Vue from "vue";
import VueRouter from "vue-router";
import LoginPage from "../view/Login.vue";
import HomePage from "../view/HomePage.vue";
import PlayGame from "../view/PlayGame.vue";
import GameDetail from "../view/GameDetail.vue";
import RegisteredAccount from "../view/RegisteredAccount.vue";
import ResetPassword from "../view/ResetPassword.vue";
import store from "../store";
import { Message } from "element-ui";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/play",
    name: "PlayGame",
    component: PlayGame,
  },
  {
    path: "/home",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/reg",
    name: "RegisteredAccount",
    component: RegisteredAccount,
  },
  {
    path: "/res",
    name: "ResetPassword",
    component: ResetPassword,
  },
  {
    path: "/detail",
    name: "GameDetail",
    component: GameDetail,
  },
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  const token = store.getters.getToken;
  if (to.path === "/" || to.path === "/reg" || to.path === "/res") {
    if (token && to.path === "/") {
      next("/home");
    } else {
      next();
    }
  } else {
    const localUserInfo = store.getters.getUserInfo;

    if (!localUserInfo || !token) {
      Message.warning("未登录，请先登录！");
      next("/");
    } else {
      next();
    }
  }
});

export default router;
