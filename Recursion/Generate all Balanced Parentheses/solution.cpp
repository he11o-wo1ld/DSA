#include<bits/stdc++.h>
using namespace std;

void solve(string output, int n, int open, int close, int i){
	if(i == 2*n){
		cout<<output<<endl;
		return;
	}

	if(open < n){
		output += '(';
		solve(output, n, open+1, close, i+1);
		output.pop_back();
	}

	if(close < open){
		output += ')';
		solve(output, n, open, close+1, i+1);
		output.pop_back();
	}
}

int main(){
	string output;
	int n;
	cout << '>';
	cin >> n;
	solve(output, n, 0, 0, 0);
	return 0;
}