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

    private static void quickSort(int[] intArray) {
        if(start >= end){return;}
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
