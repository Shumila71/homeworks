def main(x):
    lookup_table = {
        (2017,None,None,None): 12,
        (1982,None,1982,'C++'): 6,
        (1982,1965,None,'C++'): 7, 
        (1982,1978,None,'C++'): 8, 
        (1982,None,1968,'NU'): 9,
        (1982,None,1964,'NU'): 10,
        (1982,None,None,'MINID'): 11,
        (1960,1978,None,None): 5,
        (1960,1965,1968,None): 3,
        (1960,1965,1964,None): 4,
        (1960,1971,None,'C++'): 0,
        (1960,1971,None,'NU'): 1,
        (1960,1971,None,'MINID'): 2
    }
    for key in lookup_table.keys():
        if all(x[i] == key[i] or key[i] is None for i in range(len(x))):
            return lookup_table[key]
    return 0


print(main([1982, 1971, 1968, 'NU'])) #= 9
