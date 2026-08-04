# JCOS v2.0.0 - CNT-003 EDITORIAL WORKFLOW

## 범용 구조 편집·문장 편집·교정·인계 절차

| Field | Value |
|---|---|
| Document ID | CNT-003 |
| Title | EDITORIAL WORKFLOW |
| Korean Title | 범용 구조 편집·문장 편집·교정·인계 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | JCOS Canonical Draft와 채널 Variant의 구조·문장·표기·일관성 편집 |
| Priority | HIGH |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~002 v2.0.0 LOCKED |
| Extends | COR-002·CNT-002 WRT-001~080 |
| Depends On | COR-002 WRITING PRINCIPLES, COR-005 QUALITY GATE, CNT-001 RESEARCH WORKFLOW, CNT-002 WRITING WORKFLOW |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-003 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-003은 CNT-002의 Canonical Draft와 Editorial Handoff를 구조 편집, 문장 편집, Copy Edit와 일관성 검수로 처리하는 표준 절차를 정의한다. 편집 결과는 원문의 목적과 Claim 의미를 보존하면서 더 명확하고 일관되며 검수 가능한 Editorial Candidate가 되어야 한다.

이 문서는 편집자가 무엇을 더 좋아하는지 정하지 않는다. 어떤 순서로 편집하고, 어떤 변경을 직접 수행하며, 어떤 변경을 Writer·Research·Fact Checking에 반환하고, 무엇을 증거로 남길지를 정한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Editorial Request와 기준본 Binding
- Canonical Draft·Variant·Writing QA 인계 확인
- 기준 원고 Snapshot과 Issue Inventory 생성
- 구조·정보 순서·섹션 역할·중복 편집
- 문장 명료성·흐름·어조·용어·표기 편집
- 제목·리드·요약·결론·목록·표의 역할 정합성
- Claim Trace·귀속·불확실성 보존 검사
- 의미 변경과 비의미 변경 분류·승인·기록
- Variant 간 의미·상태·표기 일관성 검사
- Editorial QA와 Fact Check Handoff

## 2.2 비범위

- 새로운 조사, Source 선정 또는 Claim 검증 상태 확정
- Writer의 목적·핵심 메시지·Project Schema를 임의 재정의
- 독립 Fact Check, SEO 최적화, 채널 게시·배포
- DOCX·HTML·CSS의 시각 디자인 변경
- 특정 교정 도구의 설정·사전·API·Prompt 구문
- Runtime 자동화와 운영 Release

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 문장·구조·어조의 공통 원칙 | COR-002 WRITING PRINCIPLES |
| 결함 등급·Gate 판정 | COR-005 QUALITY GATE |
| 조사 기록·근거 공백 | CNT-001 RESEARCH WORKFLOW |
| 메시지·Outline·Canonical Draft 작성 | CNT-002 WRITING WORKFLOW |
| 구조·문장·표기·일관성 편집 | CNT-003 EDITORIAL WORKFLOW |
| Claim·Source 독립 재검증 | CNT-004 FACT CHECKING |
| 제목·검색·태그 최적화 | CNT-005 SEO SYSTEM |
| 공개·배포·정정 공지 | CNT-006 PUBLISHING SYSTEM |
| 프로젝트 고유 필드·문체·금지어 | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Editorial Request | 편집 대상·목적·범위·기한·인계 대상을 지정한 요청 |
| Baseline Draft | 편집 시작 시 해시와 버전을 고정한 Canonical Draft |
| Editorial Brief | 편집 목표·우선순위·허용 범위·Style Sheet를 고정한 계약 |
| Editorial Pass | 구조·문장·Copy·일관성 등 하나의 목적을 가진 편집 회차 |
| Editorial Issue | 원고의 결함·모호성·충돌·결정 필요를 추적하는 항목 |
| Semantic Change | Claim 의미·범위·강도·조건·귀속·결론을 바꾸는 변경 |
| Non-semantic Change | 의미를 유지하며 명료성·문법·표기를 개선하는 변경 |
| Change Record | 변경 전·후·이유·적용 Rule·영향·승인을 기록한 항목 |
| Query | Editor가 Writer·Research·Owner에게 보내는 판단 요청 |
| Editorial Candidate | 편집 QA를 통과해 Fact Checking에 전달 가능한 원고 |
| Fact Check Handoff | Candidate·Claim Trace·변경·열린 이슈·QA의 인계 묶음 |

