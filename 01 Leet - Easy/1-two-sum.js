/*

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

*/

let array = [2, 7, 11, 15];

// let twoSum = (nums, target) => {
//   let stack = [];
//   let i = 0;

//   while (i < nums.length) {
//     // Search for second element
//     for (let j = i + 1; j < nums.length; j++) {
//       if (target === nums[i] + nums[j]) {
//         stack.push(i, j);
//       }
//     }
//     // Increment
//     i++;
//   }

//   return stack;
// };

// Optimal using dictionary

let twoSum = (nums, target) => {
  let dict = {};
  for (let i = 0; i < nums.length; i++) {
    if (dict[nums[i]] >= 0) {
      return [dict[nums[i]], i]
    }
    dict[target - nums[i]] = i
  }
}

console.log(twoSum(array, 26));