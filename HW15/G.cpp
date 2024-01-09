#include <iostream>
#include <vector>
#include <cmath>

bool is_not_prime(int n) {
    if (n == 1) {
        return true;
    }
    int i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            return true;
        }
        i++;
    }
    return false;
}

int main() {
    int a, b;
    std::cin >> a >> b;

    std::vector<int> lst;
    for (int i = a; i <= b; i++) {
        lst.push_back(i);
    }

    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] && is_not_prime(lst[i])) {
            lst[i] = 0;
        }
    }

    std::vector<int> d;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i]) {
            d.push_back(lst[i]);
        }
    }

    for (int i : d) {
        std::cout << i << " ";
    }

    return 0;
}

