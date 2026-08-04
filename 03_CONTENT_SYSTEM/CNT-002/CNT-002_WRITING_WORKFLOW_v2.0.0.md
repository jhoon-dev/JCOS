# JCOS v2.0.0 - CNT-002 WRITING WORKFLOW

## 범용 원고 설계·작성·인계 절차

| Field | Value |
|---|---|
| Document ID | CNT-002 |
| Title | WRITING WORKFLOW |
| Korean Title | 범용 원고 설계·작성·인계 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | JCOS의 기사·보고서·가이드·비교·분석·프로젝트 콘텐츠 원고 작성 |
| Priority | HIGH |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001 v2.0.0 LOCKED |
| Extends | COR-002 WRT-001~050 |
| Depends On | COR-002 WRITING PRINCIPLES, COR-004 SOURCE POLICY, COR-005 QUALITY GATE, CNT-001 RESEARCH WORKFLOW |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-002 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-002는 조사 결과와 프로젝트 계약을 독자가 이해하고 사용할 수 있는 원고로 변환하는 표준 실행 절차를 정의한다. 같은 Brief, Claim Map과 Output Contract를 받은 다른 사람 또는 AI가 메시지 선택, 구조, 문장과 근거 연결을 재현할 수 있어야 한다.

이 문서는 좋은 문장의 원칙보다 어떤 입력을 확인하고 어떤 순서로 원고를 설계·작성·자체 검수해 편집 단계에 넘길지를 다룬다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Writing Request와 기준본 Binding
- Research Handoff 및 Claim 사용 가능성 확인
- 독자·목적·채널·언어·분량·Schema 계약
- Message Map과 Outline 설계
- 제목·리드·본문·요약·결론 초안
- Claim·Source·표현의 추적성 유지
- 사실·귀속 주장·해석·전망·불확실성의 문장화
- 가변 Cardinality와 채널 Variant 작성
- 자체 Writing QA와 Editorial Handoff
- 수정·갱신·정정 시 원고 계보 보존

## 2.2 비범위

- 조사 수행, Source 신뢰 규칙과 Claim 검증 상태의 재판정
- 프로젝트별 콘텐츠 목적·필드·고정 표현의 신규 정의
- 최종 편집 승인, 독립 Fact Check, SEO, 게시와 배포
- DOCX·HTML·CSS의 시각 디자인 규칙
- 특정 도구의 Prompt 구문, API 호출법 또는 CMS 조작
- Runtime 자동화와 운영 Release

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 독자·구조·문장·어조 원칙 | COR-002 WRITING PRINCIPLES |
| Source 표시·인용·귀속 | COR-004 SOURCE POLICY |
| 조사 기록과 Research Handoff | CNT-001 RESEARCH WORKFLOW |
| 원고 설계·작성·Editorial Handoff | CNT-002 WRITING WORKFLOW |
| 구조·문장·표기 최종 편집 | CNT-003 EDITORIAL WORKFLOW |
| Claim의 독립 사실 검증 | CNT-004 FACT CHECKING |
| 제목·검색·태그 최적화 | CNT-005 SEO SYSTEM |
| 채널별 발행·배포 | CNT-006 PUBLISHING SYSTEM |
| 프로젝트 필드·수량·문체 | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Writing Request | 작성 목적·독자·채널·언어·기한을 지정한 요청 |
| Output Contract | 필수 섹션·필드·형식·분량·Variant·금지 항목 계약 |
| Research Handoff | CNT-001이 전달한 Brief·Claim·Source·Gap·QA 묶음 |
| Usable Claim | 사용 조건과 검증 상태가 원고 작성에 충분한 Claim |
| Message Map | 핵심 메시지, 보조 메시지, 독자 질문과 근거 연결 |
| Outline | 섹션 순서, 역할, Claim과 예상 분량을 정한 원고 골격 |
| Draft Unit | 제목·리드·문단·목록·표·요약 등 독립 검수 가능한 작성 단위 |
| Claim Trace | 원고 문장을 Claim ID와 Source ID로 되돌리는 연결 |
| Channel Variant | 동일 의미를 채널 계약에 맞게 축약·재배열한 파생 원고 |
| Canonical Draft | 편집 인계의 기준이 되는 하나의 확정 작성본 |
| Editorial Handoff | 원고·추적 정보·열린 이슈·자체 QA를 묶은 편집 인계물 |

