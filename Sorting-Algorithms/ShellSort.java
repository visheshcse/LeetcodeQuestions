package com.sorting.algorithms;

public class ShellSort {
    public static void main(String[] args) {
        int[] intArray = {-11, 12, 39, 0, 42, -22};
        shellSort(intArray);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void shellSort(int[] intArray) {
        for (int gap = intArray.length / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < intArray.length; i++) {
                int temp = intArray[i];
                int j = i;
                while (j >= gap && intArray[j - gap] > intArray[j]) {
                    intArray[j] = intArray[j - gap];
                    j -= gap;
                }
                intArray[j] = temp;
            }
        }
    }
}
