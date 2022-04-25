import Slush
import time 
import sys
b = Slush.sBoard()

#define the motor that is being used
m1 = Slush.Motor(0) 
#print the position of the motor before we spin it
print("Starting position: " + str(m1.getPosition()))


while True:
    #User types in input
    user_input = input("Enter the ammount of steps to move the motor (must be an int) (type e to exit):  ")
    
    #if input is e then end the program
    if user_input == "e" or user_input == "E": 
        print("Exiting program") 
        #Print the final position of the motor   
        print("Final Position: " + str(m1.getPosition()))
        #exit program
        sys.exit()
    
    #checks to see if the user input is an int
    try: 
        int(user_input)
   
   #Asks user to repeat if the value isn't an int
    except ValueError: 
        print("Please select a valid input") 
        continue

    #if the value is an int
    else: 
        #convert input to int
        user_input = int(user_input)
        #move the ammount of steps that the user input
        m1.move(user_input) 
        #print the current position of the motor
        print("Spin position: " + str(m1.getPosition()))
        
