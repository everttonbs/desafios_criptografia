
def hex_base64(cifra):
    pass

def treat_hex(cifra_hex):
    dic_hex = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    }

    list_hex = []
    for i in cifra_hex:
        if i in ['a','b', 'c', 'd', 'e', 'f']:
            i = dic_hex[i] 
        list_hex.append(int(i))
    
    return list_hex


text_cifra = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

list_hex = treat_hex(text_cifra)
print(list_hex)

# hex_base64(text_cifra)


