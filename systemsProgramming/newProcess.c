// Create a new process using the fork system call.
// Question: Write a program that creates a new child process using the fork system call and prints messages
// from both the parent and child processes.

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    pid_t pid = fork();
    if (pid == -1)
    {
        perror("fork");
        return 1;
    }
    else if (pid == 0)
    {
        printf("This is the child process.\n");
    }
    else
    {
        printf("This is the parent process.\n");
    }
    return 0;
}