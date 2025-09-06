#Fun 


#Project 1: Codebreaker



passcode = ""

alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"]

bruteList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"]


counter = 0

#Verify function 
def verify(test):
    global counter
    if test == passcode:
        print("You did it!")
        print("This took a total of", counter, "tries!")
        quit()
    else:
        counter = counter + 1
'''
        if counter == 1500:
            print(bruteList)
            quit() 
'''
for space in range(len(passcode)-1): #Repeat based on the number of letters in the pass

    #We need to go though all the previous indexs and add a letter to them
    
    for brute in bruteList:

        for letter in alphabet:
            
            test = (brute + letter)
            print(test) 
            verify(test)

            #Add it to the end of the bruteList
            bruteList.append(test)

        #bruteList.remove(brute)
        #del bruteList[0]

#The above code works but there is some sort of doubling back.
            

