<!-- 小块拼图 -->
<template>
  <div
    class="puz-block-box"
    ref="puzBlockBox"
    @mousedown.left.prevent="move"
    @click.right.prevent="clickRightPuz()"
  >
    <div class="puzzle-row" v-for="(item, index) in puzValMat" :key="index">
      <div v-for="(cell, indexCell) in item" :key="indexCell">
        <div
          class="puzzle-cell"
          :style="computCellPos(index, indexCell, cell)"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapGetters } from "vuex";
import { rotateMatrix, flipMatrix } from "../utils/util";
import { throttle } from "lodash";
let count = 0;
export default {
  name: "BlockCell",
  props: {
    puzCel: {
      type: Object,
      require: true,
    },
    valueArr: {
      type: Array,
      require: true,
    },
  },
  inject: ["homeInfo"],
  components: {},
  data() {
    return {
      puzValMat: this.valueArr,
      leftNum: this.puzCel.left,
      topNum: this.puzCel.top,
      puzBlockBoxSty: {
        left: `${this.puzCel.left}px`,
        top: `${this.puzCel.top}px`,
        zIndex: 0,
        transition: "none",
        transform: "",
      },
    };
  },
  computed: {
    ...mapGetters(["getQueue", "getCellSide"]),
  },
  watch: {},
  created() {},
  mounted() {
    const self = this;
    this.changePuzBox(this.puzBlockBoxSty);
    self.clickRightPuzThr = throttle(() => {
      self.changePuzBox(
        {
          transform: "rotateX(180deg)",
          transition: "transform 0.3s ease",
        },
        true
      );
    }, 500);
    self.clickleftPuzThr = throttle(() => {
      self.changePuzBox(
        {
          transform: "rotate(90deg)",
          transition: "transform 0.3s ease",
        },
        true
      );
    }, 500);
  },
  methods: {
    ...mapMutations(["setQueue"]),
    computCellPos(rowIndex, colIndex, value) {
      let str = `top:${rowIndex * this.getCellSide}px;left:${
        colIndex * this.getCellSide
      }px;`;
      if (value) {
        str += `background-color:${this.puzCel.color};border:0;`;
      } else {
        str += "visibility:hidden;";
      }
      return str;
    },
    saveGame() {
      this.$parent.$parent.saveGame(false);
    },
    changePuzBox(boxStyle, isRotate) {
      const curPuzzleblockSty = this.$refs["puzBlockBox"].style;
      for (const key in boxStyle) {
        if (Object.hasOwnProperty.call(boxStyle, key)) {
          const ele = boxStyle[key];
          curPuzzleblockSty[key] = ele;
        }
      }
      if (isRotate) {
        setTimeout(() => {
          curPuzzleblockSty.transform = "";
          curPuzzleblockSty.transition = "none";
        }, 300);
      }
    },
    rotate(optType) {
      const self = this;
      const left = this.leftNum;
      const top = this.topNum;
      // 原始cell数据
      const cellValue = self.puzValMat;
      const queue = self.getQueue;
      // 数据修改
      const matrix = optType ? rotateMatrix(cellValue) : flipMatrix(cellValue);
      // queue修改
      const j = left / self.getCellSide;
      const i = top / self.getCellSide;
      for (let m = i; m < i + 4; m++) {
        const element = queue[m];
        for (let n = j; n < j + 4; n++) {
          if (cellValue[m - i][n - j]) {
            element[n] = 0;
          }
        }
      }
      // 回退操作
      const backQueue = function () {
        // 还原
        for (let m = i; m < i + 4; m++) {
          const element = queue[m];
          for (let n = j; n < j + 4; n++) {
            if (cellValue[m - i][n - j]) {
              element[n] = cellValue[m - i][n - j];
            }
          }
        }
        const temStr = optType ? "旋转" : "翻转";
        self.$message({
          message: `此位置不可${temStr}！`,
          type: "warning",
        });
      };
      // 判断是否能拖放在面板位置上
      const judgeCanMove = function () {
        // 有1的位置不能超出边界
        // 有1的位置 对应的queue的cell必须为0
        // 获取 拼图对应的queue cell 数据
        const j = left / self.getCellSide;
        const i = top / self.getCellSide;
        let queuePuzz = new Array(4)
          .fill(null)
          .map((item, iIndex) =>
            new Array(4)
              .fill(0)
              .map((JItem, jIndex) =>
                queue[i + iIndex] != undefined &&
                queue[i + iIndex][j + jIndex] != undefined
                  ? queue[i + iIndex][j + jIndex]
                  : -1
              )
          );
        const flag = queuePuzz.some((row, r) =>
          row.some((col, c) => col && matrix[r][c])
        );
        return !flag;
      };
      if (judgeCanMove()) {
        if (optType) {
          self.clickleftPuzThr();
        } else {
          self.clickRightPuzThr();
        }
        // 修改queue
        for (let m = i; m < i + 4; m++) {
          const element = queue[m];
          for (let n = j; n < j + 4; n++) {
            if (matrix[m - i][n - j]) {
              element[n] = matrix[m - i][n - j];
            }
          }
        }
        // 保存游戏
        // 等翻转动作完成后在刷新页面
        setTimeout(() => {
          self.setQueue(JSON.parse(JSON.stringify(queue)));
          // 修改 queuecell
          self.puzValMat = matrix;
          self.saveGame();
        }, 300);
      } else {
        backQueue();
      }
    },
    changePuzbloSty(bloStyle) {
      const puzzleblockStyle = bloStyle;
      const curPuzzleblockSty = this.$refs["puzBlockBox"].style;
      for (const key in puzzleblockStyle) {
        if (Object.hasOwnProperty.call(puzzleblockStyle, key)) {
          const ele = puzzleblockStyle[key];
          curPuzzleblockSty[key] = ele;
        }
      }
    },
    clickRightPuz() {
      this.rotate(false);
    },
    // 拖拽
    move(e) {
      const self = this;
      const puzBlockBoxSty = self.puzBlockBoxSty;
      const el = e.currentTarget;
      const queue = self.getQueue;
      puzBlockBoxSty.zIndex = count++;
      let disx = e.pageX - el.offsetLeft;
      let disy = e.pageY - el.offsetTop;
      let left = el.offsetLeft;
      let top = el.offsetTop;
      let oriLeft = el.offsetLeft;
      let oriTop = el.offsetTop;
      let oriJ = Math.round(el.offsetLeft / self.getCellSide);
      let oriI = Math.round(el.offsetTop / self.getCellSide);
      // 获取 Puzzle cell  拼图 数据
      const cellValue = this.puzValMat;

      for (let m = oriI; m < oriI + 4; m++) {
        const element = queue[m];
        for (let n = oriJ; n < oriJ + 4; n++) {
          if (cellValue[m - oriI][n - oriJ]) {
            element[n] = 0;
          }
        }
      }

      let isRotate = true;
      document.onmousemove = function (e) {
        isRotate = false;
        left = e.pageX - disx;
        top = e.pageY - disy;
        puzBlockBoxSty.left = left + "px";
        puzBlockBoxSty.top = top + "px";
        self.changePuzBox(puzBlockBoxSty);
      };
      document.onmouseup = function () {
        document.onmousemove = document.onmouseup = null;
        if (
          isRotate ||
          (Math.abs(left - oriLeft) < 5 && Math.abs(top - oriTop) < 5)
        ) {
          self.rotate(true);
        } else {
          // 向最近的交叉点吸附
          const leftOffset = left % self.getCellSide;
          const topOffset = top % self.getCellSide;
          left = left - (left % self.getCellSide);
          top = top - (top % self.getCellSide);
          if (leftOffset > 0) {
            if (leftOffset > self.getCellSide / 2) left += self.getCellSide;
          } else {
            if (leftOffset < -self.getCellSide / 2) left -= self.getCellSide;
          }
          if (topOffset > 0) {
            if (topOffset > self.getCellSide / 2) top += self.getCellSide;
          } else {
            if (topOffset < -self.getCellSide / 2) top -= self.getCellSide;
          }
          const j = Math.round(left / self.getCellSide);
          const i = Math.round(top / self.getCellSide);
          if (judgeCanMove()) {
            // 修改位置
            puzBlockBoxSty.transition = "all 0.15s ease-out";
            puzBlockBoxSty.left = left + "px";
            puzBlockBoxSty.top = top + "px";
            self.changePuzBox(puzBlockBoxSty);
            setTimeout(() => {
              puzBlockBoxSty.transition = "none";
              self.changePuzBox(puzBlockBoxSty);
            }, 150);
            self.leftNum = left;
            self.topNum = top;
            // 修改queue  cellValue 并且将原位置处改为0
            for (let m = i; m < i + 4; m++) {
              const element = queue[m];
              for (let n = j; n < j + 4; n++) {
                if (cellValue[m - i][n - j]) {
                  element[n] = cellValue[m - i][n - j];
                }
              }
            }
            self.setQueue(JSON.parse(JSON.stringify(queue)));
            // 保存游戏
            self.saveGame();
          } else {
            backQueue();
          }
        }
      };
      // 回退操作
      const backQueue = function () {
        puzBlockBoxSty.transition = "all 0.3s linear";
        puzBlockBoxSty.left = oriLeft + "px";
        puzBlockBoxSty.top = oriTop + "px";
        self.changePuzBox(puzBlockBoxSty);
        setTimeout(() => {
          puzBlockBoxSty.transition = "none";
          self.changePuzBox(puzBlockBoxSty);
        }, 300);

        // 还原
        for (let m = oriI; m < oriI + 4; m++) {
          const element = queue[m];
          for (let n = oriJ; n < oriJ + 4; n++) {
            if (cellValue[m - oriI][n - oriJ]) {
              element[n] = cellValue[m - oriI][n - oriJ];
            }
          }
        }
        self.$message({
          message: "不可移动到此位置！",
          type: "warning",
        });
      };
      // 判断是否能拖放在面板位置上
      const judgeCanMove = function () {
        // 有1的位置不能超出边界
        // 有1的位置 对应的queue的cell必须为0
        // 获取 拼图对应的queue cell 数据
        const j = left / self.getCellSide;
        const i = top / self.getCellSide;
        let queuePuzz = new Array(4)
          .fill(null)
          .map((item, iIndex) =>
            new Array(4)
              .fill(0)
              .map((JItem, jIndex) =>
                queue[i + iIndex] != undefined &&
                queue[i + iIndex][j + jIndex] != undefined
                  ? queue[i + iIndex][j + jIndex]
                  : -1
              )
          );
        const flag = queuePuzz.some((row, r) =>
          row.some((col, c) => col && cellValue[r][c])
        );
        return !flag;
      };
    },
  },
};
</script>

<style scoped>
.puz-block-box {
  position: absolute;
  top: 0;
  left: 0;
  transform-origin: calc(var(--cell-side) * 2) calc(var(--cell-side) * 2);
  transition: transform 0.5s linear;
}
.puzzle-row {
  display: flex;
}
.puzzle-cell {
  position: absolute;
  height: var(--cell-side);
  width: var(--cell-side);
  box-sizing: border-box;
  border: 1px #767670c7 solid;
}
</style>