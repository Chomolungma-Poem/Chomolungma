import xc

class XMLNamespace ( xc.AttributeType ):
    def __init__ ( self, name : str ):
        self.textType = xc.String (  )
        self.stdText = "https://xmlns.chomolungma.org/"
        xc.AttributeType.__init__ ( self, name )

'''
Root element
'''
class ROOT ( xc.ElementType ):
    def __init__( self, name : str ):
        self.textType = xc.Empty (  )
        self.stdText = ""
        xc.ElementType.__init__( self, name )

cml : xc.ElementType = ROOT ( "cml" )
