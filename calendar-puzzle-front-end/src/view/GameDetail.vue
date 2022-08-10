<!-- 查看游戏详情 -->
<template>
  <div class="game-view">
    <div class="view-header">
      <div class="view-header--left">
        <el-button type="primary" @click="backHall">返回大厅</el-button>
      </div>
      <div class="view-header__name">{{ homeInfo.gameName }}</div>
      <div class="view-header--right">
        <user-avatar />
      </div>
    </div>
    <div>
      <div>
        <div class="game-info" :style="`width:${infoWidth}px`">
          <div class="game-info--left">玩家：{{ homeInfo.player }}</div>
          <div class="game-info--right">游戏时长：{{ homeInfo.duration }}</div>
        </div>
      </div>
      <div class="game-block" :style="`width:${infoWidth}px`">
        <show-puzzle
          :matrixValue="homeInfo.matrixValue"
          :curMonth="homeInfo.month"
          :curDay="homeInfo.day"
          :duration="homeInfo.duration"
          :boxWidth="infoWidth"
          :boxHeight="infoWidth"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import showPuzzle from "../components/ShowPuzzle";
import userAvatar from "../components/UserAvatar.vue";

let timer = null;
export default {
  name: "GameDetail",
  components: {
    showPuzzle,
    userAvatar,
  },
  data() {
    return {
      homeInfo: {
        id: 1,
        matrixValue: [
          [0, 0, 0, 0, 0, 0, -1],
          [0, 0, 0, 0, 0, 0, -1],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, -1, -1, -1, -1],
        ],
        month: 1,
        day: 1,
        gameName: "",
        duration: "00:00",
        player: "",
      },
      infoWidth: 50 * 7,
    };
  },
  computed: {
    ...mapGetters(["getCellSide", "getUserInfo"]),
  },
  created() {},
  mounted() {
    const self = this;
    this.id = this.$route.query.id;
    self.getHomeInfo();
    timer = setInterval(() => {
      self.getHomeInfo();
    }, 1000);
  },
  methods: {
    getHomeInfo() {
      this.$api.puzzle.getGameInfoById({ game_id: this.id }).then((res) => {
        const { data } = res;
        this.homeInfo.matrixValue = data.puzzle_cell;
        this.homeInfo.duration = data.puzzle_duration;
        this.homeInfo.player = data.player;
      });
    },
    backHall() {
      this.$router.push("/home");
    },
  },
  destroyed() {
    clearInterval(timer);
  },
};
</script>

<style scoped>
.game-view {
  padding: 10px;
}
.view-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 96px;
  height: 40px;
}
.view-header--left {
  display: flex;
}
.view-header__intr {
  font-size: 40px;
  padding: 0 25px;
  cursor: pointer;
}
.view-header__name {
  font-size: 30px;
  font-weight: bold;
}
.game-info,
.game-block {
  display: flex;
  margin: 0 auto;
  justify-content: space-between;
  margin-bottom: 16px;
}
</style>