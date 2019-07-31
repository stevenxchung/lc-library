/*

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

*/

let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

let rotate = matrix => {
  // Assume N x N matrix
  let mLen = matrix.length;

  // Transpose matrix
  for (let i = 0; i < mLen; i++) {
    for (let j = i; j < mLen; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }

  // Reverse each row
  for (let i = 0; i < mLen; i++) {
    matrix[i] = matrix[i].reverse();
  }

  return matrix;
};

// Test
console.log(rotate(matrix));
