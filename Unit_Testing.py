import os 
from pwd import getpwuid
from grp import getgrgid

def finds_first_repeated_number(V1,V2):
    dic={};F1=-1
    for i in range(len(V1)-1):dic[V1[i]]=1
    for i in range(len(V2)-1,-1,-1):
        if V2[i] in dic.keys():
            F1=i
    return F1
    
    
def find_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name=str(os.path.join(root, file))
            if getpwuid(os.stat(file_name).st_uid).pw_name=='admin':
                if os.access(file_name,os.X_OK):
                    if os.stat(file_name).st_size < (14*2^20):
                        return file_name
                        
                        

def Coin_Flips(seq):
    odd=seq[::2];even=seq[1::2]
    if seq.count(0)-seq.count(1)==0:
        if odd.count(0)>even.count(0):
            MinPermit=odd.count(1)
        else:
            MinPermit=odd.count(0)
    elif seq.count(0)-seq.count(1) in [1,-1]:
        if seq.count(0)>seq.count(1):
            MinPermit=odd.count(1)
        else:
            MinPermit=odd.count(0)
    else:
        MinPermit=-1
    return MinPermit