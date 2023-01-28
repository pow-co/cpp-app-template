#include <iostream>
#include <argh.h>
#include <websocketpp/client.hpp>

int main(int argc, char* argv[]) {

    argh::parser cmdl(argv);

    if (cmdl[{ "-v", "--verbose" }])

        std::cout << "Verbose, I am.\n";

    std::cout << "Hello C++" << std::endl;
}
