import Vue from "vue";
import Vuex from "vuex";
import { cellSide } from "./utils/util";
import createPersistedState from "vuex-persistedstate";
import { queue } from "./utils/util";

Vue.use(Vuex);

const dataState = createPersistedState({
  paths: ["userInfo", "token"],
});

const store = new Vuex.Store({
  state: {
    queue: JSON.parse(JSON.stringify(queue)),
    userInfo: {
      name: "",
      id: 1,
    },
    cellSide,
    token: ""
  },
  getters: {
    getQueue: (state) => {
      return state.queue;
    },
    getUserInfo: (state) => {
      return state.userInfo;
    },
    getCellSide: (state) => {
      return state.cellSide;
    },
    getToken: (state) => {
      return state.token;
    }
  },
  mutations: {
    setQueue(state, queue) {
      state.queue = queue;
    },
    setUserInfo(state, userInfo) {
      state.userInfo = userInfo;
    },
    setToken(state, token) {
      state.token = token;
    }
  },
  plugins: [dataState],
});

export default store;
