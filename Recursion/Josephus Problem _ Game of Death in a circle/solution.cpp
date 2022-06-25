#include <bits/stdc++.h>
using namespace std;

void solve(vector<int> ip, int k, int index, int& ans){
	if(ip.size() == 1){
		ans = ip[0];
		return;
	}
	
	index = (index+k) % ip.size();
	ip.erase(ip.begin()+index);
	solve(ip, k, index, ans);
	return;
}

int main(){
	int n;
	int k;
	cin >> n >> k;
	
	vector<int> ip;
	for (int i=1; i<=n; i++){
		ip.push_back(i);
	}
	
	k--;
	int index = 0;
	int ans = -1;
	
	solve(ip, k, index, ans);
	cout<<ans;
	return 0;
}