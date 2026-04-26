# 🚀 flask-backend-middle

Инструкция по развертыванию и запуску проекта

### 🛠 Подготовка окружения

Сначала создайте рабочую директорию и настройте виртуальное окружение:

```
    mkdir flask-backend-middle
```

```
    cd flask-backend-middle
```

```
    py -3 -m venv .venv
```

### 📦 Установка зависимостей

Активируйте виртуальное окружение и установите необходимые библиотеки:

```
    .venv\Scripts\activate
```

```
    pip install -r requirements.txt
```

### 🐘 Настройка базы данных PostgreSQL

Запустите контейнер PostgreSQL с помощью Docker:

```
    docker run --name flask-backend-middle -p 5432:5432 -e POSTGRES_PASSWORD=root -d postgres
```

После запуска контейнера создайте базу данных:

```
    CREATE DATABASE "flask-backend-middle-db";
```

### ⚙️ Миграции и запуск

Примените последние миграции базы данных и запустите сервер:

```
    flask db upgrade
```

**Обычный запуск**

```
    flask --app main.py run
```

**Запуск в режиме отладки (Debug mode)**

```
    flask --app main.py run --debug
```

---

⚠️ _Убедитесь, что Docker запущен перед выполнением команд по настройке базы данных._
