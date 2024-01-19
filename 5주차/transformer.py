from flask import Flask, url_for, request, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv
# .env에 저장된 값들 로딩
load_dotenv()

#
app = Flask(__name__)
# 경로 추가
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_post():
    original_text=request.form['text']
    target_language=request.form['language']

    key = os.environ['KEY']
    endpoint=os.environ['ENDPOINT']
    location=os.environ['LOCATION']

    path = '/translate?api-version=3.0'

    target_language_parameter = '&to=' + target_language
    full_url = endpoint + path + target_language_parameter

    headers = {
        'Ocp-Apim-Subsciption-Key':key,
        'Ocp-Apim-Subsciption-Region':location,
        'Content-type':'application/json',
        'X-ClientTraceid':str(uuid.uuid4())
    }
    #번역 요청할 본문 생성
    body = [{'text': original_text }]
    # post로 translator 서비스 호출
    translator_request = requests.post(full_url, headers=headers, json=body)
    # 응답받은 json 탐색
    translator_response = translator_request.json()
    # 번역 검색
    translated_text=translator_response[0]['translations'][0]['text']
    # 렌더링 템플릿 호출, 번역된 텍스트, 원본 텍스트 및 대상 언어틀 템플릿에 전달
    return render_template(
        "results.html",
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )
