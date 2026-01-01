#include<iostream>
#include<stdlib.h>
int partition(int *, int, int);
using namespace std;
int pivot(int *a, int start, int end){
    int partitionIndex;
    int pivotIndex = rand(start,end);
    swap(a[pivotIndex],a[end]);
    return partitionIndex = partition(a,start,end);
}
int partition(int *a, int start, int end){
    int pivot = a[end];
    int partitionIndex = start;
    for (int i = start; i < end; i++){
        if(a[i] <= pivot){
           swap(a[i],a[partitionIndex]);
           partitionIndex++;
        }
    }
    swap(a[partitionIndex],a[end]);
    return partitionIndex;
}
void quickSort(int *a, int start, int end){
    if(start >= end){ return; }
    int partitionIndex = partition(a, start, end);
    quickSort(a,start,partitionIndex-1);
    quickSort(a,partitionIndex+1,end);
}
void printArray(int *a,int start, int end){
    for(int i = start; i <= end; i++){
        cout<<a[i]<<" ";
    }
}

int main(){
    int a[] = {7,49016,254,8194,7561,1,46};
    quickSort(a,0,6);
    printArray(a,0,6);
    return 0;
}
