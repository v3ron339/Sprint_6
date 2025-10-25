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

Sprint_6/
│
├── data/
│   └── urls.py
│
├── locators/
│   ├── main_page_locators.py
│   └── order_page_locators.py
│
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
│
├── tests/
│   ├── test_faq_questions.py
│   └── test_order_flow.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── allure_results/