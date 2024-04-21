/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const lower = []
    const upper = []
    const special = []
    const banned = []
    for (let i = 0; i < word.length; i++) {
        const c = word[i];
        if (special.includes(c.toLowerCase()) && c.toUpperCase() == c) {
            continue;
        }
        if (banned.includes(c.toLowerCase())) {
            continue;
        }
        if (c.toLowerCase() == c) {
            if (!lower.includes(c)) {
                lower.push(c);
            }
            if (upper.includes(c.toUpperCase())) {
                banned.push(c.toLowerCase());
                if (!special.includes(c.toLowerCase())) {
                    special.push(c.toLowerCase());
                }
            }   
        }
        if (c.toUpperCase() == c) {
            if (!upper.includes(c)) {
                upper.push(c);
            }
            if (lower.includes(c.toLowerCase())) {
                special.push(c.toLowerCase());      
            }
        }
    }

    return special.length - banned.length;
};
