import os 
import ctypes, sys

from is_admin import is_admin

# file = os.path.join('c:',"host_file.txt")

# with open(file,mode='w') as openedfile:
#     for line in openedfile:
#         print(line)
# quit()



if is_admin():
   print("I'm in admin mode")
    
else:
    #Re-run the program with admin rights
    print('Program requires admin priviledges')
    quit()
