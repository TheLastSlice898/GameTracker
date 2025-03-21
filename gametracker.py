import psutil
processlist= []




# check if the count of processes has changed

## if it has then check if its a game on the tracking list. 



## then check if a game has closed 
    #then take it off the list of tracked 



## if the game is currently running add the time to the list of tracked games 
## add time since its done this function to make sure it takes computational time into account. 


## sort functions for different filters 

# Check if idle 
#   if so then add that istead of active time




for process in psutil.process_iter():
    processlist.append(process.name())
print(processlist)
    



