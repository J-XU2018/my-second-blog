# try:
#     f = open('goodtutoral')
# except Exception:
#     print("not exist")
# finally:
#     print("finally this run")

# more speciafilly except
# try:
#     f = open('test.txt')
#     # var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("finally this run")

# rase excepton on purpose
try:
    f = open('test.txt')
    # var = bad_var
    if f.name == 'test.txt':
        raise Exception
except FileNotFoundError as e:
    print("file not found")
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("finally this run")
