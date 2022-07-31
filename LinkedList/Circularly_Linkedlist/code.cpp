#include<bits/stdc++.h>
using namespace std;

bool isCircular(Node* head){
    // Write your code here.
    if(head==NULL)
       return true;
   if(head->next==NULL)
       return false;
   if(head->next==head)
       return true;
   Node* fast=head->next->next;
   Node* slow=head->next;
   while(fast!=NULL && fast->next!=NULL && slow!=head && slow!=fast){
      
       fast=fast->next->next;
       slow=slow->next;
               
   }
   if(slow==head) return true;
   return false;
}


int main(){
	return 0;
}