# 4. 입력 계약과 편집 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| editorial_request_id | 편집 실행 고유 식별자 |
| target_draft_ref | Canonical Draft 위치·버전·해시 |
| writing_handoff_ref | CNT-002 Editorial Handoff 위치 |
| editorial_scope | 구조·문장·Copy·일관성 등 허용 범위 |
| output_contract | 필수 구조·필드·Variant·금지 항목 |
| style_sheet | 용어·이름·수치·날짜·문장부호·Brand Voice |
| binding | 적용 기준본 ID·버전·상태 |
| risk_profile | Critical Claim·민감 표현·고위험 영역 |
| deadline_or_as_of | 편집 기한 또는 콘텐츠 기준 시점 |

필수 입력이 없거나 여러 Canonical Draft가 동시에 기준으로 제시되면 하나를 임의 선택하지 않는다. 편집 결과를 바꿀 수 있는 누락은 `BLOCKED` 또는 Query로 처리한다.

## 4.2 편집 상태

| 상태 | 의미 |
|---|---|
| READY | 입력·Binding·Baseline 확인 완료 |
| STRUCTURE_EDIT | 구조·순서·중복 편집 중 |
| LINE_EDIT | 문장·문단·흐름 편집 중 |
| COPY_EDIT | 문법·용어·표기·링크 편집 중 |
| ISSUE_HOLD | 의미 결정·근거·승인을 기다림 |
| SELF_REVIEW | 편집자 자체 QA 중 |
| FACT_CHECK_READY | Editorial Candidate와 인계물 준비 완료 |
| SUPERSEDED | 새 편집 실행 또는 정정본으로 대체됨 |

# 5. 표준 편집 수명주기

1. Editorial Request를 등록하고 대상 Draft를 식별한다.
2. 적용 기준본·Output Contract·Style Sheet를 Binding한다.
3. CNT-002 Editorial Handoff와 Writing QA를 확인한다.
4. Canonical Draft의 버전·해시를 Baseline으로 고정한다.
5. Editorial Brief와 편집 허용 범위를 확정한다.
6. Issue Inventory를 만들고 심각도·책임·상태를 부여한다.
7. 구조·정보 순서·섹션 역할·중복을 편집한다.
8. 문단·문장·어조·연결과 독자 명료성을 편집한다.
9. 용어·이름·수치·날짜·문장부호·링크를 Copy Edit한다.
10. Claim Trace·귀속·불확실성·Variant 정합성을 검사한다.
11. Semantic Change를 Writer·Research·Owner에게 Query한다.
12. 승인된 변경을 반영하고 Change Record를 완결한다.
13. Editorial QA를 수행하고 Editorial Candidate를 고정한다.
14. Candidate와 Fact Check Handoff를 CNT-004에 전달한다.

편집 회차는 목적별 순서를 유지한다. 구조가 확정되기 전에 세부 문장부호를 반복 교정하거나, Copy Edit 후 승인되지 않은 구조 개편을 추가하지 않는다.

# 6. Preflight와 Baseline

## 6.1 Canonical Draft 확인

CNT-002가 `EDITORIAL_READY`로 인계한 하나의 Canonical Draft를 확인한다. Draft ID·버전·해시·언어·Variant 관계와 작성 기준 시점을 기록한다.

## 6.2 인계물 확인

- Writing Request와 Output Contract
- Message Map과 Outline
- Canonical Draft와 Claim Trace
- Variant Map과 생략·변경 내역
- Open Issues와 Writing QA 판정
- Research Handoff 참조와 Critical Claim 목록

## 6.3 Baseline Snapshot

