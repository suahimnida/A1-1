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