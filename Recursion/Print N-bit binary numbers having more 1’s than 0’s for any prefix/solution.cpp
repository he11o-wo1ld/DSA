#include <bits/stdc++.h>
using namespace std;

void solve(int N, string op, int one, int zero){
    if (N == 0){
        cout << op << " ";
        return;
    }
    
    string op1 = op;
    op1.push_back('1');
    solve(N-1, op1, one+1, zero);
    
    if (one > zero){
        string op2 = op;
        op2.push_back('0');
        solve(N-1, op2, one, zero+1);
    }
    return;
}

int main(){
    int n;
    cin >> n;
    while (n--){
        int N;
        cin >> N;
        string op = "";
        int one = 0;
        int zero = 0;
        
        solve(N, op, one, zero);    
    }
    return 0;
}
