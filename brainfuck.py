import os

#set to None for unlimited memmory
MERRORY_STORAGE_MAX=None
#set to None for allowing the point to got to the negitive
ALLOW_MEMMORY_NEGITIVE=None
#set LIMIT_TO_ONE_BYTE to False if you don't want the 1 byte limit it also limits to not go into the negitive and will post error 
LIMIT_TO_ONE_BYTE = False

my_file = open(r"C:\Users\ethan\Desktop\copilot knowoff\hello.brainfuck", "r")
code = my_file.read()
code = code.replace("\n" , '')
my_file.close()

## compile code
'''
initate the memory as a list
initate the point with POINTER 0 is the diffult pointer
'''
memory = {0:0}
MIN_POINTER=0
POINTER = 0
MAX_POINTER=0
GOTO = False
#go though all the code
for i in code:
    if not GOTO:
        if i == ">":
            if not MERRORY_STORAGE_MAX == None:
                if POINTER >= MERRORY_STORAGE_MAX:
                    raise ValueError("Reached max pointer position")
                else:
                    POINTER += 1
            else:
                POINTER += 1
            if POINTER > MAX_POINTER:
                    MAX_POINTER = POINTER
                    memory[POINTER] = 0
        elif i == "<":
            if not ALLOW_MEMMORY_NEGITIVE == None:
                if POINTER > 0:
                    POINTER -= 1
                else:
                    raise ValueError("Reached negitive position")
            else:
                POINTER -= 1
            if POINTER < MIN_POINTER:
                    MIN_POINTER = POINTER
                    memory[POINTER] = 0
        elif i == "+":
            if LIMIT_TO_ONE_BYTE: 
                if memory[POINTER] >= 256:
                    raise ValueError("Out of memmory")
                else:
                    memory[POINTER] +=1
            else:
                memory[POINTER] +=1
        elif i == "-":
            if LIMIT_TO_ONE_BYTE: 
                if memory[POINTER] <= 0:
                    raise ValueError("too low")
                else:
                    memory[POINTER] -=1
            else:
                memory[POINTER] -=1
        elif i == ".":
            try:
                print(chr(memory[POINTER]))
            except:
                raise ValueError("Chararctor error")
        elif i == ",":
            try:
                input()
                memory[POINTER] = ord()
            except:
                raise ValueError("bad input")
        elif i == "[":
            GOTO = True
        else:
            raise SyntaxError("Charactor not recognized \n if triyng to comment use []")
    else:
        if i == "]":
            GOTO = False









