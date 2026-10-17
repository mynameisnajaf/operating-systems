#include <stdio.h>
#include <pthread.h>
#include <sched.h>

void *worker(void *arg)
{
    int id = *(int *)arg;

    for (int i = 1; i <= 5; i++) {
        printf("Thread %d: step %d\n", id, i);
        sched_yield();
    }

    return NULL;
}

int main(void)
{
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;

    if (pthread_create(&t1, NULL, worker, &id1) != 0) {
        perror("Failed to create thread 1");
        return 1;
    }

    if (pthread_create(&t2, NULL, worker, &id2) != 0) {
        perror("Failed to create thread 2");
        pthread_join(t1, NULL);
        return 1;
    }

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Both threads finished.\n");

    return 0;
}
