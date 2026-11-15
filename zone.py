class Zone():
    def __init__(self,name,depth,description,creatures):
        self.name = name 
        self.depth = depth
        self.description = description
        self.creatures = creatures
        self.next = None
