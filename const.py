# ----- constants for GUI -----
appName = 'IO4Tool'
defaultSize = '800x650'

# ----- Digital Inputs -----

class INPUT:
    byte: int
    shift: int
    def __init__(self, _byte: int, _shift: int):
        self.byte = _byte
        self.shift = _shift

# Byte Sequence, reference to https://manalogues.com/posts/2025/03/21
# Byte 0
#  7  6  5  4  3  2  1  0
# 67 66 65 64 63 62 61 60
i1 = INPUT(0, 7) # 1p start
i25 = INPUT(0, 6) # 1p service
i7 = INPUT(0, 5) # 1p up
i9 = INPUT(0, 4) # 1p down
i5 = INPUT(0, 3) # 1p left
i3 = INPUT(0, 2) # 1p right
i11 = INPUT(0, 1) # 1p push1
i13 = INPUT(0, 0) # 1p push2
# Byte 1
#  7  6  5  4  3  2  1  0
# 77 76 75 74 73 72 71 70
i15 = INPUT(1, 7) # 1p push3
i17 = INPUT(1, 6) # 1p push4
i19 = INPUT(1, 5) # 1p push5
i21 = INPUT(1, 4) # 1p push6
i23 = INPUT(1, 3) # 1p push7
i31 = INPUT(1, 2) # 1p push8
i27 = INPUT(1, 1) # TEST
i28 = INPUT(1, 0) # TILT
# Byte 2
#  7  6  5  4  3  2  1  0
# c7 c6 c5 c4 c3 c2 c1 c0
i2 = INPUT(2, 7) # 2p start
i26 = INPUT(2, 6) # 2p service
i8 = INPUT(2, 5) # 2p up
i10 = INPUT(2, 4) # 2p down
i6 = INPUT(2, 3) # 2p left
i4 = INPUT(2, 2) # 2p right
i12 = INPUT(2, 1) # 2p push1
i14 = INPUT(2, 0) # 2p push2
# Byte 3
#  7  6  5  4  3  2  1  0
# e7 e6 e5 e4 e3 e2 e1 e0
i16 = INPUT(3, 7) # 2p push3
i18 = INPUT(3, 6) # 2p push4
i20 = INPUT(3, 5) # 2p push5
i22 = INPUT(3, 4) # 2p push6
i24 = INPUT(3, 3) # 2p push7
i32 = INPUT(3, 2) # 2p push8
i29 = INPUT(3, 1) # COIN 1
i30 = INPUT(3, 0) # COIN 0

inputs = [
    i1, i2, i3, i4, i5, i6, i7, i8,
    i9, i10, i11, i12, i13, i14, i15, i16,
    i17, i18, i19, i20, i21, i22, i23, i24,
    i25, i26, i27, i28, i29, i30, i31, i32
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