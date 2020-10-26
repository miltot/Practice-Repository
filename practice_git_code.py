"""simple social network for tracking connectins between people  """


class Person:
    """a person in a social network
    Attributes: 
    
    name(str): the name of the person 
    connections (set of person) : other people on the social network who know this person
    
    
    
    
    """
    
    def __init__(self,name):
        """initialize a new person object"""
        self.name = name 
        self.connections = set()
        
    def connect(self,person2):
        """connect with person 2"""
        
        
    