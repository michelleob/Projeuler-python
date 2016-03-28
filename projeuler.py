#!/usr/bin/env python

def problem1(a):
    """Returns the sum of ints that are multiples of 3 or 5"""
    sum=0
    for x in range(a):
        if x%5==0:
            sum+=x
        elif x%3==0:
            sum+=x
    return sum

def problem2(n):
    """Returns the sum of even numbers in the Fibonnaci sequence.
    For values less than 4 million use n=32"""
    sum=0
    a=1
    b=2
    for i in range(n-1):
        a = b
        b = a+b
        if a%2==0:
            sum+=a
    return sum

def problem3(n):
    """Returns the largest prime factor of a number
    solve for the number 600851475143"""
    list=[]
    end = n
    i=3
    while i < end:
        if n%i==0:
            end=n/i 
            if isprime(i):
                list.append(i)
        i=i+2
    return max(list)
        
def isprime(x):
    """Returns true if x is a prime number"""
    i=3
    if x==2:
        return True
    while i < (x/2):
        if x%2==0:
            return False
        if x%i==0:
            return False
        i+=2
    return True

def primes_upto(limit):
    """Returns the number of primes up to a limit"""
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def problem4():
    """Returns the largest palindrome made from the product of two 3-digit numbers"""
    list=[]
    x=999
    y=999
    for x in range(99,999):
        for y in range(99,999):
            if ispalindrome(x*y):
               list.append(x*y)
    return max(list)
    

def ispalindrome(x):
    """Returns true if the number is a palindrome"""
    s=str(x)
    if len(s) < 2:
        return True
    return s[0] == s[-1] and ispalindrome(s[1:-1])

def problem5():
    """Can be solved by inspection"""
    return 232792560

def problem6(x):
    """Returns the difference between the sum of the squares of the first 100
    natural numbers and the square of the sum"""
    sum1=0
    sum2=0
    for i in range(x+1):
        sum1+=i
    for i in range(x+1):
        sum2+=(i**2)
    return ((sum1**2)-sum2)

def problem7(x):
    """Returns the xth prime number"""
    i=0
    num=2
    while i<= x:
        if isprime(num):
            i+=1
        num+=1
    return num-1

def problem8():
    """Returns the greatest product of thirteen adjacent digits in this 1000-digit number"""
    x=list('73167176531330624919225119674426574742355349194934'+
    '96983520312774506326239578318016984801869478851843'+
    '85861560789112949495459501737958331952853208805511'+
    '12540698747158523863050715693290963295227443043557'+
    '66896648950445244523161731856403098711121722383113'+
    '62229893423380308135336276614282806444486645238749'+
    '30358907296290491560440772390713810515859307960866'+
    '70172427121883998797908792274921901699720888093776'+
    '65727333001053367881220235421809751254540594752243'+
    '52584907711670556013604839586446706324415722155397'+
    '53697817977846174064955149290862569321978468622482'+
    '83972241375657056057490261407972968652414535100474'+
    '82166370484403199890008895243450658541227588666881'+
    '16427171479924442928230863465674813919123162824586'+
    '17866458359124566529476545682848912883142607690042'+
    '24219022671055626321111109370544217506941658960408'+
    '07198403850962455444362981230987879927244284909188'+
    '84580156166097919133875499200524063689912560717606'+   
    '05886116467109405077541002256983155200055935729725'+
    '71636269561882670428252483600823257530420752963450')
    i=0
    multlist=[]
    while i<987:
        multlist.append(int(x[i+1])*int(x[i+2])*int(x[i+3])*int(x[i+4])*
                        int(x[i+5])*int(x[i+6])*int(x[i+7])*int(x[i+8])*
                        int(x[i+9])*int(x[i+10])*int(x[i+11])*int(x[i+12])*int(x[i+13]))
        i+=1
    return max(multlist)
    
def problem9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Returns the product abc."""
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if (a**2)+(b**2)==(c**2) and (a+b+c)==1000:
                    return a*b*c

def problem10(x):
    """Returns the sum of primes up to a certain number"""
    summy=0
    for i in primes_upto(x):
        summy+=i
    return summy