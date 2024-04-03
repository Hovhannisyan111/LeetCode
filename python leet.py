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

def get_index(haystack, needle):
    if not needle:
        return [i for i in range(len(haysack) + 1)]
    if needle not in haystack:
        return -1
    ml = []
    start = 0
    while start < len(haystack):
        index = haystack.find(needle, start)
        if index == -1:
            break
        ml.append(index)
        start = index + 1 
    return ml


haystack = "sadbutsad"
needle = "w"
print(get_index(haystack, needle))
