import random
import ImplementedHeap
from ImplementedHeap import heap
import math

def distance(q1, q2):
    dlat = 2 * math.pi * (q2[0] - q1[0]) / 360
    mlat = 2 * math.pi * (q1[0] + q2[0]) / 2 / 360
    dlon = 2 * math.pi * (q2[1] - q1[1]) / 360
    return 6371009 * (dlat ** 2 + (math.cos(mlat) * dlon) ** 2) ** 0.5


#initalising all the variables for x,y coord
N = 0
#contains all x coordinates
graphx = []
#contains all y coordinates
graphy = []



#reading file and saving variables in input
filepage = open('graph1000.txt', 'r')
while(N != '1000'):

    #storing all x coordinates and y coordinates in designated arrays
    readfile = filepage.readline()
    inputline = readfile.split()
    removedcom = inputline[2]
    #remove commas
    removedcom = removedcom[:-1]
    N = inputline[0]
    graphx.append(removedcom)
    graphy.append(inputline[3])
    
readfile = filepage.readline()

#initialising dicionary storing interactions between points
connections = {}

#storing all the relationsships between nodes in the dictionary
count = 1
while(count <= 1000):
     readfile = filepage.readline()
     connections[count] = readfile
     count = count + 1

#initalizing list of 20 random coordinates
q1 = []
q2 = []
size = 0
while (size < 20):
    i = random.randint(1, 1001)
    if i not in q1:
        q1.append(i)
        size = size+1
       
size = 0
while(size < 20):
    j = random.randint(1,1001)
    if j not in q2:
        q2.append(j)
        size = size + 1

for inp in range(0,20):
    #start of djistras
    #obtaining random point
    startingpoint = q1[inp]
    endpoint = q2[inp]
    #arrays to put into the distance function
    p1 = []
    p2 = []
    #dictionary that stores the distance from the origin for each visited node
    dist = {}
    dist[startingpoint] = 0
    #keeping track of visited nodes
    visited = []

    #enqueue origin point
    queue = heap()
    queue.insertKey(dist[startingpoint])
    total = 0

    while(queue.isEmpty() == False):
        #dequeue node with minimum distance
        minimum = queue.removemin()
        #find minimum distance
        #and find in dictionary to get key node
        for key,val in dist.items():
            if val == minimum:
                savedkey = key
        #store dequeued keys into another array
        #so they are not visited again
        if (savedkey not in visited):
            visited.append(savedkey)
        
        #if the dequeued distance is the target node
        #then quit
        if (key == endpoint):
            answer = minimum
            break

        #taking out commas and spaces in input string
        connectionssplit = connections[savedkey].replace(',','')
        connectionssplit = connectionssplit.split()

        #save current key's coordinates in an array
        p1.append(float(graphx[savedkey-1]))
        p1.append(float(graphy[savedkey-1]))

        
        for i in range(2,len(connectionssplit)):
             #find neighboring nodes's coordinates of current key
             p2.append(float(graphx[int(connectionssplit[i])-1]))
             p2.append(float(graphy[int(connectionssplit[i])-1]))
            
             #compute distance between p1 and p2
             distv = distance(p1,p2)
             #add the computed distance to the total distance from the node
             diste = distv + minimum
             #if the node's distance is not infinity
             #then you have to compare new distance to previous distance
             if (int(connectionssplit[i]) in dist.keys()):
                    
                     #if the neighbornodes have been visited and dequeued
                     #skip it
                     if (int(connectionssplit[i]) not in visited):
                         #if the new distance is smaller than the previous distance
                         if (dist[int(connectionssplit[i])] > diste):
                             #update newdistance in dictionary and heap
                             queue.removeKey(dist[int(connectionssplit[i])])
                             dist[int(connectionssplit[i])] = diste
                             queue.insertKey(diste)
                     
             else:
                 #enqueue node in heap and record distance value in dictionary 
                 dist[int(connectionssplit[i])] = diste
                 queue.insertKey(diste)

             p2.pop()
             p2.pop()
             
        p1.pop()
        p1.pop()
        
             
    
        
        



    
    
    
