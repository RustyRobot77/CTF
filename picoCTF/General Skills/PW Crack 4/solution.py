#!/usr/bin/env python3

from operator import xor

with open('level4.flag.txt.enc', 'rb') as file:
  flag_enc = file.read().decode()

# The secret key is one of the items in this list, pasted from level4.py
keys = ["6288", "6152", "4c7a", "b722", "9a6e", "6717", "4389", "1a28", "37ac", "de4f", "eb28", "351b", 
        "3d58", "948b", "231b", "973a", "a087", "384a", "6d3c", "9065", "725c", "fd60", "4d4f", "6a60", 
        "7213", "93e6", "8c54", "537d", "a1da", "c718", "9de8", "ebe3", "f1c5", "a0bf", "ccab", "4938", 
        "8f97", "3327", "8029", "41f2", "a04f", "c7f9", "b453", "90a5", "25dc", "26b0", "cb42", "de89", 
        "2451", "1dd3", "7f2c", "8919", "f3a9", "b88f", "eaa8", "776a", "6236", "98f5", "492b", "507d", 
        "18e8", "cfb5", "76fd", "6017", "30de", "bbae", "354e", "4013", "3153", "e9cc", "cba9", "25ea", 
        "c06c", "a166", "faf1", "2264", "2179", "cf30", "4b47", "3446", "b213", "88a3", "6253", "db88", 
        "c38c", "a48c", "3e4f", "7208", "9dcb", "fc77", "e2cf", "8552", "f6f8", "7079", "42ef", "391e", 
        "8a6d", "2154", "d964", "49ec"
       ]

# The number of possibilities is still small and can be bruteforced
for key in keys:
  flag = ''.join([chr(xor(ord(flag_enc[i]), ord(key[i % len(key)]))) for i in range(len(flag_enc))])
  if 'picoCTF' in flag:
    print(flag)
