import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguements ({})'.format(func.__name__,args))
        print(func(*args))
    return log_func

def add(a,b):
    return a+b

def sub(a,b):
    return a - b
add_logger = logger(add)
sub_logger = logger(sub)

add_logger(2,3)
sub_logger(5,2)