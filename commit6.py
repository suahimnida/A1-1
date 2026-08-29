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