// --- Day 8: Space Image Format ---
// https://adventofcode.com/2019/day/8

import java.util.ArrayList;
import java.util.List;

class SpaceImage {
    public static void main(String[] args) {
        Integer width = 25;
        Integer height = 6;
        String spaceImage = "puzzle-input";

        Integer startIndex = 0;
        List<String> layers = new ArrayList<String>();
        while (spaceImage.length() > startIndex) {
            layers.add(spaceImage.substring(startIndex, startIndex + width * height));
            startIndex += width * height;
        }
        System.out.println("Space image length " + spaceImage.length());
        System.out.println("Space image layers count " + layers.size());
        System.out.println("Space image first layer\n" + layers.get(0));

        int minZeroIndex = 0;
        int minZeroCount = 9999;
        for (int i = 0; i < layers.size(); i++) {
            int zeroCount = 0;
            for (int j = 0; j < layers.get(i).length(); j++) {
                if (layers.get(i).charAt(j) == '0') {
                    zeroCount++;
                }
            }
            if (minZeroCount > zeroCount) {
                minZeroCount = zeroCount;
                minZeroIndex = i;
            }
        }

        int oneCount = 0;
        for (int j = 0; j < layers.get(minZeroIndex).length(); j++) {
            if (layers.get(minZeroIndex).charAt(j) == '1') {
                oneCount++;
            }
        }

        int twoCount = 0;
        for (int j = 0; j < layers.get(minZeroIndex).length(); j++) {
            if (layers.get(minZeroIndex).charAt(j) == '2') {
                twoCount++;
            }
        }

        System.out.println("The product of Ones and Twos in the layer with the least zeroes is " + (oneCount * twoCount));

        int layerIndex = 0;
        char[] finalLayer = layers.get(layerIndex).toCharArray();
        for (int p = 0; p < finalLayer.length; p++) {
            layerIndex = 0;
            while (finalLayer[p] == '2') {
                layerIndex++;
                finalLayer[p] = layers.get(layerIndex).charAt(p);
            }
        }

        String finaleImage = new String(finalLayer);
        System.out.println("Final image layer\n" + finaleImage);
        finaleImage = finaleImage.replaceAll("(.{25})", "$1\n");
        System.out.println("Final image format\n" + finaleImage);
        finaleImage = finaleImage.replaceAll("1", Character.toString((char) 88));
        finaleImage = finaleImage.replaceAll("0", " ");
        System.out.println("Final image print\n\n" + finaleImage);
    }
}
