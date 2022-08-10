<!-- block -->
<template>
  <div class="block-grid" :style="`--cell-side:${getCellSide}px;`">
    <puzzle-queue />
    <puzzle-cell v-for="(item, index) in allPuzzleCell"
                 :key="index"
                 :puzCel="item"
                 :valueArr="item.value" />
    <div class="block-button">
      左键单击顺时针90度旋转<br>右键单击翻转変换<br>拼盘附近不可放置<br>刷新页面将重置<br>第一次完成游戏后将不再计时
    </div>
  </div>
</template>

<script>
import puzzleCell from "./PuzzleCell.vue";
import puzzleQueue from "./PuzzleQueue.vue";
import { mapGetters, mapMutations } from "vuex";
import { allPuzzleCell } from '../utils/util'

export default {
  name: "BlockCell",
  props: {},
  components: {
    puzzleCell,
    puzzleQueue,
  },
  data() {
    return {
      result: [], // 7*7
    };
  },
  computed: {
    ...mapGetters(["getQueue", "getCellSide"]),
  },
  created() {
    // 动态边长

    // 循环allPuzzleCell 将 queue对应位置改为对应值
    this.allPuzzleCell = allPuzzleCell
    const queue = this.getQueue;
    this.allPuzzleCell.forEach((ele) => {
      const left = ele.left;
      const top = ele.top;
      const value = ele.value;
      const j = left / this.getCellSide;
      const i = top / this.getCellSide;
      for (let m = i; m < i + 4; m++) {
        const element = queue[m];
        for (let n = j; n < j + 4; n++) {
          if (value[m - i][n - j]) {
            element[n] = value[m - i][n - j];
          }
        }
      }
    });
    this.setQueue(JSON.parse(JSON.stringify(queue)));
  },
  mounted() {},
  methods: {
    ...mapMutations(["setQueue"]),
  },
  destroyed() {}
};
</script>

<style scoped>
.block-grid {
  position: relative;
  width: calc(var(--cell-side) * 20);
  background-color: white;
  height: calc(var(--cell-side) * 15);
  border: 3px solid gray;
  left: 0;
  top: 0;
  margin: auto;
}
.block-button {
  font-family: "Courier New", Courier, monospace;
  position: absolute;
  text-align: left;
  top: 0;
  right: -217px;
}
</style>