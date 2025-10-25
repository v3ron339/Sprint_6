from selenium.webdriver.common.by import By


class MainPageLocators:
    
    # Поля формы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Второй экран
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Раздел FAQ
    FAQ_SECTION = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_BY_TEXT = (By.XPATH, "//div[text()='{}']")
    FAQ_ANSWER_BY_TEXT = (By.XPATH, "//div[text()='{}']/following-sibling::div[@class='accordion__panel']")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[img[@alt='Yandex']]")
    # Баннер cookies
    COOKIE_BANNER_BUTTON = (By.ID, "rcc-confirm-button")