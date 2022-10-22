#include<iostream>
using namespace std;
int main(){
	int *arr{new int[10]{2,4,6,8,10,12,14,16,18,20}};
	cout<<"Array with multiplication table: ";
	for(int i=0;i<10;i++){
		cout<<arr[i]<<endl;
	}
	delete(arr);
}