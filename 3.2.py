spisok_company = {'Microsoft':1000000,'Apple':12000000,'GM':123000000,'Xiaomi':1000001}


list_values = sorted(list(spisok_company.values()), reverse=True)[:3]                    # O(n)
for el in list_values:                                                               # O(1)
    for k, v in spisok_company.items():                                                   # O(n)
        if v == el:
            print(k, ':', v)   