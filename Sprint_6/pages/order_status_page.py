from selenium.webdriver.common.by import By


class OrderStatusPage:
    ORDER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    GO_BUTTON = (By.XPATH, "//button[text()='Go!']")
    VIEW_BUTTON = (By.XPATH, "//button[text()='Посмотреть']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Отменить заказ']")
    ORDER_INFO_BLOCK = (By.CLASS_NAME, "Track_OrderInfo__2fpDL")
    ORDER_NUMBER_HIGHLIGHT = (By.CLASS_NAME, "Track_Highlight__1WZh1")
    ORDER_ROADMAP = (By.CLASS_NAME, "Track_OrderRoadmap__3elUE") 
    # --11--