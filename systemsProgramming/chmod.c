#include <sys/stat.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    char filename[256];

    printf("Enter filename: ");
    scanf("%s", filename);

    if (chmod(filename, 0444) == -1)
    {
        perror("chmod");
        return 1;
    }

    printf("Permissions changed successfully for %s!\n", filename);
    return 0;
}