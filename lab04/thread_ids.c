#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *worker(void *arg)
{
    printf("Worker process ID: %d\n", getpid());
    printf("Worker thread ID: %lu\n",
           (unsigned long)pthread_self());

    return NULL;
}

int main(void)
{
    pthread_t thread;

    printf("Main process ID: %d\n", getpid());
    printf("Main thread ID: %lu\n",
           (unsigned long)pthread_self());

    if (pthread_create(&thread, NULL, worker, NULL) != 0) {
        perror("Failed to create thread");
        return 1;
    }

    pthread_join(thread, NULL);

    return 0;
}
