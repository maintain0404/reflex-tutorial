## 소개 화면 만들기

소개 화면엔 다음이 필요합니다.

1. 소개 문구
    1. 타이틀
    2. 설명
2. 갤러리, 데모 이동 버튼
3. 샘플

### 소개 페이지 컴포넌트

`tutorial/front.py`

```python
import reflex as rx
from . import common as cm


def front():
		# 네비게이션 바, 푸터를 쓰기 위해 common에서 만든 템플릿 함수로 감쌉니다.
    return cm.build_page_component(
        rx.fragment(
            # 가운데에 배치합니다.
            rx.center(
                # 소개 문구 + 이동 버튼과, 샘플을 가로로 배치합니다.
                rx.hstack(
                    # card는 헤더, 컨텐츠, 푸터를 가진 소형 레이아웃입니다.
                    # 타이틀(헤더), 컨텐츠(설명), 푸터(버튼)이 있어 사용했습니다.
                    rx.card(
                        body="Super duper text2image model.",
                        # 타이틀은 크고(font=2em), 헤더이므로 heading을 사용했습니다.
                        header=rx.heading("Welcome to AwesomePycon!", font_size="2em"),
                        # 버튼 두 개를 가로로(hstack) 배열
                        footer=rx.hstack(
                            rx.link(
                                rx.button(
                                    rx.text("Try AwesomePycon"),
                                ),
                                href="/demo",
                            ),
                            rx.link(
                                rx.button(
                                    rx.text("See Gallery"),
                                ),
                                href="/gallery",
                            ),
                        ),
                        spacing="1.5em",
                        font_size="2em",
                        padding_top="10%",
                        background="none",
                        border="none",
                        shadow="none",
                    ),
                    # 카드에 정의된 디자인 설정을 쓰기 위해 image를 감쌌습니다.
                    rx.card(
                        rx.image(
                            src="/python_conference.jpeg", width="auto", height="auto"
                        ),
                        background="none",
                        border="none",
                        shadow="none",
                    ),
                    width="100%",
                ),
                width="100%",
                padding_bottom='5em'  # 하단 컴포넌트(푸터)와 거리를 둡니다.
            ),
        )
    )
```

### tutorial.py

새 소개화면을 쓰기 위해 바꿔줍니다.

```python
"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from . import common as cm
from .front import front

# Add state and page to the app.
app = rx.App(state=cm.RootState)
app.add_page(front, route='/')
app.compile()
```

### 실행해보기

첫 화면이 잘 나타나는지 확인해보세요. 처음에 실행한 `reflex run`을 종료하지 않았다면 자동으로 수정사항이 반영되어 있을 겁니다. 아니라면 새로 실행해주세요.