// https://leetcode.com/problems/counter

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let a = n-1;
    return function() {
        return ++a;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */