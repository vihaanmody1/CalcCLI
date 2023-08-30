import math

class Functions:
    def absolute(x): #Number-theoretic and representation functions
        return math.fabs(x)

    def factorial(x): #Number-theoretic and representation functions
        return math.factorial(x)

    def floor(x): #Number-theoretic and representation functions
        return math.floor(x)

    def ceil(x):# Number-theoretic and representation functions
        return math.ceil(x)

    def cbrt(x): #Power and logarithmic functions
        return math.cbrt(x)

    def sqrt(x):#Power and logarithmic functions
        return math.sqrt(x)

    def power(x, y): #Power and logarithmic functions
        return pow(x, y)

    def acos(x): #arc cosine Trigonometric functions
        return math.acos(x)

    def asin(x): #arc sine Trigonometric functions
        return math.asin(x)

    def atan(x): #arc tangent Trigonometric functions
        return math.atan(x)

    def cosine(x): #Trigonometric functions
        return math.cos(x)

    def sin(x): #sine Trigonometric functions
        return math.sin(x)

    def tan(x): #tangent Trigonometric functions
        return math.tan(x)

    def degrees(x): # radians to degrees Angular conversion
        return math.degrees(x)
    
    def radians(x): # degrees to radians Angular conversion
        return math.radians(x)
    
    def acosh(x):#Hyperbolic functions
        return math.acosh(x)
    
    def asinh(x):#Hyperbolic functions
        return math.asinh(x)
    
    def atanh(x):#Hyperbolic functions
        return math.atanh(x)
    
    def cosh(x):#Hyperbolic functions
        return math.cosh(x)
    
    def sinh(x):#Hyperbolic functions
        return math.sinh(x)

    def tanh(x):#Hyperbolic functions
        return math.tanh(x)
    
#----------- Constants

class Constants:
    pi = math.pi
    e = math.e # Euler's number
    tau = math.tau
    inf = math.inf
    nan = math.nan