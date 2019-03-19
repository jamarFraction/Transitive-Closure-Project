
import pyeda.inter as pyeda

# MAIN, not gucci
if __name__ == '__main__':
    
    
    # initialize the Node space, S = [0..31]
    S = pyeda.exprvars('x', 32)

    for i in range(0, 31):

        for j in range(0,31):

            if (((i+3) % 32) == j % 32) | (((i+3) % 32) == j % 32):
                
                # found a satisfying edge
                print(f"{i} and {j}")