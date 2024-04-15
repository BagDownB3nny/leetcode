function lengthOfLongestSubstring(s: string): number {
    let start = 0;
    let end = 0;
    let longest = 0;
    let map = {};
    while (end < s.length) {
        const currentLetter = s.charAt(end);
        if (!map[currentLetter]) {
            map[currentLetter] = true;
            longest = Math.max(Object.keys(map).length, longest);
        } else {
            let endLoop = false;
            while (!endLoop) {
                if (s.charAt(start) == currentLetter) {
                    start++;
                    break;
                } else {
                    delete map[s.charAt(start)];
                    start++;
                }
            }

        }
        end++;
    }
    return longest;
};
