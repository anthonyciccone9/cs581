# Anthony Ciccone
# Due: 10/28/20

# assign05_Ciccone is meant to take data from epinions.com and construct relationship data from it. 
# It will answer general questions about the data to provide more background.

# Running instructions:
# python3 assign05_Ciccnone.py and then follow the prompt.

# imports
import csv
import networkx # was mentioned in the spec


edgeCount = 0 # total edges
loopCount = 0 # total self loops
pEdge = 0 # total positive edges (1)
nEdge = 0 # total negative edges (-1)
triads = 0 # triangles in the data
pprob = 0 # positive edge probability
nprob = 0 # negative edge probability
totEdges = 0 # Number of edges used to identify triads
graph = networkx.Graph() # initializes a graph object from networkx

fileName = str(input("Please enter the filename.\n"))
with open(fileName, 'r') as csvfile: #opens the file for type reading
    readFile = csv.reader(csvfile, delimiter = ',') #uses the built-in csv.reader method to create an iterator through the file
    for row in readFile:
        edgeCount+=1
        if row[0] != row[1]:
            graph.add_edge(int(row[0]), int(row[1]), relation = int(row[2]))
            if row[2] == '1':
                pEdge+=1
            else:
                nEdge+=1
        else:
            loopCount+=1

# For calculating the distribution of triad types
TTT = 0
TTD = 0
TDD = 0
DDD = 0
#These loops are where we can find the triads, it looks through all the nodes of each edge
for edge in graph.edges:
    for node in graph.nodes:
        if graph.has_edge(edge[0], node) and graph.has_edge(edge[1], node):
            total = 0 # to keep track of positive relations in the circle
            #possible combinations
            r1 = graph[node][edge[0]]["relation"]
            r2 = graph[node][edge[1]]["relation"]
            r3 = graph[edge[0]][edge[1]]["relation"]

            if r1 == 1:
                total+=1
            if r2 == 1:
                total+=1
            if r3 == 1:
                total+=1
                    
            if total == 3:
                TTT+=1
            elif total == 2:
                TTD+=1
            elif total == 1:
                TDD+=1
            else:
                DDD+=1

            triads+=1

# Filling in the missing spaces in the variables. Need to divide them by 3 because it finds the triangles 3 times
totEdges = edgeCount - loopCount
pprob = round(pEdge / edgeCount, 2)
nprob = round(1 - pprob, 2)
triads = int(triads / 3)
TTT = int(TTT / 3)
TTD = int(TTD / 3)
TDD = int(TDD / 3)
DDD = int(DDD / 3)

# probably values of getting any of TTT, TTD, TDD, or DDD
TTTprob = round(100*pprob*pprob*pprob, 1)
TTDprob = round(3 * 100*pprob*pprob*nprob, 1)
TDDprob = round(3 * 100*pprob*nprob*nprob, 1)
DDDprob = round(100*nprob*nprob*nprob, 1)

# Expected values for the four possibilities based on the probabilites above 
TTTexp = round(TTTprob / 100 * triads, 1)
TTDexp = round(TTDprob / 100 * triads, 1)
TDDexp = round(TDDprob / 100 * triads, 1)
DDDexp = round(DDDprob / 100 * triads, 1)

# Observed values of the four possibilies
TTTreal = round(100 * TTT / triads, 1)
TTDreal = round(100 * TTD / triads, 1)
TDDreal = round(100 * TDD / triads, 1)
DDDreal = round(100 * DDD / triads, 1)


# Output the data gathered
print("Edges in network: " + str(edgeCount))
print("Self-loops: " + str(loopCount))
print("Edges Used: " + str(totEdges))
print("Trust Edges: " + str(pEdge) + "    " + "probability p: " + str(pprob))
print("Distrust Edges: " + str(nEdge) + "    " + "probability 1-p: " + str(nprob))
print("Triangles: " + str(triads) + '\n')
print("Expected Distribution *" + "    " + "Actual Distribution")
print("Type  Percent  Number" + "      " + "Type  Percent  Number")
print("TTT   " + str(TTTprob) + "     " + str(TTTexp) + "         " + "TTT    " + str(TTTreal) + "     " + str(TTT))
print("TTD   " + str(TTDprob) + "     " + str(TTDexp) + "        " + "TTD    " + str(TTDreal) + "     " + str(TTD))
print("TDD   " + str(TDDprob) + "     " + str(TDDexp) + "         " + "TDD    " + str(TDDreal) + "     " + str(TDD))
print("DDD   " + str(DDDprob) + "      " + str(DDDexp) + "        " + " DDD     " + str(DDDreal) + "     " + str(DDD))
print("Total " + str(round(TTTprob + TTDprob + TDDprob + DDDprob, 1)) + "    " + str(round(TTTexp + TTDexp + TDDexp + DDDexp, 1)) + "        " + "Total  " + str(round(TTTreal + TTDreal + TDDreal + DDDreal, 1)) + "    " + str(triads))