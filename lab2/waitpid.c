#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid = fork();

    if (pid < 0)
    {
        perror("fork");
        return 1;
    }

    if (pid == 0)
    {
        printf("Child: working...\n");
        sleep(5);
        printf("Child: finished.\n");

        return 5;
    }

    printf("Parent: waiting for child...\n");

    int status;
    waitpid(pid, &status, 0);

    printf("Parent: child finished.\n");

    return 0;
}