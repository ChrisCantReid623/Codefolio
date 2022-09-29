import java.io.*;
import java.util.*;

public class PA3Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your filename: ");
        String fileName = input.nextLine();
        File gardenFile = new File(fileName);
        Scanner commands = new Scanner(gardenFile);
        System.out.println();

        //Garden Setup
        String rows = commands.nextLine();
        String cols = commands.nextLine();
        String blankLine = commands.nextLine();
        readCommands(gardenSize(rows), gardenSize(cols), commands);
    }

    /**
     * Returns the integers used to determine the row x column dimensions of the Garden.
     *
     * @param line a string containing the row/column information
     */
    public static int gardenSize(String line) {
        String[] settings = line.split(" ");
        return Integer.parseInt(settings[1]);
    }

    /**
     * Returns the garden coordinate where a plant will be located.
     *
     * @param coordinates a string of the plant coordinate location
     */
    public static int[] getCoordinates(String coordinates) {
        int[] location = new int[2];
        location[0] = Integer.parseInt(String.valueOf(coordinates.charAt(1)));
        location[1] = Integer.parseInt(String.valueOf(coordinates.charAt(3)));
        return location;
    }

    /**
     * Returns the type of plant based on predetermined categories.
     *
     * @param plant the name of the plant
     */
    public static String getPlantType(String plant) {
        String[] flowers = {"iris", "lily", "rose", "daisy", "tulip", "sunflower"};
        String[] trees = {"oak", "willow", "banana", "coconut", "pine"};
        String[] veggies = {"garlic", "zucchini", "tomato", "yam", "lettuce"};

        String plantType = "";
        if (Arrays.asList(flowers).contains(plant)) {
            plantType = "flower";
        } else if (Arrays.asList(trees).contains(plant)) {
            plantType = "tree";
        } else if (Arrays.asList(veggies).contains(plant)) {
            plantType = "vegetable";
        }
        return plantType;
    }

    /**
     * Creates a new subClass of the Plant class.
     *
     * @param plantCommand a 'PLANT' command from the txt file
     */
    public static Plant newPlant(String[] plantCommand) {
        String type = getPlantType(plantCommand[2]);
        char token = plantCommand[2].charAt(0);

        return switch (type) {
            case "flower" -> new Flower(type, token);
            case "tree" -> new Tree(type, token);
            case "vegetable" -> new Vegetable(type, token);
            default -> null;
        };
    }

    /**
     * Reads the commands of a txt file where each line is a different command. Perform actions on the Garden based
     * on the command String.
     *
     * @param rows     the number of rows in the Garden
     * @param cols     the number of columns in the Garden
     * @param commands the commands following the Garden setup dimensions
     */
    public static void readCommands(int rows, int cols, Scanner commands) {
        GardenLayout garden = new GardenLayout(rows, cols);
        //System.out.println(garden.getGarden());

        while (commands.hasNext()) {
            String command = commands.nextLine();
            String[] commandLine = command.split(" ");

            if (commandLine[0].equalsIgnoreCase("print")) {
                garden.printGarden();
            } else if (commandLine[0].equalsIgnoreCase("plant")) {
                int[] location = getCoordinates(commandLine[1]);
                Plant newPlant = newPlant(commandLine);
                garden.addNewPlant(location, newPlant);
            } else if (commandLine[0].equalsIgnoreCase("grow")) {
                System.out.println("GROW HERE");
                //TODO
            } else if (commandLine[0].equalsIgnoreCase("harvest")) {
                System.out.println("HARVEST HERE");
                //TODO
            } else if (commandLine[0].equalsIgnoreCase("pick")) {
                System.out.println("PICK HERE");
                //TODO
            } else if (commandLine[0].equalsIgnoreCase("cut")) {
                System.out.println("CUT HERE");
                //TODO
            }
        }
    }
}

/**A 2D array containing various Plant objects to simulate a garden map.*/
class GardenLayout {
    protected Plant[][] gardenMap;

    /**Sets the dimensions of the gardenMap
     * @param rows rows within the gardenMap
     * @param columns columns within each row*/
    public GardenLayout(int rows, int columns) {
        this.gardenMap = new Plant[rows][columns];
    }

    /** Adds a new Plant object to the gardenMap at a specified location.
     * @param location a list of coordinates loc[0] = row, loc[1] = column
     * @param newPlant the new Plant object being added */
    public void addNewPlant(int[] location, Plant newPlant) {
        gardenMap[location[0]][location[1]] = newPlant;
    }

    /** Prints the output of the mapGarden.*/
    public void printGarden() {
        System.out.println("> PRINT");
        for (Plant[] mapRow : gardenMap) {
            for (int plantRow = 0; plantRow < 5; plantRow++) {
                StringBuilder printLine = new StringBuilder();
                for (Plant curPlant : mapRow) {
                    String[] line = curPlant.getLine(plantRow);
                    String joined = String.join("", line);
                    printLine.append(joined);
                }
                System.out.println(printLine);
            }
        }
        System.out.println();
    }
}

/**An object placed within a "GardenLayout" object.*/
class Plant {
    protected String type;
    protected char token;
    public String[][] plot = new String[5][5];

    /**Initiates a plot of empty cells
     * @param type the plant family in which the plant belongs
     * @param token takes the first character from the plant's name */
    public Plant(String type, char token){
        this.type = type;
        this.token = token;
        for (int row = 0; row < plot.length; row ++) {
            for (int col = 0; col < plot[row].length; col++){
                this.plot[row][col] = ".";
            }
        }
    }

    /**Returns the list of cells on a specified row from the plot map.
     * @param index the index of the specified row*/
    public String[] getLine(int index) {
        return plot[index];
    }
}

/** A Plant object subclass. */
class Vegetable extends Plant {
    /**Initiates a Vegetable plot with the token in the top-center cell.
     * @param token takes the first character from the plant's name
     * @param type the plant family in which the plant belongs */
    public Vegetable(String type, char token) {
        super(type, token);
        plot[0][2] = String.valueOf(token);
    }
}

/** A Plant object subclass. */
class Tree extends Plant {
    /**Initiates a Tree plot with the token in the bottom-center cell.
     * @param token takes the first character from the plant's name
     * @param type the plant family in which the plant belongs */
    public Tree(String type, char token) {
        super(type, token);
        plot[4][2] = String.valueOf(token);
    }
}

/** A Plant object subclass. */
class Flower extends Plant {
    /**Initiates a Flower plot with the token in the center cell.
     * @param token takes the first character from the plant's name
     * @param type the plant family in which the plant belongs */
    public Flower(String type, char token) {
        super(type, token);
        plot[2][2] = String.valueOf(token);
    }
}