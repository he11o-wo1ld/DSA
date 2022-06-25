#include<bits/stdc++.h>
using namespace std;

#define ll long long unsigned int

void solve(string ip,string op){
	if(ip.length() == 0){
		cout<<'(';
        cout<<op;
        cout<<')';
		return;
	}
	
	string op1 = op;
	string op2 = op;
	
	op1.push_back(' ');
	op1.push_back(ip[0]);
	
	op2.push_back(ip[0]);
	
	ip.erase(ip.begin()+0);
	
	solve(ip, op1);
	solve(ip, op2);
}

int main(){
	int tc;
    cin>>tc;
    while(tc--)
    {
		string ip;
		cin >> ip;
		string op = "";
		op.push_back(ip[0]);
		ip.erase(ip.begin()+0);
		solve(ip, op);
	}
	
	return 0;
}