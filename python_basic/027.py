#파일 입출력
'''
file = open('sample.txt', 'w') # w : 새로 쓰기(덮어쓰기), r: 읽기, a : append 추가 

file.write('hello world')
file.write('\n')
file.write('hello world')
file.close()

print(dir(file))
'''

file = open('sample.txt', 'r') 
'''
print(file.read())          #hello world  
                            #hello world  

print(file.readline())      #hello world   
print(file.readline())      #
print(file.readline())      #hello world
'''
print(file.readlines())     #['hello world\n', 'hello world']  반복문으로 활용 가능
file.close()


#파일 입출력 관련 책 <인공지능을 활용한 업무자동화 With Google Developers Group JEJU>