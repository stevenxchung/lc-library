/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
*/

/**
 * @param {number[][]} intervals
 * @return {number}
 */

// var minMeetingRooms = function(intervals) {
//   let numRooms = 1;
//   for (let i = 0; i < intervals.length; i++) {
//     for (let j = 0; j < i; j++) {
//       if (meetingsConflict(intervals[i], intervals[j])) {
//         numRooms++;
//         break;
//       }
//     }
//   }

//   return numRooms;
// };

// var meetingsConflict = function(meeting1, meeting2) {
//   return (
//     (meeting1[0] > meeting2[0] && meeting1[0] < meeting2[1]) ||
//     (meeting1[1] > meeting2[0] && meeting1[1] < meeting2[1]) ||
//     (meeting2[0] > meeting1[0] && meeting2[0] < meeting2[1]) ||
//     (meeting2[1] > meeting1[0] && meeting2[1] < meeting1[1])
//   );
// };

/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {
  var starts = intervals.concat().sort(function(a, b) {
    return a.start - b.start;
  });
  var ends = intervals.sort(function(a, b) {
    return a.end - b.end;
  });
  var rooms = 0;
  var end = 0;
  for (var i = 0; i < intervals.length; i++) {
    if (starts[i].start < ends[end].end) {
      rooms++;
    } else {
      end++;
    }
  }
  return rooms;
};

input = [[0, 30], [5, 10], [15, 20]];
// input = [[7, 10], [2, 4]];
// input = [[2, 7]];
console.log(minMeetingRooms(input));
