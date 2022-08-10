<!-- 游戏记录 -->
<template>
  <div class="rank-box">
    <div class="rank-table">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="player" label="玩家"> </el-table-column>
        <el-table-column prop="puzzle_date" label="解密日期">
        </el-table-column>
        <el-table-column prop="puzzle_start" label="开始时间">
        </el-table-column>
        <el-table-column prop="puzzle_duration" label="游戏时长">
        </el-table-column>
        <el-table-column prop="status" label="状态"> </el-table-column>
      </el-table>
    </div>
    <div class="rank-page">
      <el-pagination
        background
        @current-change="curPageChange"
        layout="prev, pager, next, total"
        :total="total"
        :current-page="curPage"
        :page-size="curPageSize"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "GameRecord",
  components: {},
  data() {
    return {
      tableData: [],
      total: 0,
      curPage: 1,
      curPageSize: 10
    };
  },
  computed: {
    ...mapGetters(["getUserInfo"]),
  },
  created() {},
  mounted() {
    this.getGameRecordList()
  },
  methods: {
    getGameRecordList() {
      this.$api.puzzle.getGameHistoryList({
        pagination: this.curPage,
        pagesize: this.curPageSize,
      }).then(res => {
        this.tableData = res.data
          this.total = res.total
      });
    },
    curPageChange(curPage) {
      this.curPage = curPage
      this.getGameRecordList()
    }
  },
};
</script>

<style scoped>
.rank-box {
  margin-top: 20px;
}
</style>