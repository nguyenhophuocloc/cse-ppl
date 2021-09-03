#include <iostream>

using namespace std;
int *m;

int *foo(int x)
{

    static int y;

    int *z = new int;

    switch (x)
    {

    case 1:
        return &y;

    case 2:
        return &x;

    case 3:
        return z;

    case 4:
        return m;
    }
}
int main()
{
    cout << foo(2);
    return 0;
}