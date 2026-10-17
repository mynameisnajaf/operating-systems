#include <stdio.h>
#include <unistd.h>

int main(void)
{
    char *args[] = {"echo", "Hello from execve()", NULL};

    printf("Before execve()\n");

    execve("/bin/echo", args, NULL);

    perror("execve");
    return 1;
}