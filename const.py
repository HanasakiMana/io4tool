# ----- constants for GUI -----
appName = 'IO4Tool'
defaultSize = '800x650'

# ----- Digital Inputs -----

inputAlias = [
    'START',
    'RIGHT',
    'LEFT',
    'UP',
    'DOWN',
    'PUSH 1',
    'PUSH 2',
    'PUSH 3',
    'PUSH 4',
    'PUSH 5',
    'PUSH 6',
    'PUSH 7',
    'PUSH 8',
    'SERVICE'
]

sysInputAlias = [
    'TEST',
    'TILT',
    'COIN 1',
    'COIN 2'
]

# ----- Outputs (20 in total) -----
class OUTPUT:
    byte: int
    shift: int
    def __init__(self, _byte: int, _shift: int):
        self.byte = _byte
        self.shift = _shift
# Byte 0
#  7  6  5  4  3  2  1  0
# o1 o3 o5 o2 o4 o6 o7 o8
o1 = OUTPUT(0,7)
o2 = OUTPUT(0,4)
o3 = OUTPUT(0,6)
o4 = OUTPUT(0,3)
o5 = OUTPUT(0,5)
o6 = OUTPUT(0,2)
o7 = OUTPUT(0,1)
o8 = OUTPUT(0,0)
# Byte 1
#  7   6   5   4   3   2   1   0
# o9 o10 o11 o12 o13 o14 o15 o16
o9 = OUTPUT(1,7)
o10 = OUTPUT(1,6)
o11 = OUTPUT(1,5)
o12 = OUTPUT(1,4)
o13 = OUTPUT(1,3)
o14 = OUTPUT(1,2)
o15 = OUTPUT(1,1)
o16 = OUTPUT(1,0)
# Byte 2
#   7   6   5   4   3   2   1   0
# o17 o18 o19 o20 pad pad pad pad
o17 = OUTPUT(2,7)
o18 = OUTPUT(2,6)
o19 = OUTPUT(2,5)
o20 = OUTPUT(2,4)

outputs = [
     o1,  o2,  o3,  o4,  o5,  o6,  o7,  o8,
     o9, o10, o11, o12, o13, o14, o15, o16,
    o17, o18, o19, o20
    ]