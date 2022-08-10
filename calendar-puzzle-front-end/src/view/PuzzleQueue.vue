<!-- queue -->
<template>
  <div class="queue-grid">
    <div v-for="(row, index) in getQueue" :key="index" class="row">
      <div v-for="(cell, cellIndex) in row" :key="cellIndex" class="cell"></div>
    </div>
    <div class="queue-puz-block">
      <show-puzzle
        :matrixValue="curGameInfo.matrixValue"
        :curMonth="curGameInfo.month"
        :curDay="curGameInfo.day"
        :boxWidth="getCellSide * 7"
        :boxHeight="getCellSide * 7"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import showPuzzle from "../components/ShowPuzzle";
import { initHomeInfo } from "../utils/util";
export default {
  name: "BlockCell",
  props: {},
  components: {
    showPuzzle,
  },
  inject: ['homeInfo'],
  data() {
    return {
      curGameInfo: initHomeInfo,
    };
  },
  computed: {
    ...mapGetters(["getQueue", "getCellSide"]),
  },
  mounted() {
    this.curGameInfo.month = this.homeInfo.month;
    this.curGameInfo.day = this.homeInfo.day;
  },
  methods: {},
};
</script>

<style scoped>
.queue-puz-block {
  position: absolute;
  width: calc(var(--cell-side) * 7);
  height: calc(var(--cell-side) * 7);
  background-size: 93% 93%;
  background-repeat: no-repeat;
  top: calc(var(--cell-side) * 4);
  left: calc(var(--cell-side) * 7);
  font-size: 16px;
}
.row {
  display: flex;
}
.cell {
  width: var(--cell-side);
  height: var(--cell-side);
  box-sizing: border-box;
}
</style>