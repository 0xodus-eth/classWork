#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid = getpid();
    pid_t ppid = getppid();

    printf("Current process ID: %d\n", pid);
    printf("Parent process ID: %d\n", ppid);

    return 0;
}