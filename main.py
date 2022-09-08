'''
@author : SiddheshDhinge
'''

import os
import hashlib
import encryptor
import decryptor

def encryptNames(path):
    files = []
    for (root, dir, filenm) in os.walk(path):
        files.extend([[root, file] for file in filenm])

    file_mapping = []

    for file in files:
        md5hash = hashlib.md5(file[1].encode()).hexdigest() + '.bak'
        newpath = os.path.join(file[0], md5hash)
        oldpath = os.path.join(file[0], file[1])
        os.rename(oldpath, newpath)
        file_mapping.append([oldpath, newpath])

    path_keys = os.path.join(path, 'path_keys.bak')
    with open(path_keys, 'wb') as f:
        for x in file_mapping:
            f.write(bytes(f'{x[0]}:{x[1]}\n', encoding='utf-8'))

def startEncrypt():
    path = encryptor.initFolder()
    (f_key, key) = encryptor.initPassword()

    encryptNames(path)
    encryptor.encrypt(path, f_key, key)

def decryptNames(path_key):
    with open(path_key, 'rb') as f:
        for x in f:
            (oldname, newname) = x.split(b':')
            os.rename(newname[:-1], oldname)

def startDecrypt():
    path = decryptor.initFolder()
    key = decryptor.initPassword()
    decryptor.decrypt(path, key)

    path_key = os.path.join(path, 'path_keys.bak')
    decryptNames(path_key)
    os.remove(path_key)

def main():
    choice = int(input('1: Encrypt\n2: Decrypt\nEnter Choice: '))
    if(choice == 1):
        startEncrypt()
    elif(choice == 2):
        startDecrypt()
    else:
        print('Wrong Choice...')

if __name__ == '__main__':
    main()
# Example_original