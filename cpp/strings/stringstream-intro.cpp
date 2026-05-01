/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, StringStream
# link: https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem


Task
In this challenge, we work with string streams.

stringstream is a stream class to operate on strings. It implements input/output operations on memory (string) based streams. stringstream can be helpful in different type of parsing. 

Given a string of comma delimited integers, return a vector of integers.
*/

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    int temp; 
    char ch;
    stringstream ss(str);
    vector<int> intstr;
    while(ss >> temp){
        intstr.push_back(temp); // moving from temp int to the vector to allocate space
        ss >> ch; // dumping the comma
    }
    return intstr;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}