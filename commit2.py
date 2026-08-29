def get_default_prompts():
    """이전 미션에서 작성한 프롬프트를 기본 데이터로 등록"""
    return [
        {
            "title": "LLM 모델 비교 및 선정",
            "content": "Gemini 1.5 Flash와 Claude Sonnet 4.6을 비교해줘 "
                        "가독성, 신뢰성, 효율성, 접근성, 협업성",
            "category": "텍스트 생성",
            "favorite": False,
        },
        {
            "title": "인스타툰 캐릭터 홍보 영상 소스 제작",
            "content": "찹쌀떡같이 하얗고 뽀얀 캐릭터가 일상을 보내는 듯한 장면을 만들어줘 "
                        "해지는 저녁, 노을, 골목길, 교복, 찹쌀떡",
            "category": "이미지 생성",
            "favorite": True,
        },
        {
            "title": "자동화 워크플로우 설계",
            "content": "메일이 성공적으로 전송되면 디스코드에 정상적으로 메일이 전송되었음을 알리는 "
                        "메시지가 오도록 자동화 워크플로우를 설계해줘",
            "category": "자동화",
            "favorite": False,
        },
    ]