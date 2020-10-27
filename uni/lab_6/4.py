(x, y) = (int(input()) for i in range(2))
mid_a = (x + y) / 2
mid_g = (x * y) ** 0.5
print(mid_a, mid_g)
if mid_a > mid_g:
    print('arithmetic more than geometry')
elif mid_a < mid_g:
    print('arithmetic less than geometry')
else:
    print('arithmetic equal geometry')
