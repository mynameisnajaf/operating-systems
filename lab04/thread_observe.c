
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *worker(void *arg)
{
    int id = *(int *)arg;

    printf("Worker %d started. PID=%d, TID=%lu\n",
           id, getpid(), (unsigned long)pthread_self());

    sleep(15);

    printf("Worker %d finished.\n", id);

    return NULL;
}

int main(void)
{
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;

    printf("Main process PID=%d\n", getpid());

    if (pthread_create(&t1, NULL, worker, &id1) != 0) {
        perror("Failed to create Worker 1");
        return 1;
    }

    if (pthread_create(&t2, NULL, worker, &id2) != 0) {
        perror("Failed to create Worker 2");
        pthread_join(t1, NULL);
        return 1;
    }

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("All workers finished.\n");

    return 0;
}