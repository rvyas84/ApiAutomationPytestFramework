import pytest
from datetime import datetime
import os
import json

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Add timestamp to report file name
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...") # Before method
    yield
    print("\nTearing down resources...") # After method

@pytest.fixture
def load_test_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "payload", "test_payload.json")
    with open(json_file_path) as json_file:
        test_data = json.load(json_file)
    
    return test_data