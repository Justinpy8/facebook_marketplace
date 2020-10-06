from src.all_imports import *

logs = utils.create_logger()


@pytest.fixture(scope='session')
def driver():
    """this is my pytest fixture (set of code to execute before/after my scope."""
    logs.info("********** This is the SETUP fixture to run before your scope of your fixture **********")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)  # read more about this

    logs.info("********** SETUP fixture completed **********")

    yield driver

    logs.info("******** This is the TEARDOWN steps after each of your scope *************")
    logs.info(f'Current url: {driver.current_url}')
    logs.info(f'Current title:  {driver.title}')
    logs.info(f'Current win_handle:  {driver.current_window_handle}')
    logs.info(f'Current name: {driver.name}')

    driver.quit()  # this will close the browser
    logs.info("browser is closed")
    logs.info("********  TEARDOWN completed *************")
