#include<bits/stdc++.h>
using namespace std;

void SortArray(int *arr, int n){
	if(n  == 0 || n == 1)
		return ;

	for(int i=0; i<n-1; i++){
		if(arr[i] > arr[i+1])
			swap(arr[i], arr[i+1]);
	}

	SortArray(arr, n-1);
}

int main(){
	int arr[7] = {2, 5, 3, 1, 6, 4, 9};
	SortArray(arr, 7);
	for(int i = 0; i < 7; i++)
		cout << arr[i];
	cout << endl;
	return 0;
}