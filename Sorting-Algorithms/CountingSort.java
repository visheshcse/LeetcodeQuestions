package com.sorting.algorithms;

public class CountingSort {

    public static void main(String[] args) {
        int[] intArray = {11, 12, 19, 10, 15, 12};
        countingSort(intArray, 10, 19);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void countingSort(int[] intArray, int min, int max) {
        int k = max - min + 1;
        //Default value of int is 0 in java
        int[] countArray = new int[k];

        for (int value : intArray) {
            countArray[value - min]++;
        }

        int[] newInputArray = new int[intArray.length];
        int j = 0;
        for (int i = 0; i < countArray.length; i++) {
            while (countArray[i] > 0) {
                newInputArray[j++] = i + min;
                countArray[i]--;
            }
        }
        System.arraycopy(newInputArray, 0, intArray, 0, intArray.length);
    }
}
