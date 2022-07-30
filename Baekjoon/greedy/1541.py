str_math = input()
result = []

if '-' not in str_math :
    result = map(int, str_math.split('+'))
    print(sum(result))

else :
    tmp = map(str, str_math.split('-'))
    for item in list(tmp) :
        if '+' in item :
            item = sum(map(int, item.split('+')))
            result.append(item)
        else:
            result.append(int(item))

    num = result[0]
    for idx in range(1, len(result)) :
        num -= result[idx]
    print(num)
