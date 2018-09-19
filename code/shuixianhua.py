"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""

for number in range(100,1000):
  ge = number % 10
  shi = number // 10 % 10
  bai = number // 100
  if ge ** 3 + shi ** 3 + bai ** 3 == number:
    print(number)
