<!-- 用户 -->
<template>
  <div class="user-box">
    <el-dropdown @command="quitLogin">
      <span class="el-dropdown-link"> 你好，{{ getUserInfo.name }} </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>退出</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  name: "UserAvatar",
  components: {},
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["getUserInfo"]),
  },
  created() {},
  mounted() {},
  methods: {
    ...mapMutations(["setUserInfo", "setToken"]),
    quitLogin() {
      this.$api.puzzle.logout({user_id: this.getUserInfo.id}).then(() => {
        this.setToken("");
        this.setUserInfo("");
        this.$router.push("/");
      });
    },
  },
};
</script>

<style scoped>
.user-box {
  display: inline-block;
  margin: 16px;
  font-size: 24px;
}
</style>