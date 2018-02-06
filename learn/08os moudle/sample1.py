import os

print(os.getcwd())  #get current working directory
os.chdir('C:/Users/LIYY/Desktop/djangogirls/learn')
print(os.getcwd())
# print(os.listdir())
# os.mkdir('xxxx') not for tree folder
# os.mkdirs(''/'')  better way
# os.rmdir()  better
# os.removemdirs()
# os.rename('original_name', 'new_name')
# print(os.stat('xx.txt'))
# print(os.stat('xx.txt').st_size)
# ......
# os.walk()  #yield top to down,
# for dirpath, dirnames, filenames in os.walk('C:/Users/LIYY/Desktop/djangogirls/learn/'):
#     print("current path, {}".format(dirpath))
#     print("directories, {}".format(dirnames))
#     print("files:", filenames)
#     print()

print(os.environ)

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('TEMP'),'text.txt')
print(file_path)
# os.path.join(path1, path2)

# with open(file_path, 'w') as f:
    # f.wte

print(os.path.basename('/tem/test.txt'))
print(os.path.dirname('/tem/test.txt'))
print(os.path.split('/temp/text.text'))
print(os.path.splitext('/temp/text.text'))

print(os.path.exists('/temp/text.text'))
print(os.path.isfile('/temp/text.text'))

print(dir(os.path))
