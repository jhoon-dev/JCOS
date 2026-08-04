# JCOS v2.0.0 - CNT-001 RESEARCH WORKFLOW

## 범용 조사 실행·기록·인계 절차

| Field | Value |
|---|---|
| Document ID | CNT-001 |
| Title | RESEARCH WORKFLOW |
| Korean Title | 범용 조사 실행·기록·인계 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | JCOS의 기사·보고서·가이드·비교·분석·프로젝트 콘텐츠를 위한 조사 실행 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED |
| Extends | COR-003 RSH-001~050 |
| Depends On | COR-003 RESEARCH PRINCIPLES, COR-004 SOURCE POLICY, COR-005 QUALITY GATE, COR-007 VERSION POLICY |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-001 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-001은 조사 요청을 Research Brief, Question Map, Candidate Log, Source Log, Claim Map, Gap Log와 Research Handoff로 변환하는 표준 실행 절차를 정의한다. 같은 입력과 기준본을 받은 다른 사람 또는 AI가 핵심 판단을 재현할 수 있어야 한다.

이 문서는 무엇을 믿을지에 관한 원칙보다 언제 무엇을 확인하고 어떤 증거를 남겨 다음 단계에 넘길지를 다룬다.

# 2. 범위와 비범위

## 2.1 포함 범위

- 요청 접수와 기준본 Binding
- 조사 질문·포함 범위·제외 범위·완료 조건 명시
- 후보 탐색, Source 확인과 증거 추출
- Claim 단위 구조화와 교차 확인
- 최신성·버전·지역·불확실성·충돌 기록
- 조사 중단·재개·갱신·정정
- Writing과 Fact Checking 단계로의 인계
- 논리 QA와 Evidence Bundle 구성

## 2.2 비범위

- 조사 원칙과 Source 신뢰 규칙의 재정의
- 최종 문장 작성, 편집, SEO, 게시와 배포
- 프로젝트별 후보 선정 점수나 고정 수량
- 특정 도구의 검색 구문, API 호출법 또는 계정 설정
- Runtime 예약, 실패 복구 자동화와 운영 배포

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 조사 목적·범위·대표성·중단 원칙 | COR-003 RESEARCH PRINCIPLES |
| Source 계층·독립성·직접성·인용 | COR-004 SOURCE POLICY |
| 결함 등급과 통과 판정 | COR-005 QUALITY GATE |
| 조사 실행 순서와 기록물 | CNT-001 RESEARCH WORKFLOW |
| 조사 결과를 문장으로 변환 | CNT-002 WRITING WORKFLOW |
| 최종 사실 재검증 | CNT-004 FACT CHECKING |
| 프로젝트별 적격성·우선순위 | 해당 Project Rules |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Research Request | 조사 목적과 기대 결과를 전달한 원 요청 |
| Binding | 실행에 적용할 Foundation·Core·Project 기준본의 ID·버전·상태 |
| Research Brief | 질문, 범위, 기준 시점, 완료 조건과 제한을 고정한 실행 계약 |
| Question Map | 핵심 질문을 검증 가능한 하위 질문과 선행관계로 분해한 목록 |
| Candidate | 조사 대상으로 수집했지만 채택 여부가 확정되지 않은 정보 단위 |
| Source Record | 실제 확인한 Source의 식별자·역할·Locator·시점·접근 상태 기록 |
| Evidence Extract | Source가 제공한 근거의 위치와 최소 문맥을 보존한 기록 |
| Claim Record | 검증 대상 주장, 유형, 상태와 근거 Source를 연결한 기록 |
| Gap | 완료 조건에 필요하지만 확보하지 못한 정보 또는 근거 |
| Conflict | 신뢰 가능한 Source 사이의 중요한 불일치 |
| Evidence Bundle | Brief부터 Handoff까지 조사 추적성을 묶은 인계 패키지 |

# 4. 입력 계약과 실행 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| request_id | 요청을 추적할 고유 식별자 |
| purpose | 조사 결과가 지원할 결정 또는 콘텐츠 |
| core_question | 답해야 할 핵심 질문 |
| as_of | 기준 날짜·시각·시간대 또는 명시적 비적용 사유 |
| scope | 포함·제외 범위와 대상 독자·지역·버전 |
| binding | 적용 기준본 ID·버전·상태 |
| completion_criteria | 조사 완료를 판정할 조건 |
| constraints | 시간·접근·권리·언어·형식 제한 |

