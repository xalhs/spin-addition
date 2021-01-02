# spin-addition
algorithm that can add arbitrary spins with the rules of quantum mechanics (in progress)

## Already Done/ What works
1. Lowering operator, basically give it a state with a set total spin and a set spin projection and it outputs a state with the same total spin and a spin projection of "1" lower

## To Do (more or less in order of importance)
1. function that finds a state orthogonal to given states  (requires an efficient way to find the determinant of a matrix)
2. function that normalizes the coefficients of a state
3. function that gives the dot inner product of two states
4. function that gives the total spin of a state
5. function that gives the z axis spin projection of a state
6. Make a way to add an Object to another Object (Objects can be spins or other objects with a well defined total spin that may be composed of smaller spins)
7. Make a way to add an Object to a Total (a Total as I have it defined now is a collection of Objects)


## Theory
In Quantum Mechanics courses you learn that all particles have an intristic property called spin.  
The rules of adding those spins are not as trivial as simple addition and so require the use of some techniques that I plan to implement into the algorithm in order to be able to add two or more arbitrary spins.  

