#include<iostream>
using namespace std;
void bubbleSort(int *a, int n){
    for (int i = 0; i < n-1; i++){
        for(int j = 0; j < n-i-1; j++){
            if(a[j] > a[j+1]){
                swap(a[j],a[j+1]);
            }
        }
    }
}
void printArray(int *a, int n){
    for(int i = 0; i < n; i++){
        cout<<a[i]<<" ";
    }
}

int main(){
    int a[] = {7,49016,254,8194,7561,1,46};
    bubbleSort(a,7);
    printArray(a,7);
    return 0;
}
