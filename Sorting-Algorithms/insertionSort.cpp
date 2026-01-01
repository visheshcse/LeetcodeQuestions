#include<iostream>
using namespace std;
void insertionSort(int *a, int n){
    for (int i = 0; i < n; i++){
        int value = a[i];
        int hole = i;
        while ( hole > 0 && a[hole-1] > value){
            a[hole] = a[hole-1];
            hole --;
        }
        a[hole] = value;
    }
}
void printArray(int *a, int n){
    for(int i = 0; i < n; i++){
        cout<<a[i]<<" ";
    }
}

int main(){
    int a[] = {7,49016,254,8194,7561,1,46};
    insertionSort(a,7);
    printArray(a,7);
    return 0;
}