필수 입력이 없으면 임의로 채우지 않는다. 안전하게 정규화할 수 있는 표기 차이는 기록 후 보정하고, 조사 결론을 바꿀 수 있는 누락은 `BLOCKED`로 돌린다.

## 4.2 실행 상태

| 상태 | 의미 |
|---|---|
| READY | 필수 입력과 Binding이 확인됨 |
| IN_PROGRESS | 조사 수행 중 |
| HOLD | 외부 응답·접근·사용자 결정을 기다림 |
| BLOCKED | 필수 입력·기준본·Critical 근거가 없어 진행 불가 |
| HANDOFF_READY | 완료 조건과 조사 QA를 통과해 인계 가능 |
| SUPERSEDED | 더 최신 조사 실행으로 대체됨 |

# 5. 표준 조사 수명주기

1. 요청을 등록하고 중복 실행 여부를 확인한다.
2. 적용할 기준본과 Project Rules를 Binding한다.
3. Research Brief와 완료 조건을 확정한다.
4. 핵심 질문을 검증 가능한 하위 질문으로 분해한다.
5. Source 계획과 탐색 순서를 세운다.
6. 후보를 수집하고 Candidate Log에 등록한다.
7. 실제 Source에 접근해 메타데이터와 상태를 기록한다.
8. 근거를 최소 문맥과 위치 정보와 함께 추출한다.
9. Claim을 원자화하고 Source 근거를 연결한다.
10. 핵심 Claim을 교차 확인하고 충돌·공백을 판정한다.
11. 기준 시점·지역·버전·불확실성을 재검토한다.
12. 중단 조건과 완료 조건을 적용한다.
13. Evidence Bundle을 조립하고 독립 QA를 수행한다.
14. Writing과 Fact Checking에 Research Handoff를 전달한다.

단계 생략은 허용 근거와 영향이 기록된 경우에만 가능하다. 단순하거나 반복적인 요청이라는 이유로 Binding, Source 접근 확인, Claim 근거 연결을 생략하지 않는다.

# 6. Research Brief

Research Brief는 실행 중 범위가 조용히 바뀌는 것을 막는다. 다음 필드를 최소 계약으로 사용한다.

| 필드 | 내용 |
|---|---|
| decision_target | 결과가 지원할 결정·콘텐츠 |
| core_question | 최종적으로 답할 질문 |
| subquestions | 검증 가능한 하위 질문 ID |
| audience_and_use | 독자와 사용 맥락 |
| included | 포함 대상 |
| excluded | 제외 대상 |
| as_of | 기준 시점과 시간대 |
| locale_version | 지역·언어·제품·정책 버전 |
| critical_claims | 반드시 근거가 필요한 Claim 후보 |
| completion_criteria | 완료 Gate |
| constraints | 접근·시간·권리·형식 제한 |

범위 변경은 이전 값을 삭제하지 않고 변경 이유, 승인 주체, 시점과 완료 조건에 미치는 영향을 추가한다.

# 7. Question Map과 조사 계획

## 7.1 질문 분해

하위 질문은 한 번의 증거 판정으로 답할 수 있는 크기로 작성한다. 정의·현황·원인·비교·영향·예외·시간 변화를 필요에 따라 분리하며, 서로 다른 단위나 기준을 한 질문에 섞지 않는다.

## 7.2 선행관계

용어 정의, 기준 시점과 대상 식별처럼 후속 판단을 바꾸는 전제를 먼저 확인한다. 선행 질문이 `BLOCKED`면 그 결과에 의존하는 질문을 확정하지 않는다.

## 7.3 Source 계획

각 하위 질문마다 필요한 Source 역할, 직접성, 독립성, 최신성, 접근 경로와 대체 확인 경로를 계획한다. Source 우선순위 자체는 COR-004를 따른다.

# 8. 후보 탐색과 Source 확인

## 8.1 후보 등록

후보를 발견하면 다음을 기록한다.

| 필드 | 내용 |
|---|---|
| candidate_id | 후보 고유 ID |
| question_ids | 관련 하위 질문 |
| summary | 후보가 제공할 수 있는 정보 |
| discovered_at | 발견 시점·시간대 |
| locator | 실제 후보 위치 |
| decision_state | INCLUDE·EXCLUDE·HOLD·MERGE |
| decision_reason | 적용 Rule과 근거 |

