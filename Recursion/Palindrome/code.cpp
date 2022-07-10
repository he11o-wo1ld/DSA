#include<bits/stdc++.h>
using namespace std;

bool checkPalindrome(string& S, int l){
	if (l > S.length()-1 - l)
		return true;

	if (S[l] != S[S.length()-1 - l])
		return false;
	else
		checkPalindrome(S, l+1);
}


int main(){
	string S = "abcdeadcba";
	bool check = checkPalindrome(S, 0);
	if (check)
		cout << S << " : Is Palindrome"<< endl;
	else
		cout << S << " : Is Not Palindrome" << endl;
	return 0;
}