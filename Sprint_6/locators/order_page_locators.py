from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля формы заказа
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Дата и срок аренды
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    # Подтверждение заказа
    ORDER_BUTTON_FINAL = (By.XPATH, "//button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")


    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSM')]")

    RENT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, "//div[@class='Dropdown-root']")
    PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    CONFIRM_YES = (By.XPATH, "//button[contains(text(), 'Да')]")
    SUCCESS_POPUP = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")


    # Поля формы (первая часть)
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_FIRST_OPTION = (By.XPATH, "//li[@data-index='0']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка перехода к следующему шагу
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая часть формы
    RENT_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DATE_TODAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_PERIOD_DAY = (By.XPATH, "//div[text()='сутки']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")


    # Подтверждение заказа
    ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal__YZ-d3')]//button[text()='Да']")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons__1xGrp')]//button[text()='Заказать']")
    ORDER_MODAL_TITLE = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")
    # Окно успешного заказа
    ORDER_SUCCESS_POPUP = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

     # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")

    #  Нижняя кнопка "Заказать" (та, о которой ты написала)
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")

# Баннер cookies
    COOKIE_BANNER_BUTTON = (By.ID, "rcc-confirm-button")
    
    DATEPICKER_POPUP = (By.CLASS_NAME, "react-datepicker")

    RENT_OPTION_BY_TEXT = (  By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space(text())='{}']")
