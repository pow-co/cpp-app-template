from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from os import environ

class CPPAappTemplateConan(ConanFile):
    name = "CppAppTemplate"
    version = "0.3"
    license = "OpenSource"
    author = "Powco"
    url = "https://github.com/ProofOfWorkCompany/cpp-app-template"
    description = "Best practices with c++"
    topics = ("what", "this", "app", "is", "about")
    settings = "os", "compiler", "build_type", "arch"   
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "src/*"
    requires = "argh/1.3.2", "gtest/1.12.1", "boost/1.80.0", "taocpp-pegtl/3.2.7"

    def set_version (self):
        if "CIRCLE_TAG" in environ:
            self.version = environ.get ("CIRCLE_TAG")[1:]
        if "CURRENT_VERSION" in environ:
            self.version = environ['CURRENT_VERSION']
        else:
            self.version = "v0.0.13"

    def config_options (self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure_cmake (self):
        cmake = CMake (self)
        cmake.configure()
        return cmake
    
    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build (self):
        cmake = self.configure_cmake ()
        cmake.build ()

    def package (self):
        cmake = CMake(self)
        cmake.install()

    def package_info (self):
#        self.cpp_info.libdirs = ["lib"]  # Default value is 'lib'
        self.cpp_info.libs = ["CppAppTemplate"]
