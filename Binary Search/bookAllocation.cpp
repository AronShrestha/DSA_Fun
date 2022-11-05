#include<iostream>
#include<utility>
#include<vector>
#include<numeric>
using namespace std;

bool check(vector<int> books, int std,int mid){
    int pages=0;
    int no_std=1;
    for( int i=0;i<books.size();i++){
        if( books[i]>mid){
            return false;
        }
        if (books[i]+pages>mid){
            no_std+=1;
            pages=books[i];
            if(no_std>std) return false;

        }
        else{
            pages+=books[i];
        }
    }
    return true;

}

int main(){
    vector <int> v1={10,20,30,40,50};
    int low,high,mid;
    int std=2;
    int size ;
    int ans;
    size = v1.size();
    low = v1[size-1];
    high  = accumulate(v1.begin(),v1.end(),0);
    cout<<"Low "<<low<<endl;
    cout<< "Hgh "<<high<<endl;
    mid = low - (low-high)/2;
    while (low <= high){
        
        
        if (check(v1,std,mid)){
            ans = mid;
            high = mid-1;

        }
        else{
            low = mid +1;
        }
        mid = low - (low-high)/2;
        
    } 
    cout<<"Max allocation possible is "<<ans;
    return 0;
}
