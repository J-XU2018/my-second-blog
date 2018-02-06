f = open('C:/Users/LIYY/Desktop/djangogirls/learn/goodtutoral.txt', 'r+')

print(f.name)
print(f.mode)

f.close

# context manager, auto close file, even any exception
with open('C:/Users/LIYY/Desktop/djangogirls/learn/goodtutoral.txt', 'r+') as f:
    pass

print(f.closed)

# another smaple
with open('C:/Users/LIYY/Desktop/djangogirls/learn/goodtutoral.txt', 'r+') as f:
    f_content = f.read()
    f_content2 = f.readlines()
    f_content3 = f.readline()
    print(f_content, f_content2)

    
