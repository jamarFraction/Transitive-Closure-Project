
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
    xFormula = xFormula[:-3]
    yFormula = yFormula[:-3]

    # form a new Formula with both x and y expressions
    E_i_j = f"({xFormula}) & ({yFormula})"


    return E_i_j

def joinEdgeFormulaList(edgeFormulaList):

    jointFormula = ""

    # Add the OR between each formula
    for edgeFormula in edgeFormulaList:
        
        jointFormula += f"({edgeFormula}) | "

    # Convert the formula string to a pyeda expression
    # chopping off the extra OR for formatting
    jointFormula = pyeda.expr(jointFormula[:-3])

    return jointFormula




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


    # Create a big boolean expression, F, for the entire graph G
    F = joinEdgeFormulaList(edgeFormulaList)

    # Convert F into BDD: R 
    R = pyeda.expr2bdd(F)
    
          