# 4. 입력 계약과 작성 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| writing_request_id | 작성 실행 고유 식별자 |
| purpose | 원고가 달성할 독자 행동 또는 이해 |
| audience | 독자 수준·맥락·필요 |
| channel_and_variant | 대상 채널과 출력 Variant |
| output_language | 언어와 필요한 표기 규칙 |
| output_contract | 필수 구조·필드·형식·분량·금지 항목 |
| binding | 적용 기준본 ID·버전·상태 |
| research_handoff_ref | 승인 가능한 조사 인계물 위치 |
| deadline_or_as_of | 작성 기한 또는 콘텐츠 기준 시점 |

필수 입력을 추정해 채우지 않는다. 표현상의 사소한 정규화는 기록 후 수행할 수 있지만 독자, 목적, 필드, Claim 범위 또는 공개 수준을 바꿀 누락은 `BLOCKED`로 처리한다.

## 4.2 작성 상태

| 상태 | 의미 |
|---|---|
| READY | 입력·Binding·Research Handoff 확인 완료 |
| PLANNED | Message Map과 Outline 확정 |
| DRAFTING | Draft Unit 작성 중 |
| SELF_REVIEW | 작성자 자체 QA 중 |
| BLOCKED | 필수 입력·Claim·계약이 없어 진행 불가 |
| EDITORIAL_READY | Canonical Draft와 인계물이 준비됨 |
| SUPERSEDED | 새 작성 실행 또는 정정본으로 대체됨 |

# 5. 표준 작성 수명주기

1. Writing Request를 등록하고 중복 실행을 확인한다.
2. Foundation·Core·Content·Project 기준본을 Binding한다.
3. Output Contract와 대상 독자·채널·언어를 확인한다.
4. Research Handoff의 상태·Claim·Source·Gap을 검사한다.
5. 사용할 Claim과 사용하지 않을 Claim을 이유와 함께 선택한다.
6. 핵심 메시지와 보조 메시지를 Message Map으로 고정한다.
7. 섹션 역할·순서·Claim·분량을 Outline에 배치한다.
8. 제목·리드·핵심 섹션을 작성한다.
9. 본문·목록·표·요약·결론을 작성한다.
10. Claim 유형·근거·귀속·불확실성을 문장과 대조한다.
11. 용어·수치·날짜·이름·단위와 가변 Cardinality를 검사한다.
12. 채널 Variant가 필요하면 Canonical Draft에서 파생한다.
13. Writing QA를 수행하고 열린 이슈를 분류한다.
14. Canonical Draft와 Editorial Handoff를 전달한다.

단계 생략은 Output Contract 또는 비적용 근거가 기록된 경우에만 허용한다. 짧은 원고라도 Binding, Research Handoff 확인, Claim Trace와 자체 QA를 생략하지 않는다.

# 6. Preflight와 Claim 사용 판정

## 6.1 Binding 확인

기준본의 ID·버전·상태가 실제 파일과 일치하는지 확인한다. REVIEW 후보나 과거 초안을 APPROVED·LOCKED 기준본 대신 사용하지 않는다.

## 6.2 Research Handoff 확인

다음을 최소 검사한다.

- Research Brief의 목적·범위·기준 시점
- Claim 유형과 CONFIRMED·PARTIAL·UNVERIFIED·CONFLICT·INFERENCE 상태
- 실제 Source와 Evidence Extract 연결
- Gap·Conflict·사용 제한과 후속 Fact Check 우선순위
- CNT-001 QA와 Handoff 상태

## 6.3 Claim 사용 상태

