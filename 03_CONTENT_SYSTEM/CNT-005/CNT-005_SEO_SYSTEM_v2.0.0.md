# JCOS v2.0.0 - CNT-005 SEO SYSTEM

## 범용 검색 의도·제목·메타데이터·탐색 경로 최적화 절차

| Field | Value |
|---|---|
| Document ID | CNT-005 |
| Title | SEO SYSTEM |
| Korean Title | 범용 검색 의도·제목·메타데이터·탐색 경로 최적화 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | Fact Check를 통과한 Canonical Content와 검색·탐색용 파생 필드 |
| Priority | HIGH |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~004 v2.0.0 LOCKED |
| Extends | SEO-001~SEO-030 |
| Depends On | COR-002 WRITING PRINCIPLES, COR-004 SOURCE POLICY, COR-005 QUALITY GATE, CNT-004 FACT CHECKING |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-005 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-005는 CNT-004의 Checked Candidate를 독자가 검색·탐색 과정에서 정확히 발견하고 이해할 수 있도록 검색 의도, 제목, 설명, 태그, URL 제안과 내부 연결을 최적화하는 표준 절차를 정의한다. 결과는 원문의 사실·범위·귀속·불확실성을 보존하면서 검수 가능한 SEO Candidate와 Publishing Handoff가 되어야 한다.

SEO는 노출을 위해 의미를 바꾸는 작업이 아니다. 검색 수요와 콘텐츠의 실제 답변 범위를 연결하고, 기대와 본문이 어긋나는 표현을 차단하며, 변경 근거와 파생 필드의 계보를 남기는 작업이다.

# 2. 범위와 비범위

## 2.1 포함 범위

- SEO Request와 Checked Candidate Binding
- 기준 콘텐츠 Snapshot과 Search Brief 생성
- 독자 질문·검색 의도·주제·용어 Candidate 분석
- Primary Topic과 Supporting Topic 선택
- 검색 제목·페이지 제목·설명·요약·태그 작성
- 제목 계층·내부 링크·Anchor·URL 제안 정합성
- 사실·Claim·Source·기준 시점 보존 검사
- 중복·Cannibalization·Variant 차이 검사
- SEO QA와 Publishing Handoff

## 2.2 비범위

- 새로운 사실·수치·인용·근거 생성 또는 Fact Verdict 변경
- 검색량·순위·트래픽·전환 성과의 보장
- 광고 집행·입찰·유료 키워드 운영
- 크롤러·서버·사이트맵·리디렉션·캐시의 기술 구현
- CMS 입력·예약 게시·배포·정정 공지
- 특정 검색 엔진의 비공개 알고리즘 추정이나 조작

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 문장·제목의 공통 정확성·명료성 | COR-002 WRITING PRINCIPLES |
| Source·Claim·근거 보존 | COR-004 SOURCE POLICY |
| 결함 등급·Gate 판정 | COR-005 QUALITY GATE |
| 독립 Fact Check와 Checked Candidate | CNT-004 FACT CHECKING |
| 검색 의도·제목·설명·태그·내부 탐색 | CNT-005 SEO SYSTEM |
| 공개·배포·정정·Release | CNT-006 PUBLISHING SYSTEM |
| 장기 성과·갱신·폐기 | CNT-007 LIFECYCLE SYSTEM |
| 프로젝트 고유 채널·문체·필드·제약 | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| SEO Request | 대상·목표 독자·채널·언어·기한·인계 대상을 지정한 요청 |
| Baseline Content | 최적화 시작 시 버전과 해시를 고정한 Checked Candidate |
| Search Brief | 독자 질문·의도·주제·범위·제약·완료 조건의 계약 |
| Search Intent | 사용자가 검색·탐색으로 해결하려는 정보·비교·행동 목적 |
| Primary Topic | 콘텐츠가 완전하고 정확하게 답하는 중심 주제 |
| Supporting Topic | 중심 주제를 보조하지만 독립 핵심으로 과장하지 않는 주제 |
| Search Title | 검색·목록 노출에 제안하는 제목 |
| Page Title | 실제 콘텐츠 상단에서 독자가 읽는 제목 |
| Description | 콘텐츠 범위와 가치를 사실적으로 요약한 탐색용 설명 |
| Tag Set | 분류·탐색을 위해 승인된 정규화 태그 묶음 |
| Internal Link | 같은 콘텐츠 체계 안의 관련 문서로 연결되는 링크 |
| SEO Candidate | SEO QA를 통과해 Publishing에 인계 가능한 콘텐츠와 파생 필드 묶음 |