## 8.2 Source Record

후보를 근거로 사용할 때 Source Record를 생성한다. 제목, 발행자, 작성자 또는 책임 주체, 발행·갱신일, 확인 시점, 실제 Locator, Source 역할, 접근 상태와 알려진 제한을 기록한다.

검색 결과의 제목·요약·자동 생성 미리보기는 원 Source가 아니다. 원문 접근이 불가능하면 접근 제한을 남기고 검증 상태를 낮춘다.

## 8.3 중복과 관계

같은 원자료를 반복 전재한 Source는 독립 근거 수를 늘리지 않는다. 원자료, 공식 설명, 독립 분석과 반증 Source의 역할을 구분하고 복제·인용 관계를 가능한 범위에서 연결한다.

# 9. Evidence Extract와 조사 메모

Evidence Extract는 Claim을 실제 Source 위치로 되돌릴 수 있어야 한다.

| 필드 | 내용 |
|---|---|
| extract_id | 추출 고유 ID |
| source_id | 실제 Source Record |
| supports_questions | 관련 질문 ID |
| locator_detail | 페이지·절·표·문단·타임코드 등 |
| evidence_summary | 의미를 바꾸지 않은 요약 |
| exact_quote | 필요한 경우의 최소 직접 인용 |
| context | 조건·대상·예외·단위 |
| checked_at | 확인 시점 |

개인 메모, 추론과 Source의 표현을 구분한다. 인용은 필요한 최소 범위만 보존하고 권리·출처 표시 요구를 따른다.

# 10. Claim Map

## 10.1 Claim 원자화

한 Claim에는 하나의 검증 가능한 주장을 둔다. 사실과 해석, 현재 상태와 전망, 서로 다른 시점의 수치를 분리한다.

## 10.2 Claim 유형

| 유형 | 의미 |
|---|---|
| FACT | Source로 확인할 수 있는 사실 |
| ATTRIBUTED_CLAIM | 특정 주체의 발언·입장·주장 |
| INTERPRETATION | 확인된 사실에서 도출한 해석 |
| OUTLOOK | 미래 조건과 불확실성을 포함한 전망 |

## 10.3 검증 상태

| 상태 | 의미 |
|---|---|
| CONFIRMED | 요구되는 직접성·최신성·교차 확인을 충족 |
| PARTIAL | 일부 근거 또는 범위만 확인 |
| UNVERIFIED | 확인 가능한 근거를 확보하지 못함 |
| CONFLICT | 신뢰 가능한 Source가 중요한 지점에서 불일치 |
| INFERENCE | Source 사실에서 분리해 표시한 추론 |

FACT와 ATTRIBUTED_CLAIM은 실제 Source ID를 가져야 한다. INTERPRETATION과 OUTLOOK은 근거 Claim, 가정과 제한을 연결한다.

# 11. 교차 확인과 충돌 처리

Critical Claim은 COR-004가 요구하는 Source 조합으로 확인한다. 여러 Source가 같은 원자료에 의존하면 독립 교차 확인으로 계산하지 않는다.

충돌이 발견되면 다음을 수행한다.

1. 용어·대상·기간·단위·지역·버전 차이를 먼저 확인한다.
2. 각 Source의 직접성, 책임 주체, 갱신 시점과 근거 범위를 비교한다.
3. 해소되지 않으면 한쪽을 임의 선택하지 않고 `CONFLICT`를 유지한다.
4. 충돌이 결론과 후속 콘텐츠에 미치는 영향을 기록한다.
5. 후속 확인으로 해소되면 확인 시점과 근거를 추가한다.

# 12. 시간·지역·버전 관리

모든 시간 민감 정보에는 기준 시점과 확인 시점을 둔다. 상대 날짜는 가능한 경우 절대 날짜로 정규화하고 시간대를 보존한다.

정책, 가격, 사양, 조직 역할, 소프트웨어와 일정은 지역·제품·문서 버전을 함께 확인한다. 과거 Source를 현재 상태의 근거로 사용할 때는 여전히 유효한지 다시 확인한다.

조사 시간이 길어 기준 시점이 바뀌면 Brief를 조용히 수정하지 않는다. 기존 실행을 유지하거나 새 실행·Update로 분기하고 변경 영향을 기록한다.

