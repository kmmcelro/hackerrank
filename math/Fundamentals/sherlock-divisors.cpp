/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Sherlock and Divisors
# link: https://www.hackerrank.com/challenges/sherlock-and-divisors/problem


Task
Watson gives an integer N to Sherlock and asks him: What is the number of divisors of N that are divisible by 2?.
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'divisors' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

int divisors(int n) { 
    if (n % 2 == 1){
        return 0;
    }
    else{
        int num = 1;
        for(int i = 2; i <= sqrt(n); i++){
            if (n % i == 0){
                if(i == n/i && i % 2 == 0){ // case both factors being checked are the same and even
                    num++;
                }
                else if (i % 2 == 0 && (n/i) % 2 == 0){ // both factors are even
                    num += 2;
                }
                else if(i % 2 == 0){ // only i is even
                    num++;
                } 
                else if ((n/i) % 2 == 0){ //only n/i is even
                    num++;
                }
            }
        }
        return num;
    }

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

        int n = stoi(ltrim(rtrim(n_temp)));

        int result = divisors(n);

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
