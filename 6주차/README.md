# pytorch  
배운 내용  
pytorch CNN, VGG,LeNet, Resnet, AlexNet, transformer, word2vector,object detection, OpenCV  
**pytorch와 tencerflow의 차이**  
동적신경망과 정적신경망
  
**GPU 와 CPU의 차이**
GPU는 병렬연산의 최적화  

22년 말 chat-gpt의 등장으로 구글의 성장이 주춤  

touch.autograd: 자동 미분 패키지  
torch.nn: 
touch.multiprocessing  
touch.utills  

인텔과 엔비디아  
cpu 다루는 api는 인텔
gpu 다루는 api는 cuda
cuda ai 라이브러리 쉽게쓰게 해줌  

파이토치 아키텍처  

offset: 텐서에서 첫 번째 요소가 스토리지에 저장된 미션  
stride:  
conda create -n torch_book python = 3.9.0  

tencer는 새로운 자료형  

view를 쓰면 tensor의 shape을 바꿀 수 있음  
__-__이런것은 내부함수

합성곱 신경망 구조<br/><br/>
⚫ 즉, 합성곱층을 요약하면 다음과 같음<br/>
입력 데이터: W1×H1×D1 (W1<br/>
: 가로, ×H1<br/>
: 세로, ×D1<br/>
: 채널 또는 깊이)<br/><br/>
하이퍼파라미터<br/>
• 필터 개수: K<br/>
• 필터 크기: F<br/>
• 스트라이드: S<br/>
• 패딩: P<br/><br/>
출력 데이터<br/>
• W2 = (W1-F+2P)/S+1<br/>
• H2 = (H1-F+2P)/S+1
• D2 = K<br/>  

### 전이학습  
전이학습(Transfer learning)은 어떤 목적을 이루기 위해 학습된 모델을 다른 작업에 이용하는 것  
즉 모델의 지식을 다른 문제에 이용하는 것으로 볼 수 있습니다.  

**특성-추출 기법**
opencv깔기  
## LeNet-5  <br/>
② _ _call_ _ 함수는 클래스를 호출할 수 있도록 하는 메서드<br/>
⚫ _ _init_ _은 인스턴스 초기화를 위해 사용한다면 _ _ call_ _은 인스턴스가 호출되었을 때<br/>
실행
⚫ 즉, 클래스에 _ _call_ _ 함수가 있을 경우 클래스 객체 자체를 호출하면 _ _call_ _ 함수의<br/>
리턴(return) 값이 반환<br/>
⚫ 이미지가 위치한 디렉터리에서 데이터를 불러온 후 훈련용으로 400개의 이미지, <br/>
검증용으로 92개의 이미지, 테스트용으로 열 개의 이미지를 사용<br/>
피쳐맵은 줄어들고 채널은 늘어나는 구조  <br/>

maxpool2d는 보통 2이다
커널 사이즈를 조정하는게 낫다
stride를 늘리면 패딩사이즈가 확줄음

### VGG-NET  
합성곱을 많이씀  
진정한 딥러  

이미지 전체를 받아서 넣는다 피쳐맵에서 뽑느다
왜? 너무 많아서 피쳐맵으로 뽑는것이 좋음
CCNN 양방향 풀리커넥티드 한쪽에서는 있냐 없냐 한쪽에서는 좌표를 
그리드를 만들어서 각점으로 16개나 4개를 만들어서 

yolo는 한층에서만 했지만 신뢰도도 평가야하여 보완함

정확도는 faster r-cnn 속도는 yolo
# transformer 
인코더 디코더 둘다 존재  
인코더의 경우 self-attention 사용
트랜스포머는 입력되는 문장을 순차적으로 처리하지않고 병렬로 한번에 처리  
때문에 단어 정보와 위치정보를 합해서 처
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/6ffd68e8-9f01-4ce8-8584-ec3ed375c68c)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/78ea0a36-a194-4df3-b853-793cdcf69e54)  
gpt는 한단어 한단어 내뱉음  
때문에 내뱉은 단어가 다시 input되고  
cross-attention 번역 시작
a, b, c가 있을 때
b에 대한 a,c 학습 c에 대한 a,b 학습 3개의 연관성 a,b,c 학습
각 단어와 다른 단어들의 연관성을 끊어서 생각
학습을 함 그렇기 때문에 a,b,c에 대한 연관성을 알게됌  
그렇기 때문에 gpt는 디코더만 쓰고 
디코더만 쓰는게 대세가 됌
cross-attention은 번역에 쓰임
gpt가 번역하는 거는
나는 너를 사랑해는 i love you야 라고 생성하고 i love you를 쓰는것
그러므로 cross-attention이 아니라 self-attention많으로 번역 등등 많은 것들을 수행하는 것임  
vision 트랜스포머  
속도와 양을 
vivit  
# opencv  
인텔에서 만든 라이브러리  
바퀴를 다시 발명reinventing the wheel하는 쓸데없는 노력을 방지할 목적
▪ 인텔 칩의 성능을 평가할 목적

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/da6eafbb-b156-4330-ab50-67e15d5279ba)
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/c22adf30-79ae-4f06-adca-1c7f5cf00bc0)

