#include <stdio.h>
#include <stdlib.h>

void towersOfHanoi(int n, char source, char destination, char auxiliary)
{
    int totalMoves = (1 << n) - 1;

    printf("Solving Towers of Hanoi for %d disks:\n", n);
    printf("Moving from %c to %c using %c as auxiliary\n\n", source, destination, auxiliary);

    if (n % 2 == 0)
    {
        char temp = destination;
        destination = auxiliary;
        auxiliary = temp;
    }

    for (int i = 1; i <= totalMoves; i++)
    {
        int diskToMove = (i & -i);

        int diskNumber = 0;
        int temp = diskToMove;
        while (temp > 1)
        {
            temp >>= 1;
            diskNumber++;
        }
        diskNumber++;

        char from, to;

        if (diskNumber % 2 == 1)
        {
            int position = ((i - 1) / diskToMove) % 3;
            char cycle[3] = {source, destination, auxiliary};
            from = cycle[position];
            to = cycle[(position + 1) % 3];
        }
        else
        {
            int position = ((i - 1) / diskToMove) % 3;
            char cycle[3] = {source, auxiliary, destination};
            from = cycle[position];
            to = cycle[(position + 1) % 3];
        }

        printf("Move %d: Move disk %d from %c to %c\n", i, diskNumber, from, to);
    }

    printf("\nTotal moves: %d\n", totalMoves);
}

int main()
{
    int n;

    printf("Enter the number of disks: ");
    scanf("%d", &n);

    if (n <= 0)
    {
        printf("Number of disks must be positive!\n");
        return 1;
    }

    if (n > 10)
    {
        printf("Warning: %d disks will require %d moves!\n", n, (1 << n) - 1);
        printf("Continue? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y')
        {
            return 0;
        }
    }

    printf("\n");
    towersOfHanoi(n, 'A', 'C', 'B');

    return 0;
}