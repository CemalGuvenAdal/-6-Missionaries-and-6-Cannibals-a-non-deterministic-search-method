# Hw1, 02.17.2021
# @authors Cemal Güven Adal, Batuhan Budak
#          Furkan Ahi, Umutcan Baştepe, Cankat Anday Kadim
# Missionaries and Cannibal Problem
import random
class State():
    # Constructor
    def __init__(self, eastC, eastM, boat):
        self.eastC = eastC
        self.eastM = eastM
        self.boat = boat
        self.westC = 6-eastC
        self.westM = 6-eastM
        self.parent = None

    # Checks equaility of States
    def equal(self, other):
            return self.eastC == other.eastC and self.westC == other.westC \
        and self.boat == other.boat and self.eastM == other.eastM \
        and self.westM == other.westM

    # Checks is the given state valid and not fail
    def noteaten(self):
        if self.eastC >= 0 \
           and self.westC >= 0 and self.westM >= 0 and self.eastM >= 0 \
           and (self.eastM == 0 or self.eastM >= self.eastC) \
           and (self.westM == 0 or self.westM >= self.westC):
               return True
        else:
            return False

    # Checks is the boat valid or not
    def boatequal(self,other):
        if(other.boat == 'east'):
            missionaryInBoat =  abs(other.eastM-self.eastM)
            cannibalInBoat = abs(other.eastC - self.eastC)
            if(missionaryInBoat == 0):
                return True
            elif(cannibalInBoat == 0):
                return True
            elif(cannibalInBoat <= missionaryInBoat):
                return True
            else:
                return False
        else:
            missionaryInBoat =  abs(other.westM-self.westM)
            cannibalInBoat = abs(other.westC - self.westC)
            if(missionaryInBoat == 0):
                return True
            elif(cannibalInBoat == 0):
                return True
            elif(cannibalInBoat <= missionaryInBoat):
                return True
            else:
                return False

    # Checks is the given state goal or not
    def success(self):
        if self.eastC == 6 and self.eastM == 6:
            return True

        else:
            return False

    # Returns how many steps taken to find the solution
    def getStepNo(self):
        tempParent = self.parent
        stepNo = 0
        while tempParent:
            tempParent = tempParent.parent
            stepNo += 1
        return stepNo

    # Returns necessary information about the state
    def printInfo(self):
        return ("EastC: " + str(self.eastC) + " EastM: " + str(self.eastM) +
              " WestC: " + str(self.westC) + " WestM: " + str(self.westM) )

