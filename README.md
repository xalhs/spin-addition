# spin-addition
algorithm that can add arbitrary spins with the rules of quantum mechanics (in progress)

## Already Done/ What works
1. Lowering operator, basically give it a state with a set total spin and a set spin projection and it outputs a state with the same total spin and a spin projection of "1" lower
2. function that normalizes the coefficients of a state (.normalize() class function), give it a state and it returns the same state only that the norm squares of its coefficients sum to 1
3. function that gives the dot inner product of two states, does what it says you give it two states and it returns their inner product
4. function that gives the total spin of a state (get_total_spin() class function), give it a state and it produces the total spin of that state (not the "z" projection)
5. function that gives the z axis spin projection of a state (get_spin_proj() class function, gives as output the z projection of a state

## To Do (more or less in order of importance)
1. function that finds a state orthogonal to given states  (requires an efficient way to find the determinant of a matrix)
2. Make a way to add an Object to another Object (Objects can be spins or other objects with a well defined total spin that may be composed of smaller spins)
3. Make a way to add an Object to a Total (a Total as I have it defined now is a collection of Objects)

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
