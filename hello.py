def validate_jumin(jumin):
    # 주민등록번호 형식 체크
    if len(jumin) != 14 or jumin[6] != '-':
        return "형식이 잘못되었습니다. 예: YYMMDD-XXXXXXX"
    
    # 숫자만 추출
    jumin = jumin.replace("-", "")
    
    if not jumin.isdigit():
        return "주민등록번호는 숫자만 포함해야 합니다."
    
    # 주민등록번호 유효성 검사
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]  # 가중치 배열
    total = 0
    
    for i in range(12):  # 첫 12자리 숫자에 대해 계산
        total += int(jumin[i]) * weights[i]
    
    check_digit = (11 - (total % 11)) % 10  # 검증수 계산
    
    # 마지막 1자리가 검증수와 일치하는지 확인
    if int(jumin[12]) == check_digit:
        return "유효한 주민등록번호입니다."
    else:
        return "유효하지 않은 주민등록번호입니다."

# 테스트
print(validate_jumin("060101-1234567"))  # 예시 번호
print(validate_jumin("060101-1234568"))  # 유효하지 않은 번호
