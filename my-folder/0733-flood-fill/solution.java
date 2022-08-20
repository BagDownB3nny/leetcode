import java.util.HashSet;

class Solution {
    HashSet<Integer[]> filled = new HashSet<>();
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int pix_color = image[sr][sc];
        image[sr][sc] = color + 1;
        int[][] directions = new int[][] {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int[] direction : directions) {
            int new_sr = sr + direction[1];
            int new_sc = sc + direction[0];
            if (new_sc >= image[0].length || new_sc < 0) {
                continue;
            }
            if (new_sr >= image.length || new_sr < 0) {
                continue;
            }
            if (image[new_sr][new_sc] == pix_color) {
                floodFill(image, new_sr, new_sc, color);
            }
        }
        image[sr][sc] = color;
        return image;
    }
}
