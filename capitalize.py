"""

Project 2 Advanced Algorithmts 2021/22
Margarida Martins

"""


import sys
import os 

folder = sys.argv[1]
filenames = next(os.walk(folder))[2]

for f in filenames:
    fi=open(folder+f, "r+")
    f_content= fi.read().upper()
    fi.seek(0)
    fi.truncate()
    fi.write(f_content)
    fi.close()
