import random

def Encryption(string, operation):
    new_string = ""
    for i in range(len(string)):
      new_string += chr(int(ord(string[i]) + operation))
    return new_string

def Decryption(string, operation):
    old_string = ''
    for i in range(len(string)):
       old_string += chr(int(ord(new_string[i]) - operation))
    return old_string

while(True):
    eord = input("Encryption or Decryption ")
    if(eord == 'e' or 'encryption'):
        string = input("what do you want to encrypt? ")
        operation = int(input("What is the seed? ")) % 128
        print(Encryption(string, operation))
    elif(eord == 'd' or 'decryption'):
        string = input("what do you want to decrypt? ")
        operation = int(input("What is the seed? ")) % 128
        print(Decryption(string, operation))
    else:
        print("please enter e or encryption or d or decryption")

