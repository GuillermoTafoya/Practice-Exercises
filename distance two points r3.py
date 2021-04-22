

a,b,c, d,e,f = map(float, input("x1 y1 z1 x2 y2 z2\n").split())

result = ((d-a)**2+(e-b)**2+(f-c)**2)**(1/2)

print(result)