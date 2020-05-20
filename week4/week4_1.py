#print("Hello World!")
#print("Good Bye")

f = open("test.txt", "w") #open이라는 함수를 통해 파일을 열 수 있다. w모드 사용을 통해 새로운 파일을 만들었다.
f.write("Hello World\n")
f.write("Good Bye")
f.close() # 핸드폰의 홈 버튼