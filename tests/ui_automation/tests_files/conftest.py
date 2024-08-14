from time import sleep
import pytest
from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.ui_automation.read_utilities.config import Config
from tests.ui_automation.page_objects.build_audience import BuildAudience





@pytest.fixture(params=["chrome"], scope='class')
def init_driver_all(request):
    """This fixture is used to test the all the other test functionality.
   """
    url = "https://qaomni.annalect.com/4359f5cc-6569-11e9-bc97-12cc0f0e8006/apps/an_construct_gwiae?"
    config = Config().get_config()

    admin_username = config["OmniLogin_QA"]["admin1_username"]
    admin_password = config["OmniLogin_QA"]["admin1_password"]


    web_driver = None
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--headless")
    options.add_argument("--test-type")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(7)
    shadow = Shadow(web_driver)
    request.cls.shadow = shadow

    web_driver.delete_all_cookies()
    web_driver.maximize_window()

    web_driver.delete_all_cookies()
    web_driver.maximize_window()
    web_driver.get(url)
    sleep(5)

    build_aud = BuildAudience(web_driver, shadow)
    build_aud.login(admin_username, admin_password)
    web_driver.refresh()
    sleep(40)
    web_driver.switch_to.frame(build_aud.iframe_ch3())


    yield
    web_driver.close()


