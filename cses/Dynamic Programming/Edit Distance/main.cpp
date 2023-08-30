#include <bits/stdc++.h>
using namespace std;
#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


int main(){
    string a,b;
    cin >> a >> b;

    int dp[a.size()+1][b.size()+1];
    for(int i = 0;i <= a.size();i++)
        dp[i][0] = i;

    for(int i = 0;i <= b.size();i++)
        dp[0][i] = i;

    
    for(int i = 1;i <= a.size();i++){
        for(int j = 1;j <= b.size();j++){
            dp[i][j] = min(min(dp[i-1][j] + 1,dp[i][j-1] + 1),dp[i-1][j-1] + (a[i-1] != b[j-1]));
        }
    }
    cout << dp[a.size()][b.size()];
    return 0;
}