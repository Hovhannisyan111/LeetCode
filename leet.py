#LeetCode 13
#def rom(num):
#    md = {
#            'I': 1,
#            'V': 5,
#            'X': 10,
#            'L': 50,
#            'C': 100,
#            'D': 500,
#            'M': 1000
#    }
#    result = 0
#    n_value = 0
#    for i in num:
#        value = md[i]
#        if value > n_value:
#            result += value - 2 * n_value
#        else:
#            result += value 
#            n_value = value
#    return result
#
#print(rom("III"))
#print(rom("X"))
#print(rom("LXIII"))
#print(rom("MCMXCIV"))

#LeetCode 14

#def prefix(ml):
#    if not ml:
#        return ""
#    
#    length = min([len(word) for word in ml])
#
#    for i in range(length):
#        ch = set([word[i] for word in ml])
#        if len(ch) > 1:
#            return ml[0][:i]
#
#    return ml[0][:length]
# 
#ml = ["flower","flow","flight"]
#
#print(prefix(ml))

#LeetCode 20
#
#def par(s):
#    ml = []
#    md = {')': '(', '}': '{', ']': '['}
#    for i in s:
#        if i in md.values():
#            ml.append(i)
#        elif i in md.keys():
#            if not ml or ml.pop() != md[i]:
#                return False
#        else:
#            pass
#    return not ml
#print(par('()'))
#print(par('()[]{}'))
#print(par('[){}'))
#print(par('[()]'))
#print(par('[(])'))

#LeetCode 28
#
#def get_index(haystack, needle):
#    if needle not in haystack:
#        return -1
#    ml = []
#    start = 0
#    while start < len(haystack):
#        index = haystack.find(needle, start)
#        if index == -1:
#            break
#        ml.append(index)
#        start = index + 1 
#    return ml
#
#
#haystack = "sadbutsad"
#needle = "sad"
#print(get_index(haystack, needle))
#LeetCode 69
#
#def sqrt(x):
#    if x == 0:
#        return 0
#    left = 1
#    right = x
#    while  left  < right:
#        mid = left + (right - left) // 2
#        if mid * mid == x:
#            return mid
#        elif mid  * mid < x:
#            left = mid  + 1
#        else:
#            right = mid - 1 
#
#    return right 
#
#print(sqrt(4))
#print(sqrt(8))
#print(sqrt(81))
#print(sqrt(625))

#LeetCode 202
#
#def h_num(n):
#    ms = set()
#    while n != 1:
#        n = sum(int(i)**2 for i in str(n))
#        if n in ms:
#            return False
#        ms.add(n)
#    return True
#print(h_num(19))
#print(h_num(2))
#print(h_num(31))
#print(h_num(41))
