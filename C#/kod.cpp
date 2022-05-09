/*Find minimum number of rectangle posters needed to cover n adjacent building of given length and height*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stack>

using namespace std;

int main() {
	int n, h, posters = 0, tmp;
	stack<int> corners;

	// just to make the stack not empty
	corners.push(0);

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%*d %d", &h);
		while (corners.top() > h) {
			tmp = corners.top();
			corners.pop();
			posters++;
		}
		if (corners.top() != h) corners.push(h);
	}

	// -1 because first corner 0 should not be counted
	printf("%d", posters + corners.size() - 1);
}