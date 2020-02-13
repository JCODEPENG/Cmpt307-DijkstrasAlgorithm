import math

#implemented heap

class heap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapify(self):
        if (self.size == 0 or self.size == 1):
            return
        i = self.size-1
        
        
        while (i>=1):
            if (self.heap[i] <  self.heap[(i-1)//2]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[(i-1)//2]
                self.heap[(i-1)//2] = tmp
            i= i-1
        return

    def insertKey(self, k):
        self.heap.append(k)
        self.size = self.size+1
        self.heapify()
 
        return
    def isEmpty(self):
        if (self.size == 0):
            return True
        else:
            return False
    def removeKey(self,x):
        index = 0
        if (self.size == 0):
            return
        if (self.size == 1):
            self.heap[0] = x
        for j in self.heap:
            if x == j:
                break
            index = index + 1

        for i in range(index, self.size - 1):
            self.heap[i] = self.heap[i+1]
        
        self.heap.pop()
        self.size = self.size - 1
        return 
            
                
    def removemin(self):
        minnumber = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop()
        count = 0;
        for i in self.heap:
            if (2*count + 1 < self.size-1):
                if (i > self.heap[2*count + 1]):
                    tmp = i
                    self.heap[count] = self.heap[2*count + 1]
                    self.heap[2*count + 1] = tmp
                    
            elif (2*count + 2 < self.size-1):
                if(i < self.heap[2*count + 2]):
                    tmp = i
                    self.heap[count] = self.heap[2*count + 2]
                    self.heap[2*count + 1] = tmp
            count = count + 1
        self.size = self.size-1
        self.heapify()
        return minnumber

def distance(q1, q2):
    dlat = 2 * math.pi * (q2[0] - q1[0]) / 360
    mlat = 2 * math.pi * (q1[0] + q2[0]) / 2 / 360
    dlon = 2 * math.pi * (q2[1] - q1[1]) / 360
    return 6371009 * (dlat ** 2 + (math.cos(mlat) * dlon) ** 2) ** 0.5
