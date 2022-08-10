<!-- 登录 -->
<template>
  <div class="box">
    <div class="box-title">欢迎登录</div>
    <div class="box-middle">
      <div class="acc-pass">
        <el-input v-model="account" placeholder="请输入账号">
          <i slot="prepend" class="el-icon-user"></i>
        </el-input>
      </div>
      <div class="acc-pass">
        <el-input v-model="password" type="password" placeholder="请输入密码">
          <i slot="prepend" class="el-icon-lock"></i>
        </el-input>
      </div>
      <div class="login-but cur-poi" @click.left="login">登录</div>
    </div>
    <div class="box-foot">
      <div class="cur-poi" @click="regAcc">注册账号</div>
      <div class="cur-poi" @click="forPass">忘记密码</div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "loginPage",
  components: {},
  data() {
    return {
      account: "",
      password: "",
    };
  },
  computed: {},
  created() {},
  mounted() {},
  methods: {
    ...mapMutations(["setUserInfo", "setToken"]),
    login() {
      this.$api.puzzle
        .login({ username: this.account, password: this.password })
        .then((result) => {
          const { data } = result;
          const userInfo = { name: data.user_name, id: data.user_id };
          this.setUserInfo(userInfo);
          this.setToken(data.token);
          this.$router.push("/home");
        });
    },
    regAcc() {
      console.log("注册账号");
      this.$router.push("/reg");
    },
    forPass() {
      this.$router.push("/res");
    },
  },
};
</script>

<style scoped>
.box {
  margin: 281px auto;
  width: 363px;
  height: 364px;
  line-height: 20px;
  border-radius: 3px;
  color: rgba(16, 16, 16, 100);
  font-size: 14px;
  text-align: center;
  box-shadow: 0px 1px 5px 0px rgba(0, 0, 0, 0.2);
  font-family: Roboto;
}
.box-title {
  border-block-end: 2px solid rgba(58, 98, 215, 100);
  margin: auto;
  width: 96px;
  height: 30px;
  color: rgba(16, 16, 16, 100);
  font-size: 24px;
  text-align: center;
  font-family: SourceHanSansSC-regular;
}
.acc-pass {
  margin: 15px auto 0;
  width: 287px;
  height: 45px;
  color: rgba(170, 170, 170, 100);
  font-size: 16px;
  text-align: left;
  font-family: SourceHanSansSC-regular;
}
.login-but {
  margin: 30px auto 0;
  width: 287px;
  height: 45px;
  line-height: 45px;
  border-radius: 3px;
  background-color: rgba(58, 98, 215, 100);
  color: rgba(255, 255, 255, 100);
  font-size: 16px;
  text-align: center;
  font-family: Roboto;
  border: 1px solid rgba(58, 98, 215, 100);
}
.box-foot {
  margin: 10px auto 0;
  width: 287px;
  height: 45px;
  display: flex;
  justify-content: space-between;
  color: rgba(58, 98, 215, 100);
}
.cur-poi {
  cursor: pointer;
}
</style>