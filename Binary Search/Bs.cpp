#include <iostream>
using namespace std;

void display(int a[],int n){
    for ( int i =0;i<n;i++)
    {
        cout<<a[i]<<endl;
    }
}

int Search(int a[],int target,int m,int r, int l){
    if (l>r) return -1;
    if (target ==a[m]) return m;
    else{
        if (target>a[m]){
            l=m+1;
            m= l-(l-r)/2;//for handling last integer value 2^31-1
            return Search(a,target,m,r,l);

        }
        else if (target<a[m]){
            r=m-1;
            m=l- (l-r)/2;
            return Search(a,target,m,r,l);

        }
    }
    return -1;

    
}
int main(){
    int a[] ={1,2,3,4,5};
    int b[] = {1,3,4,5,6,7};
    int target=7;
    int ans=0;
    ans=Search(b,target,3,6,0);
    cout<<ans;

}