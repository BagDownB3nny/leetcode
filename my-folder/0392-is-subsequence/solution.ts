function isSubsequence(s: string, t: string): boolean {
    let ptr1 = 0;
    let ptr2 = 0;
    while (ptr2 < t.length) {
        if (t.charAt(ptr2) == s.charAt(ptr1)) {
            ptr1++;
        }
        ptr2++;
    }
        
    return ptr1 == s.length;
};
