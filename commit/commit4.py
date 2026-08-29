def input_nonempty(prompt_text):
    """빈 값이 입력되면 다시 입력받는 헬퍼 함수"""
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("입력값이 비어있습니다. 다시 입력해주세요.")


def choose_category():
    """카테고리를 목록에서 선택하거나 직접 입력"""
    print("\n[카테고리 목록]")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}. {cat}")
    print(f"{len(CATEGORIES) + 1}. 직접 입력")

    choice = input("카테고리 번호를 선택하세요: ").strip()
    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(CATEGORIES):
            return CATEGORIES[num - 1]
        elif num == len(CATEGORIES) + 1:
            return input_nonempty("카테고리를 직접 입력하세요: ")
    print("잘못된 입력입니다. '기타'로 저장합니다.")
    return "기타"