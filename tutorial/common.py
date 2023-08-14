import reflex as rx


# 상속 편의를 위해 최상위 State를 미리 선언해 두었습니다.
class RootState(rx.State):
    pass


def menu():
    return rx.menu(
        rx.menu_button(rx.text("Menu")),
        rx.menu_list(
            rx.link("Demo", href="/demo", padding="1em"),
            # 없으면 데모와 갤러리가 구분되지 않아 한 줄에 출력됩니다.
            rx.menu_divider(),
            rx.link("Gallery", href="/gallery", padding="1em"),
        ),
    )


def color_mode_btn():
    return rx.color_mode_button(
        rx.color_mode_icon(),  # reflex에서 제공하는 기본 다크모드 변환 아이콘입니다.
        position="fixed",  # 화면에서 위치를 고정합니다.
        z_index=10,  # 다른 컨텐츠보다 앞에 보이게 합니다.
        right=0,  # 우측에 고정시킵니다.
    )


def navbar():
    return rx.box(
        rx.hstack(
            rx.link(rx.heading("AwesomePycon"), href="/"),  # 페이지 타이틀
            # 페이지 타이틀과 메뉴 사이 여유 공간(spacer)을 만들어 양쪽 정렬합니다.
            rx.spacer(),
            # 화면이 넓을 때(tablet_and_desktop)는 메뉴 버튼을 만들지 않고
            # 상단 네비게이션 바에 가로로(hstack) 퍼뜨립니다.
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.link(rx.text("Demo"), href="/demo"),
                    rx.link(rx.text("Gallery"), href="/gallery"),
                )
            ),
            # 화면이 좁을 때(mobile_only)는 메뉴 버튼을 만듭니다.
            rx.mobile_only(menu()),
            justify="space-between",
            padding_x="2em",
            padding_y="1em",
        ),
        # 아래 옵션은 네비게이션 바를 상단에(top=0px) 고정(positions=fixed)하고
        # 너비를 화면 전체(width=100%)로 하며 다른 컨텐츠보다
        # 앞에 보이게(z_index=5) 합니다.
        positions="fixed",
        width="100%",
        top="0px",
        z_index="5",
    )


def footer():
    return rx.box(
        # 가로로 타이틀과 링크 배열
        rx.hstack(
            rx.heading("PyconCompany"),  # 타이틀
            rx.spacer(),  # 양쪽 정렬을 위한 가운데 빈 공간
            rx.link("Github", href="https://github.com"),
            rx.link("LinkedIn", href="https://linkedin.com"),
            rx.link("Discord", href="https://discord.com"),
            rx.link("Twitter", href="https://twitter.com"),
            justify="space-between",  # flex박스 배치 css. 복잡하므로 설명 생략
            padding_x="2em",
            padding_y="1em",
        ),
        width="100%",
    )


# 화면 내용 컴포넌트(content)를 받아 공통 컴포넌트를 포함시켜 반환합니다.
def build_page_component(content: rx.Component):
    return rx.fragment(
        navbar(),
        color_mode_btn(),
        # 내용, 여유 공간(spacer), 하단 푸터(footer)를 세로로(vstack) 배치합니다.
        rx.vstack(
            content,
            rx.spacer(),
            footer(),
            width="100%",  # 화면 전체를 채웁니다.
        ),
    )
