FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get -y install python3-pip build-essential manpages-dev software-properties-common git cmake

RUN add-apt-repository ppa:ubuntu-toolchain-r/test

RUN apt-get update && apt-get -y install gcc-11 g++-11

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 20

RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 20

RUN pip install conan

RUN conan profile new default --detect

COPY . /home/conan/cpp-app-template
WORKDIR /home/conan/cpp-app-template
RUN chmod -R 777 .

RUN conan install .
RUN CONAN_CPU_COUNT=1 conan build .

CMD ./bin/CppAppTemplate