편집 전 Draft를 덮어쓰지 않고 Baseline으로 보존한다. 편집 결과와 Change Record는 이 Baseline을 기준으로 비교할 수 있어야 한다.

# 7. Editorial Brief와 Issue Inventory

## 7.1 Editorial Brief

| 필드 | 내용 |
|---|---|
| edit_goal | 이번 편집이 해결할 독자·품질 목표 |
| pass_scope | 수행할 편집 회차와 제외 범위 |
| protected_meaning | 바꾸면 안 되는 메시지·Claim·조건 |
| style_authority | 적용 Style Sheet·Brand Voice·금지어 |
| priority_sections | 위험·가치가 높은 섹션 |
| query_route | Writer·Research·Owner·Fact Check 반환 경로 |
| completion_criteria | FACT_CHECK_READY 판정 조건 |

## 7.2 Issue Record

| 필드 | 내용 |
|---|---|
| issue_id | 편집 이슈 고유 ID |
| target_ref | Draft Unit·문장·표·Variant 위치 |
| issue_type | STRUCTURE·CLARITY·CONSISTENCY·COPY·CLAIM·DECISION |
| severity | CRITICAL·MAJOR·MINOR |
| description | 관찰한 문제와 영향 |
| owner | Editor·Writer·Research·Owner·Fact Checker |
| status | OPEN·QUERY·RESOLVED·ACCEPTED_RISK·BLOCKED |
| evidence | 기준본·Claim·Style Sheet·비교 근거 |

취향 차이는 결함으로 기록하지 않는다. 독자 이해, 계약, 근거, 일관성 또는 검수 가능성에 미치는 영향을 설명할 수 있어야 한다.

# 8. 구조 편집

## 8.1 섹션 역할

각 섹션이 Output Contract와 Outline의 질문 하나를 해결하는지 확인한다. 역할 없는 섹션, 같은 기능을 반복하는 섹션과 본문에 연결되지 않는 장식 요소를 제거하거나 통합한다.

## 8.2 정보 순서

핵심 정보, 전제, 근거, 예외와 다음 단계가 선택한 논리에 맞게 이어지는지 확인한다. 중요한 조건을 독자가 결론을 읽은 뒤에야 발견하도록 숨기지 않는다.

## 8.3 제목 계층

제목 수준은 실제 포함 관계를 반영하며 건너뛰거나 같은 수준에서 역할을 섞지 않는다. 제목은 본문의 Claim보다 강하거나 넓지 않아야 한다.

## 8.4 Cardinality와 중복

실제 적격 내용에 따라 섹션·항목·표 행을 반복·병합·삭제한다. 고정 수량 계약이 없다면 빈 슬롯이나 중복 항목을 남기지 않는다.

# 9. 문장 편집

## 9.1 문단

문단당 하나의 중심 판단을 유지하고 주제문·근거·해석·전환의 관계를 명확히 한다. 서로 다른 시점이나 Claim을 한 문단에 무리하게 묶지 않는다.

## 9.2 문장

주체·행동·대상·조건을 명확히 하고 불필요한 명사화, 중첩 수식, 지시어와 반복을 줄인다. 짧게 만드는 것보다 의미와 검증 가능성을 보존하는 것이 우선이다.

## 9.3 어조와 독자

자신감 수준을 근거와 맞추고 독자를 과소평가하거나 감정적으로 몰아가지 않는다. Project Brand Voice는 Core 원칙과 충돌하지 않는 범위에서 적용한다.

## 9.4 의미 보호

FACT·ATTRIBUTED_CLAIM·INTERPRETATION·OUTLOOK의 역할, 귀속, 조건, 예외와 불확실성을 유지한다. 문장을 자연스럽게 만들기 위해 Claim 강도를 높이지 않는다.

# 10. Copy Edit와 일관성

## 10.1 Style Sheet

| 항목 | 검사 내용 |
|---|---|
| 용어·약어 | 승인 용어, 첫 사용 정의, 동의어 통제 |
| 고유명사 | 공식 표기·대소문자·띄어쓰기 |
| 수치·단위 | 값·단위·기간·분모·반올림 |
| 날짜·시간 | 절대 날짜, 시간대, 기준 시점 |
| 문장부호 | 언어·프로젝트 표기 규칙 |
| 링크 | 실제 목적지·표시 문구·Source 역할 |
| 제목 체계 | 수준·대소문자·평행 구조 |

