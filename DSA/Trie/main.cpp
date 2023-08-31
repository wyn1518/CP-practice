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

struct Node{
    bool end = false;
    map<char,Node*> character;
};
struct Trie{
    Node* root;
    Trie(){
        root = new Node();
    }
    void insert(char s[],ll n){
        Node* node = this->root;
        for(int i = 0;i < n;i++){
            
            if(node->character.find(s[i]) == node->character.end()){
                node->character[s[i]] = new Node();
            }
            node = node->character[s[i]];
        }
        node->end = true;
    }
    ll search(char word[],ll n){
        vector<ll> ans(n+1);
        ans[n] = 1;
        for(ll i = n-1;i >= 0;i--){
            Node* node = this->root;
            for(ll j = i;j < n;j++){
                if(node->character.find(word[j]) == node->character.end()){
                    // cout << "not found\n";
                    break;
                }
               
                node = node->character[word[j]];
                if(node->end){
                    ans[i] = (ans[i]%MOD + ans[j+1]%MOD)%MOD;
                }
            }
        }
        // for(ll el:ans){
        //     cout << el << ' ';
        // }
        // cout << '\n';
        return ans[0];
    }
};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string temp; cin >> temp;
    ll n = temp.size();
    // cout << n << '\n';
    char word[n];
    for(ll i = 0;i < temp.size();i++){
        word[i] = temp[i];
    }
    ll k; cin >> k;
    Trie trie;
    while(k--){
        cin >> temp;
        char c[temp.size()];
        
        for(ll i = 0;i < temp.size();i++)
            c[i] = temp[i];

        trie.insert(c,temp.size());
    }
    cout << trie.search(word,n);
    return 0;
}
