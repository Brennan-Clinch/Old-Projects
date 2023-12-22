# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:46:40 2019

@author: xfang13
"""

#The plain text 
plain_text = "Talks between the United Auto Workers union and General Motors \"have taken a turn for the worse, according to the union's chief negotiator, suggesting that no immediate end is in sight for the auto industry's longest strike in decades. The setback in talks followed several days of reported progress between the two sides. They hope to reach a new four-year deal. Terry Dittes, the vice president of the United Auto Workers union negotiating team, sent a letter to members midday Sunday saying that the union found the company's latest contract proposal to be totally unacceptable to the union."

def look_up_list_gen(text):
    return list(set(text))


class CaesarCipher:
    def __init__(self, key, look_up_list):
        assert(key > 0 and type(key) == int)
        
    def encrypt(self, plain_text):
        
    def decrypt(self):
                    


class VigenereCipher:
    def __init__(self, key, look_up_list):
        assert(type(key) == str)
        
    def encrypt(self, plain_text):
        assert(len(self.key) <= len(plain_text))
        
    def decrypt(self):
                   
            
if __name__ == "__main__":
    caesar = CaesarCipher(89000,look_up_list_gen(plain_text))
    caesar.encrypt(plain_text)
    print("Encrypted text: "+caesar.cipher_text)
    print("Decrypted text: "+caesar.decrypt())

    vigenere = VigenereCipher(plain_text[:5],look_up_list_gen(plain_text))
    vigenere.encrypt(plain_text)
    print("Encrypted text: "+vigener.cipher_text)
    print("Decrypted text: "+vigener.decrypt())                         