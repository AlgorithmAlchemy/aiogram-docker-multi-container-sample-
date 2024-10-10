#!/bin/bash

# Читаем токены из файла и запускаем контейнер для каждого токена
while IFS= read -r token; do
    docker run -d --name "bot_$token" --rm your_docker_image_name "$token"
done < api_keys.txt