#include <stdio.h>   // Standard I/O
#include <stdlib.h>  // For malloc, free, rand, qsort
#include <stdbool.h> // For boolean types (optional)
#include <time.h>    // For clock timing

#define MAX_ELEMENT_IN_ARRAY 1000000001 // Max value for random elements

// Comparison function for qsort (ascending)
int cmpfunc(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

// Generate an array with random integers
int *generate_random_array(int n)
{
    srand(time(NULL));                       // Seed RNG
    int *a = (int *)malloc(sizeof(int) * n); // Allocate memory
    for (int i = 0; i < n; ++i)
        a[i] = rand() % MAX_ELEMENT_IN_ARRAY;
    return a;
}

// Make a copy of an array
int *copy_array(int a[], int n)
{
    int *arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        arr[i] = a[i];
    return arr;
}

// Insertion sort in ascending order
void insertion_sort_asc(int a[], int start, int end)
{
    for (int i = start + 1; i <= end; ++i)
    {
        int key = a[i];
        int j = i - 1;
        while (j >= start && a[j] > key)
        {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
}

// Merge two sorted arrays for merge sort
void merge(int a[], int start, int end, int mid)
{
    int i = start, j = mid + 1, k = 0;
    int *aux = (int *)malloc(sizeof(int) * (end - start + 1)); // Temp array

    while (i <= mid && j <= end)
    {
        if (a[i] <= a[j])
            aux[k++] = a[i++];
        else
            aux[k++] = a[j++];
    }

    while (i <= mid)
        aux[k++] = a[i++];
    while (j <= end)
        aux[k++] = a[j++];

    for (i = start, k = 0; i <= end; ++i, ++k)
        a[i] = aux[k];

    free(aux); // Free temp memory
}

// Recursive merge_sort implementation
void __merge_sort(int a[], int start, int end)
{
    if (start < end)
    {
        int mid = start + (end - start) / 2;
        __merge_sort(a, start, mid);
        __merge_sort(a, mid + 1, end);
        merge(a, start, end, mid);
    }
}

// Merge_sort wrapper
void merge_sort(int a[], int n)
{
    __merge_sort(a, 0, n - 1);
}

// Hybrid of insertion_sort and merge_sort
void insertion_and_merge_sort_combine(int a[], int start, int end, int k)
{
    if (start < end)
    {
        int size = end - start + 1;
        if (size <= k)
        {
            insertion_sort_asc(a, start, end); // Use insertion for small arrays
            return;
        }
        int mid = start + (end - start) / 2;
        insertion_and_merge_sort_combine(a, start, mid, k);
        insertion_and_merge_sort_combine(a, mid + 1, end, k);
        merge(a, start, end, mid);
    }
}

// Test and compare sorting algorithms
void test_sorting_runtimes(int size, int num_of_times)
{
    int n = size;
    int t = num_of_times;

    // Time accumulators
    double insertion_sort_time = 0;
    double merge_sort_time = 0;
    double hybrid_time = 0;
    double qsort_time = 0;

    while (t--)
    {
        clock_t start, end;

        // Generate base array
        int *a = generate_random_array(n);

        // Insertion Sort
        int *b = copy_array(a, n);
        start = clock();
        insertion_sort_asc(b, 0, n - 1);
        end = clock();
        insertion_sort_time += (double)(end - start) / CLOCKS_PER_SEC;
        free(b);

        // Merge Sort
        int *c = copy_array(a, n);
        start = clock();
        merge_sort(c, n);
        end = clock();
        merge_sort_time += (double)(end - start) / CLOCKS_PER_SEC;
        free(c);

        // Hybrid Sort
        int *d = copy_array(a, n);
        start = clock();
        insertion_and_merge_sort_combine(d, 0, n - 1, 100); // k=100
        end = clock();
        hybrid_time += (double)(end - start) / CLOCKS_PER_SEC;
        free(d);

        // qsort
        int *e = copy_array(a, n);
        start = clock();
        qsort(e, n, sizeof(int), cmpfunc);
        end = clock();
        qsort_time += (double)(end - start) / CLOCKS_PER_SEC;
        free(e);

        free(a); // Free original array after all tests
    }

    // Calculate average times after all iterations
    insertion_sort_time /= num_of_times;
    merge_sort_time /= num_of_times;
    hybrid_time /= num_of_times;
    qsort_time /= num_of_times;

    // Print results
    printf("\nAverage time to sort %d elements over %d run(s):\n", size, num_of_times);
    printf("%-35s %f sec\n", "1. Insertion Sort:", insertion_sort_time);
    printf("%-35s %f sec\n", "2. Merge Sort:", merge_sort_time);
    printf("%-35s %f sec\n", "3. Insertion-Merge Hybrid:", hybrid_time);
    printf("%-35s %f sec\n", "4. qsort (C library):", qsort_time);
}

// Main function to test the sorting algorithms
int main()
{
    int size, runs;

    printf("Enter array size: ");
    scanf("%d", &size);

    printf("Enter number of test runs: ");
    scanf("%d", &runs);

    if (size <= 0 || runs <= 0)
    {
        printf("Size and runs must be positive!\n");
        return 1;
    }

    test_sorting_runtimes(size, runs);

    return 0;
}