# 13. 공백·불확실성·중단

## 13.1 Gap Log

| 필드 | 내용 |
|---|---|
| gap_id | 공백 고유 ID |
| question_or_claim | 영향받는 질문·Claim |
| severity | CRITICAL·MAJOR·MINOR |
| reason | 미확인의 원인 |
| attempts | 시도한 확인 경로 |
| impact | 결론과 인계에 미치는 영향 |
| next_action | 추가 확인·보류·제외·사용자 결정 |

## 13.2 중단 조건

- 완료 조건과 Critical Claim 근거가 충족됐다.
- 추가 Source가 결론 강도나 주요 공백을 실질적으로 바꾸지 않는다.
- 승인된 시간·비용·접근 한도에 도달했다.
- 필수 기준본, 입력 또는 Critical 근거가 없어 `BLOCKED`다.
- 사용자 또는 상위 Workflow가 중단을 지시했다.

수량을 맞추기 위해 근거가 약한 후보나 Claim을 추가하지 않는다. 미완료 상태는 축소하거나 숨기지 않는다.

# 14. 갱신·정정·재개

`UPDATE`는 기준 시점 이후의 새 사실을 추가하고, `CORRECTION`은 기존 조사 기록의 오류를 바로잡는다. 둘 다 선행 Research Run, 변경 전·후 내용, 근거, 시점과 영향 범위를 연결한다.

일시적 접근 실패 후 재개하면 기존 Candidate·Source·Claim ID를 가능한 범위에서 유지하고 새 확인 시점을 추가한다. 선행 기록을 삭제해 추적을 끊지 않는다.

같은 Source의 대체 접근 경로는 동일한 내용·버전인지 확인한다. 캐시, 미러, 보관본은 현재 원문과 동일하다고 자동 가정하지 않는다.

# 15. Research Handoff

## 15.1 필수 인계물

| 인계물 | 최소 내용 |
|---|---|
| Research Brief | 요청·Binding·범위·기준 시점·완료 조건 |
| Question Map | 질문·상태·선행관계 |
| Candidate Log | 포함·제외·보류·병합 판단과 이유 |
| Source Log | 실제 Source, Locator, 역할, 확인 시점과 접근 상태 |
| Claim Map | Claim 유형·검증 상태·근거 연결 |
| Gap and Conflict Log | 미확인·충돌·영향·다음 조치 |
| Research Summary | 확인된 답, 제한과 결론 강도 |
| QA Record | Gate 판정, 결함과 승인 상태 |

## 15.2 Writing 인계

CNT-002에는 사용할 수 있는 CONFIRMED·PARTIAL Claim, 직접 인용 제한, Source 표시 요구, 금지된 일반화, 남은 공백과 기준 시점을 전달한다. 조사 메모를 사실처럼 넘기지 않는다.

## 15.3 Fact Checking 인계

CNT-004에는 Critical Claim 목록, Source Record, Evidence Extract, 충돌, 최신성 위험과 재확인 우선순위를 전달한다. `HANDOFF_READY`는 최종 Fact Check 통과를 의미하지 않는다.

# 16. QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 필수 입력과 목적이 추적 가능 |
| G2 Binding | 적용 기준본 ID·버전·상태 확인 |
| G3 Scope | 포함·제외·기준 시점·완료 조건 확정 |
| G4 Source | 실제 접근·메타데이터·역할·제한 기록 |
| G5 Claim | 유형·상태·근거 Source 연결 |
| G6 Cross-check | Critical Claim과 충돌 처리 완료 |
| G7 Freshness | 시간·지역·버전 정합성 확인 |
| G8 Handoff | 필수 인계물과 미완료 상태 공개 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 뒤의 두 상태는 PASS로 계산하지 않는다.

## 16.2 Critical 결함

- 존재하지 않는 Source, Locator, 인용 또는 확인 사실을 생성함
- 접근하지 않은 내용을 확인한 것처럼 기록함
- Critical FACT가 실제 Source에 연결되지 않음
- 중요한 Source 충돌 또는 기준 시점 차이를 숨김
- 필수 Binding이 없거나 허용되지 않은 기준본을 사용함

Critical 결함이 열려 있으면 `HANDOFF_READY`로 표시하지 않는다.

