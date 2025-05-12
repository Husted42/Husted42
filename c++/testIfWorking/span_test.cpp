// C++20 span test
// you can build the code with:
// clang++ -std=c++2a -stdlib=libc++ -Wall -Wextra -pedantic span_test.cpp -o span_test

#include <vector>
#include <span>
#include <iostream>


void print_content(std::span<int> container) {
    for(const auto &e : container) {
        std::cout << e << ' ';
    }
    std::cout << '\n';
}

int main() {
    int a[]{23, 45, 67, 89};
    print_content(a);

    std::vector<int> v{1, 2, 3, 4, 5};
    print_content(v);
}