#include <stdio.h>

void printMessage() {
    printf("Hello, World!\n");
}

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    if (result > 0) {
        printMessage();
    }
    else {
        printf("Result is less than or equal to 0\n");
    }
    return 0;
}
