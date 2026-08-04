# JCOS v2.0.0 - CNT-004 FACT CHECKING

## 범용 Claim·Source 독립 검증·판정·교정·인계 절차

| Field | Value |
|---|---|
| Document ID | CNT-004 |
| Title | FACT CHECKING |
| Korean Title | 범용 Claim·Source 독립 검증·판정·교정·인계 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | Editorial Candidate와 파생 Variant의 검증 가능한 Claim·Source·귀속·수치·인용 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~003 v2.0.0 LOCKED |
| Extends | COR-004 SOURCE POLICY SRC-001~050 |
| Depends On | COR-004 SOURCE POLICY, COR-005 QUALITY GATE, CNT-001 RESEARCH WORKFLOW, CNT-003 EDITORIAL WORKFLOW |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-004 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-004는 CNT-003이 인계한 Editorial Candidate의 사실 주장, 수치, 날짜, 이름, 인용, 귀속과 Source 연결을 독립적으로 검증하는 표준 절차를 정의한다. 결과는 각 Claim의 판정과 근거, 발견된 결함, 교정과 재검증 이력이 추적 가능한 Fact Check Report여야 한다.

이 문서는 사실을 새롭게 창작하거나 문장을 더 매력적으로 만드는 방법을 정하지 않는다. 무엇을 검증하고, 어떤 Source를 실제로 확인하며, 불일치와 불확실성을 어떻게 판정하고, 어떤 조건에서 후속 단계에 인계할지를 정한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Fact Check Request와 Editorial Candidate Binding
- 검증 전 Candidate Snapshot과 Claim Inventory 생성
- Claim 원자화·분류·위험도·우선순위 지정
- Claim별 Verification Plan과 Source 독립성 확인
- Source 접근·정체성·시점·위치·내용 일치 검사
- 수치·날짜·이름·직함·인용·귀속·맥락 검증
- 충돌 Source·불확실성·추론·최신성 처리
- Claim Verdict와 Finding 심각도 판정
- 교정 요청·반영 확인·재검증·Variant 전파 검사
- Fact Check QA와 Content Ready Handoff

## 2.2 비범위

- 근거 없는 Claim, 통계, 인용 또는 Source의 생성
- Writer·Owner의 목적·핵심 메시지·결론을 임의 변경
- 법률·의료·재무 등 전문 자격자의 최종 판단 대체
- SEO 키워드·검색 제목·메타데이터 최적화
- 공개 승인·게시·배포·정정 공지와 운영 Release
- 특정 검색식·API·Prompt·모델·도구 설정 강제

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| Source 등급·기록·충돌의 공통 원칙 | COR-004 SOURCE POLICY |
| 결함 등급·Gate 판정 | COR-005 QUALITY GATE |
| 조사 계획·Evidence Pack·근거 공백 | CNT-001 RESEARCH WORKFLOW |
| 구조·문장·표기 편집과 Candidate 생성 | CNT-003 EDITORIAL WORKFLOW |
| Claim·Source 독립 재검증과 교정 확인 | CNT-004 FACT CHECKING |
| 제목·검색·태그 최적화 | CNT-005 SEO SYSTEM |
| 공개·배포·정정 공지 | CNT-006 PUBLISHING SYSTEM |
| 프로젝트 고유 임계값·승인자·전문 검토 | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Fact Check Request | 대상·범위·기준 시점·위험·인계 대상을 지정한 검증 요청 |
| Baseline Candidate | 검증 시작 시 버전과 해시를 고정한 Editorial Candidate |
| Claim Inventory | 검증 대상 Claim의 위치·유형·위험·Source·상태 목록 |
| Critical Claim | 오류가 안전·권리·평판·금전·핵심 결론에 중대한 영향을 주는 Claim |
| Verification Plan | Claim별 확인 항목·Source·방법·완료 조건의 계획 |
| Evidence Match | Source 내용이 Claim의 대상·범위·시점·강도를 직접 지지하는 관계 |
| Independent Source | 다른 Source의 반복 인용이 아니라 별도 원자료나 독립 검증에 근거한 Source |
| Verdict | Claim별 VERIFIED·PARTIAL·UNVERIFIED·CONFLICT·INCORRECT 판정 |
| Finding | 검증 중 발견한 결함·공백·충돌·교정 필요 항목 |
| Correction | 승인된 의미를 보존하며 오류를 고친 변경 |
| Recheck | 교정본과 영향받은 Claim·Variant를 다시 검증하는 절차 |
| Fact Check Report | Claim Verdict·근거·Finding·교정·제한·QA를 묶은 기록 |

