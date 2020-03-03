#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

#define THREAD_NUM 3

int flag = 0;

void *print_num(void *args)
{
    int timeout = 0;
    while (timeout < 10000) {
        printf("[target] thread %d is running, times : %d\n", *(int *)args, timeout);
        sleep(1);
        timeout++;
    }
    
    flag = 1;
    pthread_exit(NULL);
} 

int add(int a, int b)
{
	return a + b;
}

int main(int argc, char *argv[])
{
	int a = 3;
	int b = 4;
    int ret;
	
    pthread_t tids[THREAD_NUM] = {0};
    int index[THREAD_NUM] = {0};

    for (int i = 0; i < THREAD_NUM; i++) {
        index[i] = i;
        ret = pthread_create(tids + i, NULL, print_num, index + i);
        if (ret != 0) {
            printf("[target] pthread_create failed when create %d-th thread", i);
            pthread_exit(NULL);
            return -1;
        }
    }
    
    while (!flag) {
	   printf("[target] result is %d\n", add(a, b));
       sleep(1);
    }

	pthread_exit(NULL);
    return 0;
}
