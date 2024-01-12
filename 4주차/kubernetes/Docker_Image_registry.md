3. Docker Image 저장소 

1) Docker Registry 

공식 문서 

https://docs.docker.com/registry/ 

간단하게 도커 레지스트리를 직접 띄워본 뒤에, 방금 빌드한 my-image:v1.0.0 을 도커 레지스트리에 push 해보겠습니다. 

Docker Registry 는 이미 잘 준비된 도커 컨테이너가 존재하므로, 쉽게 사용할 수 있습니다. 

docker registry 를 띄워봅니다. 
$ docker run -d -p 5000:5000 --name registry registry 
 
$ docker ps 
# 정상적으로 registry 이미지가 registry 라는 이름으로 생성되었음을 확인할 수 있습니다. 
# localhost:5000 으로 해당 registry 와 통신할 수 있습니다. 
 

my-image 를 방금 생성한 registry 를 바라보도록 tag 합니다. 
$ docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0 
 
$ docker images | grep my-image 
# localhost:5000/my-image:v1.0.0 로 새로 생성된 것을 확인할 수 있습니다. 
 

my-image 를 registry 에 push 합니다. (업로드합니다.) 
$ docker push localhost:5000/my-image:v1.0.0 
 

정상적으로 push 되었는지 확인합니다. 
# localhost:5000 이라는 registry 에 어떤 이미지가 저장되어 있는지 리스트를 출력하는 명령 
$ curl -X GET <http://localhost:5000/v2/_catalog> 
 
# 출력 : {"repositories":["my-image"]} 
 
# my-image 라는 이미지 네임에 어떤 태그가 저장되어있는지 리스트를 출력하는 명령 
$ curl -X GET <http://localhost:5000/v2/my-image/tags/list> 
 
# 출려 : {"name":"my-image","tags":["v1.0.0"]} 
 

2) Docker Hub 

회원 가입 

hub.docker.com 

Choose a Plan 

Free 

Email 인증 

Docker login 
$ docker login 
 
# username, password 입력 
# Login Succeeded! 
 

Docker Hub 를 바라보도록 tag 생성 
$ docker tag my-image:v1.0.0 koreaeva/my-image:v1.0.0 
 
# docker tag <image_name>:<tag_name> <user_name>/<image_name>:<tag> 
 

Docker image push to Docker Hub 
$ docker push koreaeva/my-image:v1.0.0 
 
# docker push <user_name>/<image_name>:<tag> 
 

Docker hub 의 본인 계정에서 업로드한 이미지 확인 

https://hub.docker.com/repositories 
93a543c7-41fd-449e-b49e-8630f2885432 
