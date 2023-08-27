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
    ll n,x; cin >> n >> x;
    vector<ll> c(n);
    for(ll& i:c)
        cin >> i;
   
    vector<ll> rec(x+1);
    rec[0] = 1;
    for(ll el:c){
        for(ll i = 1;i <= x;i++){
            if(i - el >= 0 ){
                rec[i] += rec[i-el];
                rec[i] %= MOD;
            }
        }
    }
    cout << rec[x];
    return 0;

}