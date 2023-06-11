## finding angle mbc
## https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())
ACsqrt = pow(AB,2) + pow(BC,2)

AC = math.sqrt(ACsqrt)

MC = 0.5 * AC
x = MC/BC

angleMBC = round(math.degrees(math.asin(x)))
degree_symbol = chr(0xB0)

print(f'{angleMBC}{degree_symbol}')
