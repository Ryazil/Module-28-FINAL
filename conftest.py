import pytest
import allure
import uuid


@pytest.fixture
def chrome_options(chrome_options):
    # настройка параметров браузера / расположение chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    return chrome_options


@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    browser.set_window_size(1920, 1080)
    # Возвращение параметров браузера в тест:
    yield browser
    # Сброс параметров после проведения теста:
    if request.node.rep_call.failed:
        # Скриншот, если тест не прошёл:
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
            # Attach screenshot to Allure report:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass  # just ignore any errors here


def get_test_case_docstring(item):
    """ Эта функция получает строку документа из тестового примера и форматирует ее, чтобы показывать эту строку
    документа вместо имени тестового примера в отчетах.
    """
    full_name = ''
    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())
        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params
            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')
    return full_name


def pytest_itemcollected(item):
    """ Эта функция изменяет имена тестовых примеров "на лету" во время выполнения тестовых примеров.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменяет имена тестовых примеров "на лету", когда мы используем параметр --collect-only для
    pytest (чтобы получить полный список всех существующих тестовых примеров).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
