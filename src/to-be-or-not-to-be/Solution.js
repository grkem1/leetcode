// https://leetcode.com/problems/to-be-or-not-to-be

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(a){
        if(a === val){
            return true;
        }else{
            throw new Error(msg="Not Equal");
        }
    }
    function notToBe(b){
        if(b !== val){
            return true;
        }else{
            throw new Error("Equal");
        }
    }
    return {toBe,notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */