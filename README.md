# DRF practice

Небольшое приложение, которое требуется реализовать на курсе Stepik Academy.

**Что реализовано:**
- Развернуто стандартное приложение Django
- Установлен Django Rest Framework, requests, pillow, pathlib
- Созданы следующие модели: Item, User, Reviews
- Написан скрипт импорта в базу данных в формате Django Management Command
- Создано представлениe для получения товара по его ID - /api/v1/items/{id}

**Установка:**

Воспользуйтесь файлом requirements.txt для установки зависимостей.

Для импорта данных в базу данных воспользуйтесь командой:

*python manage.py import*

Перед запуском приложения обязательно сделайте импорт, чтобы загрузить картинки.
Сам скрипт импорта находится в папке users.

Добавлен функционал второй недели обучения:  
Реализованы методы исходя из [этой](https://editor.swagger.io/?url=https://gist.githubusercontent.com/k0t3n/f2207e98bdc80c81ee54dc011366f385/raw/schema.json) OpenAPI схемы.