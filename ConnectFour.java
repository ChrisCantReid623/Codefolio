/**Christopher Reid
 * CSC 210
 * Simulates a two-person game of Connect Four.
 * */
import java.util.Scanner;
public class ConnectFour {

    /** User decides how many sequential tokens are needed to win.*/
    private static int howManyToWin() {
        Scanner input = new Scanner(System.in);
        int sequence;
        while (true) {
            System.out.println("How many tokens in a row are needed to win: 3, 4, or 5?: ");
            sequence = input.nextInt();
            if ((sequence == 3) || (sequence == 4) || (sequence == 5)) {
                return sequence;
            } else {
                System.out.println("Sorry, this game only supports Connect 3, 4, & 5.");
                System.out.println();
            }
        }
    }

    /** Prompts players for names.
     * @param player integer identifying player 1 or 2
     * @return the player's name*/
    private static String getNames(int player) {
        Scanner input = new Scanner(System.in);
        System.out.println("Player " + player + ", enter your name: ");
        return input.nextLine();
    }

    /** Prompts player 1 for their token, either R (red) or Y (yellow).
     * @param player the player's names
     * @return the players token*/
    private static String getToken(String player) {
        Scanner input = new Scanner(System.in);
        String token;
        while (true) {
            System.out.println(player + ", please choose a token: R or Y");
            token = input.nextLine();
            if (token.equalsIgnoreCase("R") || token.equalsIgnoreCase("Y")) {
                return token.toUpperCase();
            } else {
                System.out.println("Sorry, please select a VALID token: R or Y ");
                System.out.println();
            }
        }
    }

