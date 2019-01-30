I have implemented both the parts of the assignment.
I have used python3.6.5 with opencv package.
I have tested on macOS Mojave (10.4.2).

I have referred to the official documentation from openCV to get to know about the framework.

To run the program,
I have used command line interface with the command.
 > python3 demosaic.py

I have also tried several more filters to go ahead with, but I didn't get better results on the second with them.
Some of the filters I've tried,

blue = np.array([[1.5, 0, 1.5], [0, 0, 0], [1.5, 0, 1.5]]) / 4
green = np.array([[0, 0, 0], [0, 2.5, 0], [0, 0, 0]]) / 2
red = np.array([[0, 1.5, 0], [1.5, 0, 1.5], [0, 1.5, 0]]) / 5

blue = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) / 1
green = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) / 4
red = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) / 1

# one of the possible filters (can be sharpened)
blue = np.array([[2, 0, 2], [0, 0, 0], [2, 0, 2]]) / 3
green = np.array([[0, 0, 0], [0, 4, 0], [0, 0, 0]]) / 3
red = np.array([[0, 2, 0], [2, 0, 2], [0, 2, 0]]) / 6