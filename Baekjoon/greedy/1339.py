N = int(input())
word = dict()

for _ in range(N) :
    words = input()
    for idx in range(len(words)) :
        weight = 10**(len(words)-(idx+1))
        try :
            tmp = word[words[idx]] + weight
            word[words[idx]] = tmp
        except :
            word[words[idx]] = weight

sorted_dict_by_value = sorted(word.items(), key=lambda x: x[1], reverse=True)
total = 0
for  i in range(9, 0, -1) :
    try :
        total += sorted_dict_by_value[0][1] * i
        sorted_dict_by_value.pop(0)
    except :
        break

print(total)
