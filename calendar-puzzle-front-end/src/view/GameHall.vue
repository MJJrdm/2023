<!--  -->
<template>
  <div class="game-hall-box">
    <div class="title-box">
      <div class="create-home" @click="dialogVisible = true">创建房间</div>
    </div>
    <div class="puzzle-list-box">
      <div
        v-for="item in puzzleList"
        class="puzzle-item-box"
        @click="goToDetail(item.id)"
        :key="item.id"
      >
        <div class="puzzle-item-title">
          <div class="puz-title__left">
            {{ item.gameName }}[{{ item.month }}.{{ item.day }}]
          </div>
          <div class="puz-title__right">{{ item.duration }}</div>
        </div>
        <show-puzzle
          :boxHeight="40 * 7"
          :boxWidth="40 * 7"
          :matrixValue="item.matrixValue"
          :curMonth="item.month"
          :curDay="item.day"
        />
      </div>
    </div>
    <el-pagination
      background
      @current-change="curPageChange"
      layout="prev, pager, next, total"
      :total="total"
      :current-page="curPage"
      :page-size="curPageSize"
    >
    </el-pagination>
    <el-dialog
      title="创建房间"
      :visible.sync="dialogVisible"
      width="500px"
      :before-close="handleClose"
    >
      <el-form :model="homeInfo" status-icon ref="homeInfo" label-width="100px">
        <el-form-item label="房间名称" required prop="gameName">
          <el-input v-model="homeInfo.gameName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="月" required prop="month">
          <el-select v-model="homeInfo.month" placeholder="请选择">
            <el-option
              v-for="item in optionMonths"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="日" required prop="day">
          <el-select v-model="homeInfo.day" placeholder="请选择">
            <el-option
              v-for="item in optionDays"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('homeInfo')"
            >确认</el-button
          >
          <el-button @click="dialogVisible = false">退出</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import showPuzzle from "../components/ShowPuzzle";
import { queue, optionMonths, optionDays } from "../utils/util";
import { mapGetters, mapMutations } from "vuex";
let timer = null;
export default {
  name: "GameHall",
  components: {
    showPuzzle,
  },
  data() {
    return {
      puzzleList: [],
      total: 0,
      curPage: 1,
      curPageSize: 6,
      dialogVisible: false,
      homeInfo: {
        gameName: "",
        month: 1,
        day: 1,
        id: 1,
      },
      optionMonths: optionMonths,
      optionDays: optionDays,
    };
  },
  computed: {
    ...mapGetters(["getUserInfo"]),
  },
  watch: {
    curPage: function () {
      this.getPuzzleList();
    },
  },
  created() {},
  mounted() {
    this.getPuzzleList();
    this.createTimer();
  },
  methods: {
    ...mapMutations(["setQueue"]),
    getPuzzleList() {
      this.$api.puzzle
        .getGameRealList({
          pagination: this.curPage,
          pagesize: this.curPageSize,
        })
        .then((res) => {
          const temArr = []
          const { data } = res
          data.forEach(ele => {
            const temp = ele.puzzle_date.split('.')
            temArr.push({
              id: ele.game_id,
              gameName: ele.game_name,
              userName: ele.player,
              matrixValue: ele.puzzle_cell,
              duration: ele.puzzle_duration,
              month: Number.parseInt(temp[0]),
              day: Number.parseInt(temp[1])
            })
          });
          this.puzzleList = temArr
          this.total = res.total
        });
    },
    goToDetail(id) {
      this.$router.push({ path: "/detail", query: { id } });
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(() => {
          done();
        })
        .catch(() => {});
    },
    curPageChange(curPage) {
      this.curPage = curPage
      this.getPuzzleList();
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.dialogVisible = false;
          const params = {
            game_name: this.homeInfo.gameName,
            player: this.getUserInfo.name,
            month: this.homeInfo.month,
            day: this.homeInfo.day,
          };
          this.$api.puzzle.startNewGame(params).then((res) => {
            const { data } = res;
            this.$message.success("创建游戏成功！");
            this.homeInfo.id = data["game_id"];
            this.setQueue(JSON.parse(JSON.stringify(queue)));
            this.$router.push({ path: "/play",  query: { ...this.homeInfo } });
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    createTimer() {
      const self = this;
      timer = setInterval(() => {
        self.getPuzzleList();
      }, 1000);
    },
    clearTimer() {
      clearInterval(timer);
    },
  },
  beforeDestroy() {
    this.clearTimer();
  },
};
</script>

<style scoped>
.puzzle-list-box {
  display: flex;
  flex-wrap: wrap;
  padding: 0px 100px;
}
.puzzle-item-box {
  margin: 20px;
  cursor: pointer;
  margin: 20px;
}
.puzzle-item-title {
  display: flex;
  justify-content: space-between;
}
.puz-title__left {
  width: 156px;
  height: 18px;
  color: rgba(16, 16, 16, 100);
  font-size: 14px;
  text-align: left;
  font-family: SourceHanSansSC-regular;
}
.puz-title__right {
  width: 60px;
  height: 23px;
  color: rgba(16, 16, 16, 100);
  font-size: 14px;
  text-align: right;
  font-family: SourceHanSansSC-regular;
}
.title-box {
  display: flex;
  justify-content: flex-end;
}
.create-home {
  cursor: pointer;
  width: 112px;
  color: rgba(82, 144, 255, 100);
  font-size: 28px;
  font-family: SourceHanSansSC-regular;
}
</style>