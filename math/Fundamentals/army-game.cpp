/* Author: kmmcelro
# This is my solution to the Hackerrank challenge, Diwali Lights
# link: https://www.hackerrank.com/challenges/game-with-cells/problem


Task
Luke is daydreaming in Math class. He has a sheet of graph paper with n rows and m columns, and he imagines that there is an army base in each cell for a total of n*m bases. 
He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. 
If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied.
Given n and m, what's the minimum number of packages that Luke must drop to supply all of his bases?

Ex:
Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply  bases. 
Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using  packages.
*/
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'gameWithCells' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

int gameWithCells(int n, int m) {
    int x,y;
    x = n / 2 + n % 2; 
    y = m / 2 + m % 2;
    return x*y;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    int result = gameWithCells(n, m);

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
