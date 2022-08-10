// const side = '30px';
// const _color = ['', 'rgba(59,130,246,0.4)', '', 'rgba(139,92,246,0.4)', 'rgba(236,72,153,0.4)']
const cellSide = 40;
const colorOfValue = [{
    id: 1,
    value: 1,
    color: 'rgba(255,148,148,0.8)'
  },
  {
    id: 2,
    value: 2,
    color: 'rgba(255,155,95,0.8)'
  },
  {
    id: 3,
    value: 3,
    color: 'rgba(252,231,150,0.8)'
  },
  {
    id: 4,
    value: 4,
    color: 'rgba(206,159,103,0.8)'
  },
  {
    id: 5,
    value: 5,
    color: 'rgba(255,175,228,0.8)'
  },
  {
    id: 6,
    value: 6,
    color: 'rgba(206,142,252,0.8)'
  },
  {
    id: 7,
    value: 7,
    color: 'rgba(154,235,218,0.8)'
  },
  {
    id: 8,
    value: 8,
    color: 'rgba(157,196,255,0.8)'
  }
]

const initHomeInfo = {
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
  gameName: '',
  duration: "00:00",
}

const puzzleCellList = [
  [{
      label: "JAN",
      value: 1,
      className: "",
      isMonth: true,
      dateValue: 1
    },
    {
      label: "FEB",
      value: 2,
      className: "",
      isMonth: true,
      dateValue: 2
    },
    {
      label: "MAR",
      value: 3,
      className: "",
      isMonth: true,
      dateValue: 3
    },
    {
      label: "APR",
      value: 4,
      className: "",
      isMonth: true,
      dateValue: 4
    },
    {
      label: "MAY",
      value: 5,
      className: "",
      isMonth: true,
      dateValue: 5
    },
    {
      label: "JUN",
      value: 6,
      className: "",
      isMonth: true,
      dateValue: 6
    },
    {
      label: "",
      value: 0,
      className: "",
    }
  ],
  [{
      label: "JUL",
      value: 1,
      className: "",
      isMonth: true,
      dateValue: 7
    },
    {
      label: "AUG",
      value: 2,
      className: "",
      isMonth: true,
      dateValue: 8
    },
    {
      label: "SEP",
      value: 3,
      className: "",
      isMonth: true,
      dateValue: 9
    },
    {
      label: "OCT",
      value: 4,
      className: "",
      isMonth: true,
      dateValue: 10
    },
    {
      label: "NOV",
      value: 5,
      className: "",
      isMonth: true,
      dateValue: 11
    },
    {
      label: "DEC",
      value: 6,
      className: "",
      isMonth: true,
      dateValue: 12
    },
    {
      label: "",
      value: 0,
      className: ""
    }
  ],
  [{
      label: "1",
      value: 1,
      className: "",
      isMonth: false,
      dateValue: 1
    },
    {
      label: "2",
      value: 2,
      className: "",
      isMonth: false,
      dateValue: 2
    },
    {
      label: "3",
      value: 3,
      className: "",
      isMonth: false,
      dateValue: 3
    },
    {
      label: "4",
      value: 4,
      className: "",
      isMonth: false,
      dateValue: 4
    },
    {
      label: "5",
      value: 5,
      className: "",
      isMonth: false,
      dateValue: 5
    },
    {
      label: "6",
      value: 6,
      className: "",
      isMonth: false,
      dateValue: 6
    },
    {
      label: "7",
      value: 7,
      className: "",
      isMonth: false,
      dateValue: 7
    }
  ],
  [{
      label: "8",
      value: 8,
      className: "",
      isMonth: false,
      dateValue: 8
    },
    {
      label: "9",
      value: 2,
      className: "",
      isMonth: false,
      dateValue: 9
    },
    {
      label: "10",
      value: 3,
      className: "",
      isMonth: false,
      dateValue: 10
    },
    {
      label: "11",
      value: 4,
      className: "",
      isMonth: false,
      dateValue: 11
    },
    {
      label: "12",
      value: 5,
      className: "",
      isMonth: false,
      dateValue: 12
    },
    {
      label: "13",
      value: 6,
      className: "",
      isMonth: false,
      dateValue: 13
    },
    {
      label: "14",
      value: 0,
      className: "",
      isMonth: false,
      dateValue: 14
    }
  ],
  [{
      label: "15",
      value: 1,
      className: "",
      isMonth: false,
      dateValue: 15
    },
    {
      label: "16",
      value: 2,
      className: "",
      isMonth: false,
      dateValue: 16
    },
    {
      label: "17",
      value: 3,
      className: "",
      isMonth: false,
      dateValue: 17
    },
    {
      label: "18",
      value: 4,
      className: "",
      isMonth: false,
      dateValue: 18
    },
    {
      label: "19",
      value: 5,
      className: "",
      isMonth: false,
      dateValue: 19
    },
    {
      label: "20",
      value: 6,
      className: "",
      isMonth: false,
      dateValue: 20
    },
    {
      label: "21",
      value: 0,
      className: "",
      isMonth: false,
      dateValue: 21
    }
  ],
  [{
      label: "22",
      value: 1,
      className: "",
      isMonth: false,
      dateValue: 22
    },
    {
      label: "23",
      value: 2,
      className: "",
      isMonth: false,
      dateValue: 23
    },
    {
      label: "24",
      value: 3,
      className: "",
      isMonth: false,
      dateValue: 24
    },
    {
      label: "25",
      value: 4,
      className: "",
      isMonth: false,
      dateValue: 25
    },
    {
      label: "26",
      value: 5,
      className: "",
      isMonth: false,
      dateValue: 26
    },
    {
      label: "27",
      value: 6,
      className: "",
      isMonth: false,
      dateValue: 27
    },
    {
      label: "28",
      value: 0,
      className: "",
      isMonth: false,
      dateValue: 28
    }
  ],
  [{
      label: "29",
      value: 1,
      className: "",
      isMonth: false,
      dateValue: 29
    },
    {
      label: "30",
      value: 2,
      className: "",
      isMonth: false,
      dateValue: 30
    },
    {
      label: "31",
      value: 3,
      className: "",
      isMonth: false,
      dateValue: 31
    },
    {
      label: "",
      value: 4,
      className: ""
    },
    {
      label: "",
      value: 5,
      className: ""
    },
    {
      label: "",
      value: 0,
      className: ""
    },
    {
      label: "",
      value: 0,
      className: ""
    }
  ],
];