## 10.2 목록과 표

목록 항목은 문법과 의미가 평행해야 한다. 표는 반복 비교 데이터에만 사용하고 열 제목, 단위, 행 의미와 Source 연결이 일관돼야 한다.

## 10.3 독자 접근성

제목만으로 구조를 탐색할 수 있고, 링크 문구가 목적을 설명하며, 색이나 위치만으로 의미를 전달하지 않는지 확인한다. 시각 구현 세부 기준은 DSG 문서를 따른다.

# 11. Claim Trace와 의미 변경

## 11.1 Claim Trace 검사

편집 후에도 핵심 문장을 원 Claim ID와 Source ID로 되돌릴 수 있어야 한다. 문장 분리·병합 시 Trace를 함께 갱신하고 고아 참조를 남기지 않는다.

## 11.2 Semantic Change

다음은 의미 변경으로 간주한다.

- 수치·단위·기간·대상·조건·예외 변경
- 가능성을 확정으로, 상관을 인과로 바꾸는 강도 변경
- 귀속 주체·발언 범위·Source 역할 변경
- 핵심 메시지·결론·권고·위험 수준 변경
- 중요한 제한·충돌·불확실성 삭제

Editor는 Semantic Change를 독자적으로 확정하지 않는다. Writer·Research·Owner 또는 Fact Checker에게 Query하고 승인 근거를 Change Record에 연결한다.

## 11.3 Non-semantic Change

맞춤법, 문법, 평행 구조, 중복 제거와 의미를 유지한 어순 개선은 허용 범위에서 직접 반영할 수 있다. 대량 또는 반복 변경은 적용 Rule과 범위를 묶어 기록한다.

# 12. Query와 변경 통제

## 12.1 Query Record

| 필드 | 내용 |
|---|---|
| query_id | 판단 요청 고유 ID |
| target_ref | 영향받는 Draft Unit·Claim·Variant |
| question | 필요한 결정 또는 확인 |
| options | 가능한 대안과 영향 |
| recommendation | Editor 제안과 근거 |
| owner | 응답 책임자 |
| status | OPEN·ANSWERED·BLOCKED·WITHDRAWN |
| decision_ref | 승인된 답변·근거·시점 |

## 12.2 Change Record

모든 Semantic Change와 중요한 일괄 변경은 변경 전·후, 이유, 적용 Rule, Claim·Variant 영향, 승인자와 시점을 가진다. 응답이 없다는 이유로 Editor 제안을 승인된 결정처럼 반영하지 않는다.

## 12.3 Accepted Risk

해결하지 않고 진행하는 이슈는 승인 주체, 사유, 영향, 만료 또는 재검토 조건을 기록한다. Critical 결함은 Accepted Risk로 우회할 수 없다.

# 13. Variant와 교차 원고 일관성

## 13.1 Canonical 우선

구조·의미 변경은 먼저 Canonical Draft에서 승인한다. Variant만 고쳐 기준 원고와 조용히 갈라지지 않는다.

## 13.2 Variant 비교

각 Variant의 제목·요약·수치·귀속·불확실성·링크와 생략 내용을 Canonical과 대조한다. 채널 제약으로 생략한 제한이 오해를 만들면 축약을 거부하거나 대안을 Query한다.

## 13.3 언어본

병렬 언어본은 각각의 Canonical과 번역·현지화 관계를 명시한다. 번역 과정의 의미 변경은 Non-semantic Change로 처리하지 않는다.

# 14. 내부 요소와 민감 정보

독자용 원고에서 Prompt, Placeholder, TODO, 검토 메모, 미승인 대안, 내부 점수와 접근 자격정보를 제거하거나 분리한다. 내부 전용 Variant는 독자용 파일과 물리적으로 구분한다.

