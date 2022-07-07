#include<bits/stdc++.h>
using namespace std;


bool binarySearch(int arr[], int s, int e, int k){

	if (s > e)
		return false;

	int mid = s + (e-s) / 2;

	if (arr[mid] == k)
		return true;

	else if(arr[mid] < k)
		return binarySearch(arr, mid+1, e, k);
	else
		return binarySearch(arr, s, mid-1, k);
}

int main(){
	int arr[5] = {2, 4, 6, 8, 9};
	int size = 5;
	int key = 4;
	bool res = binarySearch(arr, 0, size, key);
	if (res)
		cout << "Present"<<endl;
	else
		cout << "Absent" << endl;
	return 0;
}