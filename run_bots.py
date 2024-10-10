import subprocess

def run_bots():
    # Читаем токены из файла
    try:
        with open('api_keys.txt', 'r') as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print("Файл api_keys.txt не найден!")
        return

    # Запускаем контейнер для каждого токена
    for token in tokens:
        if not token:
            print("Токен не может быть пустым!")
            return

        token = token.strip()  # Убираем пробелы и переносы
        if token:  # Проверяем, что строка не пустая
            # Заменяем двоеточие на подчеркивание
            safe_token = token.replace(':', '_')
            container_name = f"bot_{safe_token}"
            # Формируем команду для запуска контейнера
            command = [
                'docker', 'run', '-d', '--name', container_name,
                '--rm', 'aiogram_bot_image', 'python', 'main.py', token.strip()
            ]

            try:
                # Запускаем команду
                subprocess.run(command, check=True)
                print(f"Запущен контейнер: {container_name}")
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при запуске контейнера {container_name}: {e}")

if __name__ == "__main__":
    run_bots()

