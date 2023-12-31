n, lt = int(input()), ""
for i in range(1, n + 1):
    if i % 2 == 1:
        lt += "".join([".C" for i in range(n // 2 + 1)])[1:] + "\n" if n % 2 != 0 else "".join([".C" for i in range(n // 2 + 1)])[1:][:-1] + "\n"
    else:
        lt += "".join([".C" for i in range(n // 2 + 1)])[:-1] + "\n" if n % 2 != 0 else "".join([".C" for i in range(n // 2 + 1)])[2:] + "\n"

print(lt.count("C"))
print(lt[:-1])

