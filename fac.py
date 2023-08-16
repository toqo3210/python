# 함수를 선언합니다
def factorial(n):
      # 합수를 선언합니다.
        output = 1
        # 반복문을 돌려 숫자를 더합니다.
        for i in range(1, n + 1):
            output *= i
        # 리턴합니다.
        return output

# 합수를 호출합니다.
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 팩토리얼 함수로 구현하기
def factorial(n):
     output = 1
     for i in range(1, n + 1):
        output *= i
        return output

print("6!:",factorial(6))

# 팩토리얼 재귀합수로 구현하기
def factorial(n):
    if n ==0:
     return 1
    else:
     return n* factorial(n-1)
    
    print("5!:",factorial(5))