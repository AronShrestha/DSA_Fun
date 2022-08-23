#include<iostream>
#include<utility>
#include<vector>
#include<list>
using namespace std;


int main(){
    vector <int> v1={1,2,3,4,5,6,6,6,7,7,7,7};
    pair <int,int>p;
    list<int>::iterator p;
    for(p=v1.begin();p!=v1.end;++p){
        cout<<v1[p];
    }
}
