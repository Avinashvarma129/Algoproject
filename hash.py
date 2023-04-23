class hashSet:
    def __init__(self):
        self.set = {}
    
    def insert(self,key):
        if key in self.set:
            print('\nKey is available')
            return
        self.set[key] = True
        self.print()
        
    def delete(self,key):
        if key in self.set:
            del self.set[key]
            self.print()
            return             
        else:
             return -1
             
    def print(self):
        print("")
        for key in self.set:
            print(key,end=" ")         
if __name__ == "__main__":
    hash = hashSet()
    hash.insert(1)
    hash.insert("I am")
    hash.insert(1.3)
    hash.insert(1)
    hash.delete(1)

          
                