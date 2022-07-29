#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> arr, int n, int i, int X){
	if (i==n){
		if(X == 0){
			return 1;
		}
		return 0;
	}

	int inc = solve(arr, n, i+1, X - arr[i]);
	int exc = solve(arr, n , i+1, X);

	return inc + exc;
}

int main(){
	vector<int> arr{1, 2, 3, 4, 5};
	int X = 11;
	cout << solve(arr, arr.size(), 0, X)<<endl;
	return 0;
}