/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 **/


// map1.set('name', 'alice');
// console.log(map1.get('name')); // \U0001f449️ "alice"

var canConstruct = function(ransomNote, magazine) {
    let letters = new Map();
    for (const letter of magazine) {
        if (letters.has(letter)) {
            letters.set(letter, letters.get(letter) + 1);
        } else {
            letters.set(letter, 1);
        }
    }
    for (const letter of ransomNote) {
        if (letters.has(letter) && letters.get(letter) > 0) {
            letters.set(letter, letters.get(letter) - 1);
        } else {
            return false;
        }
    }
    return true;
};
