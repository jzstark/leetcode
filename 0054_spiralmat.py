# check if over border; code clean enough?

class Solution(object):

    def __init__(self, matrix):
        n = len(matrix)
        assert(n > 0)
        m = len(matrix[0])
        assert(m > 0)

        ul = (0, 0)
        ur = (0, m - 1)
        ll = (n-1, 0)
        lr = (n-1, m-1)


    def move(self, id, direction):
        new_direction = direction
        
        if (id is self.ur): 
            new_direction = 1
            self.ul[0] += 1; self.lr[] 
        if (id is self.lr):
            new_direction = 2
            self.ur[1] -= 1; self.ll[]
        if (id is self.ll):
            new_direction = 3
            self.lr[0] -= 1; self.ul[]
        if (id is self.ul):
            new_direction = 0
            self.ll[1] += 1; self.ur[] 

        # follow direction to change direction
        if new_direction == 0: 
            new_id = (id[0], id[1] + 1)
        if new_direction == 1: 
            new_id = (id[0] + 1, id[1])
        if new_direction == 2: 
            new_id = (id[0], id[1] - 1)
        if new_direction == 3: 
            new_id = (id[0] - 1, id[1])

    
        
        return new_id, new_direction 
    

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        id = (0, 0)
        direction = 0 # 0 -> ; 1 down ;  2: <- ; 3 : up 
        for i in range(self.n * self.m): 
            output.append(matrix[id[0]][id[1]])
            id, direction = self.move(id, direction)
        return output 
            