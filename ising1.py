import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.ndimage import generate_binary_structure
from scipy.signal import convolve2d

J = 1 # initialize coupling const

H = -3 # initialize external field

N = 20 # initialize number of sites

iter = 10001 # initialize number of iterations

class Ising():
    def __init__(self, N: int, H: float, J: float, loops:int):
        self.N = N # param for # of sites
        self.lattice = np.random.randint(0, 2, size = (N, N)) # reads in 0, 1 randomly
        self.lattice[self.lattice == 0] = -1 # for each randomly generated 0 --> -1 
        self.H = H # param for external field strength
        self.J = J # param for coupling const
        self.loops = loops # param for # iter
        
    def display(self): # plots lattice at a given point in time
        visual = plt.imshow(self.lattice, cmap = "coolwarm", alpha = 0.85) 
        plt.title('Lattice Visualized', fontweight ="bold") 
        plt.colorbar(visual) 
        # plt.savefig("path_to_image/image.jpg", dpi = 800)
        plt.show()

    def get_energy(self): # returns total energy corresponding to our expression for E_v 
        '''
        Function that accepts self.lattice, number of sites (n), external field (H), 
        and coupling constant (J)
        E1 which is an nxn array indexed by i, j corresponding to each self.lattice site 
        E2 which is an nxn array indexed by i, j corresponding to each self.lattice site's nn 
        interactions 
        Returns: 
        E_tot which is the sum of E1 and E2 added together  
        '''
        kernel = generate_binary_structure(2, 1) # generate 3x3 convolution kernel 
        #where central points  and next nearest neighbors have values of true
        kernel[1][1] = False # set central point in kernel to false to avoid si*si 
        # being part of the sum 
        E2 = -1/2 * self.lattice * self.J * convolve2d(self.lattice, kernel, mode = 'same'
                                                       , boundary = 'wrap') # 1/2 here 
        # to get rid of double counting
        E1 = []
        for i in range(len(self.lattice)):
            for j in range(len(self.lattice)):
                E1.append(self.lattice[i, j] * self.H * -1) # find each s_i, multiply it by 
                # the external field, 
                # and -1 before appending to list titled "term_one"
        E_tot = np.sum(E1) + np.sum(E2)
        return E_tot
    
    def get_mag(self):
        ''' returns net spin of lattice'''
        return np.sum(self.lattice)

    def mcmove(self):
        ''' This is to execute moves'''      
        i = np.random.randint(0, self.N) # pick random site
        j = np.random.randint(0, self.N) # pick random site
        spin_i = self.lattice[i, j] # initial spin
        spin_f = -1 * spin_i # proposed spin flip
        E_i = 0 # initialize var for initial energy
        E_f = 0 # initialize var for post-flip energy
        E_i += spin_i * -H # pre-flip interaction with field 
        E_f += spin_f * -H # post-flip interaction with field
        if i >= 0:
            E_i += spin_i * self.lattice[i-1, j] * -J # periodic boundary conditions work fine when 
            # i = 0 --> 0-1 = -1 
            # which then indexes the bottom most element in the same column
            E_f += spin_f * self.lattice[i-1, j] * -J
        if i < self.N-1:
            E_i += spin_i * self.lattice[i+1, j] * -J
            E_f += spin_f * self.lattice[i+1, j] * -J
        if i+1 == self.N:
            E_i += spin_i * self.lattice[0, j] * -J # if i+1 == length(latice) = n, go to top of 
            # lattice in same column i.e. [0, j]
            E_f += spin_f * self.lattice[0, j] * -J
        if j >= 0:
            E_i += spin_i * self.lattice[i, j-1] * -J # periodic boundary conditions work fine 
            # when j = 0 --> 0-1 = -1 
            # which then indexes the bottom most element in the same column
            E_f += spin_f * self.lattice[i, j-1] * -J
        if j < self.N-1:
            E_i += spin_i * self.lattice[i, j+1] * -J
            E_f += spin_f * self.lattice[i, j+1] * -J
        if j+1 == self.N:
            E_i += spin_i * self.lattice[i, 0] * -J # if j+1 == length(latice) = n, 
            # go to leftmost element in the
            # same row of the lattice [i, 0]
            E_f += spin_f * self.lattice[i, 0] * -J
        dE = E_f - E_i # check for difference in energy between flips
        if (dE > 0): # if energy diff < 0, flip
            self.lattice[i, j] = spin_i
        if (dE < 0): # if energy diff > 0, flip
            self.lattice[i, j] = spin_f
    
        
    def simulate(self):   
        ''' Use function mcmove for each iteratation denoted by self.loop'''
        time = np.arange(0, self.loops, 1) # array to later plot net spin/energy
        # as a function of runs
        net_energy = [] # list to hold net energy at each iter
        net_spin = [] # list to hold net spin at each iter
        for i in range(self.loops):
            self.mcmove() # call mcmove to propose spin flip and assess
            net_energy.append(self.get_energy()) # calc total energy at each iter
            # and append to list
            net_spin.append(self.get_mag()) # calc total spoin at each iter
            # and append to list
            if i == 1: self.display() # display lattice at t = 1
            elif i == 100: self.display() # display lattice at t = 100
            elif i == 1000: self.display() # display lattice at t = 1000
            elif i == self.loops - 1: # display lattice at t = t_max
                self.display()
                plt.plot(time, net_energy)
                plt.xlabel('Algorithm Run Time')
                plt.ylabel('Energy')
                plt.title(r'Net Energy')
                # plt.savefig("path_to_image/net_e.jpg", dpi = 800)
                plt.show()
            if i == self.loops - 1:
                plt.plot(time, net_spin)
                plt.xlabel('Algorithm Run Time')
                plt.ylabel('Net Spin')
                plt.title(r'Net Spin')
                # plt.savefig("path_to_image/net_s.jpg", dpi = 800)
                plt.show()
            

model = Ising(N, H, J, iter) # Parameters to our object, Ising

model.simulate() # run the function, simulate
