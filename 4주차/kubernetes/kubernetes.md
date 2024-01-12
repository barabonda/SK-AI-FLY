https://learn.microsoft.com/ko-kr/azure/aks/tutorial-kubernetes-prepare-app 

 


 

Kubernetes & Docker work 
together to build & run 
containerized applications 
&docker 
docker 
& Frameworks 
Operating System 
Hardware 
Traditional 
Deployment 
System 
Hardware 
Container 
Deployment 
docker 
e docker Odocker 
Kubernetes 
Deployment 
 

Top 10 Container Orchestration Tools 
MESOS 
RED HAT 
OPENSHIFT 
MIRANTIS 
•Sappfleet 
 

012, dH21 or 
kubernetes = kybernetes • cybernetics cyber 
cyberspace(7h4JZ7L!) = 
VI. 11.3 
2019.11 
•Features 
20185-6 
GKE 1.10 GA 
AWS EKS GA 
Azure AKS GA 
2015.11 
2018.3 
Kubernetes 1.10 
Kubernetes 1.16.2 
2015.7 
Ku rnetes 1.0 
2017.9 
Kubernetes 1.8 
Oracle joined 
MS AKS preview 
AWS ECS for K8s 
2016.9 
2017.3 
Kubern 1.6 
2016. 2 
Kubernetes 1.1, 
2016.3 
Kubernetes 1.2 
Google + linux = CNCF seed tech. 
First KubeCon 2015 
2015.6 
Kubernetes 0.20 
2003-2004 
Borg: The predecessor to Kubernetes 
20152 
Kubernetes 0.10 
2015.1 
Kubernetes 0.8 
Kubernetes 1.4 Kubernetes 1.5 
Kops : for AWS, etc. 
2014.6-7 
Kubernetes: Opensource version Borg 
First github commit - MS, Redhat, IBM, Docker joined 
2013 
Omega: flexible, scalable scheduler 
 

THE KUBERNETES ECOSYSTEM 
Public cloud 
Open source frameworks 
Management 
Monitoring & Logging 
aws 
in 
cri-o 
ocker 
Tools 
gea 
zeeg 
Security 
Load Balancing 
alci& 
spotinst 
 

Kubemetes 
Tiny to small, 
MicroK8s 
minikube 
Kubernet 
Using V 
Docker Desktop 
kind 
Mid to large, Production 7hÉ 
'A O aws 
Digita10ce.n kubernetes 
O kubernetes 
CD Alibaba Cloud 
ORACLE' 
MAGNUM 
 

쿠버네티스 실습 그 
 

Kubemefes Architecture 
User interface 
Kubernetes Master 
API Server 
Scheduler 
Controller-Manager 
CLI 
Worker Node 1 
Pod 
DOCKER 
kubelet 
Kube•prory 
Worker Node 2 
pod 2 
DOCKER 
kubelet 
Kube•prory 
 

C: \Users images 
REPOSITORY 
wordpress 
mcr.microsoft.com/dotnet/core/aspnet 
mysql 
doc ker/ desktop - storage - provisioner 
azul Zulu-o en • dk-al ine 
k8s . gcr . io/kube -proxy 
k8s . gcr . io/kube -apiserver 
k8s . gcr . io/kube -controller -manager 
k8s . gcr . io/kube—scheduler 
docker/ kube - compose - control er 
docker/kube-compose -api -server 
k8s . gcr . io/ coredns 
k8s . gcr . io/etcd 
k8s . gcr . io/echoserver 
k8s . gcr . io/pause 
C: \Users\user>kubect1 get 
TAG 
latest 
3. I-buster-slim 
5.7 
vi.ø 
latest 
VI. 15 5 
VI .15 5 
VI .15 5 
VI. 15 5 
vø.4.23 
vø.4.23 
IMAGE ID 
Ød205d4886fe 
c819eb4381e7 
413be204e9c3 
6Ø5aøf683b7b 
8252ff1ea1aa 
cbd7f21fec99 
e534b1952aed 
1399a72fa1a9 
fab2dded59dd 
a8c3d87a58e7 
f3591b2cb223 
eb516548c180 
2c4adeb21b4f 
365ec6Ø129c5 
da86e6ba6ca1 
VERSION 
VI . 15.5 
CREATED 
11 days 
13 days 
13 days 
5 weeks 
ago 
ago 
ago 
ago 
2 months ago 
6 months ago 
6 months ago 
6 months ago 
6 months ago 
10 months ago 
10 months ago 
15 months ago 
16 months ago 
2 years ago 
2 years ago 
SIZE 
5401-1B 
207MB 
456MB 
33 . IMB 
155MB 
82 .4MB 
2Ø7MB 
159MB 
81. IMB 
35 .3MB 
49 .9MB 
ae. 3MB 
258MB 
95 .4MB 
742kB 
NAME 
STATUS 
docker-desktop 
Ready 
1.3.1 
3-3.10 
1.10 
3.1 
node 
ROLES 
master 
AGE 
48d 
 

