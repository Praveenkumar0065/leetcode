class Solution {
    public int reverse(int x) {
        long res = 0;
        int sign = (x < 0) ? -1 : 1;
        x *= sign;

        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
            }

            res *= sign;

            if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) {
                return 0;
                }

                return (int) res;
            }
        }