from asyncio import sleep
from enum import Enum, auto
from random import choice

import reflex as rx

from . import common as cm

# 미리 지정된 무작위 이미지 목록
IMAGES = [
    "/samples/cabin.jpeg",
    "/samples/cake.jpeg",
    "/samples/learning_python.jpeg",
    "/samples/python_source_code.jpeg",
]


# 현재 이미지의 처리 상태
class ImageProcessingState(str, Enum):
    NONE = auto()  # 처리 전
    PROCESSING = auto()  # 처리 중
    FINISHED = auto()  # 처리 완료


# 이미지 처리 State
class DemoState(cm.RootState):
		# text2img 모델의 입력으로 사용할 프롬프트
    prompt: str = ""

		# 현재 처리 상태
    processing_state: ImageProcessingState = ImageProcessingState.NONE

    # 이미지 URI
    # 처리가 완료되면 무작위 이미지 URL 중 하나로 변경
    image_url: str = "/white.avif"

		# 아래 메소드(set_~ 메소드)는 작성하지 않아도 reflex가 자동으로 만들어주지만
    # 명확성을 위해 추가하였음
    def set_prompt(self, prompt: str):
        self.prompt = prompt

    # 계산된 속성. python의 property와 사용법 동일
    # 다른 변수들로부터 유도되는 속성
    @rx.var
    def is_processing(self) -> bool:
        return self.processing_state is ImageProcessingState.PROCESSING
   
		# 이미지 선택
    def select_image(self) -> str:
        return choice(IMAGES)

    # 이미지 처리 메소드
    async def go(self):
        # 처리 중이면 무시
        if self.processing_state is not ImageProcessingState.PROCESSING:
            self.processing_state = ImageProcessingState.PROCESSING
            yield  # 상태 업데이트
            await sleep(1)  # 임의의 처리 시간동안 대기
            self.processing_state = ImageProcessingState.FINISHED
            self.image_url = self.select_image()


def demo():
    return cm.build_page_component(
        # 좌우 여백을 주기 위한 container
        rx.container(
            # 타이틀(heading)과 설명(box 내부)를 세로로 배열
            rx.vstack(
                rx.heading("The Playground"),
                rx.box(
                    rx.text(
                        "Try AwesomePycon Model for free! "
                        "It is fast, unlimited and beautiful."
                    ),
                    padding_top="1em",
                    padding_bottom="1em",
                ),
            ),
            # 입력(input)과 버튼(button)을 가로로(hstack) 배열
            rx.hstack(
                rx.input(
                    placeholder="Type something...",
                    on_blur=DemoState.set_prompt,
                ),
                # 프로세스 중이면, 처리 중 표시. 아니면 Go 표시
                rx.button(
                    rx.cond(DemoState.is_processing, rx.spinner(), rx.text("Go!")),
                    on_click=DemoState.go,
                ),
                width="100%",
            ),
            # 처리 결과
            rx.image(
                # 표시될 이미지 링크. 처리 완료되면 변화함
                src=DemoState.image_url,
                width="100%",
                margin_top="1em",  # 입력 창과 살짝 거리를 벌림
                border="none",  # 외곽선 없음
            ),
        ),
    )