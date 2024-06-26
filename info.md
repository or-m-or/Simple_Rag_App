# RAG

## RAG 의 절차

1. Loading : 데이터가 있는 곳에서 파이프라인으로 데이터를 가져오는 것
2. Indexing : 데이터를 쿼리할 수 있는 데이터 구조를 만드는 것
3. Storing : 데이터가 색인(indexing)된 후에는 거의 항상 색인과 다른 메타데이터를 저장하여 다시 색인할 필요가 없도록 해야 합니다.
4. Querying : 주어진 인덱싱 전략에 따라 하위 쿼리, 다단계 쿼리, 하이브리드 전략 등 다양한 방법으로 LLM과 LlamaIndex 데이터 구조를 활용하여 쿼리할 수 있습니다.
5. Evaluation : 모든 파이프라인에서 중요한 단계는 다른 전략과 비교하여 얼마나 효과적인지 또는 변경할 때 얼마나 효과적인지 확인하는 것으로 쿼리에 대한 응답이 얼마나 정확하고 충실하며 빠른지에 대한 객관적인 척도를 제공

---

1. Using LLMs: OpenAI나 여러 개의 호스팅된 LLM 또는 로컬로 실행되는 자체 모델 등, 색인 및 저장부터 데이터 쿼리 및 구문 분석에 이르기까지 모든 단계에서 LLM이 사용됩니다. LlamaIndex에는 안정적이고 테스트를 거친 수많은 프롬프트가 제공되며, 직접 사용자 정의하는 방법도 알려드립니다.

2. Loading: 비정형 텍스트, PDF, 데이터베이스, 다른 애플리케이션에 대한 API 등 데이터가 어디에 있든 데이터를 가져옵니다. LlamaIndex에는 모든 데이터 소스에 대한 수백 개의 커넥터가 LlamaHub에 있습니다.

3. Indexing: 데이터를 확보한 후에는 애플리케이션이 항상 가장 관련성이 높은 데이터로 작업할 수 있도록 해당 데이터에 대한 액세스를 구조화할 수 있는 무한한 방법이 있습니다. LlamaIndex에는 이러한 수많은 전략이 내장되어 있으며 가장 적합한 전략을 선택하는 데 도움을 줄 수 있습니다.

4. Storing: 데이터를 인덱싱된 형태로 저장하거나 LLM에서 제공하는 사전 처리된 요약본을 벡터 스토어(아래 참조)라는 전문 데이터베이스에 저장하는 것이 더 효율적일 수 있습니다. 인덱스, 메타데이터 등을 저장할 수도 있습니다.

5. Querying: 모든 인덱싱 전략에는 그에 상응하는 쿼리 전략이 있으며, API와 같은 구조화된 응답으로 전환하는 것을 포함하여 검색 결과의 관련성, 속도 및 정확성을 향상시키고 이를 사용자에게 반환하기 전에 LLM이 수행하는 작업을 개선할 수 있는 다양한 방법이 있습니다.

6. 정리하자면, 질의응답, 챗봇, API 또는 자율 에이전트를 구축하든 관계없이 애플리케이션을 프로덕션에 적용하는 방법을 알려드립니다.

7. Tracig and debugging: 통합 가시성이라고도 하는 이 기능은 LLM 애플리케이션에서 특히 중요한데, 어떤 일이 일어나고 있는지 내부를 들여다보고 문제를 디버깅하고 개선할 부분을 찾아낼 수 있도록 도와줍니다.

8. Evaluating: 모든 전략에는 장단점이 있으며 애플리케이션을 구축, 출시 및 발전시키는 데 있어 핵심적인 부분은 변경 사항이 정확성, 성능, 명확성, 비용 등의 측면에서 애플리케이션을 개선했는지 평가하는 것입니다. 변경 사항을 안정적으로 평가하는 것은 LLM 애플리케이션 개발의 중요한 부분입니다.

## 각 절차의 중요 개념

