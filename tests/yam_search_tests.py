import pytest
from tests_pages.links import MainPage


# Тест №1 Проверка поиска / данные на русском
def test_check_main_search_rus(web_browser):
    """ Главный поиск работает корректно. """
    page = MainPage(web_browser)
    page.search = 'айфон 12'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'iPhone' or 'iPhone 12' in title.lower(), msg


# Тест №2 Проверка поиска / английские данные введены на русской раскладке клавитатуры
def test_check_wrong_input_in_search0(web_browser):
    """ Проверка не правильного ввода с клавиатуры даёт правильный результат поиска. """
    page = MainPage(web_browser)
    page.search = 'шзрщту 12'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iPhone 12' in title.lower(), msg


# Тест №3 Проверка поиска / данные на английском
def test_check_main_search_eng(web_browser):
    """ Главный поиск работает корректно. """
    page = MainPage(web_browser)
    page.search = 'iPhone 12'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'iPhone' or 'iPhone 12' in title.lower(), msg


# Тест №4 Проверка поиска / не корректные данные на английском на русской раскладке клавиатуры
def test_check_wrong_input_in_search1(web_browser):
    page = MainPage(web_browser)
    page.search = 'шзрщт 12'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iPhone 12' in title.lower(), msg


# Тест №5 Проверка функции сортировки 1 / сортировка по цене позиций "фотоаппарат Panasonic"
def test_check_sort_by_price1(web_browser):
    page = MainPage(web_browser)
    page.search = 'одеяло'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №6 Проверка функции сортировки 2 / сортировка по цене позиций "шуруповерт"
def test_check_sort_by_price2(web_browser):
    page = MainPage(web_browser)
    page.search = 'шуруповерт'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №7 Проверка функции сортировки 3 / сортировка по цене позиций "кресло компьютерное"
def test_check_sort_by_price3(web_browser):
    page = MainPage(web_browser)
    page.search = 'кресло компьютерное'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №8 Проверка функции сортировки 4 / сортировка по цене позиций "цепная пила электрическая"
def test_check_sort_by_price4(web_browser):
    page = MainPage(web_browser)
    page.search = 'цепная пила электрическая'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №9 Проверка функции сортировки 5 / сортировка по цене позиций "ракетка теннисная"
def test_check_sort_by_price6(web_browser):
    page = MainPage(web_browser)
    page.search = 'ракетка теннисная'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №10 Проверка функции сортировки 6 / сортировка по рейтингу позиций "фен Xiaomi"
def test_check_sort_by_price7(web_browser):
    page = MainPage(web_browser)
    page.search = 'фен Xiaomi'
    page.search_run_button.click()
    page.sort_products_by_rating.scroll_to_element()
    page.sort_products_by_rating.click()
    page.wait_page_loaded()
    all_rating = page.products_rating.get_text()
    all_rating = [float(p.replace(' ', '')) for p in all_rating]
    print(all_rating)
    print(sorted(all_rating))
    assert all_rating == sorted(all_rating), "Сортировка по цене не работает!"


# Тест №11 Проверка функции сортировки 7 / сортировка по цене позиций "процессор AMD"
def test_check_sort_by_price8(web_browser):
    page = MainPage(web_browser)
    page.search = 'процессор AMD'
    page.search_run_button.click()
    page.sort_products_by_rating.scroll_to_element()
    page.sort_products_by_rating.click()
    page.wait_page_loaded()
    all_rating = page.products_rating.get_text()
    all_rating = [float(p.replace(' ', '')) for p in all_rating]
    print(all_rating)
    print(sorted(all_rating))
    assert all_rating == sorted(all_rating), "Сортировка по цене не работает!"


# Тест №12 Проверка функции сортировки 8 / сортировка по цене позиций "камера Panasonic"
def test_check_sort_by_price9(web_browser):
    page = MainPage(web_browser)
    page.search = 'камера Panasonic'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №13 Проверка функции сортировки 9 / сортировка по цене позиций "рюкзак для ноутбука"
@pytest.mark.xfail(reason="Фильтр по цене не работает")
def test_check_sort_by_price10(web_browser):
    """ Сортировка по цене работает корректно.
        Возможна ошибка из-за бага сортировки.
    """
    page = MainPage(web_browser)
    page.search = 'рюкзак для ноутбука'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"


# Тест №14 Проверка функции поиска главной страницы
def test_main_search_natural_spruse8(web_browser):
    page = MainPage(web_browser)
    page.search = 'санки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'санки' in title.lower(), msg


# Тест №15 Проверка функции поиска главной страницы
def ttest_main_search_natural_spruse7(web_browser):
    page = MainPage(web_browser)
    page.search = 'коньки'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'коньки' in title.lower(), msg


# Тест №16 Проверка функции поиска главной страницы
def test_main_search_natural_spruse6(web_browser):
    page = MainPage(web_browser)
    page.search = 'мыло'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'мыло' in title.lower(), msg


# Тест №17 Проверка функции поиска главной страницы
def test_main_search_natural_spruse5(web_browser):
    page = MainPage(web_browser)
    page.search = 'кастрюля'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'кастрюля' in title.lower(), msg


# Тест №18 Проверка функции поиска главной страницы
def test_main_search_natural_spruse4(web_browser):
    page = MainPage(web_browser)
    page.search = 'корпус для компьютера aerocool cylon wg черный'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'корпус для компьютера aerocool cylon wg черный' in title.lower(), msg


# Тест №19 Проверка функции поиска главной страницы
def test_main_search_natural_spruse3(web_browser):
    page = MainPage(web_browser)
    page.search = 'подушка ортопедическая'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'подушка ортопедическая' in title.lower(), msg


# Тест №20 Проверка функции поиска главной страницы
def test_main_search_natural_spruse2(web_browser):
    page = MainPage(web_browser)
    page.search = 'телевизор Xiaomi'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'телевизор Xiaomi' in title.lower(), msg


# Тест №21 ППроверка функции поиска главной страницы
def test_main_search_natural_spruse1(web_browser):
    page = MainPage(web_browser)
    page.search = 'наволочка'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'наволочка' in title.lower(), msg

