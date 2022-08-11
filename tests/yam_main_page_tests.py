# Команда для запуска автоматических тестов через терминал:


import pytest
from tests_pages.links import MainPage



# Тест №1 Проверка кнопки "Каталог"
def test_open_catalog(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    assert page.find_run_button


# Тест №2 Проверка кнопки "Баллы Плюс"
def test_open_scores(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_1.click()
    assert page.find_run_btn_1


# Тест №3 Проверка кнопки "Заказы"
def test_open_orders(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_2.click()
    assert page.find_run_btn_2


# Тест №4 Проверка кнопки "Избранное"
def test_open_favorites(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_3.click()
    assert page.find_run_btn_3


# Тест №5 Проверка кнопки "Корзина"
def test_open_basket(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_4.click()
    assert page.find_run_btn_4


# Тест №6 Проверка кнопки "Геолокации"
def test_open_geolocation(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_5.click()
    assert page.find_run_btn_5


# Тест №7 Проверка кнопки "Страница Яндекс"
def test_open_yandex(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_6.click()
    assert page.find_run_btn_6


# Тест №8 Проверка кнопки "Универмаг"
def test_open_univermag(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_7.click()
    assert page.find_run_btn_7


# Тест №9 Проверка кнопки "Одежда"
def test_open_odezda(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_8.click()
    assert page.find_run_btn_8


# Тест №10 Проверка кнопки "Дача"
def test_open_dacha(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_9.click()
    assert page.find_run_btn_9


# Тест №11 Проверка кнопки "Электроника"
def test_open_elektronika(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_10.click()
    assert page.find_run_btn_10


# Тест №12 Проверка кнопки "Аптека"
def test_open_apteka(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_11.click()
    assert page.find_run_btn_11


# Тест №13 Проверка кнопки "Товары для дома"
def test_open_tovary_dlia_doma1(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_9.click()
    assert page.find_run_btn_9


# Тест №14 Проверка кнопки "Детям"
def test_open_children(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_12.click()
    assert page.find_run_btn_12


# Тест №15 Проверка кнопки "Стройка"
def test_open_stroika(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_13.click()
    assert page.find_run_btn_13


# Тест №16 Проверка кнопки "Распродажа"
def test_open_sale(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_14.click()
    assert page.find_run_btn_14


# Тест №17 Проверка кнопки "продавайте на маркете"
def test_open_sell_on_the_market(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_15.click()
    assert page.find_run_btn_15


# Тест №18 Проверка кнопки "Обувь и аксессуары из меню каталога"
def test_open_odezhda_obuv_i_aksessuary(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_16.click()
    assert page.find_run_btn_16


# Тест №19 Проверка кнопки "Для спорта и отдыха из меню каталога"
def test_open_tovary_dlia_sporta_i_otdykha(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_17.click()
    assert page.find_run_btn_17


# Тест №20 Проверка кнопки "Детские товары из меню каталога"
def test_open_detskie_tovary(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_18.click()
    assert page.find_run_btn_18


# Тест №21 Проверка кнопки "Электроника из меню каталога"
def test_open_elektroniks(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_19.click()
    assert page.find_run_btn_19


# Тест №22 Проверка кнопки "Компьютеры из меню каталога"
def test_open_kompiuternaia_tekhnika(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_20.click()
    assert page.find_run_btn_20


# Тест №23 Проверка кнопки "Как выбрать товар"
def test_open_choice_goods(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_21.click()
    assert page.find_run_btn_21


# Тест №24 Проверка кнопки "Доставка"
def test_open_conditions(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_22.click()
    assert page.find_run_btn_22


# Тест №25 Проверка кнопки "Обратная связь"
def test_open_troubleshooting(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_23.click()
    assert page.find_run_btn_23


# Тест №26 Проверка кнопки "О сервисе"
def test_open_about(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_24.click()
    assert page.find_run_btn_24


# Тест №27 Проверка кнопки "Участие в исследованиях"
def test_open_jobs_pages_usability(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_25.click()
    assert page.find_run_btn_25


# Тест №28 Проверка кнопки "Возвраты"
def test_open_return(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_26.click()
    assert page.find_run_btn_26


# Тест №29 Проверка кнопки "личный кабинет продавца"
def test_open_partner(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_27.click()
    assert page.find_run_btn_27


# Тест №30 Проверка кнопки "новости компании"
def test_open_blog(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_28.click()
    assert page.find_run_btn_28


# Тест №31 Проверка кнопки "партнёрская программа"
def test_open_marketaff(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_29.click()
    assert page.find_run_btn_29


# Тест №32 Проверка кнопки "яндекс маркет в AppGallery"
def test_open_yandex_market_in_appgallery(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_30.click()
    assert page.find_run_btn_30


# Тест №33 Проверка кнопки "яндекс маркет в vk"
def test_open_yandex_market_in_vk(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_31.click()
    assert page.find_run_btn_31


# Тест №34 Проверка кнопки "Правый рекламный баннер"
def test_open_yandex_market_banner(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_32.click()
    assert page.find_run_btn_32


# Тест №35 Проверка кнопки "Войти"
def test_open_auth(web_browser):
    page = MainPage(web_browser)
    page.find_run_btn_33.click()
    assert page.find_run_btn_33


# Тест №36 Проверка кнопки "Продукты в меню каталога"
def test_prodyktu(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_34.click()
    assert page.find_run_btn_34


# Тест №37 Проверка кнопки "Красота в меню каталога"
def test_krasota(web_browser):
    page = MainPage(web_browser)
    page.find_run_button.click()
    page.find_run_btn_35.click()
    assert page.find_run_btn_35
