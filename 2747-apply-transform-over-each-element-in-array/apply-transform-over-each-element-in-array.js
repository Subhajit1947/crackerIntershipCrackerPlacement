/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const a11=[]
    for(let i=0;i<arr.length;i++){
        a11.push(fn(arr[i],i))
    }
    return a11
};