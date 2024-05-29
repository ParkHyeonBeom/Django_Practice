f = 1.12345678901234567
print(f)
print(id(f))

g = repr(f)
print(g)
print(id(g))

w = eval(g)
print(w)
print(id(w))

print(f==g) ## 값이 같은지 확인
print(g==w)
print(f==w)

print(f is g) ## 객체의 주소가 같은지 확인
print(g is w)
print(f is w)