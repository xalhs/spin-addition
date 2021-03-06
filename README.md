# spin-addition
An algorithm that can add an arbitrary amount of  spins with the rules of quantum mechanics and produce all the states with a well defined Total spin and z-component of spin.

## Quick Start
1. pip install sympy
2. change in line 296 ```tot = produce_all_states([1/2 , 1/2 , 1/2])``` the three spins to whatever number of whichever spins you want to add 
3. and then just run the algorithm, it should print all possible states that are eigenvalues to total spin operator while also being eigenvalues to the total z-component spin operator

## To Do
- [x] Lowering operator, basically give it a state with a set total spin and a set spin projection and it outputs a state with the same total spin and a spin projection of "1" lower
- [x] function that normalizes the coefficients of a state (.normalize() class function), give it a state and it returns the same state only that the norm squares of its coefficients sum to 1
- [x] function that gives the dot inner product of two states, does what it says you give it two states and it returns their inner product
- [x] function that gives the total spin of a state (get_total_spin() class function), give it a state and it produces the total spin of that state (not the "z" projection)
- [x] function that gives the z axis spin projection of a state (get_spin_proj() class function, gives as output the z projection of a state
- [x] function that finds a state orthogonal to given states, give it a list of states with the same spin projection as input and it returns a state orthogonal to them if it's unique
- [x] function that adds two spins, given two spins (e.g. 3/2 , 1/2) this function returns all states with a well defined total spin and spin projection
- [x] function to add spin to Object, produces all states that occur after adding an arbitrary spin to an already defined Object
- [x] function that adds an arbitrary amount of arbitrary spins, produces all states from the addition of these spins (e.g all states from adding spins [1/2 , 5/2 , 2])
- [ ] Make it more presentable and easy to use

## Theory
In Quantum Mechanics courses you learn that all particles have an intristic property called spin.  
The rules of adding those spins are not as trivial as simple addition and so require the use of some techniques that I plan to implement into the algorithm in order to be able to add two or more arbitrary spins.  

## How it works
*This part requires an understanding of spin addition and its rules*
The way it works is basically it takes two spins, finds the state with the highest spin spin projection ("up up") and uses the lowering operator to find all states with same total spin
Then it goes to the state with the second highest spin projection and produces a state orthogonal to it (with same spin projection). Using the lowering operator on this new state produces another set of states that are by definition orthogonal to the first ones. It continues by going to the next highest spin projection and produce an orthogonal state. The same procedure repeats until all possible states have been produced. Visual representation below.

If more than two spins are given as input, it just adds the first two and then adds the third one to the objects produces by the addition of the first two.

## To add in README
Nothing for now

## Notes
The eigenstates can get degenerate after adding more than two spins (meaning there could be two eigenstates with the same total spin and z-axis spin projection value) in principle there isn't a preferable way to pick eigenstates from a system like that. However reading through the algorithm you might realize I separate them based on their origin. For example in the spin addition of three spin 1/2 particles, it results in two Objects with total spin 1/2, I differentiate them because one came from adding the spin 1/2 particle to the triplet state and the other by adding the spin 1/2 particle to the singlet state.  

Other methods I've seen that differentiate the degenerate states are by their cyclic permutation (https://physics.stackexchange.com/questions/29443/adding-3-electron-spins)

## How it works (visual)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_1.jpg)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_2.jpg)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_3.jpg)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_4.jpg)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_5.jpg)
![](https://github.com/xalhs/spin-addition/blob/master/media/spin_addition_Page_6.jpg)