const idMapColorValue = colorOfValue.reduce((p, q) => {
  p[q.id] = q;
  return p
}, {})

let allPuzzleCell = [{
    id: 5,
    // color: idMapColorValue['1'].color,
    left: cellSide * 15,
    top: cellSide * 4,
    transform: '',
    value: [
      [1, 1, 0, 0],
      [1, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]
    ]
  },
  {
    id: 2,
    // color: idMapColorValue['2'].color,
    left: cellSide * 15,
    top: cellSide * 9,
    transform: '',
    value: [
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]
    ]
  },
  {
    id: 8,
    // color: idMapColorValue['3'].color,
    left: cellSide * 18,
    top: cellSide * 4,
    transform: '',
    value: [
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0]
    ]
  },
  {
    id: 1,
    // color: idMapColorValue['4'].color,
    left: cellSide * 0,
    top: cellSide * 9,
    transform: '',
    value: [
      [1, 1, 1, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [0, 0, 0, 0]
    ]
  },
  {
    id: 6,
    // color: idMapColorValue['5'].color,
    left: 0,
    top: cellSide * 4,
    transform: '',
    value: [
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]
    ]
  },
  {
    id: 7,
    // color: idMapColorValue['6'].color,
    left: cellSide * 4,
    top: cellSide * 9,
    transform: '',
    value: [
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0]
    ]
  },
  {
    id: 3,
    // color: idMapColorValue['7'].color,
    left: cellSide * 3,
    top: cellSide * 4,
    transform: '',
    value: [
      [1, 0, 0, 0],
      [1, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]
    ]
  },
  {
    id: 4,
    // color: idMapColorValue['8'].color,
    left: cellSide * 18,
    top: cellSide * 9,
    transform: '',
    value: [
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0]
    ]
  }
]

