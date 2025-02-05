#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:22:12 2021

@author: volodymyr
"""

from cryptography.fernet import Fernet
import base64
import os

def initFolder():
    while True:
        folder_path = input("Enter path to folder where you want to dencrypt files : ")
        print("Is it the right directory you have chosen?")
        for i in os.listdir(folder_path):
            print(i)
        confirm = input('[y/n]?')
        if confirm.lower() == 'y':
            break
        else:
            continue
    return folder_path

def initPassword():
    init_key = input("Enter password to decrypt files ---> ")
    key = bytes(str(init_key*31)[:31], 'utf8')
    key = base64.urlsafe_b64encode(key)
    key = bytes(init_key[0]+str(key)[2:-2], 'utf8')
    return key


def decrypt(folder_path, key):
    # Decrypt
    f = Fernet(key)

    list_files = []
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        list_files += [os.path.join(dirpath, file) for file in filenames]
        
    for file in list_files:
        try:
            with open(file, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()
            
            decrypted = f.decrypt(encrypted)
            
            with open(file, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
        except Exception as e:
            print(f'Some problems occur with file - {file} \n {e} ')