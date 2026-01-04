package com.sorting.algorithms;

public class QuickSort {

    public static void main(String[] args) {
        int[] intArray = {-11, 12, 39, 0, 42, -22};
        quickSort(intArray);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    // Public entry: sorts entire array
    private static void quickSort(int[] intArray) {
        quickSort(intArray, 0, intArray.length - 1);
    }

    // Recursive quicksort on subarray [start, end]
    private static void quickSort(int[] intArray, int start, int end) {
        if (start >= end) {
            return;
        }

        int pivotIndex = partition(intArray, start, end);
        // Left side of pivot
        quickSort(intArray, start, pivotIndex - 1);
        // Right side of pivot
        quickSort(intArray, pivotIndex + 1, end);
    }

    // Partition using Lomuto scheme: pivot = intArray[end]
    private static int partition(int[] intArray, int start, int end) {
        int pivot = intArray[end];
        int i = start - 1;

        for (int j = start; j < end; j++) {
            if (intArray[j] <= pivot) {
                i++;
                swap(intArray, i, j);
            }
        }

        swap(intArray, i + 1, end);
        return i + 1;
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
