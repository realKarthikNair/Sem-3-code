#include <iostream>
#include <string>

using namespace std;
class garment
{
    int code[5];
    string brand[5];
    float price[5];
    string name[5];
    public:
        garment()
        {
            for (int i = 0; i < 5; i++)
            {
                code[i] = 0;
                brand[i] = "";
                price[i] = 0;
                name[i] = "";
            }
        }
        void store_data()
        {
            for (int i = 0; i < 5; i++)
            {
                cout<<"Product Number "<<i+1<<endl;
                cout<<"Enter code: ";
                cin>>code[i];
                cout<<"Enter brand: ";
                cin>>brand[i];
                cout<<"Enter name: ";
                cin>>name[i];
                cout<<"Enter price: ";
                cin>>price[i];
            }
        }

        void print_data(int i)
        {
            for(int j=0; i<5; i++)
            {
                if (j==i)
                {
                    cout<<"Code: "<<code[i]<<endl;
                    cout<<"Brand: "<<brand[i]<<endl;
                    cout<<"Name: "<<name[i]<<endl;
                    cout<<"Price: "<<price[i]<<endl;
                }
            }
        }

        void search_brand(string b)
        {
            for (int i = 0; i < 5; i++)
            {
                if (brand[i]==b)
                {
                    print_data(i);
                }
        }
        }
         ~garment()
        {
            cout<<"Destructor called!"<<endl;
        }
};

int main()
{
    garment g;    
    string gr;
    g.store_data();
    cout<<"Enter brand name to search: ";
    cin>>gr;
    g.search_brand(gr);
    
}