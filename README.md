
# Cpp Starter Template

## Build natively

We use the following technologies:

* c++ 20
* gcc 11
* cmake
* conan

If you cannot support any of them, try [building with docker](#build-with-docker).

```
conan install . --build=missing
conan build .

```
## Build with Docker

First, make sure docker is [in](https://docs.docker.com/engine/install/). If you are on Linux, be sure to follow the [docker post install instructions](https://docs.docker.com/engine/install/linux-postinstall/). Once docker is all ready, build with

```
docker build .

```
