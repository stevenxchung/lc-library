/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
*/

/**
 * @param {number[]} heights
 * @return {number}
 */

var peakIndex = 0;
// var heightsArray = [2, 0, 2];
// var heightsArray = [4, 2, 3];
var heightsArray = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];

var trap = function(heights) {
  let total = 0;
//   let stupidTest = [2, 0, 2];

  if (heights[1] < heights[0]) {
    total += findWaterBetweenPeaks(peakIndex, heights);
  } else {
    peakIndex = 1;
  }

  for (i = peakIndex; i < heights.length; i++) {
    if (heights[i] > heights[i + 1] && heights[i] > heights[i - 1]) {
      // this is a peak
      peakIndex = i;
      total += findWaterBetweenPeaks(peakIndex, heights);
    }
  }

  return total;
};

var findWaterBetweenPeaks = function(firstPeakIndex, heights) {
  let totalBetweenPeaks = 0;
  let waterLevels = new Array(heights[firstPeakIndex]).fill(0);

  let i = firstPeakIndex + 1;
  //While in a valley
  while (i < heights.length) {
    if (i === heights.length - 1 && heights[i] > heights[i - 1]) {
      // this is a peak
      break;
    }
    if (
      (heights[i] > heights[i + 1] && heights[i] > heights[i - 1]) ||
      i === heights.length - 1
    ) {
      // this is a peak
      break;
    }

    for (j = heights[firstPeakIndex] - 1; j > heights[i] - 1; j--) {
      waterLevels[j] += 1;
    }

    i++;
  }

  for (k = heights[i]; k < waterLevels.length; k++) {
    waterLevels[k] = 0;
  }

//   console.log('waterLevel', waterLevels);
  totalBetweenPeaks = waterLevels.reduce((a, b) => a + b, 0);

//   console.log('totalBetweenPeaks', totalBetweenPeaks);

  peakIndex = i;
  return totalBetweenPeaks;
};

console.log(trap(heightsArray)); // 5
