/** Author: Christopher Reid
 * Class: CSC 210
 * Processes a csv file containing housing data and displays location density in a graphical interface window. Houses
 * priced under a user specified price threshold are plotted in a relative graphic location. */

import java.awt.*;
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.List;

public class CheapHouses {

    public static void main(String[] args) {
        createGui();
    }

    /** Creates the graphical representation of the .csv file data. Consists of the window containing a main panel.
     * The main panel contains sub panel for graphics and a sub panel for widgets. The widget panel contains two
     * text boxes for data entry, specifying the csv file to extract data and the price limit necessary to filter
     * results. Lastly the widget panel contains the button equipped with an action listener. When pressed, the
     * filter function imports data from the csv file specified in the text box and returns location data from houses
     * under the specified price limit. */
    private static void createGui() {
        JFrame window = new JFrame("Home Price Distribution");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setSize(600, 700);

        //Main Panel
        JPanel mainPanel = new JPanel(null);

        //Graphics Panel
        GPanel graphicsPanel = new GPanel();
        graphicsPanel.setLocation(0, 0);
        graphicsPanel.setSize(window.getWidth(),window.getHeight() - 100);
        graphicsPanel.setBorder(BorderFactory.createLineBorder(Color.black));
        mainPanel.add(graphicsPanel);

        //Widget Panel
        JPanel widgetPanel = new JPanel();
        widgetPanel.setLocation(0, window.getHeight() - 100);
        widgetPanel.setSize(window.getWidth(), window.getHeight() - window.getWidth());

        //File Input Field
        JLabel fileLabel = new JLabel("", JLabel.CENTER);
        fileLabel.setText("File:");
        JTextField fileTextField = new JTextField("houses.csv");
        widgetPanel.add(fileLabel);
        widgetPanel.add(fileTextField);

        //Price Limit Field
        JLabel priceLimitLabel = new JLabel("", JLabel.CENTER);
        priceLimitLabel.setText("Price:");
        JTextField priceLimitInput = new JTextField(10);
        widgetPanel.add(priceLimitLabel);
        widgetPanel.add(priceLimitInput);

        //Plot Button
        JButton plotButton = new JButton("Plot");
        plotButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (e.getSource() == plotButton) {
                    try {
                        ArrayList<List<String>> filteredData = filter(
                                fileTextField.getText(),
                                Double.parseDouble(priceLimitInput.getText())
                        );
                        double minLat = calcMinimumVal(filteredData, "latitude");
                        double maxLat = calcMaximumVal(filteredData, "latitude");
                        double minLong = calcMinimumVal(filteredData, "longitude");
                        double maxLong = calcMaximumVal(filteredData, "longitude");

                        for (List<String> filteredDatum : filteredData) {
                            minLat = Math.min(minLat, Double.parseDouble(filteredDatum.get(5)));
                            maxLat = Math.max(maxLat, Double.parseDouble(filteredDatum.get(5)));
                            minLong = Math.min(minLong, Double.parseDouble(filteredDatum.get(6)));
                            maxLong = Math.max(maxLong, Double.parseDouble(filteredDatum.get(6)));
                        }

                        for (List<String> filteredDatum : filteredData) {
                            graphicsPanel.plotPoints(filteredDatum, maxLat, minLat, maxLong, minLong);
                        }

                    }
                    catch (FileNotFoundException ex) {
                        System.out.println("This file does not exist.");
                        throw new RuntimeException(ex);
                    }
                }
            }
        });
        widgetPanel.add(plotButton);

        mainPanel.add(widgetPanel);
        window.add(mainPanel);
        window.setVisible(true);
    }

    /** Filters .csv file data to price, latitude, and longitude elements based on price parameters.
     * @param fileName the .csv file name string
     * @param priceLimit Filters the housing data below this price number
     * @return a two-dimensional array list of all the housing data */
    private static ArrayList<List<String>> filter(String fileName, double priceLimit) throws FileNotFoundException {

        Scanner inputFile = new Scanner(new File(fileName));

        ArrayList<List<String>> returnData = new ArrayList<>();
        String title = inputFile.nextLine();

        while (inputFile.hasNextLine()) {
            ArrayList<String> newLine = new ArrayList<>();
            String line = inputFile.nextLine();
            String[] lineSplit = line.split(",");
            int housePrice = Integer.parseInt(lineSplit[9]);
            if (housePrice <= priceLimit) {
                for (int i = 0; i < lineSplit.length; i++)
                    if (i==0 || i==1 || i==2 || i==3 || i==9 || i==10 || i==11) {
                    // 0 == Street, 1 == City, 2 == Zip, 3 == State, 9 == Price, 10 == Latitude, 11 == Longitude
                    newLine.add(lineSplit[i]);
                    }
                returnData.add(newLine);
            }
        }
        return returnData;
    }

    /** Calculates the minimum value from either the latitudes or longitudes from the filtered data set.
     * @param data filtered housing data based on a user input price limit
     * @param keyword string that determines which data element being processed
     * */
    public static double calcMinimumVal(ArrayList<List<String>> data, String keyword) {
        ArrayList<Double> coordinates = new ArrayList<>();
        if (keyword.equals("latitude")) {
            for (List<String> line : data) {
                for (int i = 0; i < line.size(); i++) {
                    if (i == 5) {
                        coordinates.add(Double.parseDouble(line.get(i)));
                    }
                }
            }
        } else if (keyword.equals("longitude")) {
            for (List<String> line : data) {
                for (int i = 0; i < line.size(); i++) {
                    if (i == 6) {
                        coordinates.add(Double.parseDouble(line.get(i)));
                    }
                }
            }
        }
        return Collections.min(coordinates);
    }

    /** Calculates the maximum value from either the latitudes or longitudes from the filtered data set.
     * @param data filtered housing data based on a user input price limit
     * @param keyword string that determines which data element being processed
     * */
    public static double calcMaximumVal(ArrayList<List<String>> data, String keyword) {
        ArrayList<Double> coordinates = new ArrayList<>();
        if (keyword.equals("latitude")) {
            for (List<String> line : data) {
                for (int i = 0; i < line.size(); i++) {
                    if (i == 5) {
                        coordinates.add(Double.parseDouble(line.get(i)));
                    }
                }
            }
        } else if (keyword.equals("longitude")) {
            for (List<String> line : data) {
                for (int i = 0; i < line.size(); i++) {
                    if (i == 6) {
                        coordinates.add(Double.parseDouble(line.get(i)));
                    }
                }
            }
        }
        return Collections.max(coordinates);
    }

    /** A subclass of the JPanel class. Initialized to plot housing data on a plot map. */
    private static class GPanel extends JPanel {
        public GPanel() {
        }

        /** GPanel constructor places a white square as the base graphical layer. */
        public void paintComponent(Graphics g) {
            int width = getSize().width;
            int height = getSize().height;
            g.setColor(Color.white);
            g.fillRect(0, 0, width, height);
        }

        /** Uses housing data from a filtered csv file to plot relative latitude and longitude locations based on price.
         * @param data Contains the price filterd data to generate plot points. */
        public void plotPoints(List<String> data, double maxLat, double minLat, double maxLong, double minLong) {
            Graphics plot = getGraphics();

            plot.setColor(Color.black);
            int latitude = latitudeReturn(Double.parseDouble(data.get(5)), maxLat, minLat);
            int longitude = longitudeReturn(Double.parseDouble(data.get(6)), maxLong, minLong);
            plot.fillOval(longitude, latitude, 5,5);
        }

        /** Calculates latitude coordinate for points relative to the GUI width
         * @param latitude the latitude coordinate from the csv file
         * @param maxLat the maximum latitude from the filtered data set
         * @param minLat the minimum latitude from the filtered data set
         * */
        public int latitudeReturn(double latitude, double maxLat, double minLat) {
            int endLat = 0;
            endLat = (int) ((latitude-minLat) / (maxLat-minLat)*getWidth());
            return endLat;
        }

        /** Calculates longitude coordinate for points relative to the GUI height
         * @param longitude the longitude coordinate from the csv file
         * @param maxLong the maximum longitude from the filtered data set
         * @param minLong the minimum longitude from the filtered data set
         * */
        public int longitudeReturn(double longitude, double maxLong, double minLong) {
            int endLong = 0;
            endLong = (int) ((longitude-minLong)/(maxLong-minLong)*getHeight());
            return endLong;
        }

    }

}