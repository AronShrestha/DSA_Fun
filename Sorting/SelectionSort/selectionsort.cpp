#include <iostream>
using namespace std;



void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(int arr[],int n){
 int min;
 int temp;
 for ( int i =0 ; i<n-1;i++){
    min = i;
    for(int j=i+1;j<n;j++){
        if (arr[min]>arr[j]){
            min = j;
        }
    }
    if(min!=i){
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
        // swap(&arr[min],&arr[i]);
    }

 }
}
int main(){
    int arr[] ={2,3,4,5,0,6,7,8,9};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr,n);
    for ( int i=0 ; i<n;i++){
        cout<<arr[i]<<endl;
    }
    return 0;
}