개인정보·기밀·엠바고·법적 제한은 Project 정책과 권한 계약을 따른다. Editor가 공개 범위를 추정하지 않으며 불명확하면 `ISSUE_HOLD`로 반환한다.

# 15. Fact Check Handoff

## 15.1 필수 인계물

| 인계물 | 최소 내용 |
|---|---|
| Editorial Request | 대상·목적·범위·기한 |
| Binding | 적용 기준본 ID·버전·상태 |
| Baseline Draft | 편집 전 버전·해시 |
| Editorial Candidate | 편집 후 기준 원고·버전·해시 |
| Claim Trace | Candidate 문장·Claim·Source 연결 |
| Change Log | Semantic·일괄 변경과 승인 근거 |
| Issue and Query Log | 열린 이슈·결정·Accepted Risk |
| Variant Map | Canonical과 파생본 관계·차이 |
| Editorial QA | Gate 판정·결함·제한 |

## 15.2 인계 조건

- Editorial Candidate가 하나로 식별된다.
- Critical Editorial Issue와 열린 Semantic Query가 없다.
- 핵심 문장의 Claim Trace가 유효하다.
- Output Contract와 Style Sheet 검사가 완료됐다.
- 내부 요소와 미승인 대안이 독자용 원고에서 제거됐다.
- 후속 Fact Check 대상과 우선순위가 공개돼 있다.

`FACT_CHECK_READY`는 CNT-004 검증 통과, SEO 승인 또는 공개 가능 상태를 의미하지 않는다.

# 16. Editorial QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 대상·범위·목적·기한 추적 가능 |
| G2 Baseline | Canonical Draft·버전·해시 고정 |
| G3 Structure | 섹션 역할·순서·계층·Cardinality 정합 |
| G4 Language | 문단·문장·어조·명료성 정합 |
| G5 Copy | 용어·이름·수치·날짜·링크 정합 |
| G6 Meaning | Claim Trace·귀속·불확실성 보존 |
| G7 Change | Query·승인·Change Record 완결 |
| G8 Handoff | Candidate·Issue·Variant·QA 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 뒤의 두 상태는 PASS로 계산하지 않는다.

## 16.2 Critical 결함

- 승인 없이 Claim 의미·수치·조건·귀속·결론을 변경함
- UNVERIFIED·CONFLICT·INFERENCE를 확인된 FACT처럼 편집함
- 핵심 문장의 Claim Trace 또는 Source 연결이 끊김
- 여러 Draft 중 Canonical Candidate를 식별할 수 없음
- Prompt·Credential·민감 내부 메모가 독자용 원고에 남음

Critical 결함이 열려 있으면 `FACT_CHECK_READY`로 표시하지 않는다.

# 17. 실행 규칙 (WRT-081 ~ WRT-110)

## 17.A 요청과 Baseline (WRT-081 ~ WRT-085)

### WRT-081 - 편집 요청 식별
- **Statement:** 모든 편집 실행은 고유 editorial_request_id, 대상 Draft와 허용 범위를 가져야 한다.
- **Verification:** Editorial Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### WRT-082 - 기준본 Binding
- **Statement:** 편집 전에 적용할 Core·Content·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding과 실제 파일 상태를 대조한다.
- **Exceptions:** 없음.

### WRT-083 - Canonical 단일성
- **Statement:** 편집 시작 전에 하나의 Canonical Draft를 ID·버전·해시로 식별해야 한다.
- **Verification:** target_draft_ref와 Draft Registry를 확인한다.
- **Exceptions:** 병렬 언어본은 각 Canonical과 관계를 명시한다.

### WRT-084 - Writing Handoff
- **Statement:** CNT-002 Editorial Handoff의 Contract·Message·Claim Trace·Variant·Open Issues·QA를 확인해야 한다.
- **Verification:** writing_handoff_ref와 manifest를 검사한다.
- **Exceptions:** 없음.

### WRT-085 - Baseline 보존
- **Statement:** 편집 전 Draft를 덮어쓰지 않고 재현 가능한 Baseline으로 보존해야 한다.
- **Verification:** Baseline 경로·버전·해시와 현재 파일을 대조한다.
- **Exceptions:** 없음.

