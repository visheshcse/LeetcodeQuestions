#include<iostream>
using namespace std;
void selectionSort(int *a, int n){
    int minpos;
    for (int i = 0; i < n-1; i++){
        minpos = i;
        for(int j = i+1; j < n; j++){
            if(a[j] <= a[minpos]){
                minpos = j;
            }
        }
        swap(a[i],a[minpos]);
    }
}
void printArray(int *a, int n){
    for(int i = 0; i < n; i++){
        cout<<a[i]<<" ";
    }
}

int main(){
    int a[] = {7,49016,254,8194,7561,1,46};
    selectionSort(a,7);
    printArray(a,7);
    return 0;
}
