#include <iostream>

using namespace std;
class rectangle{
    float l;
    float b;
    double area;
    public:
    rectangle(){
        l=0;
        b=0;
        area=0;
    }
    double areafunc(float x,float y){
        l=x;
        b=y;
        area=l*b;
        return area;
    }
    rectangle(float x,float y){
        l=x;
        b=y;
    }
    rectangle(rectangle &r){
        l=r.l;
        b=r.b;
    }
    void display(){
        cout<<"Length="<<l<<endl;
        cout<<"Breadth="<<b<<endl;
        cout<<"Area="<<area<<endl;
    }
    ~rectangle(){
        cout<<"Destructor called"<<endl;
    }

};
int main(){
    rectangle r1;
    r1.display();
}