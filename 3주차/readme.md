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

EC2나 리눅스에 뭔가 딱만드렁ㅆ다 그러면 패키지 업데이트해야함

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

## GIT 실습 4 (Branch)
Branch: 분기된 가지 (다른 차원)
`git branch add-coach` #브랜치 생성
`git switch add-coach` #브랜치 변경
`git switch -c new-teams` #브랜치 생성, 변경 같이 됌

간단한 플라스크 예제 우분투환경에서 해볼듯 앞으
```barabonda@barabonda-Virtual-Machine:~$ sudo add-apt-repository sudo apt-get update
[sudo] password for barabonda: 
Error: need a single repository as argument
barabonda@barabonda-Virtual-Machine:~$ sudo apt-get install git -y
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  apt-clone archdetect-deb cryptsetup-bin dctrl-tools dmeventd dpkg-repack
  gir1.2-timezonemap-1.0 gir1.2-xkl-1.0 libaio1 libdebian-installer4
  libdevmapper-event1.02.1 liblvm2cmd2.03 libreadline5 libtimezonemap-data
  libtimezonemap1 lvm2 python3-icu python3-pam rdate thin-provisioning-tools
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  git-man liberror-perl
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man liberror-perl
0 upgraded, 3 newly installed, 0 to remove and 111 not upgraded.
Need to get 5,518 kB of archives.
After this operation, 38.7 MB of additional disk space will be used.
Get:1 http://mirror.kakao.com/ubuntu focal/main amd64 liberror-perl all 0.17029-1 [26.5 kB]
Get:2 http://mirror.kakao.com/ubuntu focal-updates/main amd64 git-man all 1:2.25.1-1ubuntu3.11 [887 kB]
Get:3 http://mirror.kakao.com/ubuntu focal-updates/main amd64 git amd64 1:2.25.1-1ubuntu3.11 [4,605 kB]
Fetched 5,518 kB in 1s (6,889 kB/s)
Selecting previously unselected package liberror-perl.
(Reading database ... 139466 files and directories currently installed.)
Preparing to unpack .../liberror-perl_0.17029-1_all.deb ...
Unpacking liberror-perl (0.17029-1) ...
Selecting previously unselected package git-man.
Preparing to unpack .../git-man_1%3a2.25.1-1ubuntu3.11_all.deb ...
Unpacking git-man (1:2.25.1-1ubuntu3.11) ...
Selecting previously unselected package git.
Preparing to unpack .../git_1%3a2.25.1-1ubuntu3.11_amd64.deb ...
Unpacking git (1:2.25.1-1ubuntu3.11) ...
Setting up liberror-perl (0.17029-1) ...
Setting up git-man (1:2.25.1-1ubuntu3.11) ...
Setting up git (1:2.25.1-1ubuntu3.11) ...
Processing triggers for man-db (2.9.1-1) ...
barabonda@barabonda-Virtual-Machine:~$ git --version
git version 2.25.1
barabonda@barabonda-Virtual-Machine:~$ sudo apt-get install git -y 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
git is already the newest version (1:2.25.1-1ubuntu3.11).
The following packages were automatically installed and are no longer required:
  apt-clone archdetect-deb cryptsetup-bin dctrl-tools dmeventd dpkg-repack
  gir1.2-timezonemap-1.0 gir1.2-xkl-1.0 libaio1 libdebian-installer4
  libdevmapper-event1.02.1 liblvm2cmd2.03 libreadline5 libtimezonemap-data
  libtimezonemap1 lvm2 python3-icu python3-pam rdate thin-provisioning-tools
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 111 not upgraded.
barabonda@barabonda-Virtual-Machine:~$ git --version
git version 2.25.1
barabonda@barabonda-Virtual-Machine:~$ sudo apt-get update
Hit:1 http://mirror.kakao.com/ubuntu focal InRelease                           
Hit:2 http://mirror.kakao.com/ubuntu focal-updates InRelease                   
Hit:3 http://mirror.kakao.com/ubuntu focal-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu focal-security InRelease
Reading package lists... Done
barabonda@barabonda-Virtual-Machine:~$ sudo add-apt-repository ppa:git-core/ppa -y
Hit:1 http://mirror.kakao.com/ubuntu focal InRelease                    
Hit:2 http://mirror.kakao.com/ubuntu focal-updates InRelease            
Hit:3 http://mirror.kakao.com/ubuntu focal-backports InRelease          
Hit:4 http://security.ubuntu.com/ubuntu focal-security InRelease               
Get:5 http://ppa.launchpad.net/git-core/ppa/ubuntu focal InRelease [23.8 kB]   
Get:6 http://ppa.launchpad.net/git-core/ppa/ubuntu focal/main amd64 Packages [3,012 B]
Get:7 http://ppa.launchpad.net/git-core/ppa/ubuntu focal/main Translation-en [2,252 B]
Fetched 29.1 kB in 2s (19.4 kB/s)         
Reading package lists... Done
barabonda@barabonda-Virtual-Machine:~$ sudo apt-get install git -y
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  apt-clone archdetect-deb cryptsetup-bin dctrl-tools dmeventd dpkg-repack
  gir1.2-timezonemap-1.0 gir1.2-xkl-1.0 libaio1 libdebian-installer4
  libdevmapper-event1.02.1 liblvm2cmd2.03 libreadline5 libtimezonemap-data
  libtimezonemap1 lvm2 python3-icu python3-pam rdate thin-provisioning-tools
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  git-man
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-email git-gui gitk gitweb
  git-cvs git-mediawiki git-svn
The following packages will be upgraded:
  git git-man
2 upgraded, 0 newly installed, 0 to remove and 111 not upgraded.
Need to get 9,635 kB of archives.
After this operation, 11.1 MB of additional disk space will be used.
Get:1 http://ppa.launchpad.net/git-core/ppa/ubuntu focal/main amd64 git amd64 1:2.43.0-0ppa1~ubuntu20.04.1 [7,488 kB]
Get:2 http://ppa.launchpad.net/git-core/ppa/ubuntu focal/main amd64 git-man all 1:2.43.0-0ppa1~ubuntu20.04.1 [2,147 kB]
Fetched 9,635 kB in 3s (3,175 kB/s)
(Reading database ... 140401 files and directories currently installed.)
Preparing to unpack .../git_1%3a2.43.0-0ppa1~ubuntu20.04.1_amd64.deb ...
Unpacking git (1:2.43.0-0ppa1~ubuntu20.04.1) over (1:2.25.1-1ubuntu3.11) ...
Preparing to unpack .../git-man_1%3a2.43.0-0ppa1~ubuntu20.04.1_all.deb ...
Unpacking git-man (1:2.43.0-0ppa1~ubuntu20.04.1) over (1:2.25.1-1ubuntu3.11) ...
Setting up git-man (1:2.43.0-0ppa1~ubuntu20.04.1) ...
Setting up git (1:2.43.0-0ppa1~ubuntu20.04.1) ...
Processing triggers for man-db (2.9.1-1) ...
barabonda@barabonda-Virtual-Machine:~$ git --version
git version 2.43.0
barabonda@barabonda-Virtual-Machine:~$ 

```

