def main(x):
    lookup_table = {
        (2006, 1970, None, 1966): 2,
        (2006, 1970, None, 1959): 1,
        (2006, 1970, None, 1988): 0,
        (2006, 1979, None, None): 3,
        (2006, 1969, None, None): 4,
        (2007, None, 2013, None): 5,
        (2007, None, 1968, 1988): 6,
        (2007, None, 1968, 1959): 7,
        (2007, None, 1968, 1966): 8,
        (2007, None, 1964, 1988): 9,
        (2007, None, 1964, 1959): 10,
        (2007, None, 1964, 1966): 11
    }
    key = next((k for k in lookup_table.keys() if all(
        x[i] == k[i] or k[i] is None for i in range(len(x)))), None)
    return lookup_table.get(key, 0)

print(main([2006, 1970, 2013, 1966])) #= 2
print(main([2007, 1979, 1968, 1966])) #= 8
print(main([2007, 1979, 2013, 1988])) #= 5
print(main([2006, 1970, 2013, 1959])) #= 1
print(main([2006, 1969, 2013, 1959])) #= 4
