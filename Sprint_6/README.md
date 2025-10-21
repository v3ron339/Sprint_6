UI-тесты сервиса "Самокат"

Автоматизированные UI-тесты учебного проекта "Яндекс Самокат" с использованием Python + Selenium + Pytest + Allure.

---

##  Стек технологий

- Python 3.11
- Pytest
- Selenium WebDriver
- Allure — для формирования отчётов
- Page Object Model (POM) — структура проекта


##  Структура проекта

sprint-6/
│
├── pages/                 # Page Object файлы (описание локаторов и действий)
│   ├── home_page.py
│   ├── order_page.py
│   └── faq_page.py
│
├── tests/                 # Автоматизированные тесты
│   ├── test_order_scooter.py
│   └── test_faq_section.py
│
├── conftest.py            # Фикстуры Selenium WebDriver
├── requirements.txt       # Зависимости проекта
└── README.md              # Документация