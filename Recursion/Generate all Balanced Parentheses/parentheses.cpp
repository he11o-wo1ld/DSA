#include <bits/stdc++.h>
using namespace std;

void solve(int open, int close, string op){
	if (open == 0 && close == 0){
		cout << op << end;
		return;
	}
	
	if (open != 0){
		string op1 = op;
		op1.push_back('(');
		solve(open-1, close, op);
	}
	
	if (open < close){
		string op2 = op;
		op2.push_back(')');
		solve(open, close-1, op);
	}
	return;
}

vector<string> Solution::generateParenthesis(int n) {
    int open=n;
    int close=n;
    string op="";
    vector<string> ans;
    solve(open,close,op,ans);
    return ans;
}

int main(){
	int n;
	cin >> n;
	
}
