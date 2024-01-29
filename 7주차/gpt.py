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

st.header('welcome to GPT Bot', divider='rainbow')
st.write('궁금한것을 물어보세요!:sunglasses:')

query = st.text_input('query?' )
button_click = st.button('run')

if button_click:
    with st.spinner('please wait...'):
        result = openai.chat.completions.create(
            model = 'dev-model',
            temperature=1,
            messages=[
                {'role':'system','content':'You are a 19 years old Black boy, who is grown up in Hood, using slangs frequently'},
                {'role':'user','content':query}
            ]
        )


        st.write(result.choices[0].message.content)
        st.success("done!")