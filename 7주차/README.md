# gpt, azure, streamlit의 콜라보 시인 챗봇
```
import openai
import streamlit as st 

OPENAI_API_KEY = '6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT = 'https://sktfly2.openai.azure.com/'
OPEN_API_TYPE = 'azure'
OPENAI_API_VERSION='2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPEN_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header('welcome to AI Poem ', divider='rainbow')
st.write('아름다운 시를 함께 지어BoA yo~~!!:sunglasses:')

name = st.text_input('작가의 이름을 입력하세요' )
st.write(name + "님 반갑습니다.")
if (name):
    st.write(name + '님 반갑습니다.')

subject = st.text_input('시의 주제를 입력하세요')
content = st.text_area('시의 내용을 입력하세요')

button_click = st.button('RUN')

if button_click:
    with st.spinner('please wait...'):
        result = openai.chat.completions.create(
            model = 'dev-model',
            temperature=1,
            messages=[
                {'role':'system','content':'You are profeccer'},#You are a 19 years old Black boy, who is grown up in Hood, using slangs frequently
                {'role':'user','content': '작가의 이름은' + name},
                {'role':'user','content': '시의 주제는' + subject},
                {'role':'user','content': '시의 내용을' + name},
                {'role':'user','content': '이 정보로 시를 생성해줘' }
            ]
        )


        st.write(result.choices[0].message.content)
        st.success("done!")
```
## 웹페이지 생성완료
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/d5749a71-2be6-4353-a14c-94cdcb78cf46)

1. 대화형 모델
2. 완성형 모델
3. embedding 모델

   다 만들어보기
# Lengchain기반 Few-shotlearning으로 gpt-3.5 삼행시 시키기  

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/4610eb4f-a170-4203-859d-4351e3c868a3)

오늘 쓸 모
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/41c49469-480c-42a2-aeb9-6bd7d4adece1)

Community Cloud 이건 github와 연동해서 하나의 웹사이트를 올릴 수 있음
그말인 즉슨 깃허브에 소스코드가 업데이트가 되면 여기도 같이 업데이트 됌
포트폴리오를 만드는 것 추천 * 숙제
대신 여기에 배포할때는 requirements.txt 도 같이 배포해야함
하나의 컨테이너이기 때문
