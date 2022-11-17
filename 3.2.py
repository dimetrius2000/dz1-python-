spisok_company = {'Microsoft':1000000,'Apple':12000000,'GM':123000000,'Xiaomi':1000001}


list_values = sorted(list(spisok_company.values()), reverse=True)[:3]                    # O(n logn)
for el in list_values:                                                                   # O(n^2)
    for k, v in spisok_company.items():                                                  # O(n^2)
        if v == el:                                                                      # O(1)
            print(k, ':', v)                                                             # O(1)
           # Oбщее O(N^2)
