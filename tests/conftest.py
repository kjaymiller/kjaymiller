import os

import pytest
from applitools.selenium import (
    Configuration,
    Eyes,
    BatchInfo,
    BrowserType,
    DeviceName,
    ScreenOrientation,
    VisualGridRunner,
)
from selenium import webdriver


@pytest.fixture(scope="session")
def batchinfo():
    """Return Batch Info"""
    return BatchInfo("Jay's Blog")


@pytest.fixture(scope="session")
def visual_grid_runner():
    """Create a VisualGridRunner"""
    runner = VisualGridRunner()
    yield runner
    print(runner.get_all_test_results())


@pytest.fixture(scope="session")
def eyes_configuration(batchinfo):
    """Create a Applitools Configuration Object"""
    config = Configuration()
    config.set_api_key(os.environ.get("APPLITOOLS_API_KEY", None))
    config.set_batch(batchinfo)
    config.add_browser(1600, 1200, BrowserType.CHROME)
    config.add_browser(1024, 768, BrowserType.CHROME)

    devices = (DeviceName.iPhone_5SE, DeviceName.iPad)

    for device in devices:
        config.add_device_emulation(device, orientation=ScreenOrientation.PORTRAIT)
        config.add_device_emulation(device, orientation=ScreenOrientation.LANDSCAPE)

    return config


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def eyes(
    browser,
    eyes_configuration,
    request,
    visual_grid_runner,
):
    """Create a Eyes Object"""
    eyes = Eyes(visual_grid_runner)
    eyes.set_configuration(eyes_configuration)
    eyes.open(
        driver=browser,
        app_name="Jay's Blog",
        test_name=request.node.name,
    )
    yield eyes
    eyes.close_async()  # Gives Applitools time to process the results
