#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v;
    stack<int> s;

    int arr = [4,5,2,10,8];

    for(int i = 0; i<arr.size(); i++){
        if(arr.size() == 0){
            v.push_back(-1);
        }
        else if(s.size() > 0 && s.top() < afr[i]){
            v.push_back(s.top());
        }
        else if(s.size() > 0 && s.top() > arr[i]){
            while(s.size() > 0 && s.top() >= arr[i]){
                s.pop();
            }
            if (s.size() == 0){
                v.push_back(-1);
            } else {
                v.push_back(s.top());
            }
        }
        s.push_back(arr[i]);
    }
    return 0;
}