# 4. 입력 계약과 최적화 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| seo_request_id | SEO 실행 고유 식별자 |
| target_content_ref | Checked Candidate 위치·버전·해시 |
| fact_check_handoff_ref | CNT-004 Content Ready Handoff 위치 |
| audience_and_need | 목표 독자와 해결할 질문 |
| channel_contract | 허용 필드·길이·형식·금지 항목 |
| language_and_locale | 언어·지역·표기 기준 |
| taxonomy_ref | 승인된 Category·Tag·용어 체계 |
| related_content_index | 내부 링크와 중복 검사 대상 목록 |
| binding | 적용 기준본 ID·버전·상태 |

필수 입력이 없거나 여러 Candidate가 기준으로 제시되면 하나를 임의 선택하지 않는다. 결과의 의미나 대상 독자를 바꿀 수 있는 누락은 `BLOCKED` 또는 Query로 처리한다.

## 4.2 최적화 상태

| 상태 | 의미 |
|---|---|
| READY | 요청·Binding·Baseline 확인 완료 |
| INTENT_ANALYSIS | 독자 질문·의도·주제 분석 중 |
| FIELD_OPTIMIZATION | 제목·설명·태그·링크 작성 중 |
| QUERY | 의미·범위·분류·중복 결정 대기 |
| SEO_QA | SEO Gate 검수 중 |
| PUBLISHING_READY | SEO Candidate와 인계물 준비 완료 |
| BLOCKED | 필수 입력·근거·결정 부재로 중단 |
| SUPERSEDED | 새 콘텐츠 또는 SEO 실행으로 대체됨 |

# 5. 표준 SEO 수명주기

1. SEO Request를 등록하고 대상 Checked Candidate를 식별한다.
2. 적용 기준본·채널 계약·분류 체계를 Binding한다.
3. CNT-004 Handoff와 Fact Check Report를 확인한다.
4. Candidate 버전·해시를 Baseline으로 고정한다.
5. 독자 질문과 실제 검색·탐색 의도를 정의한다.
6. 본문이 완전하게 답하는 Primary Topic을 선택한다.
7. Supporting Topic과 제외 주제를 기록한다.
8. Search Title·Page Title·Description 후보를 작성한다.
9. Category·Tag·URL·내부 링크 후보를 정리한다.
10. 제목 계층과 Anchor의 설명 가능성을 검사한다.
11. Claim·귀속·조건·불확실성·기준 시점을 원문과 대조한다.
12. 중복·Cannibalization·Variant 정합성을 검사한다.
13. SEO QA를 수행하고 SEO Candidate를 고정한다.
14. Candidate·필드·근거·제한·QA를 CNT-006에 인계한다.

키워드나 제목을 먼저 고른 뒤 본문을 그 표현에 맞춰 왜곡하지 않는다. Baseline이 의미 변경을 필요로 하면 SEO 단계에서 직접 확정하지 않고 Writer·Editor·Fact Checker·Owner에게 Query한다.

# 6. Preflight와 Baseline

## 6.1 Checked Candidate 확인

CNT-004가 `CONTENT_READY`로 인계한 하나의 Checked Candidate를 확인한다. Content ID·버전·해시·언어·Variant 관계와 Fact Check 기준 시점을 기록한다.

## 6.2 인계물 확인