# 17. 실행 규칙 (RSH-051 ~ RSH-080)

## 17.A 요청과 Binding (RSH-051 ~ RSH-055)

### RSH-051 - 요청 식별
- **Statement:** 모든 조사 실행은 고유 request_id와 목적을 가져야 한다.
- **Verification:** Brief에서 request_id와 decision_target을 확인한다.
- **Exceptions:** 없음.

### RSH-052 - 기준본 Binding
- **Statement:** 실행 전에 적용할 Foundation·Core·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding 목록과 실제 파일 상태를 대조한다.
- **Exceptions:** 없음.

### RSH-053 - 기준 시점
- **Statement:** 시간 민감 조사는 날짜·시각·시간대를 포함한 as_of를 가져야 한다.
- **Verification:** Brief와 Source 확인 시점의 정합성을 검사한다.
- **Exceptions:** 시간과 무관하면 비적용 사유를 기록한다.

### RSH-054 - 범위 계약
- **Statement:** 포함·제외 범위와 대상 지역·버전을 조사 전에 기록해야 한다.
- **Verification:** Brief의 scope 필드를 확인한다.
- **Exceptions:** 없음.

### RSH-055 - 완료 조건
- **Statement:** 조사 시작 전에 Critical Claim과 완료 조건을 정의해야 한다.
- **Verification:** completion_criteria와 critical_claims를 확인한다.
- **Exceptions:** 탐색적 조사는 종료·시간 한도를 대신 명시한다.

## 17.B 질문과 계획 (RSH-056 ~ RSH-060)

### RSH-056 - 검증 가능한 질문
- **Statement:** 핵심 질문을 한 번의 증거 판정이 가능한 하위 질문으로 분해해야 한다.
- **Verification:** Question Map의 각 항목이 단일 판단을 갖는지 본다.
- **Exceptions:** 단일 사실 확인은 핵심 질문 자체를 사용할 수 있다.

### RSH-057 - 선행관계
- **Statement:** 후속 결론을 바꾸는 정의·대상·시점 질문을 먼저 확인해야 한다.
- **Verification:** Question Map의 dependency를 확인한다.
- **Exceptions:** 독립 질문에는 적용하지 않는다.

### RSH-058 - Source 역할 계획
- **Statement:** 각 핵심 질문에 필요한 Source 역할과 독립성 요구를 계획해야 한다.
- **Verification:** Source Plan을 COR-004와 대조한다.
- **Exceptions:** 없음.

### RSH-059 - 대체 확인 경로
- **Statement:** 핵심 Source 접근 실패 가능성이 있으면 허용되는 대체 확인 경로를 기록해야 한다.
- **Verification:** Plan에 fallback과 한계가 있다.
- **Exceptions:** 유일한 권위 Source만 유효하면 BLOCKED 조건을 적는다.

### RSH-060 - 범위 변경 추적
- **Statement:** 실행 중 범위 변경은 이전 값·이유·승인·영향을 보존해야 한다.
- **Verification:** Brief revision 또는 Decision Log를 확인한다.
- **Exceptions:** 의미 없는 표기 정규화는 변경 사유만 남길 수 있다.

## 17.C 후보와 Source (RSH-061 ~ RSH-065)

### RSH-061 - 후보 기록
- **Statement:** 중요한 후보는 포함 여부와 관계없이 ID·질문·Locator·결정 이유를 기록해야 한다.
- **Verification:** Candidate Log의 필수 필드를 확인한다.
- **Exceptions:** 명백한 스팸·중복 탐색 노이즈는 집계 기록할 수 있다.

### RSH-062 - 원 Source 접근
- **Statement:** 검색 결과 요약이 아니라 실제 Source에 접근한 뒤 근거로 사용해야 한다.
- **Verification:** Source Record의 Locator와 access_status를 확인한다.
- **Exceptions:** 원문 접근 불가 시 제한과 낮춘 검증 상태를 기록한다.

### RSH-063 - Source 메타데이터
- **Statement:** 사용한 Source에는 책임 주체·제목·날짜·Locator·확인 시점·역할을 기록해야 한다.
- **Verification:** Source Log 필수 필드 완전성을 검사한다.
- **Exceptions:** 제공되지 않은 필드는 `UNKNOWN`과 영향을 기록한다.