# 4. 입력 계약과 검증 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| fact_check_request_id | 검증 실행 고유 식별자 |
| target_candidate_ref | Editorial Candidate 위치·버전·해시 |
| editorial_handoff_ref | CNT-003 Fact Check Handoff 위치 |
| verification_scope | 전체·표본·Critical Claim 등 검증 범위 |
| as_of | 사실 판단 기준 날짜·시간대 |
| claim_trace | Candidate 문장·Claim ID·Source ID 연결 |
| source_records | Source 정체성·위치·접근 시점·상태 |
| risk_profile | Critical Claim·민감 주제·전문 검토 영역 |
| binding | 적용 기준본 ID·버전·상태 |

대상 Candidate가 하나로 식별되지 않거나 기준 시점·Claim Trace·핵심 Source가 누락되면 추정으로 진행하지 않는다. 판정에 영향을 주는 누락은 `BLOCKED` 또는 Query로 기록한다.

## 4.2 검증 상태

| 상태 | 의미 |
|---|---|
| READY | 요청·Binding·Baseline 확인 완료 |
| CHECKING | Claim과 Source 검증 중 |
| QUERY | 의미·범위·근거 확인 대기 |
| CORRECTION_REQUIRED | 오류 또는 근거 공백의 교정 필요 |
| RECHECK | 교정본 재검증 중 |
| QA_REVIEW | Fact Check QA 수행 중 |
| CONTENT_READY | Critical 결함 없이 후속 단계 인계 가능 |
| BLOCKED | 필수 입력·접근·권한·결정 부재로 중단 |
| SUPERSEDED | 새 Candidate 또는 검증 실행으로 대체됨 |

# 5. 표준 Fact Check 수명주기

1. Fact Check Request를 등록하고 대상 Candidate를 식별한다.
2. 적용 Core·Content·Project 기준본과 기준 시점을 Binding한다.
3. CNT-003 Handoff와 Editorial QA를 확인한다.
4. Candidate 버전·해시를 Baseline으로 고정한다.
5. Claim Inventory를 만들고 Claim을 검증 가능한 단위로 나눈다.
6. 유형·영향·가역성에 따라 위험도와 우선순위를 정한다.
7. Claim별 Verification Plan과 필요한 Source 독립성을 정한다.
8. Source에 실제 접근해 정체성·시점·위치·내용을 확인한다.
9. Claim의 대상·범위·수치·날짜·이름·귀속·맥락을 대조한다.
10. 각 Claim에 하나의 Verdict와 근거를 기록한다.
11. 충돌·공백·오류를 Finding으로 만들고 교정을 요청한다.
12. 교정본과 영향받은 Claim·Variant를 Recheck한다.
13. Fact Check QA를 수행하고 Fact Check Report를 고정한다.
14. Candidate·Report·제한·열린 항목을 후속 Content 단계에 인계한다.

순서는 위험 기반으로 조정할 수 있으나 Baseline과 Claim Inventory 없이 판정을 시작하지 않는다. 교정 후에는 이전 Verdict를 조용히 덮어쓰지 않고 Recheck 이력을 남긴다.

# 6. Preflight와 Baseline

## 6.1 Candidate 단일성

CNT-003이 `FACT_CHECK_READY`로 인계한 하나의 Editorial Candidate를 확인한다. Candidate ID·버전·해시·언어·Variant 관계와 기준 시점을 기록한다.

## 6.2 인계물 확인