- Fact Check Request와 적용 Binding
- Baseline Candidate와 Checked Candidate
- Claim Inventory와 현재 Verdict
- Source Records와 재확인 조건
- Finding·Correction·Recheck Log
- Variant Impact Map과 Fact Check QA

## 6.3 SEO Baseline

최적화 전 Checked Candidate를 덮어쓰지 않고 보존한다. SEO 파생 필드와 변경 기록은 이 Baseline을 기준으로 비교할 수 있어야 한다.

# 7. Search Brief와 의도

## 7.1 Search Brief

| 필드 | 내용 |
|---|---|
| audience | 콘텐츠를 찾는 주 대상 |
| user_question | 독자가 해결하려는 구체적 질문 |
| intent_type | INFORMATIONAL·COMPARISON·NAVIGATIONAL·ACTION_SUPPORT |
| expected_answer | 본문이 실제 제공하는 답의 범위 |
| primary_topic | 중심 주제와 정규화 표현 |
| exclusions | 다루지 않거나 보장하지 않는 내용 |
| locale | 언어·지역·시점 조건 |
| completion_criteria | PUBLISHING_READY 통과 조건 |

## 7.2 의도와 답변 일치

독자가 기대하는 질문과 본문이 실제 제공하는 답을 대조한다. 제목이나 설명이 본문보다 더 넓은 문제 해결, 최신성, 완전성 또는 성과를 약속하지 않아야 한다.

## 7.3 의도 분리

서로 다른 독자 목적을 하나의 콘텐츠에 억지로 결합하지 않는다. 중심 의도 밖의 주제는 Supporting Topic 또는 별도 콘텐츠 후보로 기록하되 이 문서에서 신규 콘텐츠 제작 범위를 확장하지 않는다.

# 8. Topic과 용어 선택

## 8.1 Primary Topic

Primary Topic은 본문의 핵심 Claim과 섹션 다수가 직접 답하고 있어야 한다. 검색 수요가 있어도 본문이 충분히 설명하지 못하면 중심 주제로 선택하지 않는다.

## 8.2 Supporting Topic

Supporting Topic은 실제 본문 위치와 역할을 가진다. 단순 언급, Source 이름, 장식적 표현을 독립 주제로 과장하지 않는다.

## 8.3 용어 정규화

독자가 쓰는 표현과 프로젝트의 승인 용어를 함께 고려한다. 동의어·약어·번역어는 첫 사용 정의와 의미 차이를 보존하며 무관한 반복 삽입을 하지 않는다.

# 9. 제목과 설명

## 9.1 Search Title

Search Title은 중심 주제, 독자 가치와 구분 요소를 간결하게 담고 본문 범위 안에서 작성한다. 클릭을 유도하기 위해 결과·숫자·최신성·권위를 과장하지 않는다.

## 9.2 Page Title과 제목 계층

Page Title은 콘텐츠의 실제 목적을 명확히 표현하고 Search Title과 의미가 일치해야 한다. 하위 제목은 섹션 역할과 포함 관계를 반영하며 Primary Topic을 기계적으로 반복하지 않는다.

## 9.3 Description

Description은 누가 무엇을 얻는지와 중요한 범위·조건을 사실적으로 요약한다. 본문에 없는 혜택, 보장, 비교 우위 또는 긴급성을 추가하지 않는다.

## 9.4 길이와 잘림

채널 길이는 입력 계약으로 받되 임의의 보편적 글자 수를 규범으로 고정하지 않는다. 잘릴 가능성이 있으면 핵심 의미를 앞에 두고 잘림 후에도 오해가 생기지 않는지 검사한다.

# 10. Category·Tag·URL

## 10.1 Category

Category는 승인된 Taxonomy에서 콘텐츠의 주 역할을 나타내는 가장 구체적인 유효 항목을 선택한다. 여러 범주를 노출 확대 목적으로 중복 지정하지 않는다.

## 10.2 Tag Set

