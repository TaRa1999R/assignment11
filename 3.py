                     # COMPLEX NUMBER

class Complex_number :

    def __init__ ( self , real , imaginary ) :
        #properties
        self.r = real
        self.i = imaginary

    #methods
    def show ( self ) :
        if self.i > 0 and self.r != 0 :
            print ( self.r , "+", self.i , "i")
        
        elif self.i < 0 and self.r != 0 :
            print ( self.r , "-" , self.i * -1 , "i" )

        elif self.i != 0 and self.r == 0 :
            print ( self.i , "i" )
        
        elif self.i == 0 :
            print ( self.r )

    def sum ( self , other ) :
        result_r = self.r + other.r
        result_i = self.i + other.i
        result = Complex_number ( result_r , result_i )
        return result

    def sub ( self , other ) :
        result_r = self.r - other.r
        result_i = self.r - other.r
        result = Complex_number ( result_r , result_i )
        return result
    
    def mul ( self , other ) :
        result_r = ( self.r * other.r ) - ( self.i * other.i )
        result_i =  ( self.r * other.i ) + ( self.i * other.r )
        result = Complex_number ( result_r , result_i )
        return result

a = Complex_number ( 10 , 20 )
a.show ()

b = Complex_number ( 3 , -2 )
b.show ()

c = Complex_number ( 0 , 2 )
c.show ()

d = Complex_number ( 3 , 0 )
d.show ()

e = Complex_number ( 0 , 0 )
e.show ()

f = a.sum ( b )
f.show ()

g = b.sub ( a )
g.show ()

h = a.mul ( b )
h.show ()