- Editorial Request와 적용 Binding
- Baseline Draft와 Editorial Candidate
- Claim Trace와 Source Record
- Change Log와 Semantic Change 승인 근거
- Issue·Query·Accepted Risk Log
- Variant Map과 Editorial QA

## 6.3 Baseline Snapshot

검증 전 Candidate를 덮어쓰지 않고 보존한다. 검증 결과와 교정본은 이 Baseline을 기준으로 비교할 수 있어야 하며 새 Candidate가 도착하면 새 실행으로 식별하거나 명시적으로 Supersede한다.

# 7. Claim Inventory와 우선순위

## 7.1 Claim 원자화

한 문장에 독립적으로 참·거짓을 판정할 수 있는 사실 요소가 여러 개면 Claim을 나눈다. 수사적 표현이나 의견 속에 포함된 검증 가능한 전제도 별도 Claim으로 기록한다.

## 7.2 Claim Record

| 필드 | 내용 |
|---|---|
| claim_id | 검증 Claim 고유 ID |
| target_ref | Candidate 문장·표·캡션·Variant 위치 |
| claim_text | 검증 시점의 정확한 Claim 표현 |
| claim_type | FACT·ATTRIBUTED_CLAIM·NUMBER·DATE·NAME·QUOTE·CAUSAL·OUTLOOK |
| risk | CRITICAL·HIGH·MEDIUM·LOW |
| source_ids | 연결된 Source ID 목록 |
| verdict | VERIFIED·PARTIAL·UNVERIFIED·CONFLICT·INCORRECT |
| finding_refs | 관련 Finding·Correction·Recheck 참조 |

## 7.3 위험도와 순서

안전·권리·금전·평판·법적 의무, 핵심 결론, 제목·리드, 큰 수치와 직접 인용을 우선 검증한다. 빈도나 문장 위치만으로 위험을 낮추지 않는다.

# 8. Verification Plan과 Source 독립성

## 8.1 Claim별 계획

각 Claim에 확인할 사실 요소, 필요한 Source 유형, 최소 독립성, 기준 시점, 검증 방법과 완료 조건을 기록한다. 모든 Claim에 같은 Source 수를 강제하지 않는다.

## 8.2 Source 계층

가능하면 원문·공식 기록·원자료를 먼저 확인한다. 2차 Source는 맥락·해석·교차 확인에 사용할 수 있으나 원자료를 보지 못한 사실을 숨기지 않는다.

## 8.3 독립성 판정

여러 매체가 같은 보도자료·통신 기사·데이터셋을 반복하면 하나의 근거 계열로 본다. 도메인 수가 아니라 기원과 검증 경로의 독립성을 확인한다.

# 9. Source 접근과 Evidence Match

## 9.1 실제 접근

제목·요약·검색 결과만으로 본문을 확인했다고 기록하지 않는다. 접근한 Source의 식별자, 버전 또는 발행 시점, 접근 시점, 정확한 위치와 접근 제한을 남긴다.

## 9.2 위치와 내용

페이지·섹션·문단·표·행·타임코드 등 재확인 가능한 Locator를 기록한다. 링크 목적지와 기록한 Source가 다르거나 내용이 변경됐으면 상태를 갱신한다.

## 9.3 Evidence Match

Source가 Claim의 대상, 범위, 기간, 단위, 조건, 예외와 강도를 직접 지지하는지 확인한다. 관련 주제를 다룬다는 이유만으로 Claim을 VERIFIED로 판정하지 않는다.

# 10. Claim 유형별 검증

## 10.1 수치와 계산

값·단위·분모·기간·표본·통화·환율·반올림을 확인하고 파생 수치는 계산을 재현한다. 백분율과 퍼센트포인트, 명목값과 실질값을 구분한다.

## 10.2 날짜·이름·직함

절대 날짜, 시간대, 효력 발생일과 기준 시점을 구분한다. 사람·조직·제품의 공식 명칭과 해당 시점의 직함·상태를 확인한다.

## 10.3 인용과 귀속

인용문은 원문과 허용 범위에서 대조하고 화자·매체·날짜·맥락을 확인한다. 생략이나 번역이 의미·강도·조건을 바꾸지 않아야 한다.

