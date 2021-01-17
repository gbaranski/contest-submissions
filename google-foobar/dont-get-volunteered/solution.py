import math

# -*- coding: utf-8 -*- 
"""
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
"""

def toPoint(n):
    return n % 8, n / 8


def isValidMove(src, dest):
    src_x, src_y = toPoint(src)
    dest_x, dest_y = toPoint(dest)
    return abs((src_x - dest_x) * (src_y - dest_y)) == 2



def solution(src, dest):
    if src == dest:
        return 0

    if(isValidMove(src,dest)): return 1

    # Im aware that this code is shit, that can be done recursively but i got no head for this
    for a in range(63):
        if(isValidMove(src, a)):
            if(isValidMove(a, dest)):
                return 2
            for b in range(63):
                if(isValidMove(a, b)):
                    if(isValidMove(b, dest)):
                        return 3

    for a in range(63):
        if(isValidMove(src, a)):
            if(isValidMove(a, dest)):
                return 2
            for b in range(63):
                if(isValidMove(a, b)):
                    if(isValidMove(b, dest)):
                        return 3
                    for c in range(63):
                        if(isValidMove(b, c)):
                            if(isValidMove(c, dest)):
                                return 4
    for a in range(63):
        if(isValidMove(src, a)):
            if(isValidMove(a, dest)):
                return 2
            for b in range(63):
                if(isValidMove(a, b)):
                    if(isValidMove(b, dest)):
                        return 3
                    for c in range(63):
                        if(isValidMove(b, c)):
                            if(isValidMove(c, dest)):
                                return 4
                            for d in range(63):
                                if(isValidMove(c, d)):
                                    if(isValidMove(d, dest)):
                                        return 5

    for a in range(63):
        if(isValidMove(src, a)):
            if(isValidMove(a, dest)):
                return 2
            for b in range(63):
                if(isValidMove(a, b)):
                    if(isValidMove(b, dest)):
                        return 3
                    for c in range(63):
                        if(isValidMove(b, c)):
                            if(isValidMove(c, dest)):
                                return 4
                            for d in range(63):
                                if(isValidMove(c, d)):
                                    if(isValidMove(d, dest)):
                                        return 5
                                    for e in range(63):
                                        if(isValidMove(d, e)):
                                            if(isValidMove(e, dest)):
                                                return 6
    return 7

print(solution(29,4))
# Row 1
assert solution(29, 0) == 4
assert solution(29, 1) == 3
assert solution(29, 2) == 2
assert solution(29, 3) == 3
assert solution(29, 4) == 2
assert solution(29, 5) == 3
assert solution(29, 6) == 2
assert solution(29, 7) == 3

# Row 2
assert solution(29, 8) == 3
assert solution(29, 9) == 2
assert solution(29, 10) == 3
assert solution(29, 11) == 4
assert solution(29, 12) == 1
assert solution(29, 13) == 2
assert solution(29, 14) == 1
assert solution(29, 15) == 4

# Row 3
assert solution(29, 16) == 4
assert solution(29, 17) == 3
assert solution(29, 18) == 2
assert solution(29, 19) == 1
assert solution(29, 20) == 2
assert solution(29, 21) == 3
assert solution(29, 22) == 2
assert solution(29, 23) == 1

# Row 4
assert solution(29, 24) == 3
assert solution(29, 25) == 2
assert solution(29, 26) == 3
assert solution(29, 27) == 2
assert solution(29, 28) == 3
assert solution(29, 29) == 0
assert solution(29, 30) == 3
assert solution(29, 31) == 2


# Row 5
assert solution(29, 32) == 4
assert solution(29, 33) == 3
assert solution(29, 34) == 2
assert solution(29, 35) == 1
assert solution(29, 36) == 2
assert solution(29, 37) == 3
assert solution(29, 38) == 2
assert solution(29, 39) == 1

# Row 6
assert solution(29, 40) == 3
assert solution(29, 41) == 2
assert solution(29, 42) == 3
assert solution(29, 43) == 4
assert solution(29, 44) == 1
assert solution(29, 45) == 2
assert solution(29, 46) == 1
assert solution(29, 47) == 4

# Row 7
assert solution(29, 48) == 4
assert solution(29, 49) == 3
assert solution(29, 50) == 2
assert solution(29, 51) == 3
assert solution(29, 52) == 2
assert solution(29, 53) == 3
assert solution(29, 54) == 2
assert solution(29, 55) == 3

# Row 8
assert solution(29, 56) == 3
assert solution(29, 57) == 4
assert solution(29, 58) == 3
assert solution(29, 59) == 2
assert solution(29, 60) == 3
assert solution(29, 61) == 2
assert solution(29, 62) == 3
assert solution(29, 63) == 2

print("Tests passed")
