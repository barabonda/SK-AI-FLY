# pytorch  
  
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