| 상태 | 의미 |
|---|---|
| USE | 계약과 근거가 작성에 충분함 |
| USE_WITH_QUALIFIER | 조건·불확실성·범위를 문장에 보존해야 함 |
| HOLD | 추가 확인 또는 사용자 결정을 기다림 |
| EXCLUDE | 범위·근거·품질 기준에 맞지 않아 사용하지 않음 |

작성자는 Claim의 검증 상태를 임의로 높이지 않는다. 새로운 사실이 필요하면 조사 메모로 꾸미지 않고 CNT-001 또는 CNT-004에 반환한다.

# 7. Output Contract

Output Contract는 글이 보기 좋아지는 방향보다 요청된 역할을 정확히 수행하게 한다.

| 필드 | 내용 |
|---|---|
| artifact_type | 기사·보고서·가이드·요약·비교 등 |
| required_sections | 필수 섹션과 순서·역할 |
| required_fields | Schema 필드와 Cardinality |
| length_budget | 전체·섹션·필드의 허용 범위 |
| tone_and_voice | Core 원칙과 Project Brand Profile |
| source_display | Source 표시 위치·형식 |
| channel_constraints | 채널별 마크업·길이·금지 요소 |
| variants | Canonical·Full·Summary 등 파생 요구 |
| acceptance_criteria | Editorial Ready 판정 조건 |

상한을 맞추기 위해 의미를 왜곡하거나 필수 Claim을 삭제하지 않는다. 충족할 수 없는 제약은 Writer가 조용히 우회하지 않고 충돌과 대안을 기록한다.

# 8. Message Map과 Outline

## 8.1 Message Map

| 필드 | 내용 |
|---|---|
| core_message | 독자가 기억해야 할 한 문장 |
| supporting_messages | 핵심 메시지를 설명하는 보조 판단 |
| reader_questions | 반드시 답할 독자 질문 |
| claim_refs | 각 메시지를 뒷받침하는 Claim ID |
| caveats | 조건·예외·불확실성 |
| intended_action | 읽은 뒤 가능한 다음 행동 또는 이해 |

## 8.2 Outline

각 섹션에 고유 역할, 핵심 질문, 사용할 Claim, 예상 분량, 필요한 표·목록과 연결 순서를 둔다. 같은 Claim을 여러 섹션에서 반복하려면 반복 목적이 설명돼야 한다.

## 8.3 구조 Gate

- 제목·리드·본문·요약·결론의 역할이 중복되지 않는다.
- 중요한 정보와 독자 질문이 앞쪽에서 해결된다.
- 섹션 순서가 원인·비교·절차·시간 등 선택한 논리를 유지한다.
- Claim 없는 섹션과 목적 없는 장식 섹션을 만들지 않는다.
- 적격 콘텐츠 수가 가변이면 빈 슬롯이나 임의 항목을 남기지 않는다.

# 9. 제목·리드·요약·결론

## 9.1 제목

제목은 주체와 실질 변화를 식별하고 본문보다 강한 단정을 하지 않는다. 클릭 유도를 위해 미확인 결과, 과장된 인과 또는 숨긴 조건을 추가하지 않는다.

## 9.2 리드

리드는 독자가 본문을 읽을 이유와 핵심 상황을 필요한 만큼 완결한다. 제목을 단순 반복하거나 본문에 없는 결론을 앞세우지 않는다.

## 9.3 요약

요약은 Canonical Draft의 핵심 정보만 축약한다. 새 Claim, 새 수치, 새 해석 또는 더 강한 확신을 추가하지 않는다.

## 9.4 결론

결론은 확인된 범위에서 의미·제한·다음 단계를 정리한다. 근거가 없는 권고, 예측 또는 보편화를 추가하지 않는다.

# 10. Draft Unit 작성

## 10.1 섹션

섹션은 Outline에서 부여한 질문 하나를 해결한다. 첫 문단에서 역할과 핵심 판단을 드러내고 후속 문단은 근거·설명·예외·영향을 논리적으로 잇는다.

## 10.2 문단