## 10.4 인과·비교·최상급

상관관계를 인과로, 제한된 비교를 전체 우위로 확대하지 않는다. `최초`, `유일`, `최대` 같은 최상급은 비교 집합과 기준 시점을 함께 검증한다.

# 11. 충돌·불확실성·추론

## 11.1 Source 충돌

신뢰 가능한 Source가 다르면 차이를 삭제하거나 임의 평균하지 않는다. 정의·시점·범위·방법의 차이를 분석하고 해소되지 않으면 `CONFLICT`와 잔여 위험을 기록한다.

## 11.2 불확실성과 최신성

잠정치·추정치·예측·변경 가능한 상태는 확정 사실과 구분한다. 기준 시점 이후 변경 가능성이 큰 Claim은 재확인 기한이나 게시 전 재검증 조건을 둔다.

## 11.3 사실과 추론

Source에 직접 적힌 사실과 작성자의 해석·계산·전망을 분리한다. 추론은 전제와 방법을 기록하고 Source가 결론 전체를 직접 말했다고 귀속하지 않는다.

# 12. Verdict와 Finding

## 12.1 Claim Verdict

| Verdict | 판정 기준 |
|---|---|
| VERIFIED | 적절한 Evidence가 Claim의 전체 범위와 강도를 지지함 |
| PARTIAL | 일부 요소는 지지되나 범위·시점·조건·표현 보완이 필요함 |
| UNVERIFIED | 접근 가능한 근거로 확인할 수 없거나 근거가 부족함 |
| CONFLICT | 신뢰 가능한 Source 간 불일치가 해소되지 않음 |
| INCORRECT | 적절한 Evidence가 Claim의 핵심 요소와 모순됨 |

Verdict는 Source의 명성만이 아니라 실제 Evidence Match에 근거한다. `PARTIAL`, `UNVERIFIED`, `CONFLICT`는 VERIFIED로 계산하지 않는다.

## 12.2 Finding Record

| 필드 | 내용 |
|---|---|
| finding_id | 검증 Finding 고유 ID |
| claim_id | 영향받는 Claim |
| severity | CRITICAL·MAJOR·MINOR |
| issue_type | WRONG·UNSUPPORTED·CONFLICT·OUTDATED·MISQUOTE·MISSING_CONTEXT |
| evidence | Source·Locator·비교·계산 근거 |
| required_action | 삭제·정정·완화·귀속·추가 Source·전문 검토 |
| owner | Writer·Editor·Research·Owner·Specialist |
| status | OPEN·CORRECTED·RECHECKED·BLOCKED |

# 13. 교정과 Recheck

## 13.1 Correction Request

교정 요청은 문제 문장, 판정 근거, 필요한 변경 범위와 금지되는 의미 확장을 명시한다. Fact Checker는 승인 권한이 없는 핵심 메시지 변경을 조용히 확정하지 않는다.

## 13.2 교정 기록

교정 전·후, 이유, 영향받는 Claim·Source·Variant, 수행자와 승인 시점을 기록한다. Source만 교체해 기존 Claim의 범위가 계속 지지되지 않는 상태를 해결로 표시하지 않는다.

## 13.3 Recheck

교정된 Claim과 주변 문맥, 제목·요약·표·캡션·Variant를 다시 검증한다. Recheck 결과는 새 Verdict, 확인자, 시점과 근거를 가져야 한다.

# 14. Variant와 파생물 일관성

Canonical Candidate에서 승인된 사실 교정은 영향받는 모든 Variant에 전파한다. 축약본이 조건·귀속·불확실성을 잃어 더 강한 Claim이 되면 별도 Finding으로 처리한다.

이미 생성된 이미지 문구, 표, 캡션, 요약, 메타 필드가 있으면 동일 Claim ID 또는 변경 전 표현을 검색해 영향 범위를 확인한다. 확인하지 못한 파생물은 제한으로 공개한다.

# 15. Content Ready Handoff

## 15.1 필수 인계물

