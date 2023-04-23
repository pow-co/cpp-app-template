FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get -y install python3-pip build-essential manpages-dev software-properties-common git cmake

RUN pip install conan

RUN conan profile detect

COPY . /home/conan/cpp-app-template
WORKDIR /home/conan/cpp-app-template
RUN chmod -R 777 .

RUN conan install . --build=missing
RUN CONAN_CPU_COUNT=1 conan build .

CMD ./bin/CppAppTemplate
