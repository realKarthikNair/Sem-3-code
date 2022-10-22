//limits
#include<iostream>
#include<limits.h>
using namespace std;
int main()
{
	cout<<"Range of signed int\n"<<INT_MIN<< " TO "<<INT_MAX;
	cout<<"\n\nRange of unsigned int\n"<<UINT_MAX;
	cout<<"\n\nRange of signed char\n"<<SCHAR_MIN<< " TO "<<SCHAR_MAX;
	cout<<"\n\nRange of unsigned char\n"<<UCHAR_MAX;
	cout<<"\n\nRange of signed short int\n"<<SHRT_MIN<< " TO "<<SHRT_MAX;
	cout<<"\n\nRange of unsigned short int\n"<<USHRT_MAX;
	cout<<"\n\nRange of signed long int\n"<<LONG_MIN<< " TO "<<LONG_MAX;
	cout<<"\n\nRange of unsigned long int\n"<<ULONG_MAX;
}