## 17.B 편집 회차와 구조 (WRT-086 ~ WRT-090)

### WRT-086 - 회차 순서
- **Statement:** 구조·문장·Copy·일관성 편집을 목적별 회차로 구분하고 승인된 순서를 유지해야 한다.
- **Verification:** Pass Log의 목적·순서·범위를 확인한다.
- **Exceptions:** 짧은 원고는 회차를 결합하되 검사 결과를 구분한다.

### WRT-087 - 섹션 역할
- **Statement:** 각 섹션은 Output Contract의 하나의 독자 질문 또는 정보 역할을 수행해야 한다.
- **Verification:** 제목·주제문·Claim과 Contract를 대조한다.
- **Exceptions:** 결론은 의미·제한·다음 단계를 함께 정리할 수 있다.

### WRT-088 - 정보 순서
- **Statement:** 핵심 정보·전제·근거·예외가 선택한 논리 순서로 이어지고 중요한 조건을 뒤에 숨기지 않아야 한다.
- **Verification:** Outline과 실제 섹션 흐름을 검사한다.
- **Exceptions:** 서사적 형식도 결론 오해를 만들면 순서를 조정한다.

### WRT-089 - 제목 계층
- **Statement:** 제목 수준은 실제 포함 관계를 반영하고 본문 Claim보다 강하거나 넓지 않아야 한다.
- **Verification:** Heading 구조와 Claim 범위를 대조한다.
- **Exceptions:** 채널이 제목 수준을 제한하면 의미 역할을 다른 구조로 보존한다.

### WRT-090 - Cardinality 정리
- **Statement:** 실제 적격 내용에 따라 섹션·항목·표 행을 반복·병합·삭제하고 빈 슬롯을 남기지 않아야 한다.
- **Verification:** Contract와 실제 Cardinality를 대조한다.
- **Exceptions:** 승인된 고정 수량 계약은 부족 상태를 BLOCKED로 기록한다.

## 17.C 문장과 의미 보호 (WRT-091 ~ WRT-095)

### WRT-091 - 회차 단일 목적
- **Statement:** 한 편집 회차에서 해결할 목적을 고정하고 무관한 대규모 변경을 섞지 않아야 한다.
- **Verification:** Pass Scope와 Change Log를 검사한다.
- **Exceptions:** 긴급 Critical 수정은 별도 표시 후 함께 반영할 수 있다.

### WRT-092 - 의미 보존 편집
- **Statement:** 명료성·간결성 개선이 Claim의 범위·강도·조건·결론을 바꾸지 않아야 한다.
- **Verification:** 변경 전·후 문장과 Claim을 대조한다.
- **Exceptions:** 승인된 Semantic Change는 Decision Ref를 연결한다.

### WRT-093 - 귀속 보존
- **Statement:** ATTRIBUTED_CLAIM의 발화자·기관·발언 범위와 Source 연결을 유지해야 한다.
- **Verification:** Candidate와 Claim·Source Record를 대조한다.
- **Exceptions:** 반복 문맥에서 주체 축약은 모호성이 없을 때만 허용한다.

### WRT-094 - 불확실성 보존
- **Statement:** PARTIAL·CONFLICT·INFERENCE·OUTLOOK의 조건과 불확실성을 편집 과정에서 약화하거나 삭제하지 않아야 한다.
- **Verification:** Baseline Claim 상태와 Candidate 표현을 비교한다.
- **Exceptions:** 후속 검증으로 상태가 바뀌면 새 근거와 시점을 연결한다.

### WRT-095 - Claim Trace 유지
- **Statement:** 문장 분리·병합·재배열 후에도 핵심 문장을 Claim ID와 Source ID로 되돌릴 수 있어야 한다.
- **Verification:** Claim Trace 참조 무결성을 검사한다.
- **Exceptions:** 순수 연결 문장은 비적용 표시가 가능하다.

## 17.D Copy와 일관성 (WRT-096 ~ WRT-100)

