## 구성하기

일단 저희가 만들 구성을 다시 살펴보면 다음과 같습니다.

공통 코드를 위한 파일, 소개 화면 파일, 갤러리 화면 파일, 데모 화면 파일을 새로 만들겠습니다.

최종 디렉토리 구조는 다음과 같습니다.
```bash
.web
   ~  # 여러 파일이 있으나 다루지 않을 예정입니다.
assets
	favicon.ico
tutorial
	__init__.py
	common.py  # 공통 코드 파일
	demo.py  # 데모 화면 파일
	front.py  # 소개 페이지 파일
	gallery.py  # 갤러리 페이지 파일
    tutorial.py
.gitignore  
rxconfig.py
```
