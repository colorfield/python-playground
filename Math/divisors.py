# Divisors
def divisor(n):
  i = 1
  while i<=n:
   if n%i == 0:
      print i
   i = i + 1
  print ''

max = 60
i = 1
while i<= max:
  print 'Divisors of', i
  print '----------------'
  divisor(i)
  i = i + 1
