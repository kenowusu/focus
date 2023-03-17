import os


hostpath = os.path.join('c:\\','Windows','System32','drivers','etc','hosts')

weblist = [
    'www.youtube.com',
    'youtube.com'
]

def focus(focusmode):
    
    if focusmode == 'on':

        try:

            with open(hostpath,mode='r') as openhostfile:
                lines = openhostfile.readlines()

                with open(hostpath,mode='w') as hostfile:

                    for line in lines:
                        print(line)
                        if  line.lstrip('#127.0.0.1 ').rstrip('\n') in weblist:
                            hostfile.write(line.lstrip('#'))
                           
                        else:
                            hostfile.write(line)
                          
        except Exception as e:
            print(e)
    
    #if focus is off
    elif focusmode =='off':
        
        try:

            with open(hostpath,mode='r') as openhostfile:
                lines = openhostfile.readlines()

                with open(hostpath,mode='w') as hostfile:

                    for line in lines:
                        if  line.lstrip('#127.0.0.1 ').rstrip('\n') in weblist:
                            hostfile.write('#'+line)
     
                        
                        else:
                            hostfile.write(line)
        except Exception as e:
            print(e)

focus('on')