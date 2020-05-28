#include <stdlib.h>
#include <stdio.h>	
typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* insert(Node *head,int data)
{
    Node* temp = head;
    Node* temp2 = malloc(sizeof(Node));
    temp2 -> data = data;
    temp2 -> next = NULL;
    if(head == NULL) {
        head = temp2;
        return head;
    }
    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = temp2;
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
  display(head);
		
}
