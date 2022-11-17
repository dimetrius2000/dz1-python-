spisok_company = {'Microsoft':1000000,'Apple':12000000,'GM':123000000,'Xiaomi':1000000}

#global max_value                                                            # O(1)
#global key_max_value                                                        # O(1)

max_profit_2 = {}                                                           # O(1)
while len(max_profit_2) < 3:                                                # O(n)
    max_value = 0                                                           # O(1)
    for key, value in spisok_company.items():                               # O(n)
        if max_value < value:                                               # O(len(max_value))
            max_value = value                                               # O(1)
            key_max_value = key                                             # O(1)
    max_value = spisok_company.pop(key_max_value)                           # O(1)
    max_profit_2.setdefault(key_max_value, max_value)                       # O(1)

print(max_profit_2)

# O(N^2)