Tag는 실제 본문 주제와 탐색 가치가 있는 정규화 항목만 사용한다. 동의어·복수형·철자 변형을 별도 태그로 중복 생성하지 않는다.

## 10.3 URL 제안

URL은 사람이 의미를 추정할 수 있는 안정적인 식별 제안을 만든다. 게시 경로 확정, 기존 URL 변경과 Redirect 실행은 CNT-006 책임이며 SEO 단계에서 직접 시행하지 않는다.

# 11. 내부 탐색과 링크

## 11.1 내부 링크 적합성

내부 링크는 현재 문맥의 독자 질문을 실제로 보완하는 유효 콘텐츠로 연결한다. 순위 목적의 무관한 링크나 동일 목적지 반복을 추가하지 않는다.

## 11.2 Anchor

Anchor는 목적지 내용과 관계를 설명하며 `여기`, `자세히` 같은 단독 표현에 의존하지 않는다. 목적지 제목을 과장하거나 현재 문장의 Claim 근거처럼 오인시키지 않는다.

## 11.3 링크 상태

제안한 목적지가 존재하고 접근 가능하며 언어·지역·버전이 적합한지 확인한다. 게시 시점의 최종 링크 검사와 Redirect 판정은 CNT-006에 인계한다.

# 12. 의미·사실 보호

## 12.1 Claim 보존

검색 필드는 Checked Candidate의 Claim 범위·강도·대상·기간·조건·예외를 보존해야 한다. VERIFIED 일부만 취해 더 넓은 결론으로 만들지 않는다.

## 12.2 귀속과 불확실성

ATTRIBUTED_CLAIM, PARTIAL, UNVERIFIED, CONFLICT, 전망과 재확인 조건을 삭제하지 않는다. 제목 공간이 부족하면 단정으로 바꾸지 말고 대체 표현 또는 Query를 사용한다.

## 12.3 최신성 표현

`최신`, `현재`, 연도와 버전 표현은 Baseline의 기준 시점과 재확인 조건이 있을 때만 사용한다. 게시 전 재검증이 필요한 표현은 Handoff에 명시한다.

# 13. 중복·Cannibalization·Variant

## 13.1 중복 콘텐츠

Related Content Index에서 동일 질문·대상·답변 범위를 가진 기존 콘텐츠를 확인한다. 신규 Candidate의 고유 가치가 없으면 병합·갱신·대체 여부를 Owner에게 Query한다.

## 13.2 Topic 충돌

여러 콘텐츠가 같은 Primary Topic을 가질 수 있으나 독자 질문·범위·시점·형식의 구분이 명확해야 한다. 단순히 다른 제목을 붙여 중복을 숨기지 않는다.

## 13.3 Variant 정합성

채널 Variant의 제목·설명·태그는 각 본문의 실제 범위와 일치해야 한다. Canonical의 키워드를 본문에 없는 Variant에 그대로 복사하지 않는다.

# 14. 변경과 Query 통제

## 14.1 SEO Change Record

Search Title·Page Title·Description·Category·Tag·URL·Link의 변경 전·후, 이유, 적용 Rule, 영향받는 Variant와 승인 상태를 기록한다.

## 14.2 Semantic Query

최적화를 위해 본문 Claim, 구조, 사실 상태 또는 핵심 메시지 변경이 필요하면 직접 수정하지 않는다. Writer·Editor·Fact Checker·Owner에게 Query하고 승인된 새 Baseline을 받은 뒤 재검사한다.

## 14.3 Accepted Risk

길이 잘림, Taxonomy 공백, 중복 가능성처럼 해결하지 않고 인계하는 항목은 승인 주체·사유·영향·재검토 조건을 가진다. 허위·과장·중대한 의미 불일치는 Accepted Risk로 우회할 수 없다.

# 15. Publishing Handoff

## 15.1 필수 인계물

