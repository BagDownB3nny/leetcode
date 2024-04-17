function longestPalindrome(s: string): string {
    
    if (s.length <= 1) {
        return s;
    }
    
    
    let start;
    let end;
    let longestLength = 0;
    
    for (let i = 0; i < s.length - 1; i++) {
        let diff = 0;
        while (i - diff >= 0 && i + diff + 1 <= s.length) {
            if (s.charAt(i - diff) != s.charAt(i + diff)) {
                break;
            }
            const l = 1 + diff * 2;
            if (l > longestLength) {
                longestLength = l;
                start = i - diff;
                end = i + diff;
            }
            diff++;
        }
        diff = 0;
        while (i - diff >= 0 && i + 2 + diff <= s.length) {
            if (s.charAt(i - diff) != s.charAt(i + 1 + diff)) {
                break;
            }
            const l = 2 + diff * 2;
            if (l > longestLength) {
                longestLength = l;
                start = i - diff;
                end = i + 1 + diff;
            }
            diff++;
        }
    }
    return s.substring(start, end + 1);
};
