def check(string):
    buffer = [0 for _ in range(len(string))]
    count = 0
    ch = True
    for i in string:
        if(i in ['(', '{', '[']):
            buffer.append(i)
        elif(i in [')', '}', ']']):
            temp = buffer.pop()
            if((i == ')' and temp == '(') or (i == '}' and temp == '{') or (i == ']' and temp == '[')):
                count += 1
            else:
                ch = False
    if(ch):
        ch = 'YES'
    else:
        ch = 'NO'
    return "{} {}".format(ch, count)

if __name__ == "__main__":
    print(check(input()))

'''
{**}
{({[]})}
}xasd[]sda231
'''