![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/d8bf20b9-2b5c-45cf-be97-890b62bd46e5)  
```
import cv2
import numpy as np
import random

def find_and_draw_circles():
    # Create a white background image (640x480)
    img = np.ones((480, 640, 3), dtype=np.uint8) * 255

    # Generate 5 random circles
    circles_info = []  # to store circle information (center, radius, color)

    for _ in range(5):
        center = (random.randint(50, 590), random.randint(50, 430))
        radius = random.randint(20, 50)
        color = (random.choice([0, 255]), random.choice([0, 255]), random.choice([0, 255]))

        # Ensure that the circle color is red, blue, or green
        while color not in [(0, 0, 255), (255, 0, 0), (0, 255, 0)]:
            color = (random.choice([0, 255]), random.choice([0, 255]), random.choice([0, 255]))

        # Draw the random circle on the image
        cv2.circle(img, center, radius, color, -1)

        # Store circle information
        circles_info.append((center, radius, color))

        # Draw rectangles around the detected circles in the original image
        cv2.rectangle(img, (center[0] - radius, center[1] - radius), 
                            (center[0] + radius, center[1] + radius), color, 2)

        # Display the color name as text
        color_name = "Red" if color == (0, 0, 255) else "Blue" if color == (255, 0, 0) else "Green"
        cv2.putText(img, color_name, (center[0] - radius, center[1] - radius - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

    # Display the image with rectangles and the result of Hough Circle Transform
    cv2.imshow('Circles with Rectangles', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return circles_info
```
cv2.circle
중심좌표 반지름 선의 색
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/ad1f727c-ff5b-4704-9471-c9ee07fffb10)  



![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/f5b28e8d-54c7-4914-989a-2f4b77cf3d5c)
특정 hsv에 있는 cv.cvtcolor추출
```
import numpy as np, cv2

image1 = cv2.imread(r".\chap06/images\add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread(r".\chap06/images\add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성
alpha, beta = 0.6, 0.7
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)

numpy_horizontal = np.hstack((image1, add_img3, image2))
cv2.imshow('dst', numpy_horizontal)

# titles = ['image1','image2','add_img3']
# for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
```
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/ba342ec9-a6dd-47dc-b6a6-cd685b8fed94)

```
import cv2
def onThreshold(value):
    result = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("result", result)
image = cv2.imread("C:/Users/2022-PC(T)-10/Desktop/SKAIFLY/opencv/chap06/images/color_space2.jpg", cv2.IMREAD_GRAYSCALE) # 컬러 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")
cv2.namedWindow("result")
cv2.createTrackbar("threshold", "result", 128, 255, onThreshold)
onThreshold(128) # 이진화 수행
cv2.imshow("image", image)
cv2.waitKey(0)
```
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/9b85ea7a-4c92-4bfe-b120-5b0e9e2a8feb)
```
import numpy as np, cv2

# 영상 읽기
image1 = cv2.imread("./images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("./images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")
# 트랙바의 콜백 함수
def nothing(x):
    pass

# 결과 이미지를 출력할 창 생성
cv2.namedWindow('dst')

cv2.createTrackbar('image1', 'dst', 0, 100, nothing)
cv2.createTrackbar('image2', 'dst', 0, 100, nothing)

while True:

    alpha = cv2.getTrackbarPos('image1', 'dst') / 100
    beta = cv2.getTrackbarPos('image2', 'dst') / 100

    # 이미지 합성
    result_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    final_result = np.hstack((image1, result_img, image2))

    cv2.imshow('dst', final_result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```
![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/aa05616f-e848-440d-b0ad-af21c1c2b49f)

```
import cv2
import numpy as np
import pytesseract
import sys

TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" #테서렉스 설치 경로
imgpath='./images/2.JPG'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기
if img is None:
    print('Image load failed')
    sys.exit()
img = cv2.resize(img, dsize=(1000,800))
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global pts_cnt
    global img
    if event== cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)
        
        pts[pts_cnt] = [x, y]
        pts_cnt +=1
        if pts_cnt == 4:
            print("4개 다 찍음")
            # 4개 다 찍으면
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)
            
            # 녹색 원의 좌표 (x, y) 획득
            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]
            
            pts1= np.float32([topLeft, topRight, bottomRight, bottomLeft]) # 변환 전 좌표
            
            #녹색 원들의 좌표간 거리 획득
            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            
            # 변환 후 이미지의 가로, 세로 크기
            width = max([w1, w2])
            height = max([h1, h2])
            
            pts2 = np.float32(([0,0], [width-1, 0], [width-1, height-1], [0, height-1])) #변환 후 좌표

            # 변환 행렬 획득 후 원근 변환 적용
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (int(width), int(height)))

            #result = cv2.warpPerspective(img, mtrx, (width, height)) #  문제 생김
            cv2.imshow('scanned', result)
            img = result
    return 0


#이미치 처리 함수
def ImgProcessing():
    global img
    # 이미지 파일 그레이 스케일로 변환
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 이미지 파일 음영 평준화
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    
    # 이미지 파일 가우시안블러 
    img = cv2.GaussianBlur(img, (3,3), 0)

    #이미지파일 오츠쓰래쉬홀드로 이산화 처리
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    #처리된 이미지 출력
    cv2.imshow("testing", img)
    
    #png 파일로 저장
    cv2.waitKey(0)
    cv2.imwrite('./images/processing.png', img)
    
    return img


#OCR 함수
def GetOCR():
    #이미지 불러오기
    global img
    ImgProcessing()

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(img, lang='kor+eng')
        
    return text


# 윈도우 창
cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, onMouse, param=None) 
cv2.imshow(win_name, img)   #이미지 출력
cv2.waitKey(0)              #입력 대기

text = GetOCR()             #OCR함수로 텍스트 추출
print(text)                 #텍스트 출력
```
점찍고 가우시안블
