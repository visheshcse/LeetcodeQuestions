package com.sorting.algorithms;

public class StableCountingSort {
    public static void main(String[] args) {
        int[] intArray = {11, 12, 19, 10, 15, 12};
        stableCountingSort(intArray, 10, 19);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void stableCountingSort(int[] intArray, int min, int max) {
        int k = max - min + 1;
        //Default value of int is 0 in java
        int[] countArray = new int[k];

        for (int value : intArray) {
            countArray[value - min]++;
        }

        for (int i = 1; i < countArray.length; i++) {
            countArray[i] += countArray[i - 1];
        }

        int[] newInputArray = new int[intArray.length];
        int j = 0;

        for (int i = intArray.length - 1; i >= 0; i--) {
            newInputArray[--countArray[intArray[i] - min]] = intArray[i];
        }
        System.arraycopy(newInputArray, 0, intArray, 0, intArray.length);
    }
}