### RSH-064 - 복제 독립성
- **Statement:** 같은 원자료를 전재한 여러 Source를 독립 근거로 계산하지 않아야 한다.
- **Verification:** Source 관계와 원자료 참조를 검사한다.
- **Exceptions:** 전재 과정의 별도 분석은 그 분석 범위만 독립 평가한다.

### RSH-065 - 접근 상태 진실성
- **Statement:** 접근 성공·제한·실패를 실제 결과대로 기록하고 보지 못한 내용을 확인했다고 표시하지 않아야 한다.
- **Verification:** 실행 로그와 Source Record를 대조한다.
- **Exceptions:** 없음.

## 17.D Evidence와 Claim (RSH-066 ~ RSH-070)

### RSH-066 - 근거 위치
- **Statement:** Evidence Extract는 Source ID와 페이지·절·문단·타임코드 등 재확인 가능한 위치를 가져야 한다.
- **Verification:** extract locator가 실제 Source 위치를 가리킨다.
- **Exceptions:** 위치 체계가 없는 Source는 최소 문맥과 확인 방법을 기록한다.

### RSH-067 - Claim 원자화
- **Statement:** 서로 독립적으로 참·거짓을 판정할 주장을 하나의 Claim에 섞지 않아야 한다.
- **Verification:** Claim Map에서 복합 주장 여부를 검사한다.
- **Exceptions:** 분리하면 의미가 사라지는 직접 인용은 하나로 둘 수 있다.

### RSH-068 - Claim 유형
- **Statement:** 모든 Claim은 FACT·ATTRIBUTED_CLAIM·INTERPRETATION·OUTLOOK 중 하나로 분류해야 한다.
- **Verification:** claim_type 완전성을 확인한다.
- **Exceptions:** 없음.

### RSH-069 - 근거 연결
- **Statement:** FACT와 ATTRIBUTED_CLAIM은 실제 Source ID와 Evidence Extract에 연결해야 한다.
- **Verification:** 참조 무결성과 근거 적합성을 검사한다.
- **Exceptions:** 확보하지 못하면 UNVERIFIED로 유지하고 최종 사실로 사용하지 않는다.

### RSH-070 - 상태 강도
- **Statement:** Claim 검증 상태는 실제 근거의 직접성·독립성·최신성보다 강하게 표시하지 않아야 한다.
- **Verification:** CONFIRMED·PARTIAL·UNVERIFIED·CONFLICT·INFERENCE를 근거와 대조한다.
- **Exceptions:** 없음.

## 17.E 교차 확인과 최신성 (RSH-071 ~ RSH-075)

### RSH-071 - Critical 교차 확인
- **Statement:** Critical Claim은 COR-004가 요구하는 Source 조합으로 교차 확인해야 한다.
- **Verification:** Claim별 독립 Source 관계를 검사한다.
- **Exceptions:** 유일한 권위 Source만 존재하면 그 사실과 제한을 공개한다.

### RSH-072 - 충돌 보존
- **Statement:** 신뢰 가능한 Source의 중요한 불일치를 숨기거나 임의로 해소하지 않아야 한다.
- **Verification:** Conflict Log에 차이·근거·영향이 있다.
- **Exceptions:** 후속 근거로 해소되면 해소 시점과 근거를 추가한다.

### RSH-073 - 시간 정합성
- **Statement:** Source 발행·갱신·확인 시점이 Brief의 as_of와 맞는지 검사해야 한다.
- **Verification:** 날짜와 시간대를 대조한다.
- **Exceptions:** 역사적 맥락 Source는 역할을 분리한다.

### RSH-074 - 지역·버전 정합성
- **Statement:** 정책·가격·사양·기능 Claim은 대상 지역과 버전에 맞는 Source를 사용해야 한다.
- **Verification:** locale_version과 Source 적용 범위를 대조한다.
- **Exceptions:** 범용 정보는 비적용 근거를 기록한다.

### RSH-075 - 최신성 재검사
- **Statement:** 완료 전에 변경 가능성이 높은 핵심 Claim을 다시 확인해야 한다.
- **Verification:** final_checked_at과 변경 여부를 확인한다.
- **Exceptions:** 변경 불가능한 과거 사실에는 적용하지 않는다.

## 17.F 완료와 인계 (RSH-076 ~ RSH-080)

