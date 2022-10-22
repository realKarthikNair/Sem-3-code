#include<iostream>
#include<string>

using namespace std;

class Garment{
    int code[5];
    string name[5];
    string brand[5];
    float price[5];

    public:
     void getdata(){
      for (int i=0; i<5; i++) {
        cout<<"Code: "<<code[i]<<endl;
        cout<<"Brand: "<<brand[i]<<endl;
        cout<<"Price: "<<price[i]<<endl;
        cout<<"Name: "<<name[i]<<endl;
     }
     }
      void putdata(){
        for (int i=0; i<5; i++){
          cout<<"Code: "<<endl;
          cin>>code[i];
          cout<<"Brand: "<<endl;
          cin>>brand[i];
          cout<<"Price: "<<endl;
          cin>>price[i];
          cout<<"Name: "<<endl;
          cin>>name[i];
      }
      }
      
};

int main(){
    Garment g[5];
    for (int i=0; i<5; i++){
    g[i].putdata();
    }
    for (int i=0; i<5; i++){
    g[i].getdata();
    }
}