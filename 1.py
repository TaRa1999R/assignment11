                       # FRACTION

class Fraction :

    def __init__ ( self , numirator , denominator) :
        #properties
        self.n = numirator
        self.d = denominator
        self.simple()

    #methods
    def show ( self ) :
        print ( self.n , "/" , self.d )

    def sum ( self , other ) :
        result_n = ( self.n * other.d ) + ( other.n * self.d )
        result_d = self.d * other.d
        result = Fraction ( result_n , result_d)
        return result
    
    def mul ( self , other ) :
        result_n = self.n * other.n
        result_d = self.d * other.d
        result = Fraction ( result_n , result_d )
        return result
    
    def sub  ( self , other ) :
        result_n = ( self.n * other.d ) - ( other.n * self.d )
        result_d = self.d * other.d
        result = Fraction ( result_n , result_d )
        return ( result )
    
    def div ( self , other ) :
        result_n = self.n * other.d
        result_d = self.d * other.n
        result = Fraction ( result_n , result_d )
        return result
    
    def fraction_to_number ( self ) :
        print ( self.n / self.d )

    def simple ( self ) :
        n_divisor = []
        d_divisor = []
        common_divisor = [ 1 ]
        
        for i in range ( 1 , self.n + 1 ) :
            if self.n % i == 0 :
                n_divisor.append ( i )

        for i in range ( 1 , self.d + 1 ) :
            if self.d % i == 0 :
                d_divisor.append ( i )

        for number in n_divisor :
            if number in d_divisor :
                common_divisor.append ( number )
        
        GCD = common_divisor [ len( common_divisor )-1 ]
        self.n = int ( self.n / GCD )
        self.d = int ( self.d / GCD )


a = Fraction ( 3 , 5 )
a.show ()
a.fraction_to_number ()

b = Fraction ( 5 , 7 )
b.show ()

c = a.sum ( b )
c.show ()

d = b.mul ( a )
d.show ()

e = a.sub ( b )
e.show ()

f = b.sub ( a )
f.show ()

g = a.div ( b )
g.show ()

h = b.div ( a )
h.show ()

z = Fraction ( 20 , 35 )
z.show ()

y = Fraction ( 35 , 20 )
y.show ()

x = z.mul ( y )
x.show ()