문단에는 하나의 중심 판단을 둔다. 주제문, 근거, 해석과 전환을 필요한 만큼 포함하되 서로 다른 Claim을 무리하게 한 문단에 묶지 않는다.

## 10.3 목록과 표

순서·조건·병렬 항목은 목록으로, 반복 가능한 비교 데이터는 표로 작성한다. 일반 설명을 표 셀에 가두거나 목록 수를 맞추기 위해 의미 없는 항목을 만들지 않는다.

## 10.4 인용과 귀속

직접 인용은 Source 의미와 문맥을 보존하고 필요한 최소 범위만 사용한다. ATTRIBUTED_CLAIM은 발화자·기관과 Source를 분명히 연결한다.

# 11. 사실·해석·전망의 문장화

## 11.1 FACT

Claim 범위, 조건, 수치, 단위와 시점을 보존한다. 여러 Source의 사실을 한 문장으로 합칠 때 독자가 하나의 Source가 전체를 뒷받침한다고 오해하지 않게 한다.

## 11.2 ATTRIBUTED_CLAIM

발언·입장·주장은 사실 자체와 구분해 귀속한다. 발화자가 주장했다는 사실과 주장 내용의 진실성을 동일시하지 않는다.

## 11.3 INTERPRETATION

확인된 FACT와 작성자의 해석을 구분하고 어떤 근거에서 도출했는지 연결한다. 대안 해석과 제한이 중요하면 함께 보존한다.

## 11.4 OUTLOOK

미래 전망은 조건, 시간 범위, 근거와 불확실성을 표시한다. 가능성을 예정 또는 확정으로 바꾸지 않는다.

## 11.5 CONFLICT와 GAP

중요한 충돌과 공백은 문장에서 숨기지 않는다. 결론을 만들 수 없으면 강도를 낮추거나 해당 내용을 제외하고 Editorial Handoff에 영향을 기록한다.

# 12. 용어·수치·날짜·링크

| 항목 | 작성 기준 |
|---|---|
| 용어 | 승인 용어 사용, 첫 등장 정의, 동의어 통제 |
| 고유명사 | 공식 표기와 대소문자·띄어쓰기 확인 |
| 수치 | 값·단위·기간·분모·비교 기준 보존 |
| 날짜·시간 | 절대 날짜와 필요한 시간대 표시 |
| 통화 | 통화 단위와 기준 시점 표시 |
| 버전 | 제품·정책·문서 버전을 Claim과 일치 |
| 링크 | 실제 Source 또는 승인된 목적 위치에 연결 |

상대 표현은 기준 시점이 흐려지지 않도록 필요한 경우 절대 표기로 바꾼다. 단위 변환과 반올림은 방법과 의미 손실 여부를 확인한다.

# 13. Cardinality와 Channel Variant

## 13.1 가변 Cardinality

항목, 문단, 요약, 전망, Action과 Source 수는 실제 적격 콘텐츠에 따라 반복·병합·삭제한다. 고정 수량이 Project Schema에 명시되지 않았다면 빈 슬롯이나 억지 내용을 만들지 않는다.

## 13.2 Canonical Draft

같은 작성 실행에는 하나의 Canonical Draft를 둔다. Variant는 Canonical의 메시지·Claim·상태를 참조하며 독립 원고처럼 조용히 갈라지지 않는다.

## 13.3 Variant 파생

채널 축약은 정보 밀도·순서·마크업을 바꿀 수 있지만 핵심 의미, Claim 강도, 수치, 귀속과 불확실성을 바꾸지 않는다. 생략한 핵심 제한이 오해를 만들면 축약하지 않는다.

# 14. 수정·갱신·정정

일반 수정은 구조·명료성·중복을 개선하되 Claim 의미를 바꾸지 않는다. 의미가 달라지는 수정은 변경 이유, 영향받는 Claim과 재검증 필요를 기록한다.

