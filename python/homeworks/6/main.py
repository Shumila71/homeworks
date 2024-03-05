def main(data):
    match data:
        case[2017, 1971, 1968, 'C++']:
            return 12
        case[2017, 1971, 1964, 'C++']:
            return 12
        case[2017, 1971, 1968, 'NU']:
            return 12
        case[2017, 1971, 1964, 'NU']:
            return 12
        case[2017, 1971, 1968, 'MINID']:
            return 12
        case[2017, 1971, 1964, 'MINID']:
            return 12
        case[2017, 1965, 1968, 'C++']:
            return 12
        case[2017, 1965, 1964, 'C++']:
            return 12
        case _:
            return main2(data)


def main2(data):
    match data:
        case[2017, 1965, 1968, 'NU']:
            return 12
        case[2017, 1965, 1964, 'NU']:
            return 12
        case[2017, 1965, 1968, 'MINID']:
            return 12
        case[2017, 1965, 1964, 'MINID']:
            return 12
        case[2017, 1978, 1968, 'C++']:
            return 12
        case[2017, 1978, 1964, 'C++']:
            return 5
        case[2017, 1978, 1968, 'NU']:
            return 5
        case[2017, 1978, 1964, 'NU']:
            return 5
        case _:
            return main3(data)


def main3(data):
    match data:
        case[2017, 1978, 1968, 'MINID']:
            return 12
        case[2017, 1978, 1964, 'MINID']:
            return 12
        case[1982, 1971, 1982, 'C++']:
            return 6
        case[1982, 1965, 1982, 'C++']:
            return 6
        case[1982, 1978, 1982, 'C++']:
            return 6
        case[1982, 1965, 1968, 'C++']:
            return 7
        case[1982, 1965, 1964, 'C++']:
            return 7
        case[1982, 1978, 1968, 'C++']:
            return 8
        case _:
            return main4(data)


def main4(data):
    match data:
        case[1982, 1978, 1964, 'C++']:
            return 8
        case[1982, 1978, 1968, 'NU']:
            return 9
        case[1982, 1965, 1968, 'NU']:
            return 9
        case[1982, 1971, 1968, 'NU']:
            return 9
        case[1982, 1978, 1964, 'NU']:
            return 10
        case[1982, 1965, 1964, 'NU']:
            return 10
        case[1982, 1971, 1964, 'NU']:
            return 10
        case[1960, 1965, 1968, 'C++']:
            return 3
        case _:
            return main5(data)


def main5(data):
    match data:
        case[1960, 1965, 1968, 'NU']:
            return 3
        case[1960, 1965, 1968, 'MINID']:
            return 3
        case[1960, 1965, 1964, 'C++']:
            return 4
        case[1960, 1965, 1964, 'NU']:
            return 4
        case[1960, 1965, 1964, 'MINID']:
            return 4
        case[1960, 1971, 1964, 'C++']:
            return 0
        case[1960, 1971, 1968, 'C++']:
            return 0
        case[1960, 1971, 1964, 'NU']:
            return 1
        case _:
            return main6(data)


def main6(data):
    match data:
        case [1960, 1971, 1968, 'NU']:
            return 1
        case [1960, 1971, 1964, 'MINID']:
            return 2
        case [1960, 1971, 1968, 'MINID']:
            return 2
        case [1982, 1971, 1968, 'MINID']:
            return 11
        case [1982, 1965, 1964, 'MINID']:
            return 11
        case _:
            return main7(data)


def main7(data):
    match data:
        case [1982, 1978, 1968, 'MINID']:
            return 11
        case [1982, 1971, 1964, 'MINID']:
            return 11
        case [1982, 1965, 1968, 'MINID']:
            return 11
        case [1982, 1978, 1964, 'MINID']:
            return 11
        case _:
            return 5



print(main([1982,  1971,  1968,  'NU'])) #= 9
