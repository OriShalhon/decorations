import time
import pytest
from decorations.oop import Retry

# Initialize the Retry decorators as named objects
retry_on_value_error = Retry(limit=3, exceptions=ValueError, delay=1)
retry_on_io_error = Retry(limit=2, exceptions=IOError, delay=2)
retry_on_type_error = Retry(limit=5, exceptions=TypeError, delay=0.5)

def test_retry_decorator_with_io_error():
    @retry_on_io_error
    def function_that_raises_io_error():
        raise IOError("An IO exception")

    with pytest.raises(IOError):
        function_that_raises_io_error()

def test_retry_decorator_with_type_error():
    @retry_on_type_error
    def function_that_raises_type_error():
        raise TypeError("A Type exception")

    with pytest.raises(TypeError):
        function_that_raises_type_error()

def test_retry_decorator_with_delay():
    @retry_on_type_error
    def function_that_raises_type_error():
        raise TypeError("A Type exception")

    start_time = time.time()
    with pytest.raises(TypeError):
        function_that_raises_type_error()
    end_time = time.time()

    # Check that the delay was applied
    assert end_time - start_time >= 2.5  # 5 retries * 0.5s delay

def test_retry_decorator_with_function_that_passes_on_second_call():
    @retry_on_value_error
    def function_that_raises_once():
        if not hasattr(function_that_raises_once, "has_raised"):
            function_that_raises_once.has_raised = True
            raise ValueError("An exception")
        else:
            return "No exceptions here"

    result, tries = function_that_raises_once()
    assert result == "No exceptions here"
    assert tries == 1