`UPDATE`는 새 기준 시점의 사실을 반영하고 `CORRECTION`은 기존 원고의 오류를 바로잡는다. 둘 다 선행 Draft, 변경 전·후 문장, 근거, 시점과 영향받는 Variant를 연결한다.

초안의 오류 흔적을 조용히 삭제해 계보를 끊지 않는다. 외부 공개 후 정정 표시는 CNT-006과 프로젝트 정책을 따른다.

# 15. Editorial Handoff

## 15.1 필수 인계물

| 인계물 | 최소 내용 |
|---|---|
| Writing Request | 목적·독자·채널·언어·기한 |
| Binding | 적용 기준본 ID·버전·상태 |
| Output Contract | 구조·필드·분량·Variant·금지 항목 |
| Message Map | 핵심·보조 메시지와 Claim 연결 |
| Canonical Draft | 편집 기준 원고와 버전 |
| Claim Trace | 문장·Claim·Source 연결 |
| Variant Map | 파생 원고와 생략·변경 내용 |
| Open Issues | Gap·Conflict·HOLD·재검증 필요 |
| Writing QA | Gate 판정과 결함 상태 |

## 15.2 편집 인계 조건

- Canonical Draft가 하나로 식별된다.
- 필수 섹션과 필드가 채워졌거나 비적용 사유가 있다.
- 핵심 문장을 Claim과 Source로 되돌릴 수 있다.
- 내부 메모, Placeholder, 미승인 대안 원고가 제거 또는 분리됐다.
- 열린 이슈가 숨겨지지 않고 책임자와 다음 조치를 가진다.

`EDITORIAL_READY`는 CNT-003 편집 또는 CNT-004 Fact Check의 통과를 의미하지 않는다.

# 16. Writing QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 목적·독자·채널·언어가 추적 가능 |
| G2 Binding | 기준본과 Research Handoff 확인 |
| G3 Contract | 필수 구조·필드·분량·Variant 확정 |
| G4 Message | 핵심 메시지와 Claim 근거 정합 |
| G5 Structure | 섹션 역할·순서·Cardinality 정합 |
| G6 Claim Trace | 사실·귀속·해석·전망과 Source 연결 |
| G7 Expression | 용어·수치·날짜·어조·불확실성 정합 |
| G8 Handoff | Canonical Draft·이슈·QA 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 뒤의 두 상태는 PASS로 계산하지 않는다.

## 16.2 Critical 결함

- Research Handoff에 없는 사실·인용·Source를 생성함
- UNVERIFIED·CONFLICT Claim을 확인된 사실처럼 단정함
- 수치·단위·날짜·귀속 또는 조건을 바꿔 의미를 왜곡함
- 필수 Binding이나 Canonical Draft를 식별할 수 없음
- 내부 지시·Placeholder·민감 메모가 독자용 원고에 남음

Critical 결함이 열려 있으면 `EDITORIAL_READY`로 표시하지 않는다.

# 17. 실행 규칙 (WRT-051 ~ WRT-080)

## 17.A 요청과 Preflight (WRT-051 ~ WRT-055)

### WRT-051 - 작성 요청 식별
- **Statement:** 모든 작성 실행은 고유 writing_request_id, 목적과 대상 독자를 가져야 한다.
- **Verification:** Writing Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### WRT-052 - 기준본 Binding
- **Statement:** 작성 전에 적용할 Core·Content·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding과 실제 파일 상태를 대조한다.
- **Exceptions:** 없음.

### WRT-053 - Research Handoff
- **Statement:** 원고 작성 전에 CNT-001 Research Handoff의 상태·Claim·Source·Gap을 확인해야 한다.
- **Verification:** research_handoff_ref와 Handoff manifest를 검사한다.
- **Exceptions:** 순수 창작은 비적용 근거와 별도 사실 사용 금지를 기록한다.

### WRT-054 - Output Contract
- **Statement:** 필수 구조·필드·분량·Variant·채널 제한을 작성 전에 확정해야 한다.
- **Verification:** Output Contract 완전성을 검사한다.
- **Exceptions:** 탐색 초안은 확정하지 않은 항목과 승인 Gate를 표시한다.

