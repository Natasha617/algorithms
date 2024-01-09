#include <iostream>
#include <vector>
#include <cmath>

int main() {
    int n;
    std::cin >> n;

    std::vector<std::string> result;

    for (int k = 0; k < n; ++k) {
        int i;
        std::cin >> i;

        bool flag = true;

        if (i == 1) {
            flag = false;
        }

        int j = 2;
        while (j * j <= i) {
            if (i % j == 0) {
                flag = false;
                break;
            }
            ++j;
        }

        if (flag) {
            result.push_back("YES");
        } else {
            result.push_back("NO");
        }
    }

    for (const auto& answer : result) {
        std::cout << answer << std::endl;
    }

    return 0;
}
