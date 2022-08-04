import sys
from focus import focus 



def control_args():
    args = sys.argv[1:]
    numofargs = len(args)

    if  numofargs < 1:
        print('arguments missing')
    else:
        if(args[0] == 'on'):
            focus('on')

        elif (args[0]== 'off'):
            focus('off')
           


