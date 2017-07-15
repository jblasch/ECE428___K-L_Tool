'''
Author: Jessica Blasch
Date: 29, November, 2015
Class: ECE 428
Description: This program reads in a file (i.e. a text file) containing graph 
             information and determines the optimal partitioning based on an  
             initial split down the middle.
            - The first line contains the number of nodes and number of edges
            - All following lines contain edges (connections) associated with 
              the nodes.It is assumed the list is in ascending order of nodes 
              and there is a space in between the numbers. For example:
                    5 7       (nodes, edges)
                    2 3 4 5   (connections for node 1)
                    1 4       (connections for node 2)
                    1 4 5
                    1 2 3
                    1 3
            
            - The program will output a text file with the name of the file you 
              ran: KL_tool_output_on_"your file name and extension"
                
                e.g. KL_tool_output_on_data.txt

'''
    #These imports are built-in to python and do not require downloading a module
import copy
from datetime import datetime

'''
**********************************************************************
Begin Program
**********************************************************************
'''
begin = datetime.now()
print
print '::::::::::::::: Welcome to the KL Tool Program :::::::::::::::'
print
print 'This program reads in a file (i.e. a text file) with graph information,'
print 'seperates the nodes into two partitions, and writes to a file all iterations' 
print '(if any) of switching nodes in the partitions, the cut cost of the iteration,'
print 'as well as the final partition with the minimal cut.'
print
print 'The output file will have the name of the file you ran like the following:'
print 'KL_tool_output_on_"your file name and extension'
print 'e.g. KL_tool_output_on_data.txt'                
print
print 'To run this program: '
print '        1) Make sure your data file is in the same folder as this program.'
print '        2) Please have your file formatted like such:'
print '                    5 7       (nodes, edges)'
print '                    2 3 4 5   (connections for node 1)'
print '                    1 4       (connections for node 2)'
print '                    1 4 5      etc.'
print '                    1 2 3'
print '                    1 3'
print

f = raw_input('Please enter the name (with extention) of the file you wish to run: ')

print
print
print
print
print 'date = %s %s, %s'%(begin.month, begin.day, begin.year)
print 'program start (h:m:s) = %s: %s: %s'%(begin.hour, begin.minute, begin.second)
print
    #open file and read in as variable called inData
with open(f, 'r') as inData:    
        
        #read first line and map values as int to nodes & edges
    nodes,edges  = map(int, inData.readline().split())    
        
        #create an empty array to house incoming data
    data = []    
        
        #for the rest of the lines read in, fill empty data array with items/indexes
    for line in inData:
        data.append([int(x) for x in line.split()])

    #save the original number of nodes in case there's a dummy node
nodesOrig = nodes

    #create dummy node for graph with odd nodes
dNode = [int(0)] 

    #if not even number of nodes, add dummy node        
if nodes % 2 != 0:
    data.append(dNode)
    nodes +=1
    
    #create a list of the number of nodes in the incoming data *includes the dummy node, if present
nodeCount = 0                                                        
nodeList = []
for line in data:
    nodeCount +=1
    nodeList.append(nodeCount) 
    
    #Combine the list of nodes and list of connect values in a dictionary     
graphDict = dict(zip(nodeList,data))
#print graphDict

    #create a list for the specific nodes in partition 1 ( e.g. [1 , 2, 3] )
nodesA = nodeList[:nodes/2]

    #create a list for the specific nodes in partition 2 ( e.g. [4 , 5, 6] )
nodesB = nodeList[nodes/2:]

    #Deep copy primes, so they don't point to the same values as the originals
nodesAPrime = copy.deepcopy(nodesA)
nodesBPrime = copy.deepcopy(nodesB)

    #Deep copy node partitions to keep track of whoich nodes are in each partition
graphNodesA = copy.deepcopy(nodesA)
graphNodesB = copy.deepcopy(nodesB)

    #Set up locked lists before going into functions   ***Don't need
#nodesLockedA = []
#nodesLockedB = []

    #Set up a partial gain list to append after determining high gain set
swapGainList = []


'''
**********************************************************************
Begin list of functions to perform KL Algorithm calculations for potential node swaps  
**********************************************************************
'''

'''
    Function to compare the list of nodes to get the cut cost
'''
def graph_cut_cost(gNodeA, gNodeB, gDict):
    total = 0
    
    for key in gDict.keys():              
        for x in gNodeB:
            if x == key:
                for y in gNodeA:
                    if y in gDict[key]:            
                        total +=1
                        
    return total
                

'''
    Function to calculate internal and external cut costs
'''                                                                    
def cut_cost(nPrime, gNodeList, gDict):
    connectsList = []
    costList = []
    
        #Make a list of connect values for nList2
    for node in gNodeList:
        for key in gDict.keys():
            if node == key:
                connectsList.append(gDict[key])
                
        #Compare nList1 with connect values list for nList2 
    for node in nPrime:
        total = 0
        for line in connectsList:
            for x in line:
                if node == x:
                    total +=1
        costList.append(total)
    
    return costList


