#include<bits/stdc++.h>
using namespace std;

string keypad[] = {"", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};

void solve(string ip, string op, int i=0){
	if(ip[i] == '\0'){
		cout<<op<<endl;
		return;
	}

	int current_digit = ip[i] - '0';
	if (current_digit == 0 || current_digit == 1)
		solve(ip, op, i+1);

	for (int k = 0; k < keypad[current_digit].size(); k++){
		solve(ip, op + keypad[current_digit][k], i+1);
	}
	return;
}

int main(){
	string ip;
	cout << "> ";
	cin >> ip;
	string op;
	solve(ip, op);
	return 0;
}