| 인계물 | 최소 내용 |
|---|---|
| SEO Request | 대상·독자·채널·언어·기한 |
| Binding | 적용 기준본 ID·버전·상태 |
| Baseline Content | 최적화 전 버전·해시 |
| SEO Candidate | 본문과 승인된 파생 필드·버전·해시 |
| Search Brief | 의도·Primary Topic·범위·제외 |
| SEO Field Set | 제목·설명·Category·Tag·URL 제안 |
| Link Map | 내부 링크·Anchor·목적지·검사 상태 |
| Change and Query Log | 변경·결정·Accepted Risk |
| SEO QA | Gate 판정·결함·제한·재확인 조건 |

## 15.2 인계 조건

- SEO Candidate가 하나로 식별된다.
- Primary Topic과 독자 질문이 본문 범위에 맞는다.
- 제목·설명·태그·링크가 Claim과 Fact Verdict를 보존한다.
- 열린 Critical SEO Issue와 Semantic Query가 없다.
- 중복·Variant·Taxonomy 검사가 완료됐다.
- 게시 직전 재확인할 날짜·링크·필드가 공개돼 있다.

`PUBLISHING_READY`는 공개 승인, 게시 완료, 검색 노출, 순위 또는 성과를 의미하지 않는다.

# 16. SEO QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 대상·독자·채널·언어·기한 추적 가능 |
| G2 Baseline | Checked Candidate·버전·해시 고정 |
| G3 Intent | 독자 질문·의도·답변 범위 정합 |
| G4 Topic | Primary·Supporting Topic과 본문 근거 정합 |
| G5 Fields | 제목·설명·Category·Tag·URL 계약 정합 |
| G6 Links | 내부 링크·Anchor·목적지 유효성 |
| G7 Meaning | Claim·귀속·조건·불확실성·시점 보존 |
| G8 Handoff | Candidate·필드·변경·제한·QA 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 뒤의 두 상태는 PASS로 계산하지 않는다.

## 16.2 Critical 결함

- 제목·설명이 본문에 없는 사실·성과·최신성·보장을 주장함
- Fact Verdict의 조건·귀속·불확실성을 제거해 의미를 바꿈
- Primary Topic이 본문의 실제 답변 범위와 다름
- 다른 콘텐츠 또는 조직·인물을 사칭하거나 오인시키는 필드 사용
- 여러 Candidate 중 Publishing 대상 SEO Candidate를 식별할 수 없음
- 내부 전용 정보·미승인 문구·Credential이 공개 필드에 남음

Critical 결함이 열려 있으면 `PUBLISHING_READY`로 표시하지 않는다.

# 17. 실행 규칙 (SEO-001 ~ SEO-030)

## 17.A 요청과 Baseline (SEO-001 ~ SEO-005)

### SEO-001 - SEO 요청 식별
- **Statement:** 모든 SEO 실행은 고유 seo_request_id, 대상 콘텐츠, 독자와 채널 범위를 가져야 한다.
- **Verification:** SEO Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### SEO-002 - 기준본 Binding
- **Statement:** 최적화 전에 적용할 Core·Content·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding과 실제 기준 파일을 대조한다.
- **Exceptions:** 없음.

### SEO-003 - Baseline 단일성
- **Statement:** 하나의 Checked Candidate를 ID·버전·해시로 Baseline에 고정해야 한다.
- **Verification:** target_content_ref와 실제 파일 해시를 확인한다.
- **Exceptions:** 병렬 언어본은 각각의 Baseline과 관계를 명시한다.

### SEO-004 - Fact Check Handoff
- **Statement:** CNT-004 Handoff의 Candidate·Claim Verdict·Source·Correction·Variant·QA를 확인해야 한다.
- **Verification:** fact_check_handoff_ref와 manifest를 검사한다.
- **Exceptions:** 없음.

### SEO-005 - 채널 계약 우선
- **Statement:** 제목·설명·태그·URL·링크 필드는 명시된 channel_contract 안에서 작성해야 한다.
- **Verification:** 필드 형식·허용 수·길이·금지 항목을 대조한다.
- **Exceptions:** 계약이 없으면 보편적 제한을 추정하지 않고 Query한다.

