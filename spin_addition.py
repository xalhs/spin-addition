import sympy
from sympy import sqrt
from sympy import*

# we want total to contain the individual small objects
# and also contain the big objects (irreducible representations)
# each big object contains states


class Base:
    def __init__(self, coefficient, base ,ind_spins):
        if coefficient == 0:
            return
        rat_base = [Rational(x) for x in base]
        self.base = rat_base
        self.coefficient = coefficient
        self.ind_spins = [Rational(y) for y in ind_spins]


    def add_base(self, coefficient, base):
        self.base.append(base)
        self.coefficient.append(coefficient)


#obj.states[Rational(3/2)]

#obj[1/2]
#obj[3/2]

#obj.states[1/2].bases[]
#obj.states[3/2]

class State:

    def __init__(self, bases=None, ind_spins=None):

        self.bases = bases
        self.ind_spins = ind_spins

        if bases != None:
            self.spin = self.get_spin_proj()
            self.ind_spins = bases[0].ind_spins
            self.normalize()
        else:
            self.bases = []

    def get_spin_proj(self):
        return sum(self.bases[0].base)

    def get_total_spin(self):

        new_state = Lowering(Raising(self))

        if new_state == None:
            new_state = State(None , self.ind_spins)
        for base in self.bases:
            new_state.add_dimension(Rational(self.spin*(self.spin +1))*base.coefficient , base.base  )

        prod =  InnerProduct(self , new_state)
        return ( (-1 + sqrt(1 + 4* prod))/2  )

    def remove_dimension (self, remove_base):
        for i , base in enumerate(self.bases):
            if base.base== remove_base:
                self.bases.pop(i)
                return


    def add_dimension(self, new_coef, new_base):
        try:

            if sum(new_base) != self.spin:
                return
        except:
            pass

        try:
            for base in self.bases:
                if base.base == new_base:
                    base.coefficient += new_coef
                    if base.coefficient == 0:
                        self.remove_dimension(base.base)
                    return
        except:
            pass

        if new_base == [] or new_coef == 0:
            return

        self.bases.append(Base(new_coef , new_base , self.ind_spins))
        self.spin = self.get_spin_proj()


    def normalize(self):
        global_coef = 0
        for base in self.bases:
            coef = base.coefficient
            global_coef += coef*coef

        for base in self.bases:
            base.coefficient *= sqrt(global_coef)/global_coef



    def __repr__(self):
        s1 = 'Spin {}\n'.format(self.spin)
        s2 =  str([ (' Coefficient: ' + repr(base.coefficient) + ' Bases: ' + repr(base.base)) for base in self.bases]) + "\n\n"
        #s3 = '\n Bases:' + repr(self.bases)

        return s1 + s2 #+ s3


class Object:

    def __init__(self, states):

        self.states = {s.spin: s for s in states}
        self.spin = states[0].get_total_spin()
        #self.spin = spin

    def __getitem__(self, key):
        return self.states[Rational(key)]

    def fill(self):
        try:
            new_state = self.states[self.spin]
            while new_state != None:
                new_state = Lowering(new_state)
                if new_state != None:
                    new_state.normalize()
                    self.states[new_state.spin] = new_state
        except:
            print("Couldn't get state with highest spin")

def Raising(state):
    if state == None:
        return
    new_state = State( None , state.ind_spins )
    for base in state.bases:
        for index  in range(len(base.base)):
            new_base = []
            j = state.ind_spins[index]
            for second_index , spin in enumerate(base.base):
                if second_index == index:
                    if spin == (state.ind_spins[index]):
                        new_base = []
                        new_coeff = 0
                        break
                    else:
                        new_base.append(spin + 1)
                        new_coeff = base.coefficient*sqrt(Rational(j*(j+1)-spin*(spin+1)))
                else:
                    new_base.append(spin)

            new_state.add_dimension( new_coeff, new_base)

    if new_state.bases == []:
        return

    #new_state.normalize()
    return new_state

def Lowering(state):
    if state == None:
        return

    new_state = State( None , state.ind_spins )

    for base in state.bases:
        for index  in range(len(base.base)):
            new_base = []
            j = state.ind_spins[index]
            for second_index , spin in enumerate(base.base):
                if second_index == index:
                    if spin == -(state.ind_spins[index]):
                        new_base = []
                        new_coeff = 0
                        break
                    else:
                        new_base.append(spin - 1)
                        new_coeff = base.coefficient*sqrt(Rational(j*(j+1)-spin*(spin-1)))
                else:
                    new_base.append(spin)


            new_state.add_dimension( new_coeff, new_base)

    if new_state.bases == []:
        return

    #new_state.normalize()
    return new_state

def Orthogonal(States):
    new_state = State( None , States[0].ind_spins )
    A = [[0 for x in range(len(States) +1 )] for y in range(len(States) +1)]
    spin = States[0].spin
    for state in States:

        #A.append([])
        if len(state.bases) > len(States) + 1:
            print("ERROR: can't orthogonalize states since more bases than states were given")
            return

    all_bases = [] ########make a list with all bases
    temp_state = State([Base(1 , States[0].ind_spins , States[0].ind_spins)] )
    for l in range(sum(States[0].ind_spins) - spin):
        temp_state = Lowering(temp_state)

    all_bases = [x.base for x in temp_state.bases]
    if len(all_bases) != len(States) + 1:
        return
    for i, base in enumerate(all_bases):      #States[0]['bases']):
        A[0][i] = base
        for j , state in enumerate(States):
            for state_base in state.bases:
                if state_base.base == base:
                    A[j+1][i] = state_base.coefficient

    for i , base in enumerate(all_bases):    ##########################
        B=[]
        for j in range(1, len(A)):
            B.append([])
            for k in range(len(A)):
                if k == i:
                    continue
                else:

                    B[j-1].append(A[j][k])
        new_state.add_dimension( ((-1)**i) * Matrix(B).det(), base)

    return new_state

def two_spin_adder(ind_spin1 , ind_spin2):
    ind_spin1 = Rational(ind_spin1)
    ind_spin2 = Rational(ind_spin2)
    Total = {'ind_spins': [ind_spin1 , ind_spin2] , 'Objects': []}
    for i in range(2*min(ind_spin1 , ind_spin2) + 1):
        orth_states = []
        for j in range(i):

            orth_states.append(Total['Objects'][j].states[ind_spin1 + ind_spin2 - i])
        if i == 0:
            obj = Object([State([Base(1 , [ ind_spin1 , ind_spin2 ] , [ ind_spin1 , ind_spin2 ]  )])])
        else:
            obj = Object([Orthogonal(orth_states)])
        obj.fill()
        Total['Objects'].append(obj)

    return Total

def InnerProduct(state1 , state2):
    prod = 0
    for base in state1.bases:
        for same_base in state2.bases:
            if base.base == same_base.base:
                prod += base.coefficient*same_base.coefficient

    return prod



states = [State([Base(1 ,[1, 1/2] , [1, 1/2] )] ) ,State([Base(1 ,[-1, -1/2] , [1, 1/2] )] ) ]

obj = Object(states)

nam = State([Base(1 ,[1, 1/2] , [1, 1/2])])

tot =  two_spin_adder(3/2 , 3/2)

for object1 in tot['Objects']:
    print(object1.states)
    print("\n\n")