| 인계물 | 최소 내용 |
|---|---|
| Fact Check Request | 대상·범위·기준 시점·위험 |
| Binding | 적용 기준본 ID·버전·상태 |
| Baseline Candidate | 검증 전 버전·해시 |
| Checked Candidate | 교정·재검증 후 버전·해시 |
| Claim Inventory | Claim 위치·유형·위험·Verdict |
| Source Records | Source 정체성·Locator·접근·상태 |
| Finding and Correction Log | 결함·조치·승인·Recheck |
| Variant Impact Map | 영향받은 파생물과 반영 상태 |
| Fact Check Report | Gate 판정·제한·재확인 조건 |

## 15.2 인계 조건

- Checked Candidate가 하나로 식별된다.
- 모든 Critical Claim에 판정과 근거가 있다.
- 열린 Critical Finding과 `INCORRECT` Claim이 없다.
- 교정된 Claim과 영향받은 Variant의 Recheck가 완료됐다.
- `PARTIAL`·`UNVERIFIED`·`CONFLICT`는 표현·제한·승인 조건이 명시됐다.
- Source 접근 제한과 기준 시점 이후 재확인 조건이 공개됐다.

`CONTENT_READY`는 SEO 승인, 공개 승인, 전문 자격자의 법적·의료·재무 판단 또는 게시 완료를 의미하지 않는다.

# 16. Fact Check QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 대상·범위·기준 시점·위험 추적 가능 |
| G2 Baseline | Candidate·버전·해시 단일 고정 |
| G3 Inventory | Claim 원자화·유형·위험·위치 완결 |
| G4 Source | 실제 접근·정체성·Locator·독립성 확인 |
| G5 Match | 범위·수치·날짜·이름·인용·맥락 대조 |
| G6 Verdict | 모든 대상 Claim에 근거 기반 판정 존재 |
| G7 Correction | Finding·교정·Recheck·Variant 전파 완결 |
| G8 Handoff | Candidate·Report·제한·재확인 조건 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 뒤의 두 상태는 PASS로 계산하지 않는다.

## 16.2 Critical 결함

- Critical Claim에 Source·Locator·Verdict가 없음
- `INCORRECT` 또는 중대한 `UNVERIFIED` Claim이 독자용 Candidate에 남음
- Source를 실제 확인하지 않고 VERIFIED로 판정함
- 수치·인용·귀속·조건을 근거와 다르게 전달함
- 교정 후 Canonical과 Variant가 서로 다른 사실을 유지함
- 검증 기준 시점이나 Candidate를 식별할 수 없음

Critical 결함이 열려 있으면 `CONTENT_READY`로 표시하지 않는다.

# 17. 실행 규칙 (SRC-051 ~ SRC-080)

## 17.A 요청과 Baseline (SRC-051 ~ SRC-055)

### SRC-051 - 검증 요청 식별
- **Statement:** 모든 Fact Check 실행은 고유 fact_check_request_id, 대상 Candidate와 검증 범위를 가져야 한다.
- **Verification:** Fact Check Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### SRC-052 - 기준본 Binding
- **Statement:** 검증 전에 적용할 Core·Content·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding과 실제 기준 파일을 대조한다.
- **Exceptions:** 없음.

### SRC-053 - Candidate 단일성
- **Statement:** 검증 시작 전에 하나의 Baseline Candidate를 ID·버전·해시로 식별해야 한다.
- **Verification:** target_candidate_ref와 파일 해시를 확인한다.
- **Exceptions:** 병렬 언어본은 각각의 Candidate와 관계를 명시한다.

### SRC-054 - Editorial Handoff
- **Statement:** CNT-003 Handoff의 Candidate·Claim Trace·Change·Issue·Variant·QA를 확인해야 한다.
- **Verification:** editorial_handoff_ref와 manifest를 검사한다.
- **Exceptions:** 없음.

### SRC-055 - 기준 시점 고정
- **Statement:** 시간에 따라 변할 수 있는 사실을 판정하기 전에 as_of와 시간대를 명시해야 한다.
- **Verification:** Request·Candidate·Source Record의 기준 시점을 대조한다.
- **Exceptions:** 시점과 무관한 정의적 Claim은 NOT_APPLICABLE 근거를 남긴다.

