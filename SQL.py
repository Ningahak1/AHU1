from googlesearch import search
import requests
import time
import os
import pyfiglet
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
lo=pyfiglet.figlet_format("     AHU TEAM  ")
print(Z+lo)
print(X+"*"*+63)
dork = input(B+"Entr dork ✎ ")
print("Loding...")
time.sleep(2)
for x in search (dork, num_results=50):
           print (F+x)
