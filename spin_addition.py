import math
from math import sqrt


# we want total to contain the individual small objects
# and also contain the big objects (irreducible representations)
# each big object contains states


#Total[1][]

#Total = { small_spins , total_spin, Objects }

#total_spin = [spin_of_object0 , spin_of_object1]

#Objects = [Object0, Object1 ]

#Object = { spin_proj , states }

#states = [state0  state1 state2]

#state = {coefficients, bases}

#bases = [base0 , base1 , base2]
#coefficients = [coefficient0 , coefficient1 , coefficient2]

#coefficient0 = 1
#base0 = [+1/2 , +3/2 , -1/2 ,0]

#actual state -->      Coefficient[0] bases[0]

Total = {'small_spins': [0.5, 0.5, 0.5], 'total_spin': [], 'Objects': [{'spin_proj': [], 'states': [{'coefficients': [1], 'bases': [[0.5, 0.5, 0.5]]}]}]}

Total = {'small_spins': [1, 0.5], 'total_spin': [1.5], 'Objects': [{'spin_proj': [], 'states': [{'coefficients': [1], 'bases': [[1, 0.5]]}]}]}

#Total = {'small_spins': [1, 0.5], 'Objects': [{'states': [{1.5: [{'coefficients': [1], 'bases': [[1, 0.5]]}]}] , 'total_spin': 1.5}]} ###second idea for structure


def Lowering(small_spins , State):
    new_state = {'coefficients': [] , 'bases' : [] }
    for i, base in enumerate(State['bases']):  # up up up up


        for index  in range(len(base)):
            new_base = []
            print(str(index) + "at second loop")
            j = small_spins[index]
            for second_index , spin in enumerate(base):
                print(str(second_index) + "at third loop")
                if second_index == index:
                    if spin == -(small_spins[index]):
                        new_base = []
                        print("break")
                        break
                    else:
                        new_base.append(spin - 1)
                        print("lowered ")
                        print(new_base)
                        new_coeff = State['coefficients'][i]*sqrt(j*(j+1)-spin*(spin-1))
                else:
                    print("not lowered ")
                    print(new_base)
                    new_base.append(spin)

            if new_base == []:
                pass
            elif new_base in new_state['bases']:
                for k, same_base in enumerate(new_state['bases']):
                    print("same_base")
                    print(same_base)
                    print(new_base)
                    if same_base == new_base:
                        print("#"*50)
                        print(new_state['coefficients'][k])
                        print(new_coeff)
                        new_state['coefficients'][k] += new_coeff
            else:
                new_state['bases'].append(new_base)
                new_state['coefficients'].append(new_coeff)
    print(new_state)
    return new_state

def equiv(Object , Object2):
    pass


nam = Lowering( Total['small_spins'] ,   Total['Objects'][0]['states'][0])
nam2 = Lowering( Total['small_spins'] ,   nam)
nam3 = Lowering( Total['small_spins'] ,   nam2)
            #    new_base.append()
        #for spin in base:
