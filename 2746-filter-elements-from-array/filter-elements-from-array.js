/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const a11=[]
    for(let i=0;i<arr.length;i++){
        if(Boolean(fn(arr[i],i))===true){
            a11.push(arr[i])
        }  
    }
    return a11
};