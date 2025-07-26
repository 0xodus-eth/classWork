#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 5;
    int *arr = (int *)malloc(n * sizeof(int));
    if (!arr)
    {
        printf("Memory allocation failed\n");
        return 1;
    }
    for (int i = 0; i < n; i++)
    {
        arr[i] = i * 10;
    }
    arr = realloc(arr, 10 * sizeof(int)); // Resize array
    for (int i = 5; i < 10; i++)
    {
        arr[i] = i * 10;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    free(arr); // Don't forget to free memory!
    return 0;
}