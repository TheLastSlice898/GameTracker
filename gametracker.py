import psutil
import json
import time
processlist= []

with open('Data\detectable.json','r') as file:
    jsondata = json.load(file)


##print(jsondata[(0)])

# check if the count of processes has changed

## if it has then check if its a game on the tracking list. 



## then check if a game has closed 
    #then take it off the list of tracked 



## if the game is currently running add the time to the list of tracked games 
## add time since its done this function to make sure it takes computational time into account. 


## sort functions for different filters 

# Check if idle 
#   if so then add that istead of active time

def CheckforProcess():
    for proc in psutil.process_iter(['name']):
        x = proc.info
        name = x["name"]
        nosuffix = str(name.lower())
        print(nosuffix)
        
        for game_exe_name in jsondata.items():
            if game_exe_name == nosuffix:
                print('omg i did it')



    time.sleep(4)
    print("i wiated")
    

CheckforProcess()




    




