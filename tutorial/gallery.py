import reflex as rx

from . import common as cm


def sample_card(prompt: str, image_url: str):
    return rx.grid_item(
        # 디자인 상 편의를 위해 카드 레이아웃을 사용했습니다.
        rx.card(
            rx.box(
                rx.image(
                    src=f"/samples/{image_url}",
                    width="auto",
                    height="auto",
                    border_radius="5px",
                ),
                rx.box(rx.text(prompt), padding="0.2em", font_size="2em"),
            ),
            background="none",
            shadow="none",
            border="0.5px",
        ),
        row_span=1,  # 2 * 2 그리드에서 행 1칸
        col_span=1,  # 2 * 2 그리드 안에서 열 1칸
        width="100%",
        padding="0.5em",
    )


def gallery():
    # 네비게이션 바, 푸터를 쓰기 위해 common에서 만든 템플릿 함수로 감쌉니다.
    return cm.build_page_component(
        rx.grid(
            sample_card("cabin", "/cabin.jpeg"),
            sample_card("cake", "/cake.jpeg"),
            sample_card("learning_python", "/learning_python.jpeg"),
            sample_card("python_source_code", "/python_source_code.jpeg"),
            template_rows="repeat(2, 1fr)",  # 그리드 열 정보를 선언합니다.
            template_columns="repeat(2, 1fr)",  # 그리드 행 정보를 선언합니다. 
            width="100%",
            gap=5,  # 그리드 내부 요소 간 거리
        )
    )