#*******************************************************************************
# * Name        : triads.py
# * Author      : Colby Chaffin
# * Description : Assignment 6 - Triads/Graphs
# * Pledge      : "I pledge my honor that I have abided by the Stevens Honor System" - cchaffin 104105591
# * Program Description: 
#       - triad_graphs.py takes data from a CSV file and determines how many triangles there are,
#           as well as how many different types of relationships exist.
#           This program identifies triads and calculates a lot of different data, including the expected
#           number of different relationships vs. the actual number.
# * Running Instructions: 
#   - run from terminal window:
#       - python3 triads.py
#       - the program will prompt you to enter the file that you wish to work with
#       - enter the file name. Ex: epinions.csv / epinions_small.csv / epinions96.csv
# ******************************************************************************

# Necessary imports
import csv
import networkx # suggested in assignment description

#setting up variables
numberOfEdges = 0
numberOfSelfLoops = 0
TotalEdges = 0 # (numberOfEdges - numberOfSelfLoops)
trustedNumber = 0
distrustedNumber = 0
positiveProb = 0 # p = number of (positive edges / TotalEdges)
negativeProb = 0 # (1 - p) where p = positiveProb
triangles = 0
TTT = 0
TTD = 0
TDD = 0
DDD = 0

graph = networkx.Graph() # set up the graph

f = input("Enter the name of the file you want to work with (including the file extension): ") # takes in file name

# open file for reading
with open(f, 'r') as openFile:
    readFile = csv.reader(openFile, delimiter = ',') #needed for CSV files (COMMA separated)
    for line in readFile: # loop for every line in the given file
        numberOfEdges = numberOfEdges + 1
        if int(line[0]) == int(line[1]): # check for self-loops
            numberOfSelfLoops = numberOfSelfLoops + 1
            continue
        graph.add_edge(int(line[0]), int(line[1]), relation = int(line[2])) # add new edge
        if int(line[2]) == 1: # check to see if it's trusted
            trustedNumber = trustedNumber + 1
        elif int(line[2]) == -1: # check to see if it's NOT trusted
            distrustedNumber = distrustedNumber + 1

# loop for each node
for edge in graph.edges:
    for node in graph.nodes:
        if graph.has_edge(edge[0], node) and graph.has_edge(edge[1], node): # go through nodes of each edge and see if there's a triad
            relation1 = graph[node][edge[0]]["relation"]
            relation2 = graph[node][edge[1]]["relation"]
            relation3 = graph[edge[0]][edge[1]]["relation"]
            counter = 0 # keep track of the relationships

            if relation1 == 1:
                counter = counter + 1
            if relation2 == 1:
                counter = counter + 1
            if relation3 == 1:
                counter = counter + 1
            if counter == 3:
                TTT = TTT + 1
            elif counter == 2:
                TTD = TTD + 1
            elif counter == 1:
                TDD = TDD + 1
            else:
                DDD = DDD + 1
            triangles = triangles + 1
           
#perform calculations on the collected data for terminal output results
triangles = int(triangles / 3)
TTT = int(TTT / 3)
TTD = int(TTD / 3)
TDD = int(TDD / 3)
DDD = int(DDD / 3)
TotalEdges = numberOfEdges - numberOfSelfLoops
positiveProb = round(trustedNumber / TotalEdges, 2)
negativeProb = round(1 - positiveProb, 2)

# probabilities of getting these different relationships (TTT,TTD,TDD,DDD and any order of them)
TTTprobability = round(100 * positiveProb * positiveProb * positiveProb, 1)
TTDprobability = round(3 * 100 * positiveProb * positiveProb * negativeProb, 1)
TDDprobability = round(3* 100 * positiveProb * negativeProb * negativeProb, 1)
DDDprobability = round(100 * negativeProb * negativeProb * negativeProb, 1)

# number of the selected relationships in the data (TTT,TTD,TDD,DDD and any order of them)
TTTnumber = round(TTTprobability / 100 * triangles, 1)
TTDnumber = round(TTDprobability / 100 * triangles, 1)
TDDnumber = round(TDDprobability / 100 * triangles, 1)
DDDnumber = round(DDDprobability / 100 * triangles, 1)

actualTTTprobability = round(100 * TTT / triangles, 1)
actualTTDprobability = round(100 * TTD / triangles, 1)
actualTDDprobability = round(100 * TDD / triangles, 1)
actualDDDprobability = round(100 * DDD / triangles, 1)

# print all results

print("Edges in network: " + str(numberOfEdges))
print("Self-loops: " + str(numberOfSelfLoops))
print("Edges Used: " + str(TotalEdges))
print("Trust Edges: " + str(trustedNumber) + "      " + "probability p: " + str(positiveProb))
print("Distrust Edges: " + str(distrustedNumber) + "        " + "probability 1-p: " + str(negativeProb))
print("Triangles: " + str(triangles))
print("\n")
print("Expected Distribution *" + "     " + "Actual Distribution")
print("Type  Percent  Number" + "       " + "Type  Percent  Number")
print("TTT    " + str(TTTprobability) + "      " + str(TTTnumber) + "         " + "TTT    " + str(actualTTTprobability) + "      " + str(TTT))
print("TTD    " + str(TTDprobability) + "      " + str(TTDnumber) + "         " + "TTD    " + str(actualTTDprobability) + "      " + str(TTD))
print("TDD    " + str(TDDprobability) + "      " + str(TDDnumber) + "         " + "TDD    " + str(actualTDDprobability) + "      " + str(TDD))
print("DDD    " + str(DDDprobability) + "      " + str(DDDnumber) + "         " + "DDD     " + str(actualDDDprobability) + "      " + str(DDD))
print("Total  " + str(round(TTTprobability + TTDprobability + TDDprobability + DDDprobability, 1)) + "     " + str(round(TTTnumber + TTDnumber + TDDnumber + DDDnumber, 1)) + "         " + "Total  " + str(round(actualTTTprobability + actualTTDprobability + actualTDDprobability + actualDDDprobability, 1)) + "     " + str(triangles))