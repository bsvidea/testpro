def encode(msg):
    result=[]
    for x in msg:
        if x in 'zZ':
            y=ord(x)-25
        else:
            y=ord(x)+1
        result.append(chr(y))
    return ''.join(result)
