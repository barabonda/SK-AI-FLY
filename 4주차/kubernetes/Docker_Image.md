Docker Image 

Docker image :  

어떤 애플리케이션에 대해서, 

단순히 애플리케이션 코드뿐만이 아니라, 

그 애플리케이션과 dependent 한 모든 것을 함께 패키징한 데이터 

Dockerfile  

사용자가 도커 이미지를 쉽게 만들 수 있도록, 제공하는 템플릿 

# home 디렉토리로 이동합니다. 

$ cd $HOME 

 

# docker-practice 라는 이름의 폴더를 생성합니다. 

$ mkdir docker-practice 

 

# docker-practice 폴더로 이동합니다. 

$ cd docker-practice 

 

# Dockerfile 이라는 빈 파일을 생성합니다. 

$ touch Dockerfile 

 

# 정상적으로 생성되었는지 확인합니다. 

$ ls 


 

CMD 

명시한 커맨드를 도커 컨테이너가 시작될 때, 실행하는 것을 명시하는 명령어입니다.  

비슷한 역할을 하는 명령어로 ENTRYPOINT 가 있지만, 아직은 그 차이를 구분하기 어려울 수 있으므로 이번 강의에서는 ENTRYPOINT 에 대한 설명은 생략하겠습니다. 

하나의 Docker Image 에서는 하나의 CMD 만 실행할 수 있다는 점에서 RUN 명령어와 다릅니다. 
CMD <command> 
CMD ["executable-command", "parameter1", "parameter2"] 
CMD ["parameter1", "parameter2"] # ENTRYPOINT 와 함께 사용될 때 
 
# 예시 
CMD python main.py 
CMD  
 

WORKDIR 

이후 작성될 명령어를 컨테이너 내의 어떤 디렉토리에서 수행할 것인지를 명시하는 명령어입니다. 

해당 디렉토리가 없다면 생성합니다. 
WORKDIR /path/to/workdir 
 
# 예시 
WORKDIR /home/demo 
 

ENV 

컨테이너 내부에서 지속적으로 사용될 environment variable 의 값을 설정하는 명령어입니다. 
ENV <key> <value> 
ENV <key>=<value> 
 
# 예시 
# default 언어 설정 
RUN locale-gen ko_KR.UTF-8 
ENV LANG ko_KR.UTF-8 
ENV LANGUAGE ko_KR.UTF-8 
ENV LC_ALL ko_KR.UTF-8 
 

EXPOSE 

컨테이너에서 뚫어줄 포트/프로토콜을 지정할 수 있습니다. 

protocol 을 지정하지 않으면 TCP 가 디폴트로 설정됩니다. 
EXPOSE <port> 
EXPOSE <port>/<protocol> 
 
# 예시 
EXPOSE 8080 
 

3) 간단한 Dockerfile 작성해보기 

vi Dockerfile 혹은 vscode 등 본인이 사용하는 편집기로 Dockerfile 을 열어 다음과 같이 작성해줍니다. 

# base image 를 ubuntu 18.04 로 설정합니다. 
FROM ubuntu:18.04 
 

# apt-get update 명령을 실행합니다. 
RUN apt-get update 
 

# DOCKER CONTAINER 가 시작될 때, "Hello FastCampus" 를 출력합니다. 
CMD ["echo", "Hello FastCampus"] 
 

 
 

2. Docker build from Dockerfile 

docker build 명령어로 Dockerfile 로부터 Docker Image 를 만들어봅니다. 

$ docker build --help 
# 자세한 옵션들에 대한 설명은 생략 
 

# Dockerfile 이 있는 경로에서 다음 명령을 실행합니다. 
$ docker build -t my-image:v1.0.0 . 
 

설명  

. (현재 경로에 있는 Dockerfile 로부터) 

my-image 라는 이름과 v1.0.0 이라는 태그로 이미지를 

빌드하겠다라는 명령어 

정상적으로 이미지 빌드되었는지 확인해보겠습니다. 

# grep : my-image 가 있는지를 잡아내는 (grep) 하는 명령어 
$ docker images | grep my-image 
 

그럼 이제 방금 빌드한 my-image:v1.0.0 이미지로 docker 컨테이너를 run 해보겠습니다. 

$ docker run my-image:v1.0.0 
 

# Hello FastCampus 가 출력되는 것 확인
