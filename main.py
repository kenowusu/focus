import os 
import ctypes, sys

from is_admin import is_admin
from cmd_args import control_args




if is_admin():
   control_args()
    
else:
    #Re-run the program with admin rights
    print('Program requires admin priviledges')
    
