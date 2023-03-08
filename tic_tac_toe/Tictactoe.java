// TicTacToe Game by CuriousExpert24

public class Tictactoe {
    private String[][] board;
    private static final int ROWS = 3;
    private static final int COLS = 3;
    private String regex = "\\s{3}";

    // Default Constructor
    public Tictactoe() {
        board = new String[ROWS][COLS];
        this.initBoard();
        // this.winXtest();
    }

    // Initialize Board
    public void initBoard() {
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                board[i][j] = "   ";
            }
        }
    }

    // Sets Player's Move
    public void setGame(int i, int j, String player) {
        if (board[i][j].matches(regex))
            board[i][j] = " " + player + " ";
    }

    // Find the Winner
    public boolean isGameOver() {
        // checking rows
        for (int i = 0; i < ROWS; i++) {
            if (!board[i][0].matches(regex) && board[i][0].equals(board[i][1]) && board[i][1].equals(board[i][2])) {
                return true;
            }
        }
        // checking columns

        for (int j = 0; j < COLS; j++) {
            if (!board[0][j].matches(regex) && board[0][j].equals(board[1][j]) && board[1][j].equals(board[2][j]))
                return true;
        }
        // checking diagonals
        if (!board[0][0].matches(regex) && board[0][0].equals(board[1][1]) && board[1][1].equals(board[2][2]))
            return true;
        if (!board[0][2].matches(regex) && board[0][2].equals(board[1][1]) && board[1][1].equals(board[2][0]))
            return true;
        // no body's won
        return false;

    }

    // Prints Board
    public String printBoard() {
        String strBoard = "";
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (j == COLS - 1)
                    strBoard += board[i][j];
                else
                    strBoard += board[i][j] + "|";
            }
            if (i != ROWS - 1)
                strBoard += "\n---+---+---\n";
        }
        return strBoard;
    }

    // Checks the Win
    public void winXtest() {
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (j == 0)
                    board[i][j] = " X ";
                else
                    board[i][j] = "   ";
            }
        }
    }
}