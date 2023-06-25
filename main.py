""" 1 занятие - Практика """
s = 'aaaaa'
def character_counter_v1(s):
    counter_for_ops = 0
    for sym in s:
        counter = 0
        for sub_sym in s:
            counter_for_ops += 1
            if sym == sub_sym:
                counter += 1
        print(f'Количество "{sym}" = {counter}')
    print(counter_for_ops)

def character_counter_v2(s):
    counter_for_ops = 0
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            counter_for_ops += 1
            if sym == sub_sym:
                counter += 1
        print(f'Количество "{sym}" = {counter}')
    print(counter_for_ops)

def character_counter_v3(s):
    counter_for_ops = 0
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
        counter_for_ops += 1

    for sys, counter in syms_counter.items():
        print(f'Количество "{sym}" = {counter}')
    print(f'{counter_for_ops=}')

character_counter_v3(s)