**2024.01.05**
# CI/CD
github action에서 CI/CD를 해볼 수 있음  
github action에 뭘 만들어놓으면 컨테이너에 올리고  
따로 배포하는 곳에서도 배포할 수 있음    

**운영하는 사람 특징**  
1. 우리가 만든걸 모니터링하고있음
2. 차트에 문제있으면 해결
3. 하드웨어가 비정상적으로 과부하되고있으면 알람을 걸어서 알람이 오도록 할 수 있음(Slack 같은)
4. 당직이 아닐때 본인 part에 문제가 생기면 쉬다가도 처리

## CI(Continuous Integraion)  
지속적 통합  
programmer -> merge -> QA -> Deployment  
도커저장소에 컨테이미지를 만들어서 올리는 정도  
그거가지고 테스트/배포 azure로 배포  
고정도만해도 내가 편함  

개발자들은 좀 익숙해지면 프로젝트를 다양하게 함 오픈소스에 기여를 한다거나 ex) 한글화 

이것도 툴 굉장히 많음

## CD(Continuous Delivery Deploy)  
지속적 배포  
버전관리, 빌드/테스트, 검정, 배포 등등  
이것도 툴 엄청 많음  

Git hub -> Jenkins(실무 때 한번 써보길)  


# git hub action  
yaml json  
json을 사람의 눈으로 바꾼 것이 yaml(야믈)파일
들여쓰기 잘해야

python application
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/beb0e8af-5a5a-47d5-8978-8d5f55fe6680)
main에 push가 일어나면 아래의 이벤트가 일어날 수 있음  
job 밑에<br/>
build -> deploy
build의 run-0n 즉 컴퓨터가 생길때마다 뭘할 수 있(?)  
```
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
```
우분투에서 pull  
이것을  
```
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: "3.8"
    - name: Display Python version
      run: python -c "import sys; print(sys.version)"
```
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/8a706676-4fee-4231-9843-512e57e97640)

도커를 만들어보았다 ㄷㄷ  




이렇게 변경
