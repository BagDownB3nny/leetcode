/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {

    const stack = [];
    const openBrackets = ["(", "{", "["];
    const closeBrackets = [")", "}", "]"];

    for (const bracket of s) {
        if (openBrackets.includes(bracket)) {
            stack.push(bracket);
        } else {
            const openBracket = stack.pop();
            if (openBrackets.indexOf(openBracket) !== closeBrackets.indexOf(bracket)) {
                return false;
            }
        }
    }
    return stack.length === 0;
};
