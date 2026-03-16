class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
        boolean[] rowCheck = new boolean[10];
        boolean[] colCheck = new boolean[10];
        boolean[] boxCheck = new boolean[10];

        for (int j = 0; j < 9; j++) {
            // 1. Validate Row i
            if (board[i][j] != '.') {
                int num = board[i][j] - '0'; // Convert char to int manually
                if (rowCheck[num]) return false;
                rowCheck[num] = true;
            }

            // 2. Validate Column i
            if (board[j][i] != '.') {
                int num = board[j][i] - '0';
                if (colCheck[num]) return false;
                colCheck[num] = true;
            }

            // 3. Validate 3x3 Box i
            int r = 3 * (i / 3) + (j / 3);
            int c = 3 * (i % 3) + (j % 3);
            if (board[r][c] != '.') {
                int num = board[r][c] - '0';
                if (boxCheck[num]) return false;
                boxCheck[num] = true;
            }
        }
    }
    return true;
    }
}