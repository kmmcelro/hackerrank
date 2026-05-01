/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Strings
# link: https://www.hackerrank.com/challenges/c-tutorial-strings/problem


Task
You are given two strings, a and b, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').

You are to output the following:
* In the first line print two space-separated integers, representing the length of a and b respectively.
* In the second line print the string produced by concatenating a and b as (a+b).
* In the third line print two strings separated by a space, a' and b'. a' and b' are the same as a and b, respectively, except that their first characters are swapped.

*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a;
    string b;
    cin >> a;
    cin >> b;
    
    cout << a.size() << " " << b.size() << "\n";
    cout << a+b << "\n";
    
    char c0 = a[0];
    
    a[0] = b[0];
    b[0] = c0;
    
    cout << a << " " << b << "\n";
    
    return 0;
}