'''
    Function to calculate D-Values
'''
def d_values(extCutCostList, intCutCostList):
    Lmerge = [x - y for x, y in zip(extCutCostList, intCutCostList)]
    
    return Lmerge


'''
    Function to caluclate gains -no node pairs attached yet
'''
def swap_gain_list(dValA, dValB, nListA, nListB, gDict):
    connectsList = []
    addDABList = []
    cABList = []
       
        #Make a list of connect values for nListB
    for node in nListB:
        for key in gDict.keys():
            if node == key:
                connectsList.append(gDict[key])
                
        #Make a list of (Da + Db) values
    for dA in dValA:
        for dB in dValB:
            dAplusB = dA + dB
            addDABList.append(dAplusB)
        
        #Calculate cAB connections
    for node in nListA:
        for line in connectsList:
            total = 0
            for x in line:
                if node == x:
                    total += 1
            cAB = 2*total 
            cABList.append(cAB)
            
        #Calculate gains gab = Da + Db - 2cab                
    Lmerge = [x - y for x, y in zip(addDABList, cABList)] 
    
    return Lmerge


'''
    Function to pair potential node swap pairs with associated gain values
'''
def node_gain_list(nListA, nListB, gList):
    nAnB = []
    nAnBList = []
  
    for x in nListA:
        for y in nListB:
            nAnB = [x] + [y]
            nAnBList.append(nAnB)
    
    Lmerge = zip(nAnBList, gList)
    
    return Lmerge
    
          
'''
    Function to determine the highest gain and node pair of valid node sets
''' 
def high_gain(Lmerge):
    gain = -10000
    hiGain = -10000
    hiGainSet = []
      
    for line in Lmerge:
        if line[0] not in nodesBPrime:        
            nAB = line[0]
        gain = line[1]
        
        if gain > hiGain:
            hiGain = gain
            hinAB = nAB
            hiGainSet = [hinAB] + [hiGain]
    
    return  hiGainSet


'''
    Function to create altered Prime lists and get Locked nodes 
'''

def new_node_lists(nListA, nListB, hgSet):
    nAPrime = []
    nBPrime = []
    #nLockedA = [] #As it turns out, we don't really need to keep track of this.
    #nLockedB = [] #The reason being that the prime lists delete locked nodes, so 
                  #they are not used in calculations.
      
    a2bSwap = hgSet[0][0] #node from A moving to B
    b2aSwap = hgSet[0][1] #node from B moving to A
        
    #Aprime
    for node in nListA:
        if node != a2bSwap:
            nAPrime.append(node)
    nAPrime.sort()
    
    #A-Locked
    #nLockedA.append(b2aSwap)
    
    #BPrime
    for node in nListB:
        if node != b2aSwap:
            nBPrime.append(node)
    nBPrime.sort()
    
    #B-Locked
    #nLockedB.append(a2bSwap)
    
    return nAPrime, nBPrime#, nLockedA, nLockedB


'''
    Function to update which nodes are in each partition 
'''
def update_partition(hgSet, gNodesA, gNodesB ):
    
    #Update nodes in partition A
    for line in gNodesA:
        if line == hgSet[0][0]:
            gNodesA.remove(line)
    
    gNodesA.append(hgSet[0][1])
    gNodesA.sort()
    
    #Update nodes in partition B
    for line in gNodesB:
        if line == hgSet[0][1]:
            gNodesB.remove(line)
    gNodesB.append(hgSet[0][0])
    gNodesB.sort()
    
    return gNodesA, gNodesB

    
'''
**********************************************************************
One function to rule them all (in a loop) *Hoping to cut down on memory draw
**********************************************************************
'''    

def do_that_dance(do, that, funky, dance, mama):
    nodesAPrime2 = do 
    graphNodesA2 = that 
    nodesBPrime2 = funky
    graphNodesB2 = dance 
    graphDict = mama 
    
        #Calculate internal cut costs based on Prime lists which will shrink as you go 
    internalCutCostA2 = cut_cost(nodesAPrime2, graphNodesA2, graphDict)
    internalCutCostB2 = cut_cost(nodesBPrime2, graphNodesB2, graphDict)
            
        #Calculate internal cut costs based on Prime lists which will shrink as you go        
    externalCutCostA2 = cut_cost(nodesAPrime2, graphNodesB2, graphDict)
    externalCutCostB2 = cut_cost(nodesBPrime2, graphNodesA2, graphDict)
            
        #Calculate D-Values            
    dValuesA2 = d_values(externalCutCostA2, internalCutCostA2)
    dValuesB2 = d_values(externalCutCostB2, internalCutCostB2)
            
        #Calculate gains for potential swaps         
    swapGainsAloneList2 = swap_gain_list(dValuesA2, dValuesB2, nodesAPrime2, nodesBPrime2, graphDict)
            
        #Pair node sets with gains for potential swaps            
    nodesSwapAndGainList2 = node_gain_list(nodesAPrime2, nodesBPrime2, swapGainsAloneList2)
            
        #Find high-gain node pair
    highGainSet2  = high_gain(nodesSwapAndGainList2)
        
        #Delete high gain node pair from respective prime list
    nodesAPrime2, nodesBPrime2 = new_node_lists(nodesAPrime2, nodesBPrime2, highGainSet2)
        
        #Update nodes in partition A and B
    graphNodesA2, graphNodesB2 = update_partition(highGainSet2, graphNodesA2, graphNodesB2 )
    
        #Only return what is needed, so the program doesn't use excess memory    
    return highGainSet2, nodesAPrime2, nodesBPrime2, graphNodesA2, graphNodesB2
 
 
