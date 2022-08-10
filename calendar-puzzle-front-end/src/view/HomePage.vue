<!-- 首页 -->
<template>
  <div>
    <div class="home-user">
      <user-avatar />
    </div>
    <div class="home-tabs">
    <div class="tabs-main">
      <el-tabs type="border-card" @tab-click="tabClick">
      <el-tab-pane >
        <span slot="label"><i class="el-icon-house"></i> 游戏大厅</span>
        <game-hall ref="gameHall" />
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label"><i class="el-icon-trophy"></i> 排行榜</span>
        <ranking-list ref="rankList" />
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label"><i class="el-icon-time"></i> 游戏记录</span>
        <game-record ref="gameRecord" />
      </el-tab-pane>
    </el-tabs>
    </div>
  </div>
  </div>
</template>

<script>
import GameHall from "./GameHall.vue";
import GameRecord from "./GameRecord.vue";
import UserAvatar from "../components/UserAvatar.vue";
import RankingList from "./RankingList.vue";

export default {
  name: "HomePage",
  components: {
    GameHall,
    GameRecord,
    RankingList,
    UserAvatar
  },
  data() {
    return {};
  },
  computed: {},
  created() {},
  mounted() {},
  methods: {
    tabClick(e) {
      switch (e.index) {
        case '0':
          this.$refs.gameHall.createTimer()
          break;
        case '1':
          this.$refs.rankList.getGameRankList()
          this.$refs.gameHall.clearTimer()
          break;
        case '2':
          this.$refs.gameRecord.getGameRecordList()
          this.$refs.gameHall.clearTimer()
          break;
      
        default:
          break;
      }
    }
  },
};
</script>

<style>
.home-tabs .el-tabs__item {
  position: relative;
  width: 400px;
  height: 61px;
  background-color: rgba(236, 236, 236, 100);
  color: rgba(16, 16, 16, 100);
  font-size: 28px;
  text-align: center;
  font-family: Roboto;
  border: 1px solid rgba(230, 230, 230, 100);
}
.el-tabs--border-card > .el-tabs__header .el-tabs__item.is-active {
  border: 1px solid rgba(230, 230, 230, 100);
}

.tabs-main, .home-user {
  width: 1200px;
  margin: 0 auto;
}
.home-user {
  text-align: right;
}
</style>