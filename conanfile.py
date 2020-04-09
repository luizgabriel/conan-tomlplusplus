from conans import ConanFile, tools

class TOMLPPConan(ConanFile):
    name = "toml++"
    version = "1.2.0"
    license = "MIT"
    homepage = "https://github.com/marzer/tomlplusplus"
    url = "https://github.com/luizgabriel/conan-tomlplusplus"
    description = "TOML config parser and serializer for modern C++"
    topics = ("toml++", "toml", "parser")
    exports_sources = "toml++/include/*"
    no_copy_source = True

    def source(self):
        git = tools.Git(folder="toml++")
        git.clone("https://github.com/marzer/tomlplusplus.git", "v" + self.version)

    def package(self):
        self.copy("*.h")

    def package_id(self):
        self.info.header_only()