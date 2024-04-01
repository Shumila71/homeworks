def main(hex_data): 
    decimal_number = int(hex_data, 16) 
    bin_data = bin(decimal_number) 
    bin_data = bin_data[2: ]
    bin_data = '00000000' + bin_data 
    x1 = bin_data[-16:-10]
    x2 = bin_data[-10:-8] 
    x3 = bin_data[-8:-3] 
    x4 = bin_data[-3: ]
    return {'D1': int(x4, 2), 'D2': int(x3, 2), 'D3': int(x2, 2), 'D4': int(x1, 2)}
 
print(main('0x8b69')) 
