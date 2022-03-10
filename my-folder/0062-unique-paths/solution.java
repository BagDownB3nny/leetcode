class Solution {
    public double factorial(int n) {
        if (n==1) {
            return 1;
        }
        return n * factorial(n-1);
    }
    
    public int uniquePaths(int m, int n) {
        if (m==1) {
            return 1;
        }
        if (n==1) {
            return 1;
        }
        int x = (int) Math.round(factorial(m+n-2) / (factorial(m-1) * factorial(n-1)));
        return x;
    }
}
