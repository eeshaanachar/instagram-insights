from random import sample

file = open('./cache/__index__.txt')
values = file.read().split()
file.close()
values.sort()
values.insert(0,'')

for i in range(1,len(values)):
    print(i, values[i].title())
options = list(map(int,input('Options> ').split()))
count = list(map(int,input('Count> ').split()))

output = list()
for i in range(len(options)):
    try:
        file = open('./cache/'+values[options[i]]+'.txt')
        hashtags = file.read().split()
        file.close()
        output.extend(sample(hashtags,count[i]))
    except ValueError:
        print('Fewer added for',values[options[i]].title())
        output.extend(hashtags)
    except IndexError:
        print('Invalid Input(s)')
        input()
        exit()

output = list(dict.fromkeys(output))
file = open('output.txt','w')
file.write('#'+' #'.join(output)+' ')
file.close()
input(str(len(output))+' hashtags found')

