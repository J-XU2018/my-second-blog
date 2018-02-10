def combo(it1, it2):
    result = []
    i = 0
    while True:
        try:
            result.append((it1[i], it2[i]))
            i += 1
        except Exception:
            break
    return result

t1 = (1, 2, 3)
t2 = "123"
print(combo(t1, t2))
