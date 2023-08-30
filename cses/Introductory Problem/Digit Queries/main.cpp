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

/*

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

1 -> 9 = 9 * 1 = 9 = 9; 1 9 
10 -> 99 = 90 * 2 = 180 = 189; 10 99
100 -> 999 = 900 * 3 = 2700 = 2889; 100 999
1000 -> 9999 = 9000 * 4 = 36000 = 38889; 1000 9999
10000 -> 9999 = 90000 * 5 = 450000 = 488889; 10000 99999
100000 -> 99999 = 900000 * 6 = 5400000 = 4888889; 100000 999999

width = number of character of an integer

total_character = 9 * (10^(width-1)) * width   +   9 * (10^(width-2)) * (width-1)   +   ....
start = (10^(width-1))
end =  9 * (10^(width-1)) + 9


queries:
15 = 9 * 1 


12

*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    ll t; cin >> t;
    while(t--){
        ll n; cin >> n;
        
        ll total_digit = 9;
        ll last_total_digit = 0;
        ll width = 1;
        ll ten = 1;
        while( total_digit  < n){
            width++;
            ten*= 10;
            last_total_digit = total_digit;
            total_digit += 9 * ten * width;
            
        }
        // cout << total_digit << '\n';
        // cout << "start: " << ten-1  << '\n';
        
        ll start = (ten)-1;
        ll left = n - last_total_digit;
        ll add = left / width;
        ll ind = abs(left % width);
        // if(width == 1){
        //     cout << left << '\n';
        //     continue;
        // }
        // 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950
        // cout << last_total_digit << ' ' << total_digit << '\n';
        // cout <<  start << " :start " << '\n';
        // cout << "left: " << left << '\n';
        // cout << "width: " << width << '\n';
        // cout << "add: " << add << '\n';
        // cout << "at: " << start + add << '\n';
        // cout << "ind: " << ind << '\n';
        ll inc = ind > 0;
        // cout << to_string(start+add + inc) << '\n';
        // cout << (inc == 0?width-1:ind-1) << '\n';
        cout << to_string(start+add + inc)[inc == 0?width-1:ind-1] << '\n';
        // cout << "------------------------\n";
        // ------------------------------
 
    }
    return 0;
}