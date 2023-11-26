from datetime import datetime

def calculate_age(birthdate):
    # 현재 날짜를 가져옵니다.
    current_date = datetime.now()
    
    # 생년월일 문자열을 날짜로 변환합니다.
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # 만 나이를 계산합니다.
    age = current_date.year - birthdate.year
    
    # 생일이 아직 오지 않았으면 1을 빼줍니다.
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

# 사용자로부터 생년월일을 입력받습니다 (예: 2000-01-15).
birthdate = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

try:
    age = calculate_age(birthdate)
    print(f"만 나이: {age}세")
except ValueError:
    print("올바른 날짜 형식을 입력하세요 (YYYY-MM-DD).")
