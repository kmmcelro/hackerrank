/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Summing the N series
# link: https://www.hackerrank.com/challenges/summing-the-n-series/problem


Task
There is a sequence whose nth term is Tn = n^2 - (n - 1)^2.

Evaluate the series Sn = T1 + T2 + T3 + ... + Tn

Find Sn mod (1e9+7).
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'summingSeries' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */

int summingSeries(long n) {
    int sumN;
    const int modul = 1e9 + 7;
    n = n % modul; // transform n so it's the modulus of 1e9 + 7 
    sumN = n*n % modul; // transform the sum with modulus of 1e9 + 7 to make it int size
    return sumN;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long n = stol(ltrim(rtrim(n_temp)));

        int result = summingSeries(n);

        fout << result << "\n";
    }

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
