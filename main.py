'''
author : Mayank Malhotra
created : 10/10/15
'''

import compute


def process_info(text, key, method):
    key = ''.join('{:08b}'.format(ord(t)) for t in key)[:64]
    block = (64 - len(key) % 64) / 8
    if block is not 64:
        key += '00100000' * block
    if method is 'e':
        text = ''.join('{:08b}'.format(ord(t)) for t in text)
        block = (64 - len(text) % 64) / 8
        if block is not 64:
            text += '00100000' * block
    encryption_keys = compute.sixteen_keys(key)
    decryption_keys = list(reversed(encryption_keys))
    if method is 'e':
        conversion = ''
        for i in range(0, len(text), 64):
            conversion += compute.encrypt(text[i:i + 64], encryption_keys)
        return '\nCipher: ' + conversion
    else:
        conversion = ''
        for i in range(0, len(text), 64):
            conversion += compute.encrypt(text[i:i + 64], decryption_keys)
        return '\nMessage: ' + ''.join(chr(int(conversion[i:i + 8], 2))
                                       for i in range(0, len(conversion), 8))

text = raw_input("\nEnter the text: ")
key = raw_input("\nEnter the key: ")
option = raw_input("\nPress 'e' for encryption or 'd' for decryption: ")
print process_info(text, key, option) + '\n'
