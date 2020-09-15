#include <stdio.h>

int main() {
    int a;
    int *b;

    a = 3;
    b = &a;

    printf("%d\n", b); // 주소값 출력
    printf("%d", *b); // 실제 값 출력
}