## 17.B Claim Inventory와 계획 (SRC-056 ~ SRC-060)

### SRC-056 - Claim 원자화
- **Statement:** 독립적으로 판정 가능한 사실 요소는 고유 Claim ID로 분리해야 한다.
- **Verification:** 복합 문장·표 행·캡션과 Claim Inventory를 대조한다.
- **Exceptions:** 분리하면 의미가 왜곡되는 인용은 하나로 유지하고 내부 요소를 기록한다.

### SRC-057 - Critical Claim 우선
- **Statement:** 안전·권리·금전·평판·핵심 결론에 중대한 Claim을 먼저 식별하고 검증해야 한다.
- **Verification:** risk와 우선순위 근거를 검사한다.
- **Exceptions:** 없음.

### SRC-058 - Claim 유형 명시
- **Statement:** 각 Claim은 사실·귀속·수치·날짜·이름·인용·인과·전망 등 검증 방법을 결정하는 유형을 가져야 한다.
- **Verification:** claim_type과 Verification Plan을 대조한다.
- **Exceptions:** 복합 유형은 주 유형과 보조 유형을 함께 기록한다.

### SRC-059 - Trace 완결성
- **Statement:** 모든 대상 Claim은 Candidate 위치와 Source ID 또는 근거 공백으로 추적 가능해야 한다.
- **Verification:** Claim Inventory의 고아 Claim·고아 Source 참조를 검사한다.
- **Exceptions:** 없음.

### SRC-060 - Claim별 Verification Plan
- **Statement:** 각 Claim은 확인 요소·Source 유형·독립성·방법·완료 조건을 가져야 한다.
- **Verification:** Plan과 실제 Verification Record를 대조한다.
- **Exceptions:** 동일 형식의 저위험 반복 항목은 공통 Plan을 참조할 수 있다.

## 17.C Source와 Evidence (SRC-061 ~ SRC-065)

### SRC-061 - Source 실제 접근
- **Statement:** VERIFIED 판정에 사용한 Source는 Fact Checker가 실제 내용에 접근해 확인해야 한다.
- **Verification:** 접근 시점·방법·제한과 Locator를 검사한다.
- **Exceptions:** 접근 불가 시 UNVERIFIED 또는 제한으로 기록하며 VERIFIED로 판정하지 않는다.

### SRC-062 - Source 정체성과 Locator
- **Statement:** Source의 작성 주체·제목·버전·발행 시점·위치와 재확인 가능한 Locator를 기록해야 한다.
- **Verification:** Source Record와 실제 목적지를 대조한다.
- **Exceptions:** 위치 체계가 없는 Source는 인용 구절이 아닌 재현 가능한 대체 위치를 기록한다.

### SRC-063 - Source 독립성
- **Statement:** 복수 근거가 필요할 때 동일 원자료를 반복한 Source를 독립 근거로 계산하지 않아야 한다.
- **Verification:** 출처 계보와 인용·데이터 기원을 확인한다.
- **Exceptions:** 단일 권위 원자료로 충분한 Claim은 그 이유를 기록한다.

### SRC-064 - 시점·지역·버전 적합성
- **Statement:** Source는 Claim의 기준 시점·지역·언어·제품 또는 정책 버전과 맞아야 한다.
- **Verification:** Claim 조건과 Source 메타데이터를 대조한다.
- **Exceptions:** 과거 비교 Source는 비교 목적과 차이를 명시한다.

### SRC-065 - Evidence 범위 일치
- **Statement:** Evidence는 Claim의 대상·범위·기간·단위·조건·예외·강도를 직접 지지해야 한다.
- **Verification:** Claim 문구와 Source Locator의 내용을 요소별로 대조한다.
- **Exceptions:** 여러 Source를 조합한 추론은 각 전제와 계산을 분리 기록한다.

## 17.D 검증과 Verdict (SRC-066 ~ SRC-070)