### WRT-055 - 실행 가능성 판정
- **Statement:** 필수 입력·근거·계약이 없으면 임의 보완하지 않고 READY 또는 BLOCKED를 판정해야 한다.
- **Verification:** Preflight 상태와 근거를 확인한다.
- **Exceptions:** 안전한 표기 정규화는 변경 기록 후 허용한다.

## 17.B Claim과 메시지 (WRT-056 ~ WRT-060)

### WRT-056 - Claim 사용 판정
- **Statement:** 사용할 Claim을 USE·USE_WITH_QUALIFIER·HOLD·EXCLUDE로 판정하고 이유를 기록해야 한다.
- **Verification:** Claim Selection Log를 확인한다.
- **Exceptions:** 없음.

### WRT-057 - 검증 상태 보존
- **Statement:** 작성 과정에서 Claim의 검증 상태를 근거보다 높이지 않아야 한다.
- **Verification:** 원 Claim과 원고 표현 강도를 대조한다.
- **Exceptions:** 후속 검증으로 상태가 바뀌면 새 근거와 시점을 연결한다.

### WRT-058 - 핵심 메시지
- **Statement:** 원고는 독자가 기억해야 할 하나의 core_message를 가져야 한다.
- **Verification:** Message Map과 제목·리드·결론을 대조한다.
- **Exceptions:** 독립 항목 모음은 각 항목 메시지와 전체 편집 목적을 둔다.

### WRT-059 - 메시지 근거
- **Statement:** 핵심·보조 메시지는 실제 Claim ID에 연결해야 한다.
- **Verification:** Message Map의 claim_refs를 확인한다.
- **Exceptions:** 독자 안내 문장은 근거 Claim 비적용 사유를 둘 수 있다.

### WRT-060 - 제한 포함
- **Statement:** 결론을 바꾸는 조건·예외·불확실성은 Message Map에서 누락하지 않아야 한다.
- **Verification:** Gap·Conflict와 caveats를 대조한다.
- **Exceptions:** 없음.

## 17.C 구조와 Draft Unit (WRT-061 ~ WRT-065)

### WRT-061 - Outline 선행
- **Statement:** 장문 원고는 본문 작성 전에 섹션 역할·순서·Claim을 Outline으로 고정해야 한다.
- **Verification:** Outline과 Canonical Draft 구조를 대조한다.
- **Exceptions:** 단일 문단 출력은 Message Map으로 대체할 수 있다.

### WRT-062 - 섹션 단일 책임
- **Statement:** 각 섹션은 하나의 독자 질문 또는 정보 역할을 해결해야 한다.
- **Verification:** 섹션 제목·주제문·Claim의 정합성을 확인한다.
- **Exceptions:** 짧은 결론은 의미와 다음 단계를 함께 정리할 수 있다.

### WRT-063 - Claim 배치
- **Statement:** 모든 핵심 Claim은 적절한 섹션과 Draft Unit에 배치되고 중복 사용은 목적이 설명돼야 한다.
- **Verification:** Outline claim_refs와 원고 위치를 검사한다.
- **Exceptions:** 요약의 의도적 반복은 허용한다.

### WRT-064 - 형식 적합성
- **Statement:** 설명은 문단, 순서·병렬 항목은 목록, 반복 비교 데이터는 표로 표현해야 한다.
- **Verification:** 표·목록 과용과 prose-in-table 여부를 검사한다.
- **Exceptions:** Project MASTER가 필수 형식을 지정하면 그 계약을 따른다.

### WRT-065 - 가변 Cardinality
- **Statement:** 실제 적격 콘텐츠 수에 따라 항목을 반복·병합·삭제하고 빈 슬롯이나 억지 내용을 만들지 않아야 한다.
- **Verification:** Schema와 실제 항목 수·미사용 슬롯을 대조한다.
- **Exceptions:** 승인된 고정 수량 계약은 부족 상태를 BLOCKED로 표시한다.

