class Node():
    def __init__(self,data):
        self.data = data                                   
        self.parent = None                               
        self.left = None                                 
        self.right = None                                
        self.color = 1                                   
        self.height = 1
class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
    def insertNode(self, key,case):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   
        y = None
        x = self.root

        while x != self.NULL :                          
            y = x
            if node.data < x.data :
                x = x.left
            elif node.data==x.data:
                print("element found!",self.height(self.root))
                return
            else :
                x = x.right

        node.parent = y                              
        if y == None :                            
            self.root = node
        elif node.data < y.data :                        
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         
            node.color = 0
            if case==True:
                print(node.data,self.height(self.root))
            return

        if node.parent.parent == None :  
            if case==True:             
                print(node.data,self.height(self.root))
            return

        self.fix_Insert ( node )
        if case==True:                   
            print(node.data,self.height(self.root))
    def fix_Insert(self, k):
        while k.parent.color == 1:                       
            if k.parent == k.parent.parent.right:        
                u = k.parent.parent.left                 
                if u.color == 1:                         
                    u.color = 0                           
                    k.parent.color = 0
                    k.parent.parent.color = 1             
                    k = k.parent.parent                   
                else:
                    if k == k.parent.left:                
                        k = k.parent
                        self.right_rotate(k)                        
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:                                         
                u = k.parent.parent.right                 
                if u.color == 1:                          
                    u.color = 0                           
                    k.parent.color = 0
                    k.parent.parent.color = 1             
                    k = k.parent.parent                   
                else:
                    if k == k.parent.right:               
                        k = k.parent
                        self.left_rotate(k)                        
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)              
            if k == self.root:                            
                break
        self.root.color = 0  
    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node
    def left_rotate ( self , x ) :
        y = x.right                                      
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                        
        if x.parent == None : 
            self.root = y  
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y
    def right_rotate ( self , x ) :
        y = x.left                                       
        x.left = y.right                             
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                             
        if x.parent == None :                          
            self.root = y                               
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y 
    def fix_Delete ( self , x ) :
        while x != self.root and x.color == 0 :           
            if x == x.parent.left :                       
                s = x.parent.right                        
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.left_rotate ( x.parent )                  
                    s = x.parent.right
                
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           
                    x = x.parent
                else :
                    if s.right.color == 0 :               
                        s.left.color = 0                  
                        s.color = 1                       
                        self.right_rotate ( s )                     
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    
                    s.right.color = 0
                    self.left_rotate ( x.parent )                  
                    x = self.root
            else :                                        
                s = x.parent.left                         
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.right_rotate ( x.parent )                  
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                
                        s.right.color = 0                 
                        s.color = 1
                        self.left_rotate ( s )                     
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate ( x.parent )
                    x = self.root
        x.color = 0
        
    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return 1 + max(left_height, right_height)
    
    def __rb_transplant ( self , u , v ) :
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent
    def delete_node ( self , data ,case) :
        node=self.root        
        z = self.NULL
        while node != self.NULL :                          
            if node.data == data :
                z = node

            if node.data < data :
                node = node.right
            else  :
                node = node.left
        if z == self.NULL :                                
            return -1
        y = z
        y_original_color = y.color                          
        if z.left == self.NULL :                            
            x = z.right                                     
            self.__rb_transplant ( z , z.right )            
        elif (z.right == self.NULL) :                       
            x = z.left                                      
            self.__rb_transplant ( z , z.left )             
        else :                                              
            y = self.minimum ( z.right )                    
            y_original_color = y.color                      
            x = y.right
            if y.parent == z :                              
                x.parent = y                                
            else :
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0 :                          
            self.fix_Delete ( x )
        print(data,self.height(self.root))
   
    def inorder_traversal(self, node):
        if node is not None and node.data is not None :
            if node.data !=0:
                self.inorder_traversal(node.left)
                print(node.data)
                self.inorder_traversal(node.right)

if __name__ == "__main__":
    tree = RBTree()
    tree.insertNode(10,True)
    tree.insertNode(20,True)
    tree.insertNode(30,True)
    tree.insertNode(5,True)
    tree.insertNode(4,True)
    tree.insertNode(2,True)
    tree.insertNode(4,True)
    tree.delete_node(2,True)
    tree.delete_node(50,True)
    tree.inorder_traversal(tree.root)