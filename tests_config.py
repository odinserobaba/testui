tests_config = [
    {
        "name": "Тест 1",
        "description": "Проверяет, что главная страница доступна.",
        "command": "pytest tests/test_main.py"
    },
    {
        "name": "Тест 2",
        "description": "Проверяет структуру данных на главной странице.",
        "command": "pytest tests/test_structure.py"
    },
    {
        "name": "Тест 3",
        "description": "Проверяет логи на главной странице.",
        "command": "pytest tests/test_logs.py"
    }
]
