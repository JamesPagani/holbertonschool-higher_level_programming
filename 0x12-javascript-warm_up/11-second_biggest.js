#!/usr/bin/node
const nums = process.argv.slice(2);
let highest = nums[0];
let second = nums[1];

if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < nums.length; i++) {
    nums[i] = parseInt(nums[i]);
  }
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > highest) {
      second = highest;
      highest = nums[i];
    } else if (nums[i] > second && nums[i] < highest) {
      second = nums[i];
    }
  }
  console.log(second);
}
