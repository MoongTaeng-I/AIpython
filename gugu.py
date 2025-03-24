def print_multiplication_table():
    try:
        number = int(input("출력할 구구단의 숫자를 입력하세요: "))
        print(f"{number}단 출력")
        for i in range(1, 10):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    print_multiplication_table()