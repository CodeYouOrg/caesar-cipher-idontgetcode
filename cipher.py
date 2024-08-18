# add your code here

import sys
import string

i = 0
cipher_right_shift = 5
#string1 = 'Thanks'
#letter = string1[i]
string1 = input("Enter your Text :")
print(string1)
plain_list = string.ascii_lowercase
#print(plain_list)


for i in range(len(string1)):
    letter = string1[i]
    position_of_letter = string1.rfind(letter)
    position_of_plainletter = plain_list.rfind(letter)
    position_of_letter = (position_of_plainletter + cipher_right_shift)%26
    print(plain_list[position_of_letter], end='')


    
    
  


    

    