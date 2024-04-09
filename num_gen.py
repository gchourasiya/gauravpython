def num_generate(str1):
    lst=[]
    ele=[]
    freq=[]
    if not str1:
        return ele
    counter =1
    for i in range(len(str1)-1):
        print('if loop i is :',i ,'str1[i] is ',str1[i])
        print('if loop str1[i+1] is ',str1[i+1])
        if str1[i]==str1[i+1]:
            counter+=1
        else:
            print('else loop str1[i] is ',str1[i])
            freq.append(counter)
            ele.append(str1[i])
            print('freq in else loop', freq[-1])
            print('ele in else loop', ele[-1])

            counter=1
            print(counter)
            print('i is :',i)
    print('Out of for loop')
    print('value of counter is :',counter)
    print('value of ele before append is',ele)
    freq.append(counter)
    ele.append(str1[i+1])
    print('value of ele after append is', ele)
    print(freq,ele)


    res = [str(i)+str(j) for i,j in zip(ele,freq)]
    final_str= ''.join(res)
    return final_str

output = num_generate('551331466')
print(output)