# Returns childrens of the given state as queue
def successors(currentState):
    children = [];
    if(singleStepMode):
        print("Childrens of the state: " + currentState.printInfo() + " will be found. \n")
        print("Write 'c' to continue , 'q' to exit program.\n")
        breakpoint()
    if currentState.boat == 'east':
        #-----1 Person passing-----
        # 1 cannibal (east to west)
        newState=State(currentState.eastC - 1,currentState.eastM,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 missionary (east to west)
        newState=State(currentState.eastC,currentState.eastM - 1,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----2 People passing-----

        # 2 missionaries (east to west)
        newState=State(currentState.eastC,currentState.eastM - 2,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 cannibals (east to west)
        newState=State(currentState.eastC - 2,currentState.eastM,'west')

        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 missionary and 1 cannibal (east to west)
        newState=State(currentState.eastC - 1,currentState.eastM - 1,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----3 People passing-----

        # 3 cannibals (east to west)
        newState=State(currentState.eastC - 3,currentState.eastM,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 3 missionaries (east to west)
        newState=State(currentState.eastC,currentState.eastM - 3,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 cannibal 1 missionary (east to west)
        newState=State(currentState.eastC - 2,currentState.eastM - 1,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 cannibal 2 missionary (east to west)
        newState=State(currentState.eastC - 1,currentState.eastM - 2,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----4 People passing-----

        # 4 missionaries (east to west)
        newState = State(currentState.eastC,currentState.eastM - 4,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 3 missionaries and 1 cannibal (east to west)
        newState = State(currentState.eastC - 1,currentState.eastM - 3,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 missionaries and 2 cannibals (east to west)
        newState = State(currentState.eastC - 2,currentState.eastM - 2,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 missionary and 3 cannibals (east to west)
        newState = State(currentState.eastC - 3,currentState.eastM - 1,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 4 cannibals (east to west)
        newState = State(currentState.eastC - 4,currentState.eastM,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----5 People passing-----

        # 5 missionaries (east to west)
        newState = State(currentState.eastC,currentState.eastM - 5,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 4 missionaries and 1 cannibal (east to west)
        newState = State(currentState.eastC - 1,currentState.eastM - 4,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 3 missionaries and 2 cannibals (east to west)
        newState = State(currentState.eastC - 2,currentState.eastM - 3,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 missionaries and 3 cannibals (east to west)
        newState = State(currentState.eastC - 3,currentState.eastM - 2,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 1 missionary and 4 cannibals (east to west)
        newState = State(currentState.eastC - 4,currentState.eastM - 1,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 5 cannibals (east to west)
        newState = State(currentState.eastC - 5,currentState.eastM,'west')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)
    else:
        #-----1 Person passing-----
        # 1 cannibal (west to east)
        newState=State(currentState.eastC + 1,currentState.eastM,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 missionary (west to east)
        newState=State(currentState.eastC,currentState.eastM + 1,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----2 People passing-----

        # 2 missionaries (west to east)
        newState=State(currentState.eastC,currentState.eastM + 2,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 cannibals (west to east)
        newState=State(currentState.eastC + 2,currentState.eastM,'east')

        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 missionary and 1 cannibal (west to east)
        newState=State(currentState.eastC + 1,currentState.eastM + 1,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        #-----3 People passing-----

        # 3 cannibals (west to east)
        newState=State(currentState.eastC + 3,currentState.eastM,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 3 missionaries (west to east)
        newState=State(currentState.eastC,currentState.eastM + 3,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


         # 2 cannibal 1 missionary (west to east)
        newState=State(currentState.eastC + 2,currentState.eastM + 1,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 1 cannibal 2 missionary (west to east)
        newState=State(currentState.eastC + 1,currentState.eastM + 2,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        #-----4 People passing-----
        # 4 missionaries (west to east)
        newState = State(currentState.eastC,currentState.eastM + 4,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 3 missionaries and 1 cannibal (west to east)
        newState = State(currentState.eastC + 1,currentState.eastM + 3,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 2 missionaries and 2 cannibals (west to east)
        newState = State(currentState.eastC + 2,currentState.eastM + 2,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

         # 1 missionary and 3 cannibals (west to east)
        newState = State(currentState.eastC + 3,currentState.eastM + 1,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 4 cannibals (west to east)
        newState = State(currentState.eastC + 4,currentState.eastM,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)




        #-----5 People passing-----

        # 5 missionaries (west to east)
        newState = State(currentState.eastC,currentState.eastM + 5,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 4 missionaries and 1 cannibal (west to east)
        newState = State(currentState.eastC + 1,currentState.eastM + 4,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 3 missionaries and 2 cannibals (west to east)
        newState = State(currentState.eastC + 2,currentState.eastM + 3,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 2 missionaries and 3 cannibals (west to east)
        newState = State(currentState.eastC + 3,currentState.eastM + 2,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)


        # 1 missionary and 4 cannibals (west to east)
        newState = State(currentState.eastC + 4,currentState.eastM + 1,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)

        # 5 cannibals (west to east)
        newState = State(currentState.eastC + 5,currentState.eastM,'east')
        if newState.noteaten() and newState.boatequal(currentState):
            newState.parent = currentState
            children.append(newState)
    return children

# Non-deterministic search algorithm
def ndsearch():

    # Define initial_state
    initial_state = State(0,0,'west')

    # If initial_state is the goal return
    if initial_state.success():
        return initial_state

    explored = set() # explored set keeps visited states

    # Form a one-element queue consisting only initial_state
    q = []
    q.append(initial_state)
    if(singleStepMode):
        print("Initial State has been added to queue.")
        print("Write 'c' to continue, 'q' to exit program.\n")
        breakpoint()

    # While loop until the queue is empty
    while q:
        # Remove the first state from queue
        state = q.pop()
        if(singleStepMode):
            print("The state " + state.printInfo() + " has been popped from the queue.")
            breakpoint()
        # If the goal state is found, announce success
        if state.success():
            return state

        # Add visited states to explored set
        explored.add(state)

        # Creating new paths by extending the
        # given state to all the neighbors of it
        children = successors(state)

        # Adding new paths to queue
        if(singleStepMode):
            print("The children of the state : " + state.printInfo() + " has been added to queue.")
        while children:
            temp = children.pop()

            # Rejecting all the new paths that may cause loops

            if temp not in explored:
                if(singleStepMode):
                    print("The state: " + temp.printInfo() + " has been added to queue.")
                q.append(temp)

        if(singleStepMode):
            print("Queue will be shuffled now! \n")

        # Randomize the queue
        random.shuffle(q)
        if(singleStepMode):
            print("Queue after shuffle: ")
            for stateT in q:
                print(stateT.printInfo() + "\n")
            print("Write 'c' to continue, 'q' to exit program.\n")
            breakpoint()


    # If no solution
    return None

# Print information about given state
def printState(state):
    cannibalEastString = ""
    cannibalWestString = ""
    missionaryEastString = ""
    missionaryWestString = ""

    cannibalsString = ""
    missionariesString = ""

    # For cannibals
    for i in range(state.eastC):
        cannibalEastString = cannibalEastString + "C"
    for i in range(state.westC):
        cannibalWestString = cannibalWestString + "C"

    cannibalsString = cannibalWestString
    while len(cannibalsString) <= 10:
        cannibalsString = cannibalsString + " " # Add space between west and east
    cannibalsString = cannibalsString + cannibalEastString
    print (cannibalsString) # Print cannibals

    # For missionaries
    for i in range(state.eastM):
        missionaryEastString = missionaryEastString + "M"
    for i in range(state.westM):
        missionaryWestString = missionaryWestString + "M"

    missionariesString = missionaryWestString
    while len(missionariesString) <= 10:
        missionariesString = missionariesString + " " # Add space between west and east

    missionariesString = missionariesString + missionaryEastString
    print (missionariesString,"\n") # Print missionaries

# Print path of the solution
def printSolution(solution):

    # Initialize solution path as list
    path = list()
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    count = len(path) - 1
    # Prints solution
    print("WEST        EAST")

    while count >= 0:
        printState(path[count]) # printState() function print detailed information about the state

        # Prints which action has taken
        if path[count].boat == 'east' and count != 0:

            print("RETURN    " + str(path[count].eastC - path[count - 1].eastC) + " CANNIBALS "
                  + str(path[count].eastM - path[count - 1].eastM) + " MISSIONARIES")

        elif count != 0:
            print("SEND  " + str(path[count].westC - path[count - 1].westC) + " CANNIBALS "
                  + str(path[count].westM - path[count - 1].westM) + " MISSIONARIES")

        count -= 1

def main():
    stepNo = 20
    count = 1

    print("Do you want to activate single step and detailed information mode.\n")
    global singleStepMode
    singleStepEnabler = input(" Enter 'Y' for yes 'N' for no: ")
    if(singleStepEnabler == 'Y' or singleStepEnabler == 'y'):
        singleStepMode = True
    else:
        singleStepMode = False
    while stepNo > 7:
        print("--------------------- " + str(count) + ". TRY ---------------------\n")
        count += 1
        solution = ndsearch()
        printSolution(solution)
        stepNo = solution.getStepNo()
        print("-----Solution found in " + str(stepNo) + " steps.---- \n")
        if(singleStepMode):
            print("Write 'c' to continue, 'q' to exit program.\n")
            breakpoint()



# if called from the command line, call main()
if __name__ == "__main__":
    main()
