# -6-Missionaries-and-6-Cannibals-a-non-deterministic-search-method
the goal was to implement a program that uses a non-deterministic search
method to solve the “6 Missionaries and 6 Cannibals” problem. We used the Python
programming language for our code. After understanding the problem and had an intuition
for how to solve it we have written the program.
equal() function is used to compare two states to understand if a state is already explored.
noteaten() function is used to test the state's validity, which checks whether the side has a
natural number of cannibals and missionaries and the number of cannibals is not greater than
missionaries on either side.
success() function is used to test if the current state is the goal state.
ndsearch() function is used to implement the non-deterministic search by shuffling the queue
for randomizing, keeping tracked of the explored states and randomly expanding the state to
its children.
boatequal() function is used for checking if there are more cannibals in the boat than
missionaries
