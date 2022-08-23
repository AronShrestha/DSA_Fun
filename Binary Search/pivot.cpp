#include <iostream>
using namespace std;

int getPivot(int arr[],int n){
    int s,e,m;
    s=0;
    e=n-1;
    m=s+(e-s)/2;
    while(s<e){
        if(arr[m]>=arr[0]){
            s=m+1;
        }
        else{
            e=m;
        }
       m=s+(e-s)/2;
    }
    return s;
}
int main(){
    int arr[] ={2,3,4,5,0,6,7,8,9};
    cout<<"Pivot "<<getPivot(arr,9)<<endl;
}