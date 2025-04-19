# unfinished
# https://algo.itcharge.cn/Solutions/0001-0099/spiral-matrix
# check if over border; code clean enough?

class Solution(object):

    def move(self, id, direction, ul, ur, ll, lr):

        # follow direction to change direction
        if direction == 0: 
            new_id = (id[0], id[1] + 1)
        if direction == 1: 
            new_id = (id[0] + 1, id[1])
        if direction == 2: 
            new_id = (id[0], id[1] - 1)
        if direction == 3: 
            new_id = (id[0] - 1, id[1])

        new_direction = direction
        
        if (id is ur): 
            new_direction = 1
            ur[0] += 1; ur[1] -= 1
        if (id is lr):
            new_direction = 2
            lr[0] -= 1; lr[1] -= 1
        if (id is ll):
            new_direction = 3
            ll[0] -= 1; ll[1] += 1
        if (id is ul):
            new_direction = 0
            ul[0] += 1; ul[1] += 1 
        
        return new_id, new_direction, ul, ur, ll, lr
    

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        assert(n > 0)
        m = len(matrix[0])
        assert(m > 0)

        ul = (0, 0)
        ur = (0, m - 1)
        ll = (n-1, 0)
        lr = (n-1, m-1)


        output = []
        id = (0, 0)
        direction = 0 # 0 -> ; 1 down ;  2: <- ; 3 : up 
        for i in range(self.n * self.m): 
            output.append(matrix[id[0]][id[1]])
            id, direction, ul, ur, ll, lr = self.move(id, direction, ul, ur, ll, lr)
        
        return output 
            