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
    string s;
    cin >> s;
    ll n = stoi(s);
    ll ans = 0;
    while(n){
        ll mx = 0;
        for(char ek:s){ 
            ll temp = ek - '0';
            if(temp > mx)
                mx = temp;

        }
        n -= mx;

        s = to_string(n);
        ans++;
    }
    cout << ans;
    return 0;

}