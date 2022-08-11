import os
from tests_pages.base import WebPage
from tests_pages.elements import WebElement
from tests_pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # "Искать товары" главное поле //*[@id="header-search"]
    search = WebElement(id='header-search')

    # "Найти" кнопка /html/body/div[2]/div[3]/noindex/div/div/div[2]/div[2]/div/div/form/div/button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # "каталог товаров" кнопка вэб-элемента //*[@id="catalogPopupButton"]
    find_run_button = WebElement(id='catalogPopupButton')

    # "Баллы" ссылка на вэб-элемент
    find_run_btn_1 = WebElement(xpath='/html/body/div[4]/header/noindex/div/div/div[2]/div[3]/div[1]/div['
                                      '1]/div/div/div[1]/a/div/div[2]')

    # "Заказы" ссылка на вэб-элемент
    find_run_btn_2 = WebElement(xpath='//div[2]/div/a/span')

    # "Избранное" ссылка на вэб-элемент
    find_run_btn_3 = WebElement(xpath='//div[3]/div[1]/div[3]/div')

    # "Корзина" ссылка на вэб-элемент
    find_run_btn_4 = WebElement(xpath='//div[4]/div/div/a/span')

    # Кнопка вэб-элемента "Геолокация"
    find_run_btn_5 = WebElement(xpath='//div[1]/button[1]/div[2]')

    # "Яндекс.ру" ссылка на вэб-элемент
    find_run_btn_6 = WebElement(xpath='/html/body/div[4]/header/noindex/div/div/div[1]/div/a[1]/span')

    # "универмаг" cсылка на вэб-элемент
    find_run_btn_7 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[2]/div/div/a/span')

    # "одежда" cсылка на вэб-элемент
    find_run_btn_8 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[7]/div/div/a/span')

    # "дача" cсылка на вэб-элемент
    find_run_btn_9 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[5]/div/div/a/span')

    # "электроника" cсылка на вэб-элемент
    find_run_btn_10 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[8]/div/div/a/span')

    # "аптека" cсылка на вэб-элемент
    find_run_btn_11 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[4]/div/div/a/span')

    # "детям" cсылка на вэб-элемент
    find_run_btn_12 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[1]/li[9]/div/div/a/span')

    # "строительство и ремонт" cсылка на вэб-элемент
    find_run_btn_13 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[11]/a/span')

    # "распродажа" ссылка на вэб-элемент
    find_run_btn_14 = WebElement(xpath='/html/body/div[4]/noindex/div/div/a/img[1]')

    # "продавайте на маркете" ссылка на вэб-элемент
    find_run_btn_15 = WebElement(xpath='/html/body/div[4]/div[2]/noindex/div/div/nav/ul[2]/li[2]/div/div/a/span')

    # "одежда и обувь" ссылка на вэб-элемент
    find_run_btn_16 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[6]/a/span')

    # "спорт и отдых" ссылка на вэб-элемент
    find_run_btn_17 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[19]/a/span')

    # "детские товары" ссылка на вэб-элемент
    find_run_btn_18 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[8]/a/span')

    # "электроника" ссылка на вэб-элемент
    find_run_btn_19 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[3]/a/span')

    # "компьютеры" ссылка на вэб-элемент
    find_run_btn_20 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[4]/a/span')

    # Наименование товаров в списке
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Кнопка сортировки по рейтингу
    sort_products_by_rating = WebElement(css_selector='button[data-autotest-id="rorp"]')

    # Цена товаров в результате поиска
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    # Рейтинг товаров в результате поиска
    products_rating = ManyWebElements(xpath='//*[@id="page-uze2hw5u74"]/div/div/div/div/div['
                                            '1]/div/div/div/article/div[4]/div[1]/a[2]/div/div/div/div')

    # "как выбрать товар" ссылка на вэб-элемент
    find_run_btn_21 = WebElement(xpath='//noindex/div[3]/div[2]/div[1]/div[1]/a[1]')

    # "оплата и доставка" ссылка на вэб-элемент
    find_run_btn_22 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[1]/a[2]')

    # "обратная связь" ссылка на вэб-элемент
    find_run_btn_23 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[1]/a[3]')

    # "о сервисе" ссылка на вэб-элемент
    find_run_btn_24 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[1]/a[5]')

    # "участие в исследованиях" ссылка на вэб-элемент
    find_run_btn_25 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[1]/a[6]')

    # "возвраты" ссылка на вэб-элемент
    find_run_btn_26 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[1]/a[7]')

    # "личный кабинет продавца" ссылка на вэб-элемент
    find_run_btn_27 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[2]/a[1]')

    # "новости компании" ссылка на вэб-элемент
    find_run_btn_28 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[3]/a[1]')

    # "партнёрская программа" ссылка на вэб-элемент
    find_run_btn_29 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div[3]/div[2]/div[1]/div[3]/a[2]')

    # "яндекс маркет в AppGallery" ссылка на вэб-элемент
    find_run_btn_30 = WebElement(xpath='/html/body/div[4]/div[4]/footer/noindex/div['
                                       '1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div['
                                       '1]/div/div/div/div[3]/a/img')

    # "яндекс маркет в vk" ссылка на вэб-элемент
    find_run_btn_31 = WebElement(xpath='//div[3]/div[2]/div[2]/div/div[2]/a[2]')

    # "первый рекламный баннер справа" ссылка на вэб-элемент
    find_run_btn_32 = WebElement(xpath='/html/body/div[4]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div['
                                       '1]/div/div/div/div/div/div/div/div/a')

    # "войти" ссылка на вэб-элемент
    find_run_btn_33 = WebElement(xpath='/html/body/div[4]/header/noindex/div/div/div[2]/div[3]/div[1]/div['
                                       '6]/div/div/div[1]/a/span')

    # "продукты питания" ссылка на вэб-элемент
    find_run_btn_34 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[13]/a/span')

    # "красота" ссылка на вэб-элемент
    find_run_btn_35 = WebElement(xpath='//*[@id="catalogPopup"]/div/div/div/div/div/div/div[1]/div/ul/li[7]/a/span')