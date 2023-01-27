#include <iostream>
#include <iterator>
#include <argh.h>
#include <boost/program_options.hpp>

namespace program_options = boost::program_options;

int main(int argc, char* argv[]) {

    argh::parser cmdl(argv);

    if (cmdl[{ "-v", "--verbose" }])

    std::cout << "Verbose, I am.\n";

    std::cout << "Hello C++" << std::endl;

      try {

        program_options::options_description desc("Allowed options");
        desc.add_options()
            ("help", "produce help message")
            ("compression", program_options::value<double>(), "set compression level")
        ;

        program_options::variables_map vm;
        program_options::store(program_options::parse_command_line(argc, argv, desc), vm);
        program_options::notify(vm);

        if (vm.count("help")) {
          std::cout << desc << "\n";
            return 0;
        }

        if (vm.count("compression")) {
          std::cout << "Compression level was set to "
                 << vm["compression"].as<double>() << ".\n";
        } else {
          std::cout << "Compression level was not set.\n";
        }
    }
    catch(std::exception& e) {
      std::cerr << "error: " << e.what() << "\n";
        return 1;
    }
    catch(...) {
      std::cerr << "Exception of unknown type!\n";
    }

    return 0;
}
