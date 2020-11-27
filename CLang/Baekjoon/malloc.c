#include <stdio.h>
#include <stdlib.h>

int main() {
    int answer;
    int *size;
    printf("Input number of integers:");
    scanf("%d", &answer);

    size = (int *)malloc(sizeof(int) * 5);
    
    for (int i = 0; i < answer; i ++) {
        printf("Input integer number %d: ", i+1);
        scanf("%d", &size[i]);
    }

    for (int i = 0; i < answer; i ++) {
        printf("value of number %d: %d\n", i, size[i]);
    }

    while (!graduated) {
        study();
        age ++; money --;
    }

    return 0;
    
}