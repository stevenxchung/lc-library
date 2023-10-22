const { performance } = require("perf_hooks");

class Solution {
  method(height) {
    let [l, r] = [0, height.length - 1];
    let maxArea = 0;
    while (l < r) {
      const area = (r - l) * Math.min(height[l], height[r]);
      maxArea = Math.max(maxArea, area);
      if (height[l] < height[r]) l++;
      else r--;
    }

    return max_area;
  }

  reference(height) {
    let [left, right, max] = [0, height.length - 1, 0];

    while (left < right) {
      const [leftHeight, rightHeight] = this.getHeights(height, left, right);
      const area = this.getArea(height, left, right);

      max = Math.max(max, area);

      const isRightGreater = leftHeight <= rightHeight;
      if (isRightGreater) left++;

      const isRightLess = rightHeight < leftHeight;
      if (isRightLess) right--;
    }

    return max;
  }

  getHeights = (height, left, right) => [height[left], height[right]];

  getArea = (height, left, right) => {
    const [leftHeight, rightHeight] = this.getHeights(height, left, right);
    const _height = Math.min(leftHeight, rightHeight);
    const width = right - left;

    return _height * width;
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(input));
        else this.reference(input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  [1, 8, 6, 2, 5, 4, 8, 3, 7],
  [1, 1],
];
test.quantify(testCases);
