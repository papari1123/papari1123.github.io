QA - 질의 응답
     - BERT, pretrained model
     - MLC, SQuaD, GPT, causal language model
     * ODQA
        - open domain question answering
        - 이전 LM들은 질의어를 키워드 들의 나열, 조합으로 생각
        - 특정 정보를 catch
        - relevant context(answer가 포함된 글)가 없을 경우의 task
        - external knowledge에서 context를 가져옴 (ex. wikipedia)
        (* relevant context가 있는 경우, (context에 제한이 있는 경우) closed domain)
        - methods
          - REALM : pre-training corpus를 적용
            (REtrieval Augment Language Model)
            - 질문과 답 pair를 annotating해서 corpus를 구축
            - labeld 된 dataset으로 supervised learning
            - Maksed Language Modeling
            - 중간 과정에서 answer가 포함될 것 같은 context를 retrieve
            - Maksed된 문장과의 내적 값이 가장 큰 문서를 retrieve, Neural Knowledge Retriever
            - Retriever도 학습
            - 오리지날 문장과 검색된 문장을 concat해서 학습 진행
            - pretrain 된 transformer 기반 모델을 question-answer pair로 fine-tuning
         - ConceptNet
            - Fusing Context into Knowledge Graph
            - Knowledge graph 형태로 된 지식 구조체를 사용
            - 관계망, 단어들 간의 관계를 tagging 하여 망 형태로 표현
            - 답이 있을 것이라고 생각되는 Knowledge sub-graph를 추출
            - sub-graph 내의 단어와 관계들을 하나의 sequence(contiguous representation)로 주고 
              ALBERT (pretrained model)에 질문과 함께 입력하여 답을 구함
            - ALBERT
               - BERT 모델 경량화, overfitting 방지
               - input data 형태는 Question에 대한 answer가 4지 선다(candidate, choice)로 주어진 data
               - 각 choice 마다 문장 만들어서 입력
                  ->[CLS] output -> FC -> softmax(a,b,c,d) -> 4개 중 하나의 정답지를 예측 (multi class classification)
               - 입력에 사전의 설명 글까지도 같이 포함
            - DEKCOR 라는 모델, 지금까지도 괜찮은 성능

Open-domain Chatbot
  - closed domain이 아니기 때문에 응답이 제한적이지 않음
  - Blender Bot 2.0
    -seq2seq 기반의 Transformer 모델
    -internet search based + memory search based
    -인터넷에서 문서를 추출 + long term memory

NMT - Neural Machine Translation
       - supervised data(target이 명확한 data)로 학습
       - Unsupervised NMT
          - supervised paired dataset, parallel corpus(병렬 코퍼스) 사용 X
          - 번역 쌍에 대한 정보가 없는 상태에서도 번역 task를 어떻게 수행할 수 있을 것인가?
          - * Back-translation <-> Cycle loss
              - 번역 모델을 2개를 둠, 2개의 모델을 동시에 학습
              -> 영어 문장 하나 뽑아오고
              -> 번역된 문장 뽑아주고 (번역, 1개의 모델)
              -> 다시 원 언어의 문장으로 번역 (재번역, 또 다른 모델)
              -> 원래 문장과 동일한 문장이 나오느냐!
              -> 이 부분에서(input, output 문장 간의 차이) loss 계산 해서 학습
              - 직접적인 label 데이터가 없을 때 유용하게 사용될 수 있음

Text Style Transfer
  - seq2seq? Transformer 기반
  - 주어진 문장이 있을 때, 문장의 뜻은 유지하고 스타일만 바꿔주는 것
  (ex. 안녕히 주무세요 -> 잘 자, 굿 밤 etc..)
  - 부정 논조 -> 긍정 논조 
  - style을 분리할 수 있냐 -> disentanglement / entanglement
     - 어느 부분을 바꿔야 하고 어느 부분을 잘 유지해야 하냐

Lexically-constrained NMT
  - 어휘-제한적 NMT
  - 특정 도메인에 특화된 모델
  - 생뚱 맞게 번역되지 않고 원하는 형태로 번역하는 방법
  - source term -> target term / source term을 target term으로 변환
    - cross attention을 할 때, source term 단어의 attention score가 가장 컸을 때
      해당 단어의 output을 source term 단어 대신 target term의 단어로 뽑아줌
  - 다양한 방법론
  - External Knowledge(용어 레벨의 번역집, 풀어 설명하신 부분)를 만들어서 사용

Quality Estimation
  - 자연스럽냐 그럴 듯하냐

Large-scale Language Models
  - 생성 모델이 여전히 challenging하고 평가가 중요

In-Context Learning
  - GPT-3, zero-shot learning (지시어를 줬을 때 바로 답을 출력)
  - few-shot learning의 성능을 사용 가능한 수준으로 끌어올림
    - 지시어와 몇 개의 사례를 주고 답을 출력
    - task description / examples / prompt
       - Prompt tuning
         - prompt를 어떻게 구성할 것이냐
         - 모델은 건드리지 않고 입력 Text를 바꿔서 성능을 올리고자 하는 방법론
    - GPT-3, label 된 training 데이터를 생성하는 데도 사용됨

동향 - 모델 거대해지고 있고 설명 가능성과 정당성 제시 중요
      - interactive하게 task를 수행할 수 있는지, 더 많은 단계
      - MLOps
        - 기존 : 최적 모델을 찾아내고 architecture 손보는 일
        - MLOps : 데이터 수집 정제 레이블링부터 서비스까지 한 후 결과를 보고 다시 문제점 도출하고
                      다시 데이터 수집 과정에 반영하고 하는 전체 사이클, 파이프라인을 다루는 기술

사전 질문

Q. KNLP issue & 산업 및 학계 전망
A. 한국어라고 특별히 어렵거나 다른 점은 많이 없다.
    Large scale pretrained LM, 영어 위주로 많이 진행
    Multi-lingual model 제공, 써보면 아쉬운 부분이 있다.
    한글 데이터에 특화한 fast follower에 역량이 집중될 필요 느껴
    여전히 산업 및 학계 전망은 좋음.
    CV, NLP 양대 산맥인데 NLP가 수요가 많지만 인력이 상대적으로 많이 없어
    연구는 쉽지 않은 부분도 있다. Large scale pretrained model에 많이 의존하는 점이 아쉽다.

Q. 연구실 선발 기준
A. 학점은 변별력이 적다. 논문 실적 Big Plus, 학부 연구생 경험도 중요.
    케미랑 코드가 맞는 것.
    미리부터 교수님이나 선배들과 교류 기회를 가지는 것이 좋아 보인다.
    학점은 전체 학점, filtering의 용도, 지원자가 많은 경우.

Q. 학부 졸업생 경쟁력
A. 효과를 극대화, 효율화할 수 있는 방안을 찾아보길
    그룹 스터디, 도움을 많이 받을 수 있는 환경을 적극적으로 좇아다니는 것도 좋을 듯
    외부적인 스펙, 경진 대회나 인턴 경험 잘 쌓아두는 것도 의미 있을 듯
    혼자하는 일은 없고 팀 단위로 하는 경우가 많다, 프로젝트 내의 역할을 resume에 잘 명시하시길
    
Q. 강의 준비 방식, 공부법
A. 공부법 - study group, 최신 기술에 노출되는 것이 중요, youtube 논문 리뷰
    simple한 예시를 만들어서 공부하고 강의 준비, 명확하게 전달하는 방법을 강구



