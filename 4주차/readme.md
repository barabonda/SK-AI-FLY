# 강화학습
2024.01.08~2024.01.09
항상 기존의 것들을 기반으로 대체로 하기 때문에 알아야함
**story**
Goal
- 강화학습 중요개념
- Deep Q-learning 코드 이해
- Gym 기반 custom environment 구현
- 간단한 보드게임 학습시키기

  사람과 같은 조건에서 play<br/>
  이미지 보고 학습<br/>
  액션, 환경, 리워드<br/>
  만 정의하여 강화학습 agent 학습시킴<br/>
  모듈화를 머리속에서 생각<br/>

  아타리 게임
  <Agent> a1
  
  <Rom(Env) s1,s2
  r2
  
  S 관측할 수 있는 것

  return(value) 을 예측하도록 학습

  ## DQN 코드 이해
  Q: 왜 2개의 모델을 적용해야하는가?<br/>
  Q: Target-value?, Q - value?<br/>
  Q:histroy?<br/>
  Q: error는 어떻게 해결하는<br/>
  핵심 기술 이해보단 노하우를 많이 가지고있는게 전문가가 되는 길<br/>

  너무 명확한 데이터보다 경계선에 있는 애매한 데이터를 학습시켜야 정확도가 향상되지않을까?<br/>
  영화 엑스 마키나 추천<br/>
  - 알고리즘 적으로 관련 깊 재밌음 ㅋㅋ
  - 
fully Observaable environment
다 볼 수 있고 규칙까지 알려져있는 경우
Policy
- 에이전트가
Value Function
이 값이 얼마나 좋을지
합![image](https://github.com/barabonda/SK-AI-FLY/assets/108683454/23393fd2-10a0-4c51-8690-abbe375ad2ba)
자동차 입장에서 action 왼, 오
policy 
어떻게 카드

뉴럴네트워크는 경사하강법을 사용  
최적의 해를 찾는 것
기울기가 +일대는 늘리면 목적함수가 증가나고
기울기가 -일대는 늘리면 목적함수가 감소나고
직접 loss function을 구성하게 되면 항상 최소화가 아니라 최대화도 할 때가 있음<br/>
sgd, adam 등등 loss를 가정하고 짜는 알고리즘 즉, 기울기를 뺌<br/>  
앞에 -만 붙여주면 최대화  <br/>
optimizer.zero.grad()<br/>
배치를 모아서 한번에 업데이트 해주는 것 loss를 하나하
모델에서<br/>
X, Y는 상수<br/>
변수는 모델 파라미터<br/>
다하는건아니고<br/>
업스트림 다운스트림 메시지<br/>
돌아가기 위한 가능한 모든 미분값의 곱셈의 합산<br/>

토치의 텐서 정의  <br/>
옵티마이저 정의  <br/>
파이토치는 내부적으로 다 생성이 됌<br/>
안만들고싶으면 no_grad것 안에서 컴피티션을 만들어준다.<br/>
텐서플로우는 그건 아니고 만들어주고 정의할 필요가 있음<br/>
gradient 함수업데이트 api 차이?]==<br/>

현위치에서 어떤 방식으로 가야하는지가  회적의 해가 policy인데 
이걸 반복해서 최적의 해를 구하는 것이 policy이다.


강화학습에는 숫자가 많이 쓰이는거같다....!
방법론인가?
확률이 가장 높은 족으로 step해서 그러면 

주식 평균                                                                                                                                                                                     
Q러닝은 에피소드에 있는 액션이 아니라 액션그리디하게
나머지는 아무거입극가 사용 맥시멈 Qvalu

history(이전의 정) 컨텍스트 만 기억해도 강화학습에 대한
SARSA
웨이트 업뎃
리플렛버퍼
더블 큐러닝 자체는 오래됌
그걸 적용한 것이 16년도
H.Hasselt et al, Deep Reinforcement Learning with Double Q-learning AAAI| 2016
prioritized Experience Replay
**노하우가 중요**
key idea만 구현해서는 성능이 안나
sampling 이라던가 noise라던가  
이런 trick들이 적절하게 사용되야지만 성능이 나옴 튜닝테크닉과 트릭같은것이 없나!!  
커스텀 짐환경 만들고 로딩 액션을 반복적으로 호출하면서 골을 추출
달착륙선의 착지 조정법을 학습                    
                                       
atari  breakout
리니어모델 3개로 입력받고 출력 모델 4개
process
이미지를 cga뭐시기 하면 됌
