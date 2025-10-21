from selenium.webdriver.common.by import By


class OrderPage:
    # --- Поля формы заказа (страница 1) --
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Поля формы заказа (страница 2) ---
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # --- Кнопки и подтверждения ---
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # --- Логотипы ---
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")