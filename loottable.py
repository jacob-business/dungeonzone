#omg i can't believe i'm doing computer programming For Fun .i hate myself. not really its fine
import random
import math

print("Loot Generator (entries stolen from Maze Rats, Grave, AD&D Dungeon Master's Guide, Die Trying and also a handful of my own ideas i'm not *just* a thief.)")
print()

def GenerateLoot():
    NameFile=open("Loot.txt","r")
    NameList=NameFile.readlines()
    output=NameList[random.randint(0,len(NameList)-1)]
    return output

print (GenerateLoot())
