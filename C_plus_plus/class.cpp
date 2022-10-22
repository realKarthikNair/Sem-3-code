// C++ program to demonstrate
// accessing of data members

#include <iostream>
using namespace std;

class Student
{
	public: // Access specifier

	string std_name; // Data Members

	void printname() // Member Functions()
	{
	cout << "Student Name: " << std_name;
	}
};

int main() {

	Student obj1; // Declare an object

	obj1.std_name = "Awinash"; // accessing data member

	obj1.printname(); // accessing member function
	return 0;
}
