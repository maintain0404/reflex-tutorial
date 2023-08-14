# 추가로 해볼 만한 것

1. 하단 푸터의 경우 단순 텍스트로 만들었습니다. 아이콘을 추가할 수 있습니다.

    https://reflex.dev/docs/library/media/icon/

    <aside>
    💡 해당 서비스들의 공식 아이콘을 가져와서 소개 페이지 버튼 처럼 만들면 더 좋습니다.
    </aside>

2. 이 튜토리얼에서는 색을 거의 배제한 구성으로 진행했습니다. 색 배합을 바꿔볼 수 있습니다.
    
    <aside>
    💡 일반적으로 UI/UX에서 통용되는 몇 가지 원칙이 있습니다.

    1. 순수한 흰색, 검은색(000000, FFFFFF) 대신 약간 덜 순수한 색(2C2C2C, F2F2F2 등)을 사용합니다.
    2. 배치 비율을 수학적으로(1:1, 9:16 등) 맞추면 좋습니다.
    
    </aside>
    <br></br>
    <aside>
   💡 전역 스타일 설정 및 style 파라미터를 활용한다면 좀 더 깔끔한 코드 작성 및 디자인이 가능합니다.

    [https://reflex.dev/docs/styling/overview/](https://reflex.dev/docs/styling/overview/)
    </aside>
        
3. 본 튜토리얼에서는 실제 text2img 함수를 사용하지 않았습니다. 충분한 성능의 컴퓨터를 보유하고 있거나, API 사용이 가능하다면 실제 연결해봅시다.