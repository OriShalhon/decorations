import time
import pytest
from decorations.functional import timeout
from decorations.functional import timeit
def test_timemout_decorator():

    @timeout(1)
    def print_function_long():
        print("Starting")
        time.sleep(1)
        print("1 second")
        time.sleep(1)
        print("2 seconds")

    with pytest.raises(TimeoutError):
        print_function_long()


def test_timeit_decorator_time():

    @timeit(return_time=True)
    def function_long():
        time.sleep(1)


    _, timed = function_long()

    assert int(timed) == 1

def test_timeit_decorator_print(capfd):

    @timeit()
    def function_short():
        pass

    function_short()
    out, _ = capfd.readouterr()

    assert "Function function_short took" in out
