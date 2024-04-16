function reverseWords(s: string): string {
    let temp = "";
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) == " ") {
            if (temp != "") {
                stack.push(temp);
                temp = "";
            }
        } else {
            temp += s.charAt(i);
        }
    }
    if (temp != "") {
        stack.push(temp);
    }
    let ans = "";
    while (stack.length) {
        const word = stack.pop();
        ans += word;
        if (stack.length) {
            ans += " ";
        }
    }
    return ans;
};
