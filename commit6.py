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