from builtins import object, dict, str, bool, list
from re import  Match, compile, match, DOTALL

ANY_TEXTS : dict [ str, str ] = { "" : "" }
ANY_ELEMENTS : dict= { "" : "" }
ANY_ATTRIBUTES : dict = { "" : "" }

class TextType ( object ):
    regex : str = None
    def check ( self, string : str ) -> bool:
        matchans : Match | None = match ( compile ( self.regex ), string, DOTALL )
        if matchans == None:
            return False
        else:
            return matchans.span [ 1 ] == len ( string )

class Empty ( TextType ):
    regex : str = ""

class String ( TextType ):
    regex : str = "."

class Boolean ( TextType ):
    regex : str = "true|false"

class NumSymbol ( TextType ):
    regex : str = "[0123456789]"

class Number ( TextType ):
    regex : str = "[123456789]{0}*(\.{0}*)?".format ( NumSymbol.regex )

class LowerCase ( TextType ):
    regex : str = "[abcdefghijklmnopqrstuvwxyz]"
    
class UpperCase ( TextType ):
    regex : str = "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"

class Letter ( TextType ):
    regex : str = "{0}|{1}".format ( LowerCase.regex, UpperCase.regex )

class Symbol ( TextType ):
    regex : str = "{0}|{1}".format ( Letter.regex, NumSymbol.regex )

class Word ( TextType ):
    regex : str = "{0}*".format ( Letter.regex )
    
class TokenString ( TextType ):
    regex : str = "{0}*".format ( Symbol.regex )

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
        self.textType : TextType = String (  )
        self.stdText : str = ""
