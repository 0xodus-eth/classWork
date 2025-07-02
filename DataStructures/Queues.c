// Static Implimentation of linear Queues using Arrays

#include <stdio.h>
// #include <conio.h>
#include <stdlib.h>
#define MAXSIZE 5

void initialize();
void lqinsert();
void lqdelete();
void lqraverse();
int queue[MAXSIZE];
int front, rear;

void main()
{
    // clrscr();
    initialize();
    int choice;
    while (1)
    {
        // clrscr();
        printf("\n Static Implimentation of linear Queues");
        printf("\n ---------------------------");
        printf("\n 1. Insert");
        printf("\n 2. Delete");
        printf("\n 3. Traverse");
        printf("\n 4. Exit");
        printf("\n ---------------------------");
        printf("\n Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            lqinsert();
            break;
        case 2:
            lqdelete();
            break;
        case 3:
            lqraverse();
            break;
        case 4:
            exit(0);
            break;
        default:
            printf("\n Invalid Choice");
        }
        // getch();
    }
}
// Function to initialize queue
void initialize()
{
    front = rear = -1;
}
// Function to insert element in Queue
void lqinsert()
{
    int num;
    if (rear == MAXSIZE - 1)
    {
        printf("\n Queue is Full");
        return;
    }
    printf("\n Enter the element to be inserted: ");
    scanf("%d", &num);
    rear++;
    queue[rear] = num;
    if (front == -1)
        front = 0;
}
// Function to delete element from Queue
void lqdelete()
{
    if (front == -1)
    {
        printf("\n Queue is Empty");
        return;
    }
    int num = queue[front];
    printf("\n Deleted element is: %d", num);
    front++;
    if (front > rear)
    {
        front = rear = -1;
    }
}

// Function to display Queue
void lqraverse()
{
    if (front == -1)
    {
        printf("\n Queue is Empty");
        return;
    }
    else
    {
        printf("\n Queue elements are:\n");
        for (int i = front; i <= rear; i++)
            printf("%d\t", queue[i]);
    }
}