'''
**********************************************************************
Begin list of functions to determine KL Algorithm real swaps and process final partition  
**********************************************************************
'''
       
        #Function to take the list of potential gains and calculate the max partial gain 
def partial_gain(sGList):
    maxPGain = -10000   
    pgTotal = 0
    maxPGSwapIndex = 0
    
    c=0
    for line in swapGainList:
        pgTotal+=sGList[c][1]
        if pgTotal> maxPGain:
            maxPGain=pgTotal #max partial gain in list
            maxPGSwapIndex=c  #index at which max partial gain occurs
        c+=1
       
    return maxPGain, maxPGSwapIndex
    
    
    #Function that determines the new partition after real swap        
def partition_iteration(nListA, nListB, sgList, sgIndex):
    count = 0
       
    for n in range(0,sgIndex+1):
            #Update the partitions for a real swap
        A,B=update_partition(sgList[count], nListA, nListB)
        nListA=copy.deepcopy(A)
        nListB=copy.deepcopy(B)
        count+=1
    
    return nListA, nListB   


'''
************************************************************
Begin KL Algorithm printout to screen and file out
************************************************************
'''

        
    #Begin printing to file
file = open("KL_tool_output_on_%s" %f, "w") 
file.write("The program was run on file named %s " %f)
file.write("\n") 
file.write("\n")
file.write("::::: Initial conditions for this graph :::::")
file.write("\n")
file.write("Nodes = %s" %(nodesOrig))
file.write("\n")
file.write("Edges = %s" %(edges))
file.write("\n")

    #Get the initial graph cut cost
graphCutCost = graph_cut_cost(graphNodesA, graphNodesB, graphDict)

file.write("The initial cut cost is: %s " %graphCutCost)
file.write("\n")
file.write("\n")

FINAL_COUNT = 0

Boolean = True

    #Perform loop until partial gains < 0 
while Boolean:
    
    lenListInitial = len(nodesAPrime)
    counter = 1 
    
    #Perform all the initial calulations for all potential node swaps 
    while (counter <= lenListInitial):
        
            #Get potential partition lists, updated prime lists and high gain from current       
        highGainSet, nodesAPrime, nodesBPrime, graphNodesA, graphNodesB = do_that_dance(nodesAPrime, graphNodesA, nodesBPrime,graphNodesB, graphDict)
                  
            #Append swap gain list with high gain node pair
        swapGainList.append(highGainSet)
        counter += 1    
    
        #Determine the maximum partial gain and the index it occurs at            
    maxPartialGain, maxPartialGainIndex = partial_gain(swapGainList)       
    
    if maxPartialGain > 0:
        FINAL_COUNT +=1 #Print something to screen, so you know the propgram is running on large files
        print 'Iteration', FINAL_COUNT   
        nodesA, nodesB = partition_iteration(nodesA, nodesB, swapGainList, maxPartialGainIndex)
        graphNodesA = copy.deepcopy(nodesA)
        graphNodesB = copy.deepcopy(nodesB)
        nodesAPrime = copy.deepcopy(nodesA)
        nodesBPrime = copy.deepcopy(nodesB)
        swapGainList = []   #Reset this, or it will continue to append
        graphCutCost = graph_cut_cost(graphNodesA, graphNodesB, graphDict)
        file.write("::::: Iteration %s :::::" %(FINAL_COUNT))
        file.write("\n")
        file.write("The cut cost is: %s " %(graphCutCost))
        file.write("\n")
        file.write("\n")        
        
        #If there are no gains > 0 print the final partition    
    else:
        file.write('----------------------------')
        file.write("\n")
        file.write('       Final Partition      ')
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write("Partition 1. List of vertices: %s" %nodesA)
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("Partition 2. List of vertices: %s" %nodesB)
        Boolean = False
print
print '*** Your output file is ready in the folder with your data file. ***'
end = datetime.now()
print
print 'date = %s %s, %s'%(end.month, end.day, end.year)
print 'program completion (h:m:s) = %s: %s: %s'%(end.hour, end.minute, end.second)


file.close()