## 17.B 의도와 Topic (SEO-006 ~ SEO-010)

### SEO-006 - 독자 질문 명시
- **Statement:** SEO Candidate는 목표 독자와 해결할 하나의 중심 질문을 가져야 한다.
- **Verification:** Search Brief와 본문의 핵심 답변을 대조한다.
- **Exceptions:** 비교 콘텐츠는 하나의 비교 질문 아래 복수 대상을 가질 수 있다.

### SEO-007 - 의도·답변 일치
- **Statement:** 검색 의도가 기대하는 답과 본문이 실제 제공하는 답의 범위가 일치해야 한다.
- **Verification:** expected_answer와 섹션·Claim을 대조한다.
- **Exceptions:** 없음.

### SEO-008 - Primary Topic 근거
- **Statement:** Primary Topic은 본문의 핵심 Claim과 주요 섹션이 직접 다뤄야 한다.
- **Verification:** Topic-to-Section Map을 검사한다.
- **Exceptions:** 없음.

### SEO-009 - Supporting Topic 제한
- **Statement:** Supporting Topic은 실제 본문 위치를 가지며 중심 주제로 과장되지 않아야 한다.
- **Verification:** 각 Topic의 위치·역할·노출 필드를 확인한다.
- **Exceptions:** 단순 인용·Source 이름은 탐색 가치가 있을 때만 Topic으로 둔다.

### SEO-010 - 용어 자연성
- **Statement:** 검색 용어는 의미와 문법을 해치지 않는 자연스러운 위치에서만 사용해야 한다.
- **Verification:** 제목·설명·본문에서 반복·변형·문맥을 검사한다.
- **Exceptions:** 규정된 공식 명칭과 코드 값은 원형을 유지한다.

## 17.C 제목·설명·분류 (SEO-011 ~ SEO-015)

### SEO-011 - Search Title 정확성
- **Statement:** Search Title은 본문 범위 안에서 중심 주제와 구분 가치를 사실적으로 표현해야 한다.
- **Verification:** Title Claim과 Baseline Claim을 대조한다.
- **Exceptions:** 없음.

### SEO-012 - Page Title 정합성
- **Statement:** Page Title과 Search Title은 표현이 달라도 동일한 콘텐츠 목적과 범위를 가리켜야 한다.
- **Verification:** 두 제목의 대상·행동·조건·시점을 비교한다.
- **Exceptions:** 채널 제약에 따른 축약은 의미를 보존한다.

### SEO-013 - Description 진실성
- **Statement:** Description은 본문에 없는 혜택·보장·비교 우위·긴급성을 추가하지 않아야 한다.
- **Verification:** Description의 각 Claim을 Baseline과 대조한다.
- **Exceptions:** 없음.

### SEO-014 - Taxonomy 정규화
- **Statement:** Category와 Tag는 승인된 Taxonomy의 정규 항목을 사용하고 동의어 중복을 만들지 않아야 한다.
- **Verification:** taxonomy_ref와 Field Set을 대조한다.
- **Exceptions:** 신규 항목은 Owner 승인 전 후보 상태로만 기록한다.

### SEO-015 - URL 제안 안정성
- **Statement:** URL 제안은 콘텐츠 식별에 필요한 안정적 의미만 포함하고 변경 가능한 과장 표현을 피해야 한다.
- **Verification:** URL 토큰과 Primary Topic·버전 정책을 검사한다.
- **Exceptions:** 실제 경로와 Redirect 결정은 CNT-006에 인계한다.

## 17.D 탐색·링크·중복 (SEO-016 ~ SEO-020)

### SEO-016 - 내부 링크 관련성
- **Statement:** 내부 링크는 현재 문맥의 독자 질문을 실제로 보완하는 유효 목적지로 연결해야 한다.
- **Verification:** Source 문맥·Anchor·목적지 내용을 대조한다.
- **Exceptions:** 필수 정책·법적 고지 링크는 탐색 목적과 별도로 둘 수 있다.

