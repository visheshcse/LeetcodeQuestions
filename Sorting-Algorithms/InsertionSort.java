package com.sorting.algorithms;

public class InsertionSort {
    public static void main(String[] args) {
        int[] intArray = {-11, 12, 39, 0, 42, -22};
        insertionSort(intArray);
        System.out.println("The sorted array is: ");
        for (int i:intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void insertionSort(int intArray[]) {
        for (int firstUnsortedIndex = 1; firstUnsortedIndex < intArray.length; firstUnsortedIndex++) {
            int newElement = intArray[firstUnsortedIndex];
            int i = firstUnsortedIndex;
            while (i >= 1 && intArray[i - 1] > newElement) {
                intArray[i] = intArray[i - 1];
                i--;
            }
            intArray[i] = newElement;
        }
    }
}
