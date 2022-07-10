#include<bits/stdc++.h>
using namespace std;

int getPower(int n, int m){
	if (m == 0)
		return 1;

	if (m == 1)
		return n;

	int prod = getPower(n, m/2);
	if (m%2 == 0)
		return prod * prod;
	else
		return n * prod * prod;
}

int main(){
	int num = 5;
	int mul = 3;
	int power = getPower(num, mul);
	cout << power << endl;
	return 0;
}