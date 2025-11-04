from selenium.webdriver.common.by import By


class MainPageLocators:
    
    # Поля формы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON_HEADER = ( By.XPATH,"//button[contains(@class,'Button') and text()='Заказать' and not(contains(@class,'Middle'))]")
    ORDER_BUTTON_FOOTER = ( By.XPATH,"//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    # Второй экран
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать' and contains(@class, 'Button_Button__ra12g')])[2]")
    QUESTIONS_BUTTONS = (By.CSS_SELECTOR, "div.accordion__button[id^='accordion__heading-']")
    QUESTIONS_ANSWERS = (By.CSS_SELECTOR, "div.accordion__panel[id^='accordion__panel-']")

    # Раздел FAQ
   # FAQ_SECTION = (By.ID, "accordion__heading-0")
    FAQ_SECTION = (By.CSS_SELECTOR, "div.Home_FAQ__3uVm4")
    FAQ_QUESTION = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    FAQ_ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")
    
    #FAQ_QUESTION_BY_TEXT = (By.XPATH, "//div[text()='{}']")
   # FAQ_ANSWER_BY_TEXT = (By.XPATH, "//div[text()='{}']/following-sibling::div[@class='accordion__panel']")
    #FAQ_SECTION = (By.XPATH, "//div[contains(@class,'Home_Faq__3uVm4')]")
   
   # Шаблонные локаторы для вопросов и ответов FAQ:
    FAQ_QUESTION_TEMPLATE = "//div[contains(@class, 'accordion__button') and text()='{text}']"
    FAQ_ANSWER_TEMPLATE = "//div[contains(@class, 'accordion__panel') and preceding-sibling::div[text()='{text}']]"

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    # Баннер cookies
    COOKIE_BANNER_BUTTON = (By.ID, "rcc-confirm-button")

    # --- Вспомогательные методы (динамические локаторы) ---
    @staticmethod
    def faq_question(text):
        """Возвращает локатор конкретного вопроса FAQ по тексту."""
        return (By.XPATH, MainPageLocators.FAQ_QUESTION_TEMPLATE.format(text=text))

    @staticmethod
    def faq_answer(text):
        """Возвращает локатор конкретного ответа FAQ по тексту вопроса."""
        return (By.XPATH, MainPageLocators.FAQ_ANSWER_TEMPLATE.format(text=text))