### SRC-066 - Claim·Source 대조
- **Statement:** 관련 주제를 다룬다는 이유만으로 Source가 Claim을 지지한다고 판정하지 않아야 한다.
- **Verification:** Evidence Match 기록의 요소별 일치 여부를 검사한다.
- **Exceptions:** 없음.

### SRC-067 - 수치 재현
- **Statement:** 수치 Claim은 값·단위·분모·기간·표본·통화·반올림과 파생 계산을 확인해야 한다.
- **Verification:** Source 원값과 재계산 기록을 대조한다.
- **Exceptions:** 계산이 없는 직접 값은 원값 위치를 기록한다.

### SRC-068 - 인용·귀속·맥락
- **Statement:** 직접·간접 인용은 화자·원문·날짜·맥락·생략·번역이 의미를 보존해야 한다.
- **Verification:** Candidate와 원 Source를 나란히 대조한다.
- **Exceptions:** 공개할 수 없는 Source는 검증 책임자와 제한을 기록하되 독자에게 허위 공개 근거를 제시하지 않는다.

### SRC-069 - 사실·추론·전망 분리
- **Statement:** Source의 사실, 작성자의 계산·해석, 미래 전망을 서로 다른 근거 수준으로 표시해야 한다.
- **Verification:** Claim type·귀속·불확실성 표기와 Source 내용을 확인한다.
- **Exceptions:** 없음.

### SRC-070 - 단일 Verdict
- **Statement:** 검증 대상 각 Claim은 근거 강도에 맞는 하나의 현재 Verdict를 가져야 한다.
- **Verification:** Claim Inventory의 누락·중복·상충 Verdict를 검사한다.
- **Exceptions:** 이전 Verdict는 History에 보존하되 현재 판정과 구분한다.

## 17.E 충돌·교정·Recheck (SRC-071 ~ SRC-075)

### SRC-071 - Source 충돌 보존
- **Statement:** 신뢰 가능한 Source 간 불일치를 삭제·평균·임의 선택하지 않고 차이와 잔여 위험을 기록해야 한다.
- **Verification:** Conflict Record와 선택 또는 미해결 근거를 검사한다.
- **Exceptions:** 명백히 철회·정정된 Source는 상태와 근거를 기록하고 제외할 수 있다.

### SRC-072 - 미검증 Critical 차단
- **Statement:** Critical Claim이 INCORRECT·UNVERIFIED·CONFLICT이면 해결 또는 명시적 범위 제거 전 CONTENT_READY로 표시하지 않아야 한다.
- **Verification:** Critical Claim Verdict와 Candidate 상태를 대조한다.
- **Exceptions:** 없음.

### SRC-073 - Correction 추적
- **Statement:** 모든 사실 교정은 변경 전·후·이유·Claim·Source·수행자·승인 시점을 기록해야 한다.
- **Verification:** Correction Log와 Candidate diff를 대조한다.
- **Exceptions:** 동일 원인의 반복 표기 교정은 범위가 명확하면 묶어 기록할 수 있다.

### SRC-074 - 교정 후 Recheck
- **Statement:** 교정된 Claim은 주변 문맥과 함께 다시 검증하고 새 Verdict·근거·시점을 기록해야 한다.
- **Verification:** Correction과 Recheck Record의 일대일 연결을 검사한다.
- **Exceptions:** 없음.

### SRC-075 - Variant 전파
- **Statement:** 사실 교정은 영향받는 제목·요약·표·캡션·언어본·채널 Variant에 전파하고 확인해야 한다.
- **Verification:** Variant Impact Map과 각 결과물을 대조한다.
- **Exceptions:** 폐기된 Variant는 상태와 폐기 근거를 기록한다.

## 17.F QA와 인계 (SRC-076 ~ SRC-080)

### SRC-076 - Finding 심각도
- **Statement:** Fact Check Finding은 독자 영향과 회복 가능성에 따라 CRITICAL·MAJOR·MINOR로 분류해야 한다.
- **Verification:** Finding과 COR-005 등급 기준을 대조한다.
- **Exceptions:** 취향 차이는 Finding으로 분류하지 않는다.

