
# Тестовое задание

В данном задании требуется реализовать тестовый сценарий на примере сервиса Gitea https://github.com/go-gitea/gitea

Требования
В данном тесте использовалась работа с браузером Chrome.
Python 3.6 или выше
Виртуальное окружение (можно создать с помощью python -m venv venv)
Библиотеки из requirements.txt (установить с помощью pip install -r requirements.txt)
Docker Desktop (установить с официального сайта: https://www.docker.com/products/docker-desktop)

### Описание тестового сценария:
Тестовый сценарий должен реализовывать следующие действия:

Разворачивание Gitea локально в Docker с помощью Pytest.
Ожидание запуска контейнера и проверка доступности web-страницы сервиса Gitea на целевом выбранном порту с помощью Pytest и Requests. На странице должны находиться 3-5 эталонных CSS селекторов и эталонный текст.
Регистрация нового пользователя с помощью Selenium.
Создание нового репозитория с произвольным именем с помощью Selenium.
Создание коммита файла с произвольным именем и содержанием с помощью Selenium.
Открытие файла в браузере с помощью Selenium и проверка, что текст в файле соответствует оригинальному тексту.
Выключение контейнера.
Вывод отчёта о проведённых тестах в консоль.

### Конфигурация и запуск тестов:

1. Проведите клонирование репозитория командой:

   git clone https://github.com/Dimalright/gitea_project.git

2. Создайте виртуальное окружение и активируйте его:

    python -m venv venv

    source venv/scripts/activate
3. Установите необходимые библиотеки, обновите Docker, выполнив команды:

    pip install -r requirements.txt
    pip install docker --upgrade

4. Соберите Docker-образ и запустите контейнер с помощью следующей команды:

    docker build -t pytest .

5. Запустите последовательно тесты, выполнив команду:

    pytest test_gitea.py test_registration_new_user.py test_create_new_repository.py test_add_file_and_commit_in_rep.py test_open_file_and_check_text.py

После завершения тестов контейнер остановится и удалится автоматически

### Автор выполнения задания:

https://github.com/Dimalright