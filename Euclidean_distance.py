x, y = 0, 0
# start from origin

seq = input()
while seq != 'stop':
  if seq == 'up':
    y = y+1
  if seq == 'down':
    y = y - 1
  if seq == 'left':
    x = x-1
  if seq == 'right':
    x = x+1
  seq = input()

dist = pow(x**2 + y**2, 0.5)
print(f'{dist:0.2f}')
