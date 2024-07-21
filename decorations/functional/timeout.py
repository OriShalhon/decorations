import signal

def timeout(seconds):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError('Timed out after {} seconds in function {}'.format(seconds, func.__name__))

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator