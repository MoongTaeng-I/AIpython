#함수 만들기
def hello():
    print("hello world")

#함수 호출(실행)
hello()

def hello_name(name):
    print(f"안녕 {name}")

#함수 호출(실행)
name = input("이름을 입력 : ")
hello_name(name)