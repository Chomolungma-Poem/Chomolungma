from builtins import object, dict, str, bool, list

ANY_TEXTS : dict [ str, str ] = { "" : "" }
ANY_ELEMENTS : dict= { "" : "" }
ANY_ATTRIBUTES : dict = { "" : "" }

class TextType ( object ):
    def check ( self, string : str ) -> bool:
        return False

class Empty ( TextType ):
    def check ( self, string : str ) -> bool:
        return string == ""

class String ( TextType ):
    def check ( self, string : str ) -> bool:
        return True

class Boolean ( TextType ):
    def check ( self, string : str ) -> bool:
        return string == "true" or string == "false"
    
class Number ( TextType ):
    def check ( self, string : str ) -> bool:
        try:
            int ( string )
        except:
            return False
        else:
            return True

class ElementType ( object ):
    def __init__ ( self, name : str ):
        self.name : str = name
        self.textType : TextType = String (  )
        self.elementsIn : list [ ElementType ] = [  ]
        self.attributesIn : list [ AttributeType ] = [  ]
        self.stdText : str = ""

class AttributeType ( object ):
    def __init__ ( self, name ):
        self.name : str = name
        self.textIn : TextType = String (  )
        self.stdText : str = ""
