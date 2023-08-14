# 시작하고 탐색해보기

1. reflex 프로젝트를 시작합니다.
    
    ```bash
    reflex init
    ```
    
    <aside>
    💡 이 과정에서 프로젝트 구동에 필요한 next.js 파일을 다운받아 설정하기 때문에 네트워크에 따라 오래 걸릴 수 있습니다.
    
    </aside>
    
2. 파일 구조는 아래와 같습니다
    
    ```bash
    .web  # reflex 구동을 위한 next.js 관련 디렉토리
    	~  # 디렉토리 내부에 파일이 많습니다만, 건들지 않습니다.
    assets  # 정적 리소스(이미지, 아이콘 등) 디렉토리
    	favicon.ico  # 
    tutorial  # reflex 애플리케이션 디렉토리
    	__init__.py  # python 패키지 표시 파일
      tutorial.py  # 메인 reflex 파일
    .gitignore  
    rxconfig.py  # reflex 구동 설정파일
    ```
    
3. tutorial/tutorial.py 코드를 살펴봅니다.
    1. `State` 클래스는 reflex에서 사용할 변수를 담는 클래스입니다.
        1. 사용자가 접속한 동안 유지됩니다.
    2. `index` 함수는 화면에 표시할 컴포넌트를 만들어 반환합니다.
        1. 기본으로 생성된 코드는 타이틀과 reflex 공식 문서와 연결 링크를 포함합니다.
    
    ```bash
    """Welcome to Reflex! This file outlines the steps to create a basic app."""
    from rxconfig import config
    
    import reflex as rx
    
    docs_url = "https://reflex.dev/docs/getting-started/introduction"
    filename = f"{config.app_name}/{config.app_name}.py"
    
    class State(rx.State):
        """The app state."""
    
        pass
    
    def index() -> rx.Component:
        return rx.fragment(
            rx.color_mode_button(rx.color_mode_icon(), float="right"),
            rx.vstack(
                rx.heading("Welcome to Reflex!", font_size="2em"),
                rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
                rx.link(
                    "Check out our docs!",
                    href=docs_url,
                    border="0.1em solid",
                    padding="0.5em",
                    border_radius="0.5em",
                    _hover={
                        "color": rx.color_mode_cond(
                            light="rgb(107,99,246)",
                            dark="rgb(179, 175, 255)",
                        )
                    },
                ),
                spacing="1.5em",
                font_size="2em",
                padding_top="10%",
            ),
        )
    
    # Add state and page to the app.
    app = rx.App()
    app.add_page(index)
    app.compile()
    ```
    
4. reflex 앱을 구동해봅니다.
    
    ```bash
    reflex run
    ```
    
