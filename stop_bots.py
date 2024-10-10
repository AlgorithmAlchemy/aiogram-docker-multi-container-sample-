import subprocess


def stop_bots():
    # Читаем токены из файла
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("Файл api_keys.txt не найден!")
        return

    # Останавливаем контейнер для каждого токена
    for token in tokens:
        token = token.strip()  # Убираем пробелы и переносы
        if not token:
            print("Токен не может быть пустым!")
            continue

        # Заменяем двоеточие на подчеркивание, чтобы совпадало с именами контейнеров
        safe_token = token.replace(':', '_')
        container_name = f"bot_{safe_token}"

        # Формируем команду для остановки контейнера
        command = ['docker', 'stop', container_name]

        try:
            # Останавливаем контейнер
            subprocess.run(command, check=True)
            print(f"Контейнер {container_name} остановлен.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при остановке контейнера {container_name}: {e}")


if __name__ == "__main__":
    stop_bots()