### SEO-017 - Anchor 설명성
- **Statement:** Anchor는 목적지 내용과 관계를 자체적으로 설명해야 한다.
- **Verification:** Anchor만 읽어도 목적지 역할을 구분할 수 있는지 검사한다.
- **Exceptions:** 주변 문장과 결합해 명확한 경우 접근성 기준 안에서 허용한다.

### SEO-018 - 링크 상태 확인
- **Statement:** 제안 링크의 존재·접근·언어·지역·버전 적합성을 확인해야 한다.
- **Verification:** Link Map과 실제 목적지를 검사한다.
- **Exceptions:** 미공개 예정 목적지는 상태와 게시 선행 조건을 기록한다.

### SEO-019 - 중복 범위 검사
- **Statement:** 동일 질문·대상·답변 범위의 기존 콘텐츠와 중복 여부를 확인해야 한다.
- **Verification:** related_content_index와 Search Brief를 비교한다.
- **Exceptions:** 시점·지역·형식이 다른 경우 차이를 명시한다.

### SEO-020 - Topic 구분
- **Statement:** 같은 Primary Topic을 가진 콘텐츠는 독자 질문·범위·시점·형식 중 하나 이상의 명확한 구분을 가져야 한다.
- **Verification:** Topic Portfolio Map을 검사한다.
- **Exceptions:** 대체·통합 예정 콘텐츠는 상태와 Canonical 대상을 기록한다.

## 17.E 의미·변경·Variant (SEO-021 ~ SEO-025)

### SEO-021 - Claim 의미 보존
- **Statement:** SEO 필드는 Checked Candidate의 Claim 범위·강도·대상·기간·조건·예외를 바꾸지 않아야 한다.
- **Verification:** Field-to-Claim Trace를 검사한다.
- **Exceptions:** 없음.

### SEO-022 - 귀속·불확실성 보존
- **Statement:** 귀속, PARTIAL·UNVERIFIED·CONFLICT, 전망과 재확인 조건을 삭제해 확정 사실처럼 만들지 않아야 한다.
- **Verification:** Fact Check Report와 제목·설명·요약을 대조한다.
- **Exceptions:** 공간 제약 시 오해 없는 대체 표현을 사용하거나 필드를 보류한다.

### SEO-023 - 최신성 근거
- **Statement:** 최신·현재·연도·버전 표현은 확인된 기준 시점과 재검증 조건을 가져야 한다.
- **Verification:** 표현과 as_of·Source 상태를 대조한다.
- **Exceptions:** 변경 가능성이 없는 역사적 연도는 재검증 조건이 필요하지 않다.

### SEO-024 - Semantic Query
- **Statement:** SEO 목적의 의미·사실·구조 변경은 직접 확정하지 않고 책임자에게 Query해야 한다.
- **Verification:** Change Log에서 Semantic Change의 decision_ref를 확인한다.
- **Exceptions:** 의미를 보존한 승인 범위 내 표기 변경은 직접 수행할 수 있다.

### SEO-025 - Variant 범위 일치
- **Statement:** 각 Variant의 SEO 필드는 해당 Variant 본문의 실제 범위와 일치해야 한다.
- **Verification:** Canonical·Variant Field Set과 생략 내용을 비교한다.
- **Exceptions:** 채널 고정 필드는 계약과 차이를 기록한다.

## 17.F QA와 인계 (SEO-026 ~ SEO-030)

### SEO-026 - SEO Change 추적
- **Statement:** 주요 SEO 필드 변경은 전·후·이유·Rule·Variant 영향·승인 상태를 기록해야 한다.
- **Verification:** SEO Change Record와 결과 필드를 대조한다.
- **Exceptions:** 동일 규칙의 반복 정규화는 범위를 명시해 묶어 기록할 수 있다.

