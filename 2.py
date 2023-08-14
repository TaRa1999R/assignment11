                         # TIME

class Time :

    def __init__ ( self , second , minute , hour ) :
        #properties
        self.s = second
        self.m = minute
        self.h = hour
        self.fix ()
    
    #methods
    def show ( self ) :
        print ( self.h , ":" , self.m , ":" , self.s )

    def fix ( self ) :
        if self.s >= 60 :
            self.m += int ( self.s / 60 )
            self.s -= ( int ( self.s / 60 ) ) * 60
            
        if self.m >= 60 :
            self.h += int ( self.m / 60 )
            self.m -= ( int ( self.m / 60 ) ) * 60

        if self.s < 0 :
            self.m -= 1 
            self.s += 60

        if self.m < 0 :
            self.h -= 1
            self.m += 60

    def sum ( self , other ) :
        result_s = self.s + other.s
        result_m = self.m + other.m
        result_h = self.h + other.h
        result = Time ( result_s , result_m , result_h )
        return result

    def sub ( self , other ) :
        result_s = self.s - other.s
        result_m = self.m - other.m
        result_h = self.h - other.h
        result = Time ( result_s , result_m , result_h )
        return result

    def second_to_time ( second ) :
        if second >= 3600 :
            hour = int ( second / 3600 )
            second -= hour * 3600

        if second >= 60 :
            minute = int ( second / 60 )
            second -= minute * 60

        result = Time ( second , minute , hour )
        return result
    
    def time_to_second ( self ) :
        second = ( self.h * 3600 ) + ( self.m * 60 ) + self.s
        return second
    
    def GMT_to_TEH ( other ) :
        other.h += 4
        other.m += 30
        result = Time ( other.s , other.m , other.h)
        return result


a = Time ( 110 , 210 , 13 )
a.show ()

b = Time.second_to_time ( 200000 )
b.show ()

c = b.time_to_second ()
print ( c )

d = a.sum ( b )
d.show ()

e = b.sub ( a )
e.show ()

f = Time ( 150 , 200 , 15 )
f.show ()

g = f.sub ( a )
g.show ()

gmt = Time ( 00 , 30 , 10)
teh = Time.GMT_to_TEH ( gmt )
teh.show ()