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