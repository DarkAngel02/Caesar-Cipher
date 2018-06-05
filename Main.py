MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message')
        mode = input().lower()
        if mode in 'e encrypt d decrypt b brute'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()
    
def getKey():
    key = 0
    while True:
        print('Enter your key number (1-%s)' % (MAX_KEY_SIZE))
        key =int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = key
    translated = ''

for symbol in 'message':
    if symbol.isalpha():
        num =ord(symbol)
        num += key

if symbol.isupper():
    if num > ord('Z'):
        num -= 26
    elif num < ord('A'):
        num += 26

elif symbol.islower():
    if num > ord('z'):
        num -= 26
    elif num <ord('a'):
        num += 26
        
    translated += chr(num)
else:
    translated += symbol
    

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
key = getKey
print('Your  translated message is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
