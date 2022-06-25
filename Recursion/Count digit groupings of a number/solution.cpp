#include<bits/stdc++.h>
using namespace std;

#define ll long long



vector <string> powerSet(string s)
{
    string op="";
    vector<string> v;
    solve(s,op,v);
    sort(v.begin(),v.end());

    return v;
}
void solve(string ip, string op, vector<string>& v){
    if(ip.length() == 0){
        v.pushback(op);
        return;
    }
    
    op1 = op;
    op2 = op;
    
    op1.push_back(' ');
    if (0 <= op2.length() <= ip.length()){
        op2.push_back('-');
        op2.push_back(ip[0]);
    }
    
    ip.erase(ip.begine()+0);
    return;
}
int TotalCount(string str){
    // Code here
    vector<string> v = powerSet(s);
    op = "";
    solve(str, op, v);
    return 0;
}