# spin-addition
algorithm that can add arbitrary spins with the rules of quantum mechanics (in progress)

## Already Done/ What works
1. Lowering operator, basically give it a state with a set total spin and a set spin projection and it outputs a state with the same total spin and a spin projection of "1" lower
2. function that normalizes the coefficients of a state (.normalize() class function), give it a state and it returns the same state only that the norm squares of its coefficients sum to 1
3. function that gives the dot inner product of two states, does what it says you give it two states and it returns their inner product
4. function that gives the total spin of a state (get_total_spin() class function), give it a state and it produces the total spin of that state (not the "z" projection)
5. function that gives the z axis spin projection of a state (get_spin_proj() class function, gives as output the z projection of a state
6. function that finds a state orthogonal to given states, give it a list of states with the same spin projection as input and it returns a state orthogonal to them if it's unique
7. function that adds two spins, given two spins (e.g. 3/2 , 1/2) this function returns all states with a well defined total spin and spin projection
8. function to add spin to Object, produces all states that occur after adding an arbitrary spin to an already defined Object
9. function that adds an arbitrary amount of arbitrary spins, produces all states from the addition of these spins (e.g all states from adding spins [1/2 , 5/2 , 2])

## To Do (more or less in order of importance)
1. Make it more presentable and easy to use

## Goal
~~The final goal of this algorithm is to take as inputs an arbitrary amount of spins and produce all the states resulting from the addition of those spins~~  
Achieved!!!

## Theory
In Quantum Mechanics courses you learn that all particles have an intristic property called spin.  
The rules of adding those spins are not as trivial as simple addition and so require the use of some techniques that I plan to implement into the algorithm in order to be able to add two or more arbitrary spins.  

## How it works
*This part requires an understanding of spin addition and its rules*
The way it works is basically it takes two spins, finds the state with the highest spin spin projection ("up up") and uses the lowering operator to find all states with same total spin
Then it goes to the state with the second highest spin projection and produces a state orthogonal to it (with same spin projection). Using the lowering operator on this new state produces another set of states that are by definition orthogonal to the first ones. It continues by going to the next highest spin projection and produce an orthogonal state. The same procedure repeats until all possible states have been produced.

If more than two spins are given as input, it just adds the first two and then adds the third one to the objects produces by the addition of the first two.

## To add in README
visual representation of the way the algorithm works as well as visual representation of the algorithm itself.
