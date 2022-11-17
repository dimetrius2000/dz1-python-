spisok_company = {'Microsoft':1000000,'Apple':12000000,'GM':123000000,'Xiaomi':1000000}

def by_value(item):
    return item[1]                                                          # O(1)


max_profit = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(spisok_company.items(), key=by_value, reverse=True):     # O(n + n log n)
    if i < 3:                                                               # O(len(i))
        max_profit.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)
print(max_profit)  

# общее O(N)