◇ 00 > 
Kubemetes A 「 ctu 「 
 

NOde 3 
Node 4 
191 1680.5 
Node 1 
192.1Μ.ο.2 
Node 5 
192.16806 
Node 2 
192.1&.α3 
 

Qod port-Gorward 
ust for 
temporary, development phase 
kubectl 
port 19898 
kubectl port-forward 
19898:9898 
TCP proxy 
Control Plane 
Master 
13.124.55.24 
port 9898 
Pod 
Container A 
172.2122, 
netfilter 
iptables 
kube-proxv 
Host- 
kubelet 
172.26.10 
C 
13.126.18.11 
pod 
Container B 
O D localhost:18080 
Welcome to nginx! 
If you see this page, the nginx web server is successfully installed and 
working. Further configuration is required. 
For online documentation and support please refer to ngiD&Qrg. 
Commercial support is available at ngin&.GQm. 
Thank you for using nginx. 
 

쿠버네티스 실습 그 
 

Service 
port 30080 
SERVICE 
port 80 
POD 
Node 1 
IP: 172.31.41.126 
port 3008 
POD 
POD 
Node 2 
IP: 17231.47.81 
 

set-vice Т 
user 
рюху 
Cluster 
Clusterl 
Servte 
О 
Изег 
LoadBa]ancer 
N0dePort 
C]usterIP 
О 
е 
О 
Изо 
оку 
 

쿠버네티스 실습 5 
 

Deployment Controller 
DEPLOYMENT 
VI 
v2 
POO POO 
POD 
POD 
ReplicaSet 
ReplicaSet 
POD POD 
 

쿠버네티스 실습 
 

Qersistent Volume 
Podl 
Kubernetes 
Cluster 
Pod2 
Persistent Volume Claim 
(PVC) 
Persistent Volume 
Storage 
 

쿠버네티스 실습 6 
 

1. YAML 이란? 

데이터 직렬화에 쓰이는 포맷/양식 중 하나  

데이터 직렬화란?  

서비스간에 Data 를 전송할 때 쓰이는 포맷으로 변환하는 작업  

ex) 쿠버네티스 마스터에게 요청을 보낼 때 사용 

다른 데이터 직렬화 포맷  

XML, JSON 

파일 포맷  

.yaml, .yml 

 
 

2. YAML 특징 

가독성 

YAML 은 사람이 읽기 쉽도록 디자인  

YAML 포맷 
apiVersion: v1 
kind: Pod 
metadata: 
  name: example 
spec: 
  containers: 
    - name: busybox 
      image: busybox:1.25 
 

JSON 포맷 
{ 
  "apiVersion": "v1", 
  "kind": "Pod", 
  "metadata": { 
    "name": "example" 
  }, 
  "spec": { 
    "containers": [ 
      { 
        "name": "busybox", 
        "image": "busybox:1.25" 
      } 
    ] 
  } 
} 
 

Widely-use 

kubernetes manifests 명세 

docker compose 명세 

ansible playbook 명세 

