users = {'alex':2000,
        'egor':4432244,
        'дима':'fff4444',
        'alina':50560504
        }

users_activated = {'alex':'activated',
        'egor':'no activated',
        'дима':'activated',
        'alina':'activated'
        }

def activated_useres():#!!!#O(N)
    print('Есть ли не активированные пользователи ?')#O(1)

    if 'no activated' in users_activated.values():#O(N)
        print("yes")#O(1)
    else:
        print("no")#O(1)

    print("кто ?")#O(1)
activated_useres()
#сложность - O(N)

def get_key(user_activated, value):#!!! #O(N)
    for k, v in users_activated.items():#O(N)
        if v == value:#O(1)
            return k#O(1)
print(get_key(users_activated, 'no activated'))#O(1)
print('пользователь '+(get_key(users_activated, 'no activated'))+' пройдите обязательную активацию на сайте!')#O(1)



#общая сложность = O(N)+O(N)=O(N)








