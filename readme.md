

## Версия python: 3.10
## Установка зависимостей
```shell
pip install -r requirements.txt
```

## Лекция 1

### dto_attrs, dto_dataclasses, dto_naive, dto_pydantic
Варианты реализации концепта DTO

### shop
Пример реализации трехслойной структуры приложения


## Лекция 2
Пример реализации авторизации с использованием jwt-токенов и fastapi

Запуск:
1. Установить WorkingDirectory в папку
2. Пометить папкe lesson2 как source root
3. Скопироать .env.example с именем .env
4. Выполнить команду
```shell
uvicorn app.main:app --reload
```