

"""
프롬프트 관리 프로그램 (콘솔 기반)
- 프롬프트 추가 / 목록 보기 / 카테고리별 조회 / 검색 / 상세 보기 / 즐겨찾기 관리
"""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 작성한 프롬프트를 기본 데이터로 등록"""
    return [
        {
            "title": "LLM 모델 비교 및 선정",
            "content": "Gemini 1.5 Flash와 Claude Sonnet 4.6을 비교해줘"
                        "가독성, 신뢰성, 효율성, 접근성, 협업성",
            "category": "텍스트 생성",
            "favorite": False,
        },
        {
            "title": "인스타툰 캐릭터 홍보 영상 소스 제작",
            "content": "찹쌀떡같이 하얗고 뽀얀 캐릭터가 일상을 보내는 듯한 장면을 만들어줘"
                        "해지는 저녁, 노을, 골목길, 교복, 찹쌀떡",
            "category": "이미지 생성",
            "favorite": True,
        },
        {
            "title": "자동화 워크플로우 설계",
            "content": "메일이 성공적으로 전송되면 디스코드에 정상적으로 메일이 전송되었음을 알리는"
                        "메시지가 오도록 자동화 워크플로우를 설계해줘",
            "category": "자동화",
            "favorite": False,
        },
    ]


def show_menu():
    """메인 메뉴 출력"""
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")
    print("==================================")


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


def add_prompt(prompts):
    """새 프롬프트 추가"""
    print("\n--- 프롬프트 추가 ---")
    title = input_nonempty("제목: ")
    content = input_nonempty("내용: ")
    category = choose_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    }
    prompts.append(new_prompt)
    print(f"'{title}' 프롬프트가 추가되었습니다.")


def format_prompt_line(idx, prompt):
    """목록에 사용할 한 줄 포맷"""
    star = "★" if prompt["favorite"] else "☆"
    return f"{idx}. [{prompt['category']}] {prompt['title']} {star}"


def show_list(prompts):
    """전체 프롬프트 목록 출력"""
    print("\n--- 전체 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for idx, prompt in enumerate(prompts, start=1):
        print(format_prompt_line(idx, prompt))


def show_by_category(prompts):
    """카테고리별 조회"""
    print("\n--- 카테고리별 조회 ---")
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"{idx}. {cat}")

    choice = input("조회할 카테고리 번호를 선택하세요: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return

    selected_category = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected_category]

    if not filtered:
        print(f"'{selected_category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{selected_category}] 카테고리 프롬프트")
    for idx, prompt in enumerate(filtered, start=1):
        print(format_prompt_line(idx, prompt))


def search_prompt(prompts):
    """키워드로 제목/내용 검색"""
    print("\n--- 프롬프트 검색 ---")
    keyword = input_nonempty("검색할 키워드를 입력하세요: ")

    results = [
        p for p in prompts
        if keyword in p["title"] or keyword in p["content"]
    ]

    if not results:
        print("검색 결과가 없습니다.")
        return

    print(f"\n'{keyword}' 검색 결과 ({len(results)}건)")
    for idx, prompt in enumerate(results, start=1):
        print(format_prompt_line(idx, prompt))


def show_detail(prompts):
    """프롬프트 상세 보기"""
    print("\n--- 프롬프트 상세 보기 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)
    choice = input("상세히 볼 프롬프트 번호를 입력하세요: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]
    star = "★ 즐겨찾기" if prompt["favorite"] else "☆ 즐겨찾기 안 함"
    print(f"\n제목   : {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"상태   : {star}")
    print(f"내용   : {prompt['content']}")


def manage_favorites(prompts):
    """즐겨찾기 추가/해제 및 즐겨찾기 목록 보기"""
    print("\n--- 즐겨찾기 관리 ---")
    print("1. 즐겨찾기 추가/해제")
    print("2. 즐겨찾기 목록 보기")
    choice = input("선택하세요: ").strip()

    if choice == "1":
        if not prompts:
            print("등록된 프롬프트가 없습니다.")
            return
        show_list(prompts)
        num = input("즐겨찾기를 변경할 프롬프트 번호를 입력하세요: ").strip()
        if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
            print("잘못된 번호입니다.")
            return
        prompt = prompts[int(num) - 1]
        prompt["favorite"] = not prompt["favorite"]
        state = "추가" if prompt["favorite"] else "해제"
        print(f"'{prompt['title']}' 즐겨찾기 {state}되었습니다.")

    elif choice == "2":
        favorites = [p for p in prompts if p["favorite"]]
        if not favorites:
            print("즐겨찾기한 프롬프트가 없습니다.")
            return
        print("\n[즐겨찾기 목록]")
        for idx, prompt in enumerate(favorites, start=1):
            print(format_prompt_line(idx, prompt))
    else:
        print("잘못된 선택입니다.")


def main():
    """프로그램 실행 진입점 (메뉴 반복 루프)"""
    prompts = get_default_prompts()

    while True:
        show_menu()
        choice = input("메뉴 번호를 입력하세요: ").strip()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            show_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            manage_favorites(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
