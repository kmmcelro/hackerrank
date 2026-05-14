/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Structs
# link: https://www.hackerrank.com/challenges/c-tutorial-struct/problem


Task
You have to create a struct, named Student, representing the student's details, as mentioned above, and store the data of a student.

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


struct Student{
  int age;
  string first_name;
  string last_name;
  int standard;
    
};

int main() {
    Student st;
    
    cin >> st.age >> st.first_name >> st.last_name >> st.standard;
    cout << st.age << " " << st.first_name << " " << st.last_name << " " << st.standard;
    
    return 0;
}
