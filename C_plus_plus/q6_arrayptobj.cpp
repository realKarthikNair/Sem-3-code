#include<iostream>
#include<string>

using namespace std;

class Garment{
    int code;
    string name;
    string brand;
    float price;

    public:
     void getdata(){
        cout<<"Code: "<<code<<endl;
        cout<<"Brand: "<<brand<<endl;
        cout<<"Price: "<<price<<endl;
        cout<<"Name: "<<name<<endl;
     }
      void putdata(){
        cout<<"Code: "<<endl;
        cin>>code;
        cout<<"Brand: "<<endl;
        cin>>brand;
        cout<<"Price: "<<endl;
        cin>>price;
        cout<<"Name: "<<endl;
        cin>>name;
      }
      
};

int main(){
  Garment *ptr=new Garment[5];
  for (int i=0; i<5; i++){
  ptr[i].putdata();
  }
  for (int i=0;i<5; i++){
  ptr[i].getdata();
  }
}
