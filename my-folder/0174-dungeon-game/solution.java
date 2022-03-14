import java.util.Hashtable;

class Solution {
    Hashtable<String,Integer> h = new Hashtable<>();
    public int calculateMinimumHP(int[][] dungeon) {
        class Calculator {
            public int calculate(int[][] dungeon, int roomx, int roomy) {
                String str = "(" + roomx + "," + roomy + ")";
                if (h.get(str) != null) {
                    return h.get(str);
                }
                int height = dungeon.length;
                int breadth = dungeon[0].length;
                int room = dungeon[roomy][roomx];
                if (roomx == breadth - 1 || roomy == height - 1) {
                    if (roomx == breadth - 1 && roomy == height - 1) {
                        int ans = Math.max(0, -room);
                        h.put(str,ans);
                        return ans;
                    } else if (roomy == height - 1) {
                        int ans = Math.max(0, calculate(dungeon, roomx + 1, roomy) - room);
                        h.put(str,ans);
                        return ans;
                    } else {
                        int ans = Math.max(0, calculate(dungeon, roomx, roomy + 1) - room);
                        h.put(str,ans);
                        return ans;
                    }
                }
                int goRight = Math.max(0, calculate(dungeon, roomx + 1, roomy) - room);
                int goDown = Math.max(0, calculate(dungeon, roomx, roomy + 1) - room);
                int ans = Math.min(goRight, goDown);
                h.put(str, ans);
                return ans;
            }
        }
        Calculator c = new Calculator();
        int x = c.calculate(dungeon,0,0);
        return x + 1;
    }
}
