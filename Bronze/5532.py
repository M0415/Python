L = int(input())
lan = int(input())
math = int(input())
m_lan = int(input())
m_math = int(input())
math_total = 0
lan_total = 0

while (math_total < math) or (lan_total < lan):
    math_total += m_math
    lan_total += m_lan
    L -= 1
    
print(L)