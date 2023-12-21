#include <stdlib.h>

int square(int i) {
	return i * i;
}

int *test_array() {
	int *out = malloc(1024);
	out[0] = 1;
	out[1] = 2;
	out[2] = 3;
	return out;
}
