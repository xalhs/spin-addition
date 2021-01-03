#import math
import sympy
from sympy import sqrt
from sympy import*

# we want total to contain the individual small objects
# and also contain the big objects (irreducible representations)
# each big object contains states


class Base:
    def __init__(self, coefficient, base ,ind_spins):
        self.base = base
        self.coefficient = coefficient
        self.ind_spins = ind_spins


    def add_base(self, coefficient, base):
        self.base.append(base)
        self.coefficient.append(coefficient)

class State:

    def __init__(self, bases=None, ind_spins=None):

        self.bases = bases
        self.ind_spins = ind_spins

        if bases != None:
            self.spin = self.get_spin_proj()
            self.ind_spins = bases[0].ind_spins
        else:
            self.bases = []

    def get_spin_proj(self):
        print(self.bases[0].base)
        return sum(self.bases[0].base)


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
                    return
        except:
            pass

        if new_base == [] or new_coef == 0:
            return

        self.bases.append(Base(new_coef , new_base , self.ind_spins))
        self.spin = self.get_spin_proj()


    def __repr__(self):
        s1 = 'Spin {}\n'.format(self.spin)
        s2 =  str([ (' Coefficient: ' + repr(base.coefficient) + ' Bases: ' + repr(base.base)) for base in self.bases]) + "\n\n"
        #s3 = '\n Bases:' + repr(self.bases)

        return s1 + s2 #+ s3


class Object:

    def __init__(self, states , spin ):

        self.states = {s.spin: s for s in states}
        self.spin = spin

    def fill(self):
        try:
            new_state = self.states[self.spin]
            while new_state != None:
                new_state = Lowering(new_state)
                if new_state != None:
                    self.states[new_state.spin] = new_state
        except:
            print("Couldn't get state with highest spin")

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

def InnerProduct(state1 , state2):
    prod = 0
    for base in state1.bases:
        for same_base in state2.bases:
            if base.base == same_base.base:
                prod += base.coefficient*same_base.coefficient

    return prod



states = [State([Base(1 ,[1, 1/2] , [1, 1/2] )] ) ,State([Base(1 ,[-1, -1/2] , [1, 1/2] )] ) ]

obj = Object(states , 1.5)

nam = State([Base(1 ,[1, 1/2] , [1, 1/2])])