1. Loading 단계
   - Documents : 모든 데이터 소스(예: PDF, API 출력 또는 데이터베이스에서 데이터 검색)를 둘러싼 컨테이너
   - Node : LlamaIndex에서 데이터의 원자 단위이며 소스 문서의 '청크', 노드에는 해당 노드가 속한 문서 및 다른 노드와 관련된 메타데이터가 있습니다.
   - Connectors : data connector(=Reader)는 다양한 데이터 소스와 데이터 포맷을 Documents와 Nodes로 수집함.
2. Indexing 단계
   - Indexes : 데이터를 수집한 후에는 데이터를 검색하기 쉬운 구조로 색인화합니다. 여기에는 일반적으로 벡터 테이터베이스에 저장되는 벡터 임베딩을 생성하는 작업이 포함됩니다. 인덱스에는 데이터에 대한 다양한 메타데이터도 저장할 수 있습니다.
   - Embedding : 데이터를 수치값으로 변환합니다. 관련성있는 데이터를 필터링할 때 LlamaIndex는 쿼리도 마찬가지로 임베딩으로 변환하고 Vector Store는 쿼리의 임베딩 값과 수치적으로 유사한 데이터를 찾습니다.
3. Querying 단계
   - Retrievers : 쿼리가 주어졌을 때 인덱스에서 관련 컨텍스트를 효율적으로 검색하는 방법을 정의합니다.
   - Routers : 라우터는 지식창고에서 관련성 있는 컨텍스트를 검색하는 데 사용할 리트리버를 결정합니다.
     구체적으로 RouterRetriever 클래스는 쿼리를 실행할 하나 또는 여러 개의 후보 리트리버를 선택하는 일을 담당합니다.
     이들은 selector을 사용하여 각 후보의 메타데이터와 쿼리를 기반으로 최상의 옵션을 선택합니다.
   - Node Postprocessors : 검색된 노드 집합을 가져와 변환, 필터링 또는 순위 재지정 로직을 적용합니다.
   - Response Synthesizers : 사용자 쿼리와 검색된 텍스트 청크의 주어진 세트를 사용하여 LLM에서 응답을 생성합니다.

---

1. Data Connectors : 기본 소스 및 형식에서 기존 데이터를 수집합니다. 여기에는 API, PDF, SQL 등이 포함될 수 있습니다.
2. Data Indexes : LLM이 사용하기 쉽고 성능이 우수한 중간 표현으로 데이터를 구조화합니다.
3. Engines : 데이터에 대한 자연어 액세스를 제공합니다.
   - Query Engines : 지식 증강 출력을 위한 강력한 검색 인터페이스입니다.
   - Chat Engines : 데이터와 '주고받는' 다중 메시지 상호작용을 위한 대화형 인터페이스입니다.
4. Data Agents : 간단한 helper, API 통합, 다양한 Tools를 이용한 LLM 기반의 강화된 지식 워커입니다.
5. Application Integrations : 라마인덱스를 나머지 에코시스템과 다시 연결합니다. 여기에는 LangChain, 플라스크, 도커, ChatGPT, 또는 그 밖의 모든 것이 포함될 수 있습니다!

## 데이터 기반 LLM 애플리케이션 사용 사례의 큰 범주

1. Query Engines : 데이터에 대해 질문할 수 있는 end-to-end 파이프라인입니다. 쿼리 엔진은 자연어 쿼리를 받아 검색된 참조 컨텍스트와 함께 응답을 반환하고 LLM에 전달합니다.
2. Chat Engines : 데이터와 대화하기 위한 엔드투엔드 파이프라인입니다(단일 질문과 답변이 아닌 여러 번의 주고받기).
3. Agents : 일련의 Tools를 통해 세상과 상호 작용하는 LLM으로 구동되는 자동화된 의사 결정자입니다. 에이전트는 주어진 작업을 완료하기 위해 임의의 단계를 수행하여 미리 정해진 단계를 따르지 않고 동적으로 최선의 조치를 결정할 수 있습니다. 따라서 더 복잡한 작업을 처리할 수 있는 추가적인 유연성을 제공합니다.
