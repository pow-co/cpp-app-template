from conans import ConanFile, CMake

class BoostMinerConan(ConanFile):
    name = "CppAppTemplate"
    version = "0.2.4"
    license = "OpenSource"
    author = "Powco"
    url = "https://github.com/ProofOfWorkCompany/cpp-app-template"
    description = "Best practices with c++"
    topics = ("bitcoin", "mining", "cpu", "sha256", "proofofwork", "boost")
    settings = "os", "compiler", "build_type", "arch"   
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "src/*"
    requires = "gtest/1.12.1"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("BoostMiner", dst="bin", keep_path=False)
