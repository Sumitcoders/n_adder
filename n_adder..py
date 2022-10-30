'@Sumitcoders' 

n = int(input('Enter the number till you want to add: '))

output = ''
sum = 0
for i in range(1,n+1):
    if output =='':
        output = output + str(i)
    else:
        output = output + '+' + str(i)
    sum = sum + i

output = output + '=' + str(sum)
print(output)