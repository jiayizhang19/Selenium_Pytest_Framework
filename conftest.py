import pytest
import time
import os

"""
You can have conftest.py in different levels within your project. 
For instance, this file is located within the project root directory, so the setups defined here will be applied to all the test_.py file.
You can also have test folder level conftest, which will only apply to files under that folder. 
If exsits the same name within the differernt conftest.py, pytest will use the one closer to the test_.py

The request object is used  to pass contextual information about the current test. 
It provides details about the test  being executed, for instance test-related metadata and functionality.
 --> request.module: Refers to the module where the test resides.
 --> request.function: Represents the specific test function being run in the module.
 --> request.cls: Points to the test class where the test function is located.
"""

@pytest.fixture(scope="module",autouse=True)
def setup_airtest_report(request):
    test_file = request.module.__file__
    test_name = os.path.splitext(os.path.basename(test_file))[0]
    timestamp = time.strftime("%Y%m%d_%H%M%S")
