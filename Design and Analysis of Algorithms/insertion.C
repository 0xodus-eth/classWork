#include <stdio.h>

int main()
{
    int n, array[1000], c, d, t;

    // Ask the user to input number of elements
    printf("Enter number of elements\n");
    scanf("%d", &n);

    // ask the user to enter 'n' integers for the array
    printf("Enter %d integers\n", n);

    for (c = 0; c < n; c++)
    {
        scanf("%d", &array[c]);
    }

    for (c = 1; c < n; c++)
    {
        d = c;

        while (d > 0 && array[d - 1] > array[d])
        {
            // swap the elements
            t = array[d];
            array[d] = array[d - 1];
            array[d - 1] = t;

            d--;
        }
    }

    printf("Sorted list in ascending order:\n");

    for (c = 0; c < n; c++)
    {
        printf("%d\n", array[c]);
    }
    return 0;
}