### WRT-096 - 승인 용어
- **Statement:** 용어·약어·고유명사를 Style Sheet와 공식 표기에 맞춰 일관되게 사용해야 한다.
- **Verification:** 용어 목록과 Candidate를 대조한다.
- **Exceptions:** 직접 인용의 원 표현은 귀속과 함께 보존한다.

### WRT-097 - 수치·날짜 정합
- **Statement:** 수치·단위·기간·분모·통화·날짜·시간대를 Claim과 Source에 맞춰야 한다.
- **Verification:** 표·본문·요약 간 값을 교차 확인한다.
- **Exceptions:** 반올림은 방법과 의미 손실 여부를 기록한다.

### WRT-098 - 링크 정확성
- **Statement:** 링크 표시 문구와 실제 목적지·Source 역할이 일치해야 한다.
- **Verification:** 모든 외부·내부 링크를 열거나 Locator로 확인한다.
- **Exceptions:** 접근 제한 링크는 상태와 대체 설명을 기록한다.

### WRT-099 - 목록·표 평행성
- **Statement:** 목록 항목과 표 행·열은 문법·단위·비교 축이 평행해야 한다.
- **Verification:** Marker·Header·Unit·Row 의미를 검사한다.
- **Exceptions:** Project MASTER의 비대칭 구조는 역할을 명시한다.

### WRT-100 - 탐색 접근성
- **Statement:** 제목·링크·목록·표가 독자가 구조와 목적을 식별할 수 있게 작성돼야 한다.
- **Verification:** 제목만 읽기, 링크 문구와 표 Header를 검사한다.
- **Exceptions:** 시각 구현 상세는 DSG 기준으로 별도 검수한다.

## 17.E 변경과 Query (WRT-101 ~ WRT-105)

### WRT-101 - Semantic Change 반환
- **Statement:** 의미·수치·조건·귀속·결론을 바꾸는 변경은 Writer·Research·Owner 또는 Fact Checker의 결정을 받아야 한다.
- **Verification:** Semantic Change에 Query와 Decision Ref가 있다.
- **Exceptions:** 없음.

### WRT-102 - Non-semantic 기록
- **Statement:** 중요한 비의미 변경은 변경 범위·이유·적용 Rule을 추적 가능하게 기록해야 한다.
- **Verification:** Change Record 또는 Batch Record를 확인한다.
- **Exceptions:** 명백한 단일 오타는 집계 기록할 수 있다.

### WRT-103 - 이슈 심각도
- **Statement:** Editorial Issue를 독자 영향과 계약 위반에 따라 CRITICAL·MAJOR·MINOR로 분류해야 한다.
- **Verification:** Issue Record의 severity와 근거를 검사한다.
- **Exceptions:** 취향 차이는 결함으로 분류하지 않는다.

### WRT-104 - 열린 차단 이슈
- **Statement:** 열린 Critical Issue 또는 Semantic Query가 있으면 FACT_CHECK_READY로 표시하지 않아야 한다.
- **Verification:** Issue·Query Log와 Candidate 상태를 대조한다.
- **Exceptions:** 없음.

### WRT-105 - Accepted Risk 통제
- **Statement:** 해결하지 않고 진행하는 비Critical 이슈는 승인자·사유·영향·재검토 조건을 가져야 한다.
- **Verification:** Accepted Risk Record를 확인한다.
- **Exceptions:** Critical 결함은 Accepted Risk로 우회할 수 없다.

## 17.F Variant·QA·인계 (WRT-106 ~ WRT-110)

### WRT-106 - Canonical 우선 반영
- **Statement:** 승인된 구조·의미 변경을 Canonical에 먼저 반영한 뒤 Variant로 전파해야 한다.
- **Verification:** Variant lineage와 변경 순서를 확인한다.
- **Exceptions:** 채널 전용 표기 수정은 의미 비변경 근거를 기록한다.

