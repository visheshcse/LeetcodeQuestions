#include<iostream>
using namespace std;
void merge(int *arr, int start, int end) {
    int mid = (start+end)/2;
    int k = 0, i = start, j = mid+1;
    int temp[100];
    while(i <=mid && j <=end) {
        if (arr[i] < arr[j]) {
            temp[k] = arr[i];
            i++; k++;
        } else {
            temp[k] = arr[j];
            j++; k++;
        }
    }
    while (i <=mid) {
        temp[k] = arr[i];
        k++;i++;
    }
    while (j <= end) {
        temp[k] = arr[j];
        k++; j++;
    }
    for (int k = start; k <= end; k++) {
        arr[k] = temp[k-start];
    }
}
void mergesort(int *arr, int start, int end) {
    if (start == end) {
        return;
    }
    int mid = (start+end)/2;
    mergesort(arr, start, mid);
    mergesort(arr, mid+1, end);
    merge(arr, start, end);

}
int main() {
    int arr[] = { 1,3,4,5,2,23,45,32,12,3,521,3,531,31};
    mergesort(arr, 0,13);
    for(int i = 0; i <= 13; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
