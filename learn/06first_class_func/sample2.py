def logger(msg):

    def log_message():
        print("log: ",msg)
    return log_message

log_hi = logger('HI')
log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}><{1}><{0}'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1("Test headline!")
print_h1("Another headline")
