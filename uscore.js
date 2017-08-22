/* eslint-disable no-var, block-spacing */
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var sum = nums.filter(function(o) { return o%2 })
    .map(function(o){ return o * o})
    .reduce(function(a, b){return a+b});

console.log('Sum of the odd sq is ' + sum);