github action workflow 명세 

Strict-Validation 

줄 바꿈 

들여쓰기  

Tab vs Space 

 
 

3. 문법 

1) Key-Value 

Recursive 한 key-value pair 의 집합 

apiVersion: v1 
kind: Pod 
metadata: 
  name: example 
spec: 
  containers: 
    - name: busybox 
      image: busybox:1.25 
 

2) 주석 

# 를 줄의 맨 앞에 작성하면 주석 처리됩니다. 

# kubernetes pod exmaple 입니다. 
apiVersion: v1 
kind: Pod 
metadata: 
  name: example 
# 중간에 작성해도 됩니다. 
spec: 
# 여기도 주석을 달 수 있습니다. 
  containers: 
    - name: busybox 
      image: busybox:1.25 
 

3) 자료형 

string 

# 일반적인 문자열은 그냥 작성해도 되고, 따옴표로 감싸도 됩니다. 
example: this is 1st string 
example: "this is 1st string" 
 

# 반드시 따옴표로 감싸주어야 하는 경우 : 
# 1) 숫자를 문자열 타입으로 지정하고 싶은 경우 
example: 123 
example: "123" 
 

# y, yes, true 등의 YAML 예약어와 겹치는 경우 
example: "y" 
 

# :, {, }, ,, #, *, =, \\n 등의 특수 문자를 포함한 경우 
example: "a : b" 
example: "a#bc*" 
 

integer 

# integer type 
example: 123 
 

# hexadecimal type: 0x 로 시작 
example: 0x1fff 
 

float 

# float type 
example: 99.9 
 

# exponential type 
example: 1.23e+03 # 1.23 x 10^3 = 1230 
 

boolean 

# True 
example: true 
example: yes 
example: on 
 

# False 
example: false 
example: no 
example: off 
 

4) List 

# - 를 사용하여 list 를 명시할 수 있습니다. 
examples: 
  - ex_one: 1 
  - ex_two: 2 
 

# [ ] 로 입력해도 됩니다. 
examples: ["1", "2", "3"] 
 

# list 의 원소는 어떤 자료형이든 가능합니다. 
spec: 
  containers: 
    - name: busybox 
      image: busybox:1.25 
    - name: ubuntu 
      image: ubuntu 
      commands: 
        - sleep 
        - 3600 
    - name: python 
      image: python:3.9 
 

5) Multi-line strings 

| 

중간에 위치한 빈 줄을 \\n 으로 처리하며, 문자열의 맨 마지막에 \\n 을 붙입니다. 
example: | 
  Hello 
  Fast 
  Campus. 
# "Hello\\nFast\\nCampus.\\n" 으로 처리 
 

> 

중간에 위치한 빈 줄을 제외하고, 문자열의 맨 마지막에 \\n 을 붙입니다. 
example: > 
  Hello 
  Fast 
  Campus. 
# "Hello Fast Campus.\\n" 으로 처리 
 

|- , >- 

각각 |, > 와 동일하되, 문자열의 맨 마지막에 \\n 이 추가되지 않습니다. 

6) Multi-document yaml 

--- 라는 구분선을 통해 하나의 yaml 파일에 여러 개의 yaml document 를 작성 가능 

apiVersion: v1 
kind: Pod 
metadata: 
  name: one 
--- 
apiVersion: v1 
kind: Service 
metadata: 
  name: two 
--- 
apiVersion: v1 
kind: Deployment 
metadata: 
  name: three 
 

3 개의 yaml document 로 인식 

7) 복습 

Pod 의 명세를 작성한 yaml 예시 

# key-value pairs 
apiVersion: v1 
kind: Pod 
metadata: 
  name: example 
  labels: 
    hello: bye 
spec: 
  containers: 
    # list 
    - name: busybox 
      image: busybox:1.25 
      # list 
      ports: 
      - containerPort: 80 
    - name: another-container 
      image: curlimages/curl 
 

선언형 인터페이스를 위해서, Desired State 를 명시하는 용도로 사용 
