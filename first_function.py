#first function is on ein which function are treated as object
# function can be assigned to variable , passed to function, returned by another function

def html_tag(tag):
    def wrapper(msg):
        print("<{0}>..{1}</{0}>".format(tag,msg))
    return wrapper

print_h1 = html_tag('h1')
print_h2 = html_tag('h2')
print_h1('yo')
print_h2('yo man')
