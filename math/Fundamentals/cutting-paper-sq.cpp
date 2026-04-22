/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Cutting Paper Squares
# link: https://www.hackerrank.com/challenges/p1-paper-cutting/problem


Task
Mary has an nxm piece of paper that she wants to cut into 1x1 pieces according to the following rules:

* She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
* Each cut is a straight line from one side of the paper to the other side of the paper. 

Given n and m, find and print the minimum number of cuts Mary must make to cut the paper into n*m squares that are 1x1 unit in size.
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

long solve(int n, int m) {
    long cutNum = (long) m * n - 1; // this is mathematically the amount of cuts you need
    return cutNum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    long result = solve(n, m);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
