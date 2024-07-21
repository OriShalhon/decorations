import time

class Retry:
    def __init__(self, limit=0, exceptions=Exception, delay=0):
        self.limit = limit
        self.exceptions = exceptions
        self.delay = delay

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                try:
                    result = func(*args, **kwargs)
                    return result, count
                except self.exceptions as e:
                    count += 1
                    if self.limit and count > self.limit:
                        raise e
                    if self.delay:
                        time.sleep(self.delay)
        return wrapper