## 17.D 문장과 근거 (WRT-066 ~ WRT-070)

### WRT-066 - 원자적 문장
- **Statement:** 독립적으로 검증해야 하는 여러 Claim을 한 문장에 섞지 않아야 한다.
- **Verification:** 문장과 Claim Trace의 대응을 검사한다.
- **Exceptions:** 의미가 결합된 직접 인용은 하나로 둘 수 있다.

### WRT-067 - FACT 의미 보존
- **Statement:** FACT의 범위·조건·수치·단위·시점을 원고에서 보존해야 한다.
- **Verification:** 원 Claim·Evidence와 문장을 대조한다.
- **Exceptions:** 반올림·단위 변환은 방법과 의미 손실을 확인한다.

### WRT-068 - 귀속 명시
- **Statement:** ATTRIBUTED_CLAIM은 발화자 또는 책임 기관과 실제 Source를 명시해야 한다.
- **Verification:** 문장 귀속과 Claim·Source Record를 검사한다.
- **Exceptions:** 반복 문맥에서 주체가 명백하면 후속 문장에서 축약할 수 있다.

### WRT-069 - 해석·전망 분리
- **Statement:** INTERPRETATION과 OUTLOOK을 FACT처럼 쓰지 않고 근거·가정·시간 범위·제한을 표시해야 한다.
- **Verification:** 문장 역할과 claim_type을 대조한다.
- **Exceptions:** 없음.

### WRT-070 - Claim Trace
- **Statement:** 독자용 핵심 문장을 Claim ID와 Source ID로 되돌릴 수 있어야 한다.
- **Verification:** Claim Trace의 참조 무결성을 검사한다.
- **Exceptions:** 순수 연결·안내 문장은 비적용 표시가 가능하다.

## 17.E 표현과 Variant (WRT-071 ~ WRT-075)

### WRT-071 - 제목 강도
- **Statement:** 제목은 본문과 Claim보다 강한 인과·확신·긴급성을 추가하지 않아야 한다.
- **Verification:** 제목을 core_message와 Critical Claim에 대조한다.
- **Exceptions:** 없음.

### WRT-072 - 요약 비확장
- **Statement:** 요약과 리드는 Canonical Draft에 없는 사실·수치·해석을 추가하지 않아야 한다.
- **Verification:** 요약 문장의 Claim Trace를 검사한다.
- **Exceptions:** 독자 안내 문구는 별도 역할로 표시한다.

### WRT-073 - 표기 정합성
- **Statement:** 용어·고유명사·수치·단위·날짜·시간대·버전을 기준본과 근거에 맞춰야 한다.
- **Verification:** Style Sheet와 Source를 대조한다.
- **Exceptions:** 채널 표기 제한은 의미를 유지하는 승인 축약만 허용한다.

### WRT-074 - Canonical 단일성
- **Statement:** 같은 실행에는 하나의 Canonical Draft만 두고 대안·과거 Draft를 기준본처럼 혼용하지 않아야 한다.
- **Verification:** Draft registry와 상태를 확인한다.
- **Exceptions:** 병렬 언어본은 각 Canonical과 번역 관계를 명시한다.

### WRT-075 - Variant 의미 보존
- **Statement:** 채널 Variant는 Canonical의 핵심 의미·Claim 강도·수치·귀속·불확실성을 바꾸지 않아야 한다.
- **Verification:** Variant Map과 Canonical Draft를 대조한다.
- **Exceptions:** 생략이 허용되더라도 오해를 만들면 파생하지 않는다.

## 17.F QA와 인계 (WRT-076 ~ WRT-080)

### WRT-076 - 내부 요소 제거
- **Statement:** 독자용 원고에서 Prompt·Placeholder·검토 메모·미승인 대안을 제거하거나 분리해야 한다.
- **Verification:** 금지 패턴과 Draft 상태를 검사한다.
- **Exceptions:** 내부 전용 Variant는 독자용과 물리적으로 분리한다.

