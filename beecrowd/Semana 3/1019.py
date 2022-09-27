N = int(input())
h = N//(60*60)
m = (N - h*60*60)//60
s = (N - h*60*60 - m*60)
print(f'{h}:{m}:{s}')
