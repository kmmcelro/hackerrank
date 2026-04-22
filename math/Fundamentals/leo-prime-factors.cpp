/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Leonardo's Prime Factors
# link: https://www.hackerrank.com/challenges/leonardo-and-prime/problem


Task
Leonardo loves primes and created q queries where each query takes the form of an integer, n. 
For each n, count the maximum number of distinct prime factors of any number in the inclusive range [1,n].
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'primeCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */

int primeCount(long n) {
    int count = 0;
    int primes[15] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}; // the smallest 15 prime numbers and the product of which is the largest product of unique prime numbers in the bounds
    for(int i = 0; i < 15; i++){
        if(primes[i] <= n){
            n = n/primes[i]; // integer division which will converge on the largest product of unique primes under n
            count++;
        }
    }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long n = stol(ltrim(rtrim(n_temp)));

        int result = primeCount(n);

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