### WRT-077 - 열린 이슈 투명성
- **Statement:** HOLD·Gap·Conflict·재검증 필요를 영향과 다음 조치와 함께 Editorial Handoff에 남겨야 한다.
- **Verification:** Open Issues와 Claim 상태를 대조한다.
- **Exceptions:** 없음.

### WRT-078 - Writing Gate
- **Statement:** G1~G8 판정과 증거 없이 EDITORIAL_READY로 표시하지 않아야 한다.
- **Verification:** Writing QA Record를 확인한다.
- **Exceptions:** 없음.

### WRT-079 - 인계 상태 분리
- **Statement:** EDITORIAL_READY를 Editorial·Fact Check·SEO·Publishing 승인으로 해석하지 않아야 한다.
- **Verification:** Handoff에 후속 Gate와 책임 문서가 명시돼 있다.
- **Exceptions:** 없음.

### WRT-080 - 수정 계보
- **Statement:** UPDATE와 CORRECTION은 선행 Draft, 변경 전·후 문장, 근거·시점·영향받는 Variant를 연결해야 한다.
- **Verification:** Draft lineage와 Change Record를 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Writing Workflow

```text
1. writing_request_id, 목적, 독자, 채널, 언어, Output Contract와 기준본 Binding을 확인한다.
2. CNT-001 Research Handoff의 Claim·Source·Gap·Conflict·QA 상태를 먼저 검사한다.
3. Claim을 USE·USE_WITH_QUALIFIER·HOLD·EXCLUDE로 판정하고 검증 상태를 높이지 않는다.
4. 하나의 core_message와 보조 메시지를 실제 Claim ID에 연결한다.
5. 섹션 역할·순서·Claim·분량을 Outline에 배치한 뒤 작성한다.
6. 제목은 본문보다 강하게 쓰지 않고 리드·요약은 새 Claim을 추가하지 않는다.
7. FACT·ATTRIBUTED_CLAIM·INTERPRETATION·OUTLOOK을 구분하고 조건·불확실성을 보존한다.
8. 핵심 문장을 Claim ID와 Source ID로 되돌릴 수 있게 한다.
9. 용어·이름·수치·단위·날짜·시간대·버전을 근거와 맞춘다.
10. 실제 적격 수에 따라 항목을 반복·병합·삭제하고 빈 슬롯을 만들지 않는다.
11. 채널 Variant는 하나의 Canonical Draft에서 파생하고 의미·강도·귀속을 바꾸지 않는다.
12. Prompt·Placeholder·내부 메모를 제거하고 G1~G8 QA와 열린 이슈를 Editorial에 인계한다.
```

이 압축 블록은 상세 Workflow의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-002는 승인 가능한 조사 결과를 원고로 변환하는 순서와 기록 계약만 정의한다.
- 조사 추가·Claim 재검증은 CNT-001과 CNT-004에 반환한다.
- 최종 구조·문장·표기 편집은 CNT-003, SEO는 CNT-005가 맡는다.
- 시각 형식은 DSG 문서와 Project MASTER, 게시·정정 공개는 CNT-006이 맡는다.
- Runtime Prompt와 자동 실행은 Phase 5 Automation의 별도 Gate를 통과해야 한다.

## 19.2 알려진 제한

- 모든 콘텐츠 유형에 같은 Outline, 문장 길이 또는 항목 수를 강제하지 않는다.
- 번역·현지화의 상세 절차는 현재 범위에 포함하지 않는다.
- 법률·의료·재무 등 고위험 원고는 이 문서만으로 전문 검토를 대체하지 않는다.
- `EDITORIAL_READY`는 사실 정확성, 최종 편집 또는 공개 가능성을 보증하지 않는다.
- 프로젝트별 Schema·Brand Voice·채널 제한은 후속 또는 해당 Project 문서가 구체화한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 작성 입력·Preflight·Claim 사용·Message Map·Outline·Draft Unit·Variant·QA·Editorial Handoff와 WRT-051~080 작성; 사용자 명시적 승인 반영 |
