NLinear라는 시계열 딥러닝 모델

2024-01-04
오늘 다운로드한 것
- 우분투
- 소울트리
- 깃
- VSCODE.feat WSL, Material Icon Theme
- 
## Devops란?.feat 현직 이야기
현직에가면 알아야
뭔가 만들되고 배포되기까지 너무 오래걸림
<br/>시스템 돌아가는 것을 자동화하는 것들
<br/>Devops문화는 몰라도 툴은 알아야한다. ex)에자일
<br/>MLOps는 앞으로 2주간 알아갈것
<br/>
https://releases.ubuntu.com/20.04.6/?_ga=2.231303007.196765981.1704326920-1496082255.1704326920
<br/>
<br/>일단 이걸깔고 윈도우 기능의 Hyper-V를 활성화한다.
<br/>클라우드 호스트라고 HYPE-V를 동작시키기 위한 데이터 센터 전용(?)rmfjs cpwprk dlTdma
<br/>컴퓨터 만드는걸 자동화
<br/>앞으로 우분투를 통해 테스트 환경을 직접 만들기도 하고

<br/>여러사람이 쓰는 협업하는 환경은 리드개발자 정도 되야 변경할 수 있음
<br/>리눅스를 쓰더라도 깊이는 안들어가지만 기본적인 것들은 할줄알아야함.
- 최소 명령어 입력해서 텍스트 편집
- 리눅스를 이용해 배포를하고 상태를 보는 정도

os자체는 가상에서 실행되는지 모름

운영하는 팀은 보안이 매우 중요

앞으로 회사에가서 window 기반 노트북을 받게되면
Hyper-V 쓰는것부터 시작할듯(기본적으로 깔려있음 가장 큰 장점)

가상화되서 만들어지는건 Hyper-V가 함 os(ubuntu)X  
memory나 cpu가상화해서 넣어줌
사양에 맞게 적절하게 쓰자
하디 60GB 메모리 4GB
클라우드는 네트워크가 중요

devops 엔지니어는
보통 아키텍처든 리드개발자가 맡음

GIT을 해보게될텐데 버전관리하고 그런건 지금 당장은 안할듯

### 그 이후에 어떤일이 벌어지는지를 선임,리더급이 물어보신다.
미리 알고있는 것이 중요하다.

어딘가 문제가 생기면
개발 테스트 환경을 만들게 될거임
다른팀에서 QC/QA 테스트만 하는 사람들도 쓸테니
동일한 환경에서 운영되는 테스트 환경을 만들 것임

환경 다 구성한걸 이미지로 만듬
그 이미지를 불러와서 클릭하면 실행하기만 하면 됌
디폴트 스위치 ->
## git 시작작
git 다운
git bash - window 터미널
git bash란?
윈도우에서 git 명령어를 치는 환경을 구성해주기 위해서
window 파워셸은 많은 기능이 됌
리눅스를 계속이야기하는 이유: 거의 다 리눅스를 쓰기 때문
리눅스는 셸이 여러가지가 잇으면
그거와 매칭되는것이 윈도우 파워셸
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/5d17edde-e509-4718-98b0-49f3a399fd05)
깃설치 완료
`git`
`git help`
공식문서
`git -h init`
공식문서 가이드는 **무조건** 한번 보시길
블로그는 자기가 편한거만 써 놓
`git config --global core.autocrlf true`
- 윈도우, 맥 엔터 처리 오류 방지
- 맥이나 리눅스 input으로 설정
## sourctree 써보기
  sourctree jira 너무 깊게는 nono (오버스펙)
  깃허브에 있는 기능으로도 충분
git은 아주 중요한 자산
그래서 서버를 외부로 할듯
### 설치
건너뛰기 -> 머큐리얼 체크끄기 -> 이메일, 이름
## WINDOW와 LINUX의 관계
window가 linux를 품게됌 엄청 큰 사건
os안에는 kernel을 포함(kernel은 모든 핵심기능 보유)
커널 윗단에서는 리눅스 커널(WSL)이 브릿지역할을함 커널간의
**즉, WSL은 윈도우에 통합되어있는 리눅스 커널이다**
#### Ubuntu 20.4
git bash처럼 작업환경이 아니라 리눅스 커널이 들어가 있음
우분투를 깔면 컴퓨터를 하나 더 장만하는 셈

윈도우와 많이 통합이 되어있다 현재 리눅스는
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/218136a9-cb03-48d1-aaf5-0f77a0358bf2)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/3e54f5f2-7c11-4461-9b86-06cd07e6438b)

커널 명령어가 바뀜
셸은 명령어가 바뀌는 것 뿐만 아니라 스크립트도 바뀜 즉, OS 컨트롤 가능
리눅스 배포판 엄청 많은데 일단 두가지만 기억하자(우분투, 레드햇)
우리들의 초기 목표
- 우분투 배포해서 편집
- 커널 잘사용하기
배포판이 매우많음
지금까지 한것
WSL기반으로 우분투를 설치한것임
## 지금부터 깃을 다뤄보겠다.

<br/>` git config --global user.name "barabonda"`
<br/>` git config --global user.email "skydlalsdn2@gmail.com"`
<br/>` git config --global init.defaultBranch main`
<br/>'git config --global --list'
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/6245576d-e088-4d27-b8f0-ab93735e425c)

로컬저장소에서 원격저장소로 일부만 커밋했을 올라간다<br/>
즉, 깃허브에 올라간것만 다른 사람에 영향이 간다.

비주얼 스튜디오는 기능이 많아서 사람들 많이 쓴다.

---
우선 순위를 두거라
1. AI 프로젝트, MLOps
2. 다른 기술
---

맥은 UNIX 계열
안드는 linux 계열<br/>
잡스<br/>
apple(os) -> next -> apple(mac os)<br/>
next->iosi<br/>
리눅스 개발한 사람이 리눅스 버전관리를 위해 bitkeeper사용하려다가 실패해서 독자적으로 만든게 GIT<br/>

git source code
https://github.com/git/git/tree/e83c5163316f89bfbde7d9ab23ca2e25604af290
소스코드 발견하는 툴은 사실상 표준처럼 git이 쓰임<br/>
이제는 인프라운영하는 사람들도 씀<br/>
### Version Control System(VCS)
이런 툴없이 통합 겁나 힘들것<br/>
git에서는 어떤 작업을 추적, 복원 할 수 있음<br/>
사람과 대화, 컴퓨터와 대화 계속 번갈아하다보면 힘들고 관리힘듬 그걸 자동화 해주는 것이 git<br/>

U는 언트랙트 git이 관리하고있지않다는 
```2022-PC(T)-10@DESKTOP-5417C59 MINGW64 /c/src/hello (main)
$ git add lions.yaml

2022-PC(T)-10@DESKTOP-5417C59 MINGW64 /c/src/hello (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   lions.yaml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        tigers.yaml
```
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/572d3b55-48ac-42c3-b598-86adb177674b)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/b622614e-b808-4f1a-8a17-567c59045bca)



