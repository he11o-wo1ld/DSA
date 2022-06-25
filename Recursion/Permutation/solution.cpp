#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve(string S, int i){
	if (i == S.length() - 1){
		cout<<S<<" ";
		return;
	}

	for (int j = i; j < S.length(); j++){
		swap(S[i], S[j]);
		solve(S, i+1);
		swap(S[j], S[i]);
	}
}

int main(){
	string S;
	cin >> S;
	int index = 0;

	solve(S, index);
	return 0;
}