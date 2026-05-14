/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Variable Sized Arrays
# link: https://www.hackerrank.com/challenges/variable-sized-arrays/problem


Task
Consider an n-element array, a, where each index i in the array contains a reference to an array of ki integers (where the value of k varies from array to array). 

Given a, you must answer q queries. Each query is in the format i j, where i denotes an index in array a and j denotes an index in the array located at a[i]. 
For each query, find and print the value of element j in the array at location a[i] on a new line.
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int q;
    cin >> n >> q;
    vector<vector<int>> v(n);
    int k;
    int temp;
    
    for(int i=0; i < n; i++){ // creating the vector of variable arrays
        cin >> k;
        for(int j=0; j < k; j++){
            cin >> temp;
            v[i].push_back(temp);
        }
    }
    
    int i0;
    int j0;
    
    for(int l=0; l < q; l++){ // reading the queries
        cin >> i0 >> j0;
        cout << v[i0].at(j0) << "\n";
    }
    return 0;
}