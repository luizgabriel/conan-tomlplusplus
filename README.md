# TOML++
The conan package for the TOML++ header only library.

## Installation
```sh
git clone https://github.com/google/filament conan-filament && cd conan-filament
conan export . marzer/stable
```

In your conanfile.txt, add:
```
[requires]
toml++/1.2.0@marzer/stable
```