### RSH-076 - Gap 투명성
- **Statement:** 미확인 정보는 원인·시도·영향·다음 조치와 함께 Gap Log에 남겨야 한다.
- **Verification:** 열린 Gap과 Claim 상태를 대조한다.
- **Exceptions:** 없음.

### RSH-077 - 중단 근거
- **Statement:** 조사를 중단할 때 완료·수익 체감·한도·BLOCKED 중 적용한 조건을 기록해야 한다.
- **Verification:** Run Log의 stop_reason을 확인한다.
- **Exceptions:** 사용자의 즉시 중단도 지시와 시점을 기록한다.

### RSH-078 - Evidence Bundle
- **Statement:** 인계 전에 Brief·Question·Candidate·Source·Evidence·Claim·Gap·QA 기록을 묶어야 한다.
- **Verification:** Bundle manifest와 참조 무결성을 검사한다.
- **Exceptions:** 비적용 기록물은 사유를 명시한다.

### RSH-079 - 인계 상태 분리
- **Statement:** HANDOFF_READY를 최종 Writing·Fact Check·Publishing 승인으로 해석하지 않아야 한다.
- **Verification:** Handoff에 후속 Gate와 열린 제한이 명시돼 있다.
- **Exceptions:** 없음.

### RSH-080 - 갱신·정정 추적
- **Statement:** UPDATE와 CORRECTION은 선행 실행, 변경 전·후 내용, 근거·시점·영향을 연결해야 한다.
- **Verification:** lineage와 change record를 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Research Workflow

```text
1. request_id, 목적, 핵심 질문, as_of, 범위, 완료 조건과 기준본 Binding을 먼저 확인한다.
2. 핵심 질문을 검증 가능한 하위 질문으로 분해하고 선행관계와 Source 역할을 계획한다.
3. 후보마다 ID, 관련 질문, 실제 Locator, INCLUDE·EXCLUDE·HOLD·MERGE와 이유를 기록한다.
4. 검색 요약이 아니라 실제 Source에 접근하고 책임 주체·날짜·확인 시점·역할·접근 상태를 남긴다.
5. Source 근거는 위치와 최소 문맥을 가진 Evidence Extract로 보존한다.
6. Claim을 FACT·ATTRIBUTED_CLAIM·INTERPRETATION·OUTLOOK으로 분리하고 검증 상태를 표시한다.
7. FACT와 ATTRIBUTED_CLAIM은 실제 Source와 Evidence에 연결한다.
8. 같은 원자료의 전재를 독립 근거로 세지 않고 Critical Claim을 교차 확인한다.
9. 시간·지역·버전 차이, 충돌, 공백과 불확실성을 숨기지 않는다.
10. 완료·수익 체감·한도·BLOCKED 중 중단 근거를 기록한다.
11. Brief·Question·Candidate·Source·Evidence·Claim·Gap·QA를 Evidence Bundle로 묶는다.
12. HANDOFF_READY는 Writing·Fact Checking·Publishing의 최종 승인이 아님을 명시한다.
```

이 압축 블록은 상세 Workflow의 파생본이다. 충돌하면 본문과 상위 LOCKED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-001은 조사 실행의 순서와 기록 계약만 정의한다.
- Source 신뢰·직접성·인용 판단은 COR-004를 따른다.
- 프로젝트별 후보 적격성·우선순위·수량은 해당 Project Rules가 정한다.
- 문장 작성은 CNT-002, 편집은 CNT-003, 최종 사실 검증은 CNT-004가 맡는다.
- 게시와 운영 반영은 CNT-006과 Phase 5 Automation의 별도 Gate를 통과해야 한다.

## 19.2 알려진 제한

- Source 접근 가능성은 실행 환경, 권한, 지역과 시점에 따라 달라질 수 있다.
- 모든 주제에 동일한 수의 Source나 동일한 조사 시간을 강제하지 않는다.
- 이 문서만으로 법률·의료·재무 등 고위험 전문 판단을 승인하지 않는다.
- `HANDOFF_READY`는 실제 콘텐츠 정확성이나 운영 배포를 보증하지 않는다.
- 특정 프로젝트의 Schema와 저장 형식은 후속 Project 문서에서 정의한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 조사 입력·수명주기·기록물·Claim·Source·충돌·최신성·중단·인계 Workflow와 RSH-051~080 작성; 사용자 명시적 승인 반영 |