### WRT-107 - Variant 의미 정합
- **Statement:** Variant의 제목·요약·수치·귀속·불확실성과 생략이 Canonical 의미와 일치해야 한다.
- **Verification:** Variant Map과 Canonical을 대조한다.
- **Exceptions:** 채널 제약이 오해를 만들면 Variant를 보류한다.

### WRT-108 - 내부 요소 제거
- **Statement:** 독자용 Candidate에서 Prompt·Placeholder·TODO·검토 메모·Credential·미승인 대안을 제거하거나 분리해야 한다.
- **Verification:** 금지 패턴과 파일 분리를 검사한다.
- **Exceptions:** 내부 전용 Variant는 독자용과 물리적으로 분리한다.

### WRT-109 - Editorial Gate
- **Statement:** G1~G8 판정과 증거 없이 FACT_CHECK_READY로 표시하지 않아야 한다.
- **Verification:** Editorial QA Record를 확인한다.
- **Exceptions:** 없음.

### WRT-110 - 인계 상태 분리
- **Statement:** FACT_CHECK_READY를 Fact Check·SEO·Publishing 또는 Runtime 승인으로 해석하지 않아야 한다.
- **Verification:** Handoff에 후속 Gate와 책임 문서가 명시돼 있다.
- **Exceptions:** 없음.

# 18. AI용 압축 Editorial Workflow

```text
1. editorial_request_id, 대상 Draft, 편집 범위, Output Contract, Style Sheet와 Binding을 확인한다.
2. CNT-002 Editorial Handoff와 하나의 Canonical Draft를 버전·해시로 Baseline 고정한다.
3. Editorial Brief를 만들고 Issue에 유형·심각도·책임·상태·근거를 부여한다.
4. 구조 → 문장 → Copy → 일관성 순서로 목적별 편집 회차를 수행한다.
5. 섹션 역할·정보 순서·제목 계층·Cardinality를 먼저 정리한다.
6. 명료성을 개선하되 Claim 범위·강도·조건·귀속·불확실성을 바꾸지 않는다.
7. 문장 분리·병합 후에도 핵심 문장의 Claim·Source Trace를 유지한다.
8. 용어·이름·수치·단위·날짜·시간대·링크·목록·표를 Style Sheet와 맞춘다.
9. Semantic Change는 Writer·Research·Owner·Fact Checker에게 Query하고 승인 근거를 남긴다.
10. 열린 Critical Issue·Semantic Query가 있으면 FACT_CHECK_READY로 표시하지 않는다.
11. Canonical 변경을 Variant에 전파하고 제목·요약·귀속·불확실성·생략을 대조한다.
12. 내부 요소를 제거하고 Candidate·Claim Trace·Change·Issue·Variant·QA를 CNT-004에 인계한다.
```

이 압축 블록은 상세 Workflow의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-003은 승인된 Canonical Draft의 구조·문장·표기·일관성 편집과 기록 계약만 정의한다.
- 새 조사와 Claim 상태 변경은 CNT-001·CNT-004에 반환한다.
- 핵심 메시지·콘텐츠 필드 재설계는 CNT-002와 Project Owner의 승인이 필요하다.
- SEO는 CNT-005, 시각 구현은 DSG·Project MASTER, 공개·배포는 CNT-006이 맡는다.
- Runtime Prompt와 자동 편집은 Phase 5 Automation의 별도 Gate를 통과해야 한다.

## 19.2 알려진 제한

- 모든 장르에 같은 편집 회차 수, 문장 길이 또는 Style Sheet를 강제하지 않는다.
- 번역·현지화·법률 검토의 전문 절차는 현재 범위에 포함하지 않는다.
- 자동 맞춤법·문법 검사는 의미 보존 또는 사실 정확성을 보증하지 않는다.
- `FACT_CHECK_READY`는 독립 Fact Check, SEO 또는 공개 가능성을 보증하지 않는다.
- Project 고유 승인자·SLA·교정 기호는 해당 Project 문서가 구체화한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 편집 입력·Baseline·Issue·구조·문장·Copy·Claim Trace·Query·Variant·QA·Fact Check Handoff와 WRT-081~110 작성; 사용자 명시적 승인 반영 |
