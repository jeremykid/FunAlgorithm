CS - 223 Yale Study notes
http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html

6.4 C++
$ make helloworld
g++  -g3 -Wall  -c -o helloworld.o helloworld.cpp
g++ -g3 -Wall -o helloworld helloworld.o


6.4.1: Hello world.

***cpp

#include <iostream>

int 
main(int argc, const char **argv)
{
    std::cout << "hi\n";

    return 0;
}

***

6.4.2: References.

Call by Reference

passing a pointer

***cpp

void increment(int *x)
{
    (*x)++;
}

void increment(int &x)
{
    x++;
}

***

Call py Value

passing a value
***cpp

void increment(int x)
{
    x++;
}

***

6.4.3: Function overloading.

functions with the same name but different argument types 

***cpp

#include <iostream>

using namespace std;

const char *
typeName(int x)
{
    return "int";
}

const char *
typeName(double x)
{
    return "double";
}

const char *
typeName(char x)
{
    return "char";
}

int
main(int argc, const char **argv)
{
    cout << "The type of " << 3 << " is " << typeName(3) << ".\n";
    cout << "The type of " << 3.1 << " is " << typeName(3.1) << ".\n";
    cout << "The type of " << 'c' << " is " << typeName('c') << ".\n";

    return 0;
}

***

6.4.4 Classes.

