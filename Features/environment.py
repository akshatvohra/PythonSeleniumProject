from selenium.webdriver import Chrome


def before_all(context):
    path = "./Driver/chromedriver.exe"
    context.driver = Chrome(executable_path=path)
    context.driver.maximize_window()


def after_all(context):
    context.driver.close()
    print("Dne")