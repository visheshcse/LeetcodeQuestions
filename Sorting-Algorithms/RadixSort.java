package com.sorting.algorithms;

public class RadixSort {
    public static void main(String[] args) {
        int[] intArray = {11, 12, 19, 10, 15, 12};
        radixSort(intArray, 10, 19);
        System.out.println("The sorted array is: ");
        for (int i : intArray) {
            System.out.print(i + " , ");
        }
    }

    private static void radixSort(int[] intArray, int radix, int width) {
        for (int i = 0; i < width; i++) {
            radixSingleSort(intArray, i, radix);
        }
    }

    private static void radixSingleSort(int[] intArray, int position, int radix) {
        int[] countArray = new int[radix];
        for (int i = 0; i < intArray.length; i++) {
            countArray[getSingleDigit(intArray[i], position, radix)]++;
        }
        for (int i = 1; i < countArray.length; i++) {
            countArray[i] += countArray[i - 1];
        }
        int[] tempArray = new int[intArray.length];
        for (int i = intArray.length - 1; i >= 0; i--) {
            tempArray[--countArray[getSingleDigit(intArray[i], position, radix)]] = intArray[i];
        }
        System.arraycopy(tempArray, 0, intArray, 0, intArray.length);
    }

    private static int getSingleDigit(int value, int position, int radix) {
        return (int) (value / Math.pow(10, position) % radix);
    }
}
