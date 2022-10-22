#include<iostream>
using namespace std;
inline void printsum(int num1, int num2) {
    cout<<num1+num2<<endl;
}
int main(){
    printsum(10,20);
    printsum(2,5);
    printsum(100,400);
    return 0;
}