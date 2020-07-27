#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* removeDuplicates(Node *head){
    if(head -> next != NULL) {
        Node *temp = (struct Node*)malloc(sizeof(Node));
        temp -> data = head -> data;
        temp -> next = NULL;
        Node *ans = temp;
        head = head -> next;
        while(head != NULL) {
            if(head -> data != temp -> data) {
                Node *temp2 = (struct Node*)malloc(sizeof(Node));
                temp2 -> data = head -> data;
                temp -> next = temp2;
                temp = temp -> next;
                head = head -> next;
            }
            else {
                head = head -> next;
            }
        }
        return ans;
    }
    else {
        return head;
    }
    return 0;
}

Node* insert(Node *head,int data)
{
  Node *p = (Node*)malloc(sizeof(Node));
  p->data = data;
  p->next=NULL;   
  
  if(head==NULL){
   head=p;  
  
  }
  else if(head->next==NULL)
  {
      head->next=p;
      
  }
  else{
  Node *start=head;
  while(start->next!=NULL)
    start=start->next;
  
  start->next=p;   
  
  }
      return head;
}
void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}
int main()
{
	int T,data;
    scanf("%d",&T);
    Node *head=NULL;	
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
    head=removeDuplicates(head);
	display(head);
		
}
