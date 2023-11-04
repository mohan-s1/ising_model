# Part 1
(1) Set up a 2D lattice in the program, i.e., an indexed 2D matrix where each
matrix site is indexed by i and j, where both variables run from 0 to 19 (or 1
to 20, depending on the convention in your program of choice), and each
matrix site indexed by ij contains either “+1” or “-1”.

(2) Initialize the matrix by assigning +1 and -1 values at random to each matrix
site. This will require the use of a random number generator. You will also
want to have this part set up so that you can also start your simulation in the
all-up (all +1) or all-down (all -1) states too.

(3) Calculate the initial energy for your system, using the traditional Ising Model
energy. Make H and J both variables you can change easily. Implement 2D
periodic boundary conditions, so that row 0 interacts with row 19 as well as
with row 1, and the same for column 0 and column 19.

(4) Start the sampling of various states via a loop. Make the loop of variable
length – 10,000 steps through the loop is a good starting place (but making it
only 10 steps is more appropriate as you are writing and debugging the
code). Each time you execute the loop, your program should:

  a. Choose 1 lattice site at random.
  
  b. Calculate its interactions with its nearest neighbors and the field, i.e.
the portion of the energy that is influenced by this single spin.
  
  c. Flip it. (i.e. if it is -1, make it +1, if it is +1 make it -1. Can you think of
a computationally efficient way to do this transformation?)
  
  d. Recalculate its interaction with its nearest neighbors and the field.
  
  e. Use what you calculated in part (b) and (d) to calculate $`\Delta E_{Ising}`$ for this
“spin flip.” [NOTE – there is no need to calculate the TOTAL energy
again here, just calculating what has changed due to the flip of the
single, randomly-chosen spin, is enough and far more computationally
efficient. To check that this is working correctly, though, you may
want to add a step within the loop that does recalculate the entire
energy – just make it so that you only do a few times while you are
looping. For instance, if you go through the loop 10,000 times, then
maybe check your constantly-updated energy against the full energy
calculation every 1,000 times through.)
  
  f. If the spin flip reduced the energy, accept the change and update the
energy for the entire system (by adding the $`\Delta E_{Ising}`$ to the total energy
you had before the flip). If it increased the energy, reject the change,
flip the spin back, and keep the total energy you had before flipping
the spin.
  
  g. Print out a snapshot of the system (not every timestep, just a subset of
times during the simulation.) How to do this? You can simply print
out an array of 0s and 1s or 0s and _s, etc...
  
  h. Take any other measurements (leave as a section you can fill in with
some tasks later). Be sure to take this measurement whether or not
you accepted the spin flip.
  
  i. Start the loop again. Once this is running, check it in several ways to make sure it is doing what you want
it to be doing. Then print out some images of a series of microstates that start from
completely random and go towards some order. Choose appropriate J and T values
to make this happen. Try a few different options for the value of H. You may need
to vary the number of times you go through the loop to make sure it is reaching a
good endpoint.

Turn in a report that includes your code, your chosen values of J and H (along with
a justification), 3-4 images for each series you investigated – include these in
professional figure-style format with captions. (I’m expecting about 3-4 images for
each series). Then explain your observations in professional language. The code and
the figures will take up several pages, but, in total, the written portion should not
exceed 1 page.

In Part 2, you will implement a more advanced spin flip “acceptance criteria,” and
make more quantitative measurements of the system. In Part 3, you will implement
a biasing potential to help us observe rare states of the system
