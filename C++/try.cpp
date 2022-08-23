#include<iostream>
using namespace std;


void print(int li[]){
    for(int i=0;i<3;i++){
        cout<<li[i]<<endl;
    }
}
int main(){
    int a=5;
    int li[]={a,2,3};
    print(li);

}