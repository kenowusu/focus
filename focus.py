import os
from sty import fg, bg, ef, rs


#get host file path
hostpath = os.path.join('c:\\','Windows','System32','drivers','etc','hosts')

#web domain list to turn on and off
weblist = [
    'www.youtube.com',
    'youtube.com'
]

#focus function to turn on and off focus mode
def focus(focusmode):
    
    if focusmode == 'on':

        try:
            #open host file in read mode and read all lines
            with open(hostpath,mode='r') as openhostfile:
                lines = openhostfile.readlines()
                
                #open host file in write mode
                with open(hostpath,mode='w') as hostfile:

                    for line in lines:
                        if  line.lstrip('#127.0.0.1 ').rstrip('\n') in weblist:
                            hostfile.write(line.lstrip('#'))
                        
                        #just write domain to file
                        else:
                            hostfile.write(line)
                    print(fg.green + 'Focus mode is on' + fg.rs)
                           

                        
                          
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
                            striped_line = line.lstrip('#127.0.0.1 ')
                            hostfile.write('#127.0.0.1 '+striped_line)
                        
                        #just write domain to file
                        else:
                            hostfile.write(line)
                    print(fg.red + 'Focus mode is off' + fg.rs)

     

        except Exception as e:
            print(e)
