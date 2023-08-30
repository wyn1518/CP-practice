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
const ll as = 10e6;

void solve(ll n,ll src,ll des,ll spr){
    if(n == 1){
        
        cout << src << ' ' << des << '\n';
        return;
    }
    solve(n-1,src,spr,des);
    cout << src << ' ' << des << '\n';
    solve(n-1,spr,des,src);
    
}  

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n; cin >> n;
    
    ll s = (1<<n) - 1;
    cout << s << '\n';
    solve(n,1,3,2);
    
    return 0;
}