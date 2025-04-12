/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return{
        toBe:function(v1){
            if(val===v1){
                return true
            }
            else{
                throw "Not Equal"
            }
        },
        notToBe:function(v1){
            if(val===v1){
                throw "Equal"
            }
            else{
                return true
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */