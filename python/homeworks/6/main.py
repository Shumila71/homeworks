def main(data):
    match data:
        case["MUPAD", 1974, 1985, 2019]:
            return 0
        case["MUPAD", 1974, 1985, 2014]:
            return 0
        case["MUPAD", 1989, 1985, 2019]:
            return 1
        case["MUPAD", 1989, 1985, 2014]:
            return 1
        case["MUPAD", 2012, 1985, 2019]:
            return 2
        case["MUPAD", 2012, 1985, 2014]:
            return 2
        case["MUPAD", 1974, 2005, 2019]:
            return 3
        case["MUPAD", 1989, 2005, 2019]:
            return 3
        case _:
            return main2(data)


def main2(data):
    match data:
        case["MUPAD", 2012, 2005, 2019]:
            return 3
        case["MUPAD", 1974, 2005, 2014]:
            return 4
        case["MUPAD", 1989, 2005, 2014]:
            return 4
        case["MUPAD", 2012, 2005, 2014]:
            return 4
        case["MUPAD", 1974, 1965, 2019]:
            return 5
        case["MUPAD", 1989, 1965, 2019]:
            return 5
        case["MUPAD", 2012, 1965, 2019]:
            return 5
        case["MUPAD", 1974, 1965, 2014]:
            return 5
        case _:
            return main3(data)


def main3(data):
    match data:
        case["MUPAD", 1989, 1965, 2014]:
            return 5
        case["MUPAD", 2012, 1965, 2014]:
            return 5
        case["VHDL", 1974, 1965, 2019]:
            return 6
        case["VHDL", 1974, 1985, 2019]:
            return 6
        case["VHDL", 1974, 2005, 2019]:
            return 6
        case["VHDL", 1974, 1965, 2014]:
            return 6
        case["VHDL", 1974, 1985, 2014]:
            return 6
        case["VHDL", 1974, 2005, 2014]:
            return 6
        case _:
            return main4(data)


def main4(data):
    match data:
        case["VHDL", 1989, 1965, 2019]:
            return 7
        case["VHDL", 1989, 1985, 2019]:
            return 7
        case["VHDL", 1989, 2005, 2019]:
            return 7
        case["VHDL", 1974, 1965, 2019]:
            return 6
        case["VHDL", 1974, 1985, 2019]:
            return 6
        case["VHDL", 1974, 2005, 2019]:
            return 6
        case["VHDL", 1974, 1965, 2014]:
            return 6
        case["VHDL", 1974, 1985, 2014]:
            return 6
        case _:
            return main5(data)


def main5(data):
    match data:
        case["VHDL", 1974, 2005, 2014]:
            return 6
        case["VHDL", 1989, 1965, 2019]:
            return 7
        case["VHDL", 1989, 1985, 2019]:
            return 7
        case["VHDL", 1989, 2005, 2019]:
            return 7
        case["VHDL", 1989, 1965, 2014]:
            return 8
        case["VHDL", 1989, 1985, 2014]:
            return 8
        case["VHDL", 1989, 2005, 2014]:
            return 8
        case["VHDL", 2012, 1965, 2019]:
            return 9
        case _:
            return main6(data)


def main6(data):
    match data:
        case ["VHDL", 2012, 1985, 2019]:
            return 9
        case ["VHDL", 2012, 2005, 2019]:
            return 9
        case ["VHDL", 2012, 1965, 2014]:
            return 9
        case ["VHDL", 2012, 1985, 2014]:
            return 9
        case ["VHDL", 2012, 2005, 2014]:
            return 9
        case _:
            return 10



print(main(["VHDL", 1974, 1985, 2014]))
