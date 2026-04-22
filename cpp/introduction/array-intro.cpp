/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Array Introduction 
# link: https://www.hackerrank.com/challenges/arrays-introduction/problem


Task
You will be given an array of N integers and you have to print the integers in the reverse order.
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i]; 
    }
     for (int j = 1; j < n+1; j++){
        cout << arr[n-j] << " ";
    }
    return 0;
}