<!-- 游戏界面 -->
<template>
  <div class="game-view">
    <div class="view-header" :style="`width:${infoWidth}px;`">
      <div class="view-header--left">
        <el-button type="primary" @click="quitGame">退出游戏</el-button>
      </div>
      <div class="view-header__name">{{ homeInfo.gameName }}</div>
      <div class="view-header--right">
        <user-avatar />
      </div>
    </div>
    <div>
      <div>
        <div class="game-info" :style="`width:${infoWidth}px`">
          <div class="game-info--left">玩家：{{ getUserInfo.name }}</div>
          <div class="game-info--right">游戏时长：{{ comDuration }}</div>
        </div>
      </div>
      <div>
        <block-view />
      </div>
    </div>
  </div>
</template>

<script>
import blockView from "./BlockView.vue";
import userAvatar from "../components/UserAvatar.vue";
import { mapGetters } from "vuex";
import { cellSide } from "../utils/util.js";

let countTimer = null;
export default {
  name: "PlayGame",
  components: {
    blockView,
    userAvatar,
  },
  provide() {
    return {
      homeInfo: this.homeInfo,
    };
  },
  data() {
    const query = this.$route.query;
    return {
      infoWidth: cellSide * 20,
      homeInfo: {
        id: Number.parseInt(query.id),
        duration: "00:00",
        gameName: query.gameName,
        month: Number.parseInt(query.month),
        day: Number.parseInt(query.day),
        countTim: 0,
      },
    };
  },
  computed: {
    ...mapGetters(["getUserInfo", "getQueue"]),
    comDuration() {
      const countTim = this.homeInfo.countTim;
      return `${Math.floor(countTim / 60)}:${countTim % 60}`;
    },
  },
  beforeCreate() {},
  created() {},
  mounted() {
    const self = this;
    this.userName = this.getUserInfo.name;
    self.saveGame(true);
    countTimer = setInterval(() => {
      self.homeInfo.countTim++;
      self.saveGame(true);
    }, 1000);
  },
  methods: {
    saveGame(isTimer) {
      // 获取矩阵
      const curQueue = this.getQueue;
      const db = [];
      for (let i = 4; i < 11; i++) {
        const row = curQueue[i];
        const rowArr = [];
        for (let j = 7; j < 14; j++) {
          rowArr.push(row[j]);
        }
        db.push(rowArr);
      }
      const params = {
        game_id: this.homeInfo.id,
        duration_seconds: this.homeInfo.countTim,
        puzzle_cell: db,
      };
      this.$api.puzzle.getGameStatus(params).then((res) => {
        if (!isTimer) {
          const { data } = res;
          if (data.game_over) {
            this.clearTimer();
            this.$message({
              message: "恭喜你，完成拼图！",
              type: "success",
            });
          }
        }
      });
    },
    quitGame() {
      this.$api.puzzle.terminateGame({ game_id: this.homeInfo.id }).then(() => {
        this.$router.push("/home");
      });
    },
    clearTimer() {
      window.clearInterval(countTimer);
    },
  },
  destroyed() {
    this.clearTimer();
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
  margin: 10px auto 96px;
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
.game-info {
  display: flex;
  margin: 0 auto;
  justify-content: space-between;
  margin-bottom: 16px;
}
</style>