### SRC-077 - Critical Gate
- **Statement:** 열린 Critical Finding 또는 INCORRECT Critical Claim이 있으면 CONTENT_READY Gate는 FAIL이어야 한다.
- **Verification:** Finding Log·Claim Inventory·Gate 결과를 대조한다.
- **Exceptions:** 없음.

### SRC-078 - Fact Check Report 완결성
- **Statement:** Report는 범위·Baseline·Claim Verdict·Source·Finding·Correction·Recheck·제한·QA를 포함해야 한다.
- **Verification:** Handoff 필수 인계물과 Report를 검사한다.
- **Exceptions:** 범위 밖 Claim은 제외 사유와 위치를 기록한다.

### SRC-079 - 후속 승인 분리
- **Statement:** CONTENT_READY를 SEO·Publishing·전문 검토 또는 공개 승인으로 해석하지 않아야 한다.
- **Verification:** 상태 정의와 Handoff 문구를 확인한다.
- **Exceptions:** 없음.

### SRC-080 - 검증 계보 보존
- **Statement:** Baseline Candidate부터 Checked Candidate까지 Claim·Source·Verdict·Correction·Recheck 계보를 재현할 수 있어야 한다.
- **Verification:** ID·버전·해시·참조 연결과 변경 이력을 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Fact Checking

```text
1. fact_check_request_id, Candidate ID·버전·해시, as_of, 범위와 Binding을 고정한다.
2. CNT-003 Handoff의 Claim Trace·Source·Change·Issue·Variant·QA를 확인한다.
3. Candidate를 보존하고 검증 가능한 사실 요소를 Claim ID로 원자화한다.
4. Critical Claim을 우선하며 유형·위험·Source·위치·완료 조건을 기록한다.
5. Source 원문에 실제 접근해 정체성·시점·버전·Locator와 독립성을 확인한다.
6. Claim의 대상·범위·기간·단위·조건·예외·강도를 Evidence와 대조한다.
7. 수치는 재계산하고 날짜·이름·직함·인용·귀속·맥락을 원자료와 확인한다.
8. 사실·추론·전망을 분리하고 충돌·불확실성·접근 제한을 보존한다.
9. 각 Claim에 VERIFIED·PARTIAL·UNVERIFIED·CONFLICT·INCORRECT 중 하나를 부여한다.
10. 오류와 공백은 Finding으로 기록하고 승인된 교정 전후와 근거를 남긴다.
11. 교정된 Claim과 제목·요약·표·캡션·Variant를 Recheck한다.
12. Critical 결함이 없을 때 Candidate·Report·제한·재확인 조건을 후속 단계에 인계한다.
```

이 압축 블록은 상세 Workflow의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-004는 인계된 Candidate의 Claim·Source 검증, 판정, 교정 확인과 기록 계약만 정의한다.
- 새로운 조사 설계와 Evidence Pack 보강은 CNT-001에 반환한다.
- 핵심 메시지·구조·문장 재작성은 CNT-002·003과 Owner 승인 경로를 따른다.
- SEO는 CNT-005, 공개·배포·정정 공지는 CNT-006이 맡는다.
- 전문 자격 판단과 Project 고유 허용 기준은 해당 Project 정책과 승인자가 결정한다.

## 19.2 알려진 제한

- 모든 Claim에 동일한 Source 수나 동일한 검증 시간을 강제하지 않는다.
- Source가 비공개·유료·삭제·변경됐을 때 접근 가능성을 보증하지 않는다.
- 자동 검색·요약·모델 응답은 Source 원문 확인과 독립 판정을 대체하지 않는다.
- `CONTENT_READY`는 절대적 진실, 미래 불변성, 전문 자문 또는 공개 가능성을 보증하지 않는다.
- 기준 시점 이후 변경 가능한 Claim은 게시 직전 재확인 절차가 필요할 수 있다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 검증 입력·Baseline·Claim Inventory·Source 독립성·Evidence Match·Verdict·Correction·Recheck·Variant·QA·Content Ready Handoff와 SRC-051~080 작성; 사용자 명시적 승인 반영 |
