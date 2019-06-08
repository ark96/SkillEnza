fname = "input_user_story_1.txt"
num_lines = 0
temp = ''

def decoder(t,i,x):
    count1 = 0
    if t[1] == ' ':
        a = 0
    else:
        a = 1
        count1 += 1
    if i[0] == ' ':
        f = 0
    else:
        f = 1
        count1 += 1
    if i[1] == ' ':
        g = 0
    else:
        g = 1
        count1 += 1
    if i[2] == ' ':
        b = 0
    else:
        b = 1
        count1 += 1
    if x[0] == ' ':
        e = 0
    else:
        e = 1
        count1 += 1
    if x[1] == ' ':
        d = 0
    else:
        d = 1
        count1 += 1
    if x[2] == ' ':
        c = 0
    else:
        c = 1
        count1 += 1
    if count1 == 7:
        return '8'
    elif count1 == 2:
        return '1'
    elif count1 == 3:
        return '7'
    elif count1 == 4:
        return '4'
    elif count1 == 6:
        if g == 0:
            return '0'
        elif b == 0:
            return '6'
        elif e == 0:
            return '9'
    elif count1 == 5:
        if f+e == 0:
            return '3'
        elif f+c == 0:
            return '2'
        elif b+e == 0:
            return '5'

def convert(temp):
    inarray = temp.splitlines()
    first = inarray[-4]
    second = inarray[-3]
    third = inarray[-2]
    output = ''
    for i in range(0,len(first),3):
        f = first[i:i+3]
        s = second[i:i+3]
        t = third[i:i+3]
        output = output + decoder(f,s,t)
    print(output)
    f = open('output.txt','a')
    f.write(output+'\n')
    f.close()
    
with open(fname, 'r') as f:
    for line in f: 
        num_lines += 1
        temp = temp + line
        if num_lines>3:
            convert(temp)
            num_lines = 0
            continue
        
 