### SEO-027 - Critical Gate
- **Statement:** 허위·과장·의미 변경·대상 오인 Critical 결함이 있으면 PUBLISHING_READY Gate는 FAIL이어야 한다.
- **Verification:** Issue Log·Field Set·Gate 결과를 대조한다.
- **Exceptions:** 없음.

### SEO-028 - 필드 완결성
- **Statement:** 채널 계약이 요구하는 모든 SEO 필드는 값 또는 승인된 제외 사유를 가져야 한다.
- **Verification:** channel_contract와 SEO Field Set을 검사한다.
- **Exceptions:** NOT_APPLICABLE은 근거와 승인자를 기록한다.

### SEO-029 - 후속 승인 분리
- **Statement:** PUBLISHING_READY를 공개 승인·게시 완료·검색 노출·순위 또는 성과 보장으로 해석하지 않아야 한다.
- **Verification:** 상태 정의와 Handoff 문구를 확인한다.
- **Exceptions:** 없음.

### SEO-030 - SEO 계보 보존
- **Statement:** Baseline Content부터 SEO Candidate까지 Topic·필드·링크·변경·QA 계보를 재현할 수 있어야 한다.
- **Verification:** ID·버전·해시·참조와 Change Record를 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 SEO System

```text
1. seo_request_id, Checked Candidate ID·버전·해시, 독자·채널·언어와 Binding을 고정한다.
2. CNT-004 Handoff의 Claim Verdict·Source·Correction·Variant·QA를 확인한다.
3. Baseline을 보존하고 독자 질문·의도·실제 답변 범위를 Search Brief에 기록한다.
4. 본문이 충분히 답하는 하나의 Primary Topic과 Supporting Topic·제외 범위를 정한다.
5. Search Title·Page Title·Description은 본문 범위와 Claim 강도를 넘지 않게 작성한다.
6. Category·Tag는 승인 Taxonomy를 사용하고 동의어·철자 변형 중복을 만들지 않는다.
7. URL은 안정적 제안만 만들며 실제 경로·Redirect 실행은 Publishing에 인계한다.
8. 내부 링크는 관련 목적지로 연결하고 Anchor가 관계를 설명하도록 한다.
9. 귀속·조건·불확실성·기준 시점과 Fact Verdict를 모든 검색 필드에서 보존한다.
10. 중복·Topic 충돌과 Canonical·Variant 필드 범위를 대조한다.
11. 의미 변경은 책임자에게 Query하고 필드 변경 전후·이유·영향·승인을 기록한다.
12. Critical 결함이 없을 때 Candidate·Field Set·Link Map·제한·QA를 CNT-006에 인계한다.
```

이 압축 블록은 상세 System의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-005는 사실 검증된 콘텐츠의 검색 의도·제목·설명·분류·탐색 경로와 기록 계약만 정의한다.
- 새 조사와 Fact Verdict 변경은 CNT-001·004에 반환한다.
- 핵심 메시지·구조·문장 의미 변경은 CNT-002·003과 Owner 승인 경로를 따른다.
- 게시 경로·Redirect·공개·배포·정정은 CNT-006이 맡는다.
- 장기 성과 측정과 갱신·통합·폐기는 CNT-007이 맡는다.

## 19.2 알려진 제한

- 모든 채널에 같은 제목·설명 길이, 태그 수 또는 URL 형식을 강제하지 않는다.
- 검색 노출·순위·트래픽·전환 또는 검색 엔진 색인을 보장하지 않는다.
- 자동 키워드·요약·모델 추천은 독자 의도와 본문 일치를 보증하지 않는다.
- 검색 플랫폼의 비공개 알고리즘과 향후 정책 변경을 예측하지 않는다.
- Project 고유 Taxonomy·금지어·채널 필드는 해당 Project 문서가 구체화한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 SEO 입력·Baseline·Search Brief·Intent·Topic·Title·Description·Taxonomy·Link·Meaning·Duplicate·Variant·QA·Publishing Handoff와 SEO-001~030 작성; 사용자 명시적 승인 반영 |