const queue = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -1, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -1, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

;(function comAllPuzzleCell(allPuzzleCell) {
  allPuzzleCell.forEach(item => {
    const colorValue = idMapColorValue[item.id]
    const itemValue = item.value
    item.color = colorValue.color
    itemValue.forEach(row => {
      for (let i = 0; i < row.length; i++) {
        if (row[i] === 1) {
          row[i] = colorValue.value
        }
      }
    })
  })
})(allPuzzleCell)

const colorList = (function () {
  const arr = colorOfValue.map(item => item.color)
  arr.unshift('transparent')
  return arr
})()

const optionMonths = (function () {
  const arr = []
  comDateOptions(true, puzzleCellList[0], arr)
  comDateOptions(true, puzzleCellList[1], arr)
  return arr
})()

const optionDays = (function () {
  const arr = []
  comDateOptions(false, puzzleCellList[2], arr)
  comDateOptions(false, puzzleCellList[3], arr)
  comDateOptions(false, puzzleCellList[4], arr)
  comDateOptions(false, puzzleCellList[5], arr)
  comDateOptions(false, puzzleCellList[6], arr)
  return arr
})()

function comDateOptions(isMonth, list, arr) {
  list.forEach(item => {
    if (item.isMonth == isMonth && item.dateValue) {
      arr.push({
        label: item.label,
        value: item.dateValue
      })
    }
  })
}

const flipMatrix = function (matrix) {
  matrix = JSON.parse(JSON.stringify(matrix))
  return matrix.reverse()
}

const rotateMatrix = function (matrix) {
  matrix = JSON.parse(JSON.stringify(matrix))
  let dd = []
  dd = matrix.map((val, matrixIndex) => {
    let arr = []
    for (let i = val.length - 1; i >= 0; i--) {
      // 第一行等于第一列，以此类推
      arr.push(matrix[i][matrixIndex])
    }
    return arr
  })
  matrix.forEach((val, index) => {
    matrix[index] = dd[index]
  })
  return matrix
};

const judgeArr = function (queuePuzz, cellValue) {
  for (let i = 0; i < queuePuzz.length; i++) {
    const element = queuePuzz[i];
    for (let j = 0; j < element.length; j++) {
      if (element[i][j] && cellValue[i][j]) {
        return true
      }
    }
  }
  return false
}
const judgeIsSolve = function (queue) {
  const emptyCellArr = []
  let hasMonth = false
  let hasDay = false
  for (let i = 7; i < 14; i++) {
    const element = queue[i];
    for (let j = 7; j < 14; j++) {
      const cellValue = element[j]
      if (emptyCellArr.length > 2) {
        return false
      }
      if (cellValue === 0) {
        emptyCellArr.push([i, j])
        if ((i === 7 || i === 8) && j !== 13) {
          hasMonth = true
        } else {
          hasDay = true
        }
      }
    }
  }
  if (hasDay && hasMonth) {
    return true
  }
  return false
}

// 0,1,2,3 代表 上右下左,返回的为不需要
const judgeBorder = function (matrix, i, j) {
  let ret = []
  const arr = [
    [i - 1, j],
    [i, j + 1],
    [i + 1, j],
    [i, j - 1]
  ]

  arr.forEach((item, index) => {
    const m = item[0]
    const n = item[1]
    if (m < 4 && m >= 0 && n < 4 && n >= 0 && matrix[m][n]) {
      ret.push(index)
    }
  });
  return ret
}
const borderHiddenArr = [
  'border-top-style: none;',
  'border-right-style: none;',
  'border-bottom-style: none;',
  'border-left-style: none;'
]
export {
  queue,
  allPuzzleCell,
  judgeArr,
  rotateMatrix,
  flipMatrix,
  judgeIsSolve,
  judgeBorder,
  borderHiddenArr,
  colorList,
  puzzleCellList,
  optionMonths,
  optionDays,
  cellSide,
  initHomeInfo
}