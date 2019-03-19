
import pyeda.inter as pyeda

def edgeToBooleanFormula(i, j):

    index = 0
    xFormula = ""
    yFormula = ""
    xBin = '{0:05b}'.format(i)
    yBin = '{0:05b}'.format(j)

    # iterate over the bits in binary i to formulate the xFormula
    for digit in xBin:
        
        if int(digit) == 0:
            xFormula += f"~x{index} & "
        elif int(digit) == 1:
            xFormula += f"x{index} & "
        
        index += 1    

    # reset the indexer
    index = 0

    # iterate over the bits in binary j to formulate the yFormula
    for digit in yBin:
        
        if int(digit) == 0:
            yFormula += f"~y{index} & "
        elif int(digit) == 1:
            yFormula += f"y{index} & "
        
        index += 1  
    
    # pop the last 3 chars from the expressions
    xFormula = pyeda.expr(xFormula[:-3])
    yFormula = pyeda.expr(yFormula[:-3])

    # form a new Formula with both x and y expressions
    E_i_j = pyeda.expr(pyeda.And(xFormula, yFormula))

    return E_i_j



# MAIN, not gucci
if __name__ == '__main__':
    
    edgeFormulaList = []
    
    # Graph G:
    # for all i, j ∈ S,
    # there is an edge from node i to node j iff (i + 3)%32 = j%32
    # OR
    # (i + 7)%32 = j%32.
    for i in range(0, 31):

        for j in range(0, 31):

            if (((i+3) % 32) == j % 32) | (((i+3) % 32) == j % 32):

                # send the edge to to formula creation function
                newFormula = edgeToBooleanFormula(i, j)
                
                # add the formula to the list
                edgeFormulaList.append(newFormula)


    # Create a big boolean formula, F, for the entire graph G
    
          
