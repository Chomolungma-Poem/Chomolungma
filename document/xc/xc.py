from builtins import object

ANY_TEXTS = { "" : "" }
ANY_ELEMENTS = { "" : "" }
ANY_ATTRIBUTES = { "" : "" }

class TextType ( object ):
    def check ( self, string ):
        return False

class Empty ( TextType ):
    def check ( self, string ):
        return string == ""

class String ( TextType ):
    def check ( self, string ):
        return True

class Boolean ( TextType ):
    def check ( self, string ):
        return string == "true" or string == "false"
    
class Number ( TextType ):
    def check ( self, string ):
        try:
            int ( string )
        except:
            return False
        else:
            return True

class ElementType ( object ):
    def __init__ ( self, name ):
        self.name = name
        self.textType = String (  )
        self.elementsIn = [  ]
        self.attributesIn = [  ]
        self.stdText = ""

class AttributeType ( object ):
    def __init__ ( self, name ):
        self.name = name
        self.textIn = [  ]
        self.stdText = ""
