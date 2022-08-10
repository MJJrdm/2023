<!-- 注册 -->
<template>
  <div class="box">
    <div class="box-title">欢迎注册</div>
    <div class="box-middle">
      <div class="acc-pass">
        <el-input v-model="account"
                  placeholder="请输入账号">
          <i slot="prepend"
             class="el-icon-user"></i>
        </el-input>
      </div>
      <div class="acc-pass">
        <el-input v-model="password"
                  type="password"
                  placeholder="请输入密码">
          <i slot="prepend"
             class="el-icon-lock"></i>
        </el-input>
      </div>
      <div class="login-but cur-poi" @click.left="register">
        注册
      </div>
    </div>
    <div class="box-foot">
      <div class="cur-poi"> </div>
      <div class="cur-poi" @click="goLogin">已有账号，去登录</div>
    </div>
  </div>
</template>

<script>
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
    register() {
      this.$api.puzzle.register({username: this.account, password: this.password}).then(() => {
        this.$message.success('注册成功')
        this.goLogin()
      });
    },
    goLogin() {
      this.$router.push('/')
    }
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