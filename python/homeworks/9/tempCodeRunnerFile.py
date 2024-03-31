    pairs = []
    blocks = input_string.split("<< val ")[1:] 
    + input_string.split("<<val ")[1:]
    for block in blocks:
        pair_str = block.split("=:")
        key = pair_str[0].strip()
        value = pair_str[1].split(";")[0].strip()
        pairs.append((value, key))
    return pairs