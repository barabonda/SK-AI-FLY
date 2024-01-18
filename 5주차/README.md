컴퓨터  <br/>
네트워킹<br/>  
스토리지<br/>


퍼블릭 클라우드<br/>
프라이빗 클라우드<br/>
하이브리드 클라우드<br/>

IasS 개발<br/>
PasS 개발<br/>

cloud는 베이스로 깔고 가야함<br/>

리소스 그룹 만들기  
디스크 만들
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/d9c300eb-c816-41a3-a996-f2015bc0177b)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/2e612078-4613-46de-9375-4de2eb0f334a)

이걸 하는 이유:<br/>
서버관리는 GUI없 다 명령어임<br/>
## 파워셸에서 리소스만들고 디스크 만들기<br/>
리소스만들기<br/>
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/475d0bce-1b7e-44ed-a06b-0b095052688d)
리소스에 디스크만들기<br/>

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/b5028397-5261-49ea-b0aa-fac817e2d642)

<br/>
변수 지정하고

## ARM Template
인프라를 정의하는 개념인 Iac(Infra as Code)의 한 형태  

ARM Template 사용 이유  
- 선언적 구문 사용, 일관되고 반복된 배포가능
- CI/CD 통합
- 오케스트레이션(Orchestraion) 올바른 순서
key - value 형태로 정의


ARM Template의 변수(variable)  


이것만 알아도 돈벌고 클라우드 비용 줄임
`cholyean [~]$ az group delet --name edu-sourcecy-rg --no-wait --yes`  
리소스 그룹을 없애는데 비동기로 처리 그러면 없애는동안 난 다른걸 할 수 있음
--no-wait 비동기  

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/4e55cc9b-642e-4a53-85c2-7b996a6ebac3)
작년 하반기부터 익명도 체크해야

사용자 정의 환경
스토리지 계정만들고 리소스그룹을 만들고 디스크 만들고
그것들을 만들고 이어보는것을 해보았다.  

배쉬환경에 익숙해지자 취업하고는 GUI에서 쓴다.  
## azure 스토리지
정형 데이터/ 반정형 데이터/ 비정형 데이터
스토리지는 DB와 다르다  
데이터 분석할 때 주로 씀  
데이터를 저장 or 처리된 결과 저장  
->데이터 시각화, 분석, 학습  

**azure storage의 장점**
- 뛰어난 내구성 및 고가용성
- 보안성  
- 확장성  
- 원활한 엑세스 가능하고 개발의 편리성 제공

스토리지서비스
- 컨테이너
- 파일
- 테이블

**다중지역**
복제 해놓기

가상머신 스토리지 
를 만들기 이전에 항상 리소스 그룹
그 후 가성머신 스토리지에 옵션  

스토리지만들 때 st를 넣어 고유한 이름  
성능 표준 or 프리미엄   




finetuning
windows 10  

  선택하는 네트워크  

    가상머신
## 부하분산
확장스크랩트 설치

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/05eeb9dd-d6e8-49c5-be06-d3abeff70f68)

리소스 그룹 - 리소스 - 네트워크 - 가상머신 - 서브넷 - 벡엔드풀


버추얼 네트워크
1. 서브넷만들기
2. 어플리케이션 게이트웨이는 독자적인 서브넷 필요하니까 하나 더 만들어주고
3. 벡엔드 풀 가상 머신올려주고
4. 외부서버 올려보고
5. 어플리케이션, fe설정해고
6. 외부 public 내부 private
7. 벡엔드풀 등록
9. 회람규칙

paas  
## Azure app service  

11. 정적인 private로 변환시키고 정상적인 부하분산이 일어나면 끝난것임. 
vmss(가상머신 확장 집합)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/895b160f-f054-402d-9111-fac53d52bfc8)
vmss에서 특정 인스턴트에 접근하려면 포트를 맞춰야함

app service 계획 크기 조정  
매트릭에 따라 스케일링 (CPU 백분율, 메모리 백분율, HTTP 요청)  
일정에 따라 크기 조정(평일, 주말, 시간, 공휴일)   
  
  
# app service 만들기  
웹앱 3개만들고 traffic 매니저 지원해주는거 만들어주고
생성하고 그 웹앱가지고 노드벨러싱할수있

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/76f64947-c380-4675-ba80-fed77122071c)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/d01fd75d-115b-421c-b70c-6767a9f93108)
만들어보았다.!

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/ffa2c681-e966-4b9b-bfea-456e270ce45c)
# 정적 webapp 만들기  


  
## github와 azure와 연동하여 배포하기
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/e7e28b64-cc1b-4886-9033-063c64018240)

## 곧 만들어질거라고 축하까지 해주는 azure...ㅋㅋㅋ
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/891472a2-9cb4-4c46-b67c-4d114e08ea8f)  
## 몇초 지나서 만들어졌다!!
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/b488e6a1-798e-44a0-bac8-c764ed5dab04)
## 휴대폰에서도 반응형 웹앱으로 잘돌아간다!!
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/492f96e1-153b-43ed-b4be-4905557500ff)

2024.01.18
## 배포 슬
1. 웹앱만들기
2. 로컬 git 리포지토리 이용 git 배포 구성
3. git 클라이언트 구성 및 웹앱 소스코드 복제
4. production 슬롯에 앱을 배포하도록 git remote 구성
5. 새 staging 슬롯 만들기
6. 새 staging 슬롯에 git 배포 구성
7. Staging 슬롯에 앱을 배포하도록 git remote 구성
8. 앱 소스코드 수정 및 staging 슬롯에 배포
9. 슬롯 설정 구성 및 교환
정형화 되면
rdb, sql, 오라클

비정형
몽고db - node.js

# docker azure 서버 연결  
```
ssh -i "C:\Users\2022-PC(T)-10\Downloads\lmwi_key.pem" azureuser@52.175.32.90
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
