// https://leetcode.com/problems/apply-transform-over-each-element-in-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    rv = []
    for(let i = 0; i < arr.length; i++){
        rv.push(fn(arr[i],i));
        // console.log("here")
    }
    return rv
};