    /** Creates the blank '6x7' grid with space in-between dividers for tokens and returns as an object.
     * @return the game board object*/
    private static String[][] createBoard() {
        String[][] board = new String [7][15];
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[row].length; col++) {
                if (col % 2 == 0) {
                    board[row][col] = "|";
                } else {
                    board[row][col] = " ";
                }
                if (row==6) board[row][col] = "-";
            }
        }
        return board;
    }

    /** Prints the contents of the board.
     * @param board the game board object*/
    private static void printPattern(String[][] board) {
        for (String[] row : board) {
            for (String column : row) {
                System.out.print(column);
            }
            System.out.println();
        }
        System.out.println();
    }

    /** Checks if column input is within the board dimensions or if a chosen column is full.
     * @param col The column chosen by the current player
     * @param board The game board object*/
    private static boolean validate(int col, String[][] board) {
        if (col < 1 || col > 14){
            System.out.println("Invalid column. Please select another column.");
            return false;
        }
        if (!board[0][col].equals(" ")){
            System.out.println("This column is full. Please select another column.");
            return false;
        }
        return true;
    }

    /** Master directional winning check function.
     * @param current the last token played
     * @param board the game board object
     * @param sequence the number of sequential tokens needed to win
     * @return boolean, if a winning move is identified*/
    private static boolean isWinner(String current, String[][] board, int sequence) {
        return horizontalCheck(current, board, sequence) ||
                verticalCheck(current, board, sequence) ||
                diagonalDownCheck(current, board, sequence) ||
                diagonalUpCheck(current, board, sequence);
    }

    /** Performs the horizontal check for a winning move.
     *@param current the last token played
     *@param board the game board object
     *@param sequence the number of sequential tokens needed to win
     *@return boolean, if a winning move is identified*/
    private static boolean horizontalCheck(String current, String[][] board, int sequence) {
        int count = 0;

        for (int row = 0; row < board.length -1; row++){
            for (int col = 1; col < board[0].length - 1; col+=2){
                if (board[row][col].equals(current)){
                    count++;
                } else {
                    count = 0;
                }
                if (count >= sequence){
                    return true;
                }
            }
        }
        return false;
    }

    /** Performs the vertical check for a winning move.
     *@param current the last token played
     *@param board the game board object
     *@param sequence the number of sequential tokens needed to win
     *@return boolean, if a winning move is identified*/
    private static boolean verticalCheck(String current, String[][] board, int sequence) {
        int count = 0;

        for (int col = 1; col < board[0].length - 1; col+=2){
            for (int row = 0; row < board.length -1; row++){
                if (board[row][col].equals(current)){
                    count++;
                } else {
                    count = 0;
                }
                if (count >= sequence){
                    return true;
                }
            }
        }
        return false;
    }

    /** Performs the downward diagonal check for a winning move.
     *@param current the last token played
     *@param board the game board object
     *@param sequence the number of sequential tokens needed to win
     *@return boolean, if a winning move is identified*/
    private static boolean diagonalDownCheck(String current, String[][] board, int sequence) {
        for (int checkRow = 0; checkRow < board.length - sequence; checkRow++){
            int count = 0;
            int row, col;
            for(row = checkRow, col = 1; row < board.length && col < board[0].length; row++, col+=2){
                if (board[row][col].equals(current)){
                    count++;
                    if (count>= sequence){
                        return true;
                    }
                }
                else {
                    count = 0;
                }
            }
        }
        for (int checkCol = 1; checkCol < board[0].length - sequence; checkCol++){
            int count = 0;
            int row, col;
            for (row = 0, col = checkCol; row < board.length && col < board[0].length; row++, col+=2){
                if (board[row][col].equals(current)){
                    count++;
                    if (count >= sequence){
                        return true;
                    }
                }
                else {
                    count = 0;
                }
            }
        }
        return false;
    }

    /** Performs the upward diagonal check for a winning move.
     *@param current the last token played
     *@param board the game board object
     *@param sequence the number of sequential tokens needed to win
     *@return boolean, if a winning move is identified*/
    private static boolean diagonalUpCheck(String current, String[][] board, int sequence) {
        for (int checkRow = 5; checkRow >= 0; checkRow--){
            int count = 0;
            int row, col;
            for (row = checkRow, col = 1; row >= 0 && col < board[0].length; row--, col+=2){
                if (board[row][col].equals(current)){
                    count++;
                    if (count >= sequence){
                        return true;
                    }
                }
                else {
                    count = 0;
                }
            }
        }
        for (int checkCol = 1; checkCol < board[0].length - sequence; checkCol++){
            int count = 0;
            int row, col;
            for (row = 5, col = checkCol; row >= 0 && col < board[0].length; row--, col+= 2){
                if (board[row][col].equals(current)){
                    count++;
                    if (count >= sequence) {
                        return true;
                    }
                }
                else{
                    count = 0;
                }
            }
        }
        return false;
    }

    public static void main (String[] args) {
        //Sequence to Win
        int inARowToWin = howManyToWin();

        //Name Prompt
        String p1Name = getNames(1);
        String p2Name = getNames(2);

        //Token Prompt
        String p1Token = getToken(p1Name);
        String p2Token;
        if (p1Token.equals("R")) {
            p2Token = "Y";
        } else {
            p2Token = "R";
        }
        System.out.println();
        System.out.println(p1Name + ", your token is " + p1Token + ".");
        System.out.println(p2Name + ", your token is " + p2Token + ".");
        System.out.println();
        String[][] board = createBoard();
        Scanner input = new Scanner(System.in);

        // Game Engine
        int turn = 1;
        String current = p1Token;
        boolean winner = false;

        while (!winner && turn < 43) {
            boolean validPlay;
            int col;
            do {
                System.out.println("Player " + current + ", pick a column (1-7): ");
                System.out.println();
                printPattern(board);
                col = 2 * input.nextInt() - 1;
                validPlay = validate(col, board);
            } while (!validPlay);

            for (int row = board.length-1; row >= 0; row--) {
                if (board[row][col].equals(" ")) {
                    board[row][col] = current;
                    break;
                }
            }
            winner = isWinner(current, board, inARowToWin);

            // Switches Players
            if (current.equals(p1Token)){
                current = p2Token;
            } else {
                current = p1Token;
            }
            turn++;
        }
        if (turn == 43){
            System.out.println("No winner, the game is a draw.");
            System.out.println();
        }
        printPattern(board);
        if (winner){
            if (current.equals(p1Token)) {
                System.out.println("Congratulations " + p2Name + "! You are the winner!");
            } else {
                System.out.println("Congratulations " + p1Name + "! You are the winner!");
            }
        }
    }
}