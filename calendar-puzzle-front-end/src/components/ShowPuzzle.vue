<!-- 日历拼图展示 -->
<template>
  <div class="puzzle-box"
       :style="`width:${boxWidth}px;height:${boxHeight}px`">
    <div v-for="(row, index) in puzzleCellList"
         :key="index"
         class="box-row">
      <div v-for="(cell, cellIndex) in row"
           :key="cellIndex"
           :class="cell.className"
           :style="comCellStyle(cell.isMonth, cell.value, cell.dateValue, index, cellIndex)"
           class="box-cell">{{cell.label}}</div>
    </div>
  </div>
</template>

<script>
import { colorList, puzzleCellList } from "../utils/util";
export default {
  name: "ShowPuzzle",
  props: {
    matrixValue: {
      type: Array,
      require: true,
    },
    boxWidth: {
      type: Number,
      require: true,
    },
    boxHeight: {
      type: Number,
      require: true,
    },
    curMonth: {
      type: Number,
      require: true,
    },
    curDay: {
      type: Number,
      require: true,
    },
  },
  components: {},
  data() {
    return {};
  },
  computed: {},
  created() {
    this.puzzleCellList = puzzleCellList
  },
  mounted() {},
  methods: {
    comCellStyle(isMonth, cellValue, dateValue, rowIndex, colIndex) {
      let str = `width:${this.boxWidth / 7}px;height:${this.boxHeight / 7}px;`;
      if ((isMonth && dateValue == this.curMonth) || !isMonth && dateValue == this.curDay) {
        str += "color:black;font-weight:bold;";
      }
      str += `background-color:${
        colorList[this.matrixValue[rowIndex][colIndex]]
      }`;
      return str;
    },
  },
};
</script>

<style scoped>
.box-row {
  display: flex;
}
.box-cell {
  display: flex;
  align-items: center; /*实现水平居中*/
  justify-content: center;
  color: gray;
}
</style>