# https://leetcode.com/problems/simplify-path/

# Runtime: 23 ms, faster than 78.94% of Python online submissions for Simplify Path.
# Memory Usage: 13.4 MB, less than 81.87% of Python online submissions for Simplify Path.


class Stack:
    def __init__(self):
        self.stack = []
        self.idx = -1

    def index(self):
        return self.idx
    
    def push(self, a):
        if self.idx >= len(self.stack) - 1:
            self.stack.append(a)
        elif self.idx < 0: 
            assert self.idx == -1
            self.stack = [a]
        else:
            self.stack[self.idx + 1] = a
        self.idx += 1

    def pop(self):
        assert self.idx >= 0
        self.idx -= 1

    def get(self):
        return self.stack[:self.idx + 1]
  

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    s = Stack()
    paths = path.split('/')
    for p in paths:
        #print(s.get())
        if p == '' or p == '.': continue
        elif p == '..': 
            if s.index() >= 0 : s.pop()
        else:
            s.push(p)

    dir = '/' + '/'.join(s.get())
    return dir 

dir1 = "/home/" #"/home"
dir2 = "/../" # "/"
dir3 = "/home//foo/" # "/home/foo"
dir4 = "/a/./b/../../c/" #  "/c"
dir5 = "/a/../../b/../c//.//" # "/c"
dir6 = "/a//b////c/d//././/.." #"/a/b/c"
dir7 = "/home/foo/.ssh/../.ssh2/authorized_keys/" #"/home/foo/.ssh2/authorized_keys"

print(simplifyPath(dir1))