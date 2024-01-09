#!/bin/bash

# 도커 이미지 빌드하기
if [ "$1" == "build" ]; then
    echo "docker build --platform linux/amd64 -t docker-image:test ."
    docker build --platform linux/amd64 -t docker-image:test .

elif [ "$1" == "local" ]; then
    echo "docker run --platform linux/amd64 -p 9000:8080 docker-image:test"
    docker run --platform linux/amd64 -p 9000:8080 docker-image:test

    echo "make event in local endpoint"
    curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'