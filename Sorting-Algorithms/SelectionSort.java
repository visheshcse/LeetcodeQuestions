package com.sorting.algorithms;

public class SelectionSort {
    public static void main(String[] args) {
        int[] intArray = {-11, 12, 39, 0, 42, -22};
        selectionSort(intArray);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void selectionSort(int[] intArray) {
        int minpos;
        for (int firstUnsortedIndex = 0; firstUnsortedIndex < intArray.length-1; firstUnsortedIndex++) {
            minpos = firstUnsortedIndex;
            for (int i = firstUnsortedIndex; i < intArray.length; i++) {
                if (intArray[i] < intArray[minpos]) {
                    minpos = i;
                }
            }
            swap(intArray, firstUnsortedIndex, minpos);
        }
    }

    public static void swap(int[] intArray, int i, int j) {
        if (i == j) {
            return;
        }
        int temp = intArray[i];
        intArray[i] = intArray[j];
        intArray[j] = temp;
    }
}
