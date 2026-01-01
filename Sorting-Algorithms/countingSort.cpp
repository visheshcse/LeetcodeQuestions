#include<iostream>
using namespace std;

void printArray(int *a, int n){
    for(int i = 0; i < n; i++){
        cout<<a[i]<<" ";
    }
}
void countingSort(int *a,int n){
    int maxi = a[0],mini = a[0];
    for(int i = 0; i < n; i++){
        maxi = max(maxi,a[i]);
        mini = min(mini,a[i]);
    }
    int k = maxi - mini + 1;
    int *count = new int[k];
    int *temp = new int[n];
    fill_n(count,n,0);
    for(int i = 0; i < n; i++){
        count[a[i]-mini]++;
    }
    for(int i = 1; i < k; i++){
        count[i] += count[i-1];
    }
    for(int i = 0; i < n; i++){
        temp[count[a[i]-mini]-1] = a[i];
    }
    for(int i = 0; i < n; i++){
        a[i] = temp[i];
    }

}
int main(){
    //int a[] = {75,49,25,81,75,1,46};
    int a;
	cin>>a;
	switch(a){
	    case 1:
	         //int z = 9;
	         int y;
	         cout<<"1";
	         break;
	    case 2:
	        y=9;
	       // z=1;
	        cout<<"2";
	        break;

	}
    cout<<"a" + 10;
//    countingSort(a,7);
//    printArray(a,7);
    return 0;
}
