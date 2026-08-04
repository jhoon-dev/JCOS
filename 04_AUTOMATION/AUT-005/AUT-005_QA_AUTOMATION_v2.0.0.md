# JCOS v2.0.0 - AUT-005 QA AUTOMATION

## 범용 자동 검사·증거·회귀·Release Gate 원칙

| Field | Value |
|---|---|
| Document ID | AUT-005 |
| Title | QA AUTOMATION |
| Korean Title | 범용 자동 검사·증거·회귀·Release Gate 원칙 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | AUTOMATION |
| Applies To | JCOS Run·Schedule·Prompt·Recovery의 입력, 중간 산출물, 출력, 상태, 증거와 Release Candidate |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~007 v2.0.0 LOCKED, AUT-001~004 v2.0.0 LOCKED |
| Extends | AUT-001~AUT-120 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, AUT-001 AUTOMATION ARCHITECTURE, AUT-003 PROMPT SYSTEM, AUT-004 FAILURE RECOVERY |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 AUT-005 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

AUT-005는 자동 실행의 완료 여부를 단순 성공 코드가 아니라 승인된 계약, 검사 결과, 증거와 잔여 위험으로 판정하는 방법을 정의한다. QA는 입력·구성·권한·중간 상태·출력·부작용·인계·Release 전환을 가로지르는 Gate 체계다.

검사 실행 자체의 성공은 대상의 통과를 뜻하지 않는다. 검사 불가, 증거 누락, 환경 불일치, 불안정한 결과는 PASS로 축소하지 않고 명시적 상태로 보존한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- QA Request·Plan·Profile·Suite·Case·Assertion 계약
- Static·Schema·Policy·Behavior·Meaning·Visual·Delivery 검사 분류
- Fixture·Vector·Oracle·Baseline·Tolerance 관리
- 검사 환경·Capability·Adapter·Dependency 고정과 기록
- 결과·Defect·Evidence·Coverage·Trace 생성
- Determinism·Flaky Test·False Positive·False Negative 통제
- Regression·Difference·Change Impact 판정
- Gate·Threshold·Waiver·Expiry·Release Decision 연결
- QA 실패의 Recovery·Escalation·Runbook 인계

## 2.2 비범위

- 특정 Test Framework, CI Pipeline, 명령어, API, Dashboard 구현
- 특정 AI 모델의 자체 점수·선호·추천
- Project 고유 임계값, SLA, 성능, 비용 한도 임의 결정
- 운영자 명령, 당직, 연락, 배포·복구 순서
- 사람의 최종 안전·법무·편집 판단 대체
- QA 통과를 위한 산출물의 암묵적 자동 보정

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 품질 등급·Gate·결함 원칙 | COR-005 QUALITY GATE |
| 파일·패키지·해시·전달 무결성 | COR-006 FILE DELIVERY |
| 버전·상태·승인·잠금 | COR-007 VERSION POLICY |
| Run·환경·권한·Idempotency | AUT-001 AUTOMATION ARCHITECTURE |
| Prompt·Output·Validation 계약 | AUT-003 PROMPT SYSTEM |
| 실패 분류·재시도·복구·종료 | AUT-004 FAILURE RECOVERY |
| 자동 검사·증거·회귀·Release Gate | AUT-005 QA AUTOMATION |
| 실제 명령·수동 조치·Escalation 순서 | AUT-006 RUNBOOK |
| Project 고유 임계값·필수 Suite·승인자 | 해당 Project Rules·Project QA |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| QA Request | 대상·버전·목적·위험·필수 Gate와 판정 시점을 지정한 요청 |
| QA Plan | 실행 Suite·순서·환경·예산·증거·종료 조건 |
| QA Profile | 대상 유형과 위험 등급별 필수 검사와 Gate 묶음 |
| Test Case | 입력·전제·절차·Oracle·예상 결과·증거 요구를 가진 검사 단위 |
| Assertion | 하나의 관찰값을 계약과 비교하는 명시적 판정 |
| Oracle | 예상 결과를 정하는 승인 기준·계산·예시·사람 판단 |
| Fixture | 버전 고정 입력·상태·의존성 묶음 |
| Baseline | 회귀 비교에 사용하는 승인 결과와 해시 |
| Tolerance | 비결정적 변동에 대해 승인된 비교 범위 |
| Defect | 필수 계약·예상 결과·Gate와의 추적 가능한 불일치 |
| Flaky Test | 동일 조건에서 근거 없이 결과가 바뀌는 검사 |
| Waiver | 유효기간·범위·승인자·잔여 위험이 있는 임시 예외 |
| QA Record | 요청부터 검사·증거·결함·Gate·판정까지의 재현 기록 |

# 4. QA 계층과 판정

## 4.1 검사 계층

| 순서 | 계층 | 핵심 질문 |
|---|---|---|
| 1 | Authority | 올바른 기준·버전·승인 상태인가 |
| 2 | Integrity | 입력·패키지·해시·계보가 완전한가 |
| 3 | Safety | 권한·금지·보호정보·부작용 경계를 지켰는가 |
| 4 | Structure | Schema·Cardinality·형식·파일 계약에 맞는가 |
| 5 | Behavior | 상태 전이·Tool·Retry·Handoff가 계약대로인가 |
| 6 | Meaning | 요청과 결과의 의미·사실·완료 조건이 일치하는가 |
| 7 | Presentation | 시각·접근성·렌더·채널 제약을 지켰는가 |
| 8 | Delivery | 산출물·증거·상태·인계가 동기화됐는가 |

Authority·Integrity·Safety의 Critical 결함은 하위 점수나 통계로 상쇄할 수 없다.

## 4.2 판정 상태

- PASS: 필수 검사와 증거가 완결되고 열린 차단 결함이 없음
- FAIL: 실제 불일치 또는 차단 결함이 확인됨
- BLOCKED: 필수 입력·환경·권한·의존성 미충족
- NOT_TESTABLE: 승인된 Oracle·관찰 경로·재현 조건이 없음
- NOT_APPLICABLE: 적용조건과 근거가 명시적으로 불일치
- INCONCLUSIVE: 증거 충돌·불안정성·부분 관찰로 결론 불가

# 5. 필수 입력 계약

| 입력 | 필수 내용 |
|---|---|
| QA Request | request_id, target_id, target_version, purpose, risk_class |
| Target Manifest | 대상 Artifact·Run·Package·상태·해시 |
| Authority Set | 기준 ID·버전·상태·우선순위 |
| QA Profile | 필수 Suite·Gate·Severity·Threshold·종료 조건 |
| Environment Contract | Runtime·Capability·Adapter·Dependency·시간·Locale |
| Fixture Manifest | fixture_id, version, source, hash, sensitivity |
| Oracle Set | oracle_id, type, version, owner, approval, tolerance |
| Evidence Contract | 필수 로그·스냅샷·해시·비교·보존 요구 |
| Budget | 시간·비용·실행 수·병렬성·자원 한도 |
| Release Context | 후보 버전·변경 목록·승인자·배포 대상 |

필수 기준, Target 해시, QA Profile 또는 Evidence Contract가 없으면 PASS로 시작하지 않고 BLOCKED로 기록한다.

# 6. 표준 QA 수명주기

| 단계 | 작업 | 필수 산출물 |
|---|---|---|
| 1 | QA Request·Target 식별 | request_id·target_id·version·hash |
| 2 | Authority·Profile·Release Context 고정 | authorities·profile·candidate |
| 3 | 위험·변경 영향 분류 | risk·changed_areas·required_suites |
| 4 | 환경·Capability·Dependency Preflight | environment·adapter·limits |
| 5 | Fixture·Oracle·Baseline 고정 | fixture_set·oracle_set·baseline |
| 6 | Test Plan 조립·승인 | suites·cases·order·budget |
| 7 | 검사 환경 격리·초기화 | namespace·seed·clock·cleanup |
| 8 | Static·Schema·Policy 검사 | assertions·raw results·evidence |
| 9 | Behavior·Meaning·Visual·Delivery 검사 | observations·comparisons·artifacts |
| 10 | 재현·Flake·Oracle 건전성 확인 | reruns·variance·oracle verdict |
| 11 | Defect·Coverage·잔여 위험 집계 | defects·coverage·gaps·risk |
| 12 | Gate 판정·Waiver 검증 | gate_results·waivers·decision |
| 13 | QA Record·Evidence Package 고정 | record·report·manifest·hashes |
| 14 | Release·Recovery·Runbook 인계 | status·owners·actions·references |

# 7. QA Profile과 Test Plan

QA Profile은 Artifact 유형, 변경 영역, 위험 등급, 상태 전환, 외부 부작용으로 선택한다. 변경 파일 수만으로 축소하지 않는다. LOCKED 기준, 권한, 보호정보, 외부 게시·삭제·전송 경로를 건드리면 영향 범위가 작아도 고위험 Profile을 적용한다.

Test Plan은 각 Case의 ID, 목적, 적용 규칙, 입력, 전제, 절차, Oracle, Assertion, 증거, Severity, Timeout, Cleanup을 가진다. 독립 Case는 실행 순서에 따라 결과가 바뀌지 않아야 한다.

# 8. Fixture·Vector·Oracle

Fixture는 버전, 출처, 해시, 민감도, 생성 방법, 초기화·폐기 규칙을 가진다. 실시간 외부 데이터를 사용하면 시점, 보존 가능성, 변동 범위와 재현 제한을 기록한다.

Oracle은 Exact, Property, Reference, Differential, Human 유형으로 구분한다. AI 자동 평가자를 쓰려면 평가 계약, 버전, 입력, 점수 방법, 재현성, 편향, 사람 상승 조건을 고정한다. 자체 점수만으로 Critical Gate를 통과시키지 않는다.

# 9. 검사 환경과 재현성

검사 환경은 Runtime, OS, Locale, Time Zone, Clock, Random Seed, Font, Adapter, Capability, Dependency, Network Policy, Secret Scope, Resource Limit을 기록한다. 생산 환경과 다르면 차이와 대체 근거를 잔여 위험에 포함한다.

현재 시각, 랜덤, 외부 API, 실시간 검색, 변동 모델 출력은 통제 또는 기록하지 않으면 결정적 검사로 표시하지 않는다.

# 10. Assertion과 비교

Assertion은 관찰 대상, 예상값, 비교 연산, Tolerance, Severity, 실패 메시지, Evidence Pointer를 가진다. 여러 판정을 불투명한 점수 하나로 합치지 않고 Critical 조건의 개별 결과를 보존한다.

Tolerance는 수치 범위, 순서 비의존, 시각 차이 등 비교 차원별로 정의한다. 검사 실패를 없애기 위한 임의 조정이 아니라 버전·근거·승인이 있는 기준 변경이다.

# 11. 증거와 Traceability

Evidence Package에는 Request·Plan·Profile, Target·Fixture·Oracle·Baseline·Environment Manifest, Case별 원시 결과, 로그·스냅샷·출력·Diff·렌더, Defect·Coverage Gap·Waiver·잔여 위험, Gate·최종 판정·인계를 포함한다.

각 필수 규칙은 하나 이상의 Case에 연결되고 Case는 Assertion·Evidence·Defect·Gate로 추적 가능해야 한다. 연결되지 않은 규칙은 통과가 아니라 Coverage Gap이다.

# 12. 결함·심각도·Triage

Defect는 defect_id, target, rule, case, expected, actual, evidence, reproducibility, severity, impact, owner, status를 가진다. 중복 병합 시에도 원본 증거와 영향 대상을 보존한다.

Severity는 안전, 권한, 데이터 손실, 외부 부작용, 기준 위반, 사용자 영향, 복구 가능성으로 판정한다. 낮은 빈도나 재현 난이도로 심각도를 낮추지 않는다.

# 13. 불안정성·오탐·미탐

Flaky 판정은 동일 Target·Fixture·Oracle·Environment·Seed에서 근거 없이 결과가 바뀔 때만 사용한다. 재실행 통과로 최초 실패를 삭제하지 않고 모든 Attempt를 보존한다.

오탐·미탐은 검사의 Defect다. 검사를 무시하기 전에 Oracle, Fixture, Tolerance, Environment, Assertion 중 어느 계약이 잘못됐는지 분리한다.

# 14. Coverage와 Regression

Coverage는 규칙, 위험, 상태 전이, 입력 분할, 오류 경로, Adapter, 환경, 산출물 형식별로 기록한다. 필수 규칙의 Case 연결이 없으면 전체 통과율과 무관하게 Gap이다.

Regression은 승인 Baseline과 Candidate의 해시, 계약, 환경, 비교 차원을 고정한다. 차이는 EXPECTED, APPROVED_CHANGE, DEFECT, UNKNOWN으로 분류하며 근거와 승인을 연결한다.

# 15. Gate·Threshold·Waiver

Gate는 필수 Case, Critical·Major Defect, Coverage Gap, NOT_TESTABLE, Flaky, Evidence 완전성, Waiver 유효성, 잔여 위험을 각각 평가한다. 평균 점수나 통과율이 Critical 실패를 상쇄하지 못한다.

Waiver는 waiver_id, 대상, 범위, 사유, 영향, 대체 통제, owner, approver, issued_at, expires_at, 재검사 조건을 가진다. 만료·범위 초과·승인자 불일치 Waiver는 없는 것으로 간주한다.

# 16. QA Gate와 결함 처리

| Gate | 통과 조건 |
|---|---|
| G1 Authority | 기준·버전·상태·우선순위 완결 |
| G2 Target Integrity | Manifest·해시·계보·변경 목록 일치 |
| G3 Plan | Profile·Suite·Case·Oracle·Evidence·Budget 완결 |
| G4 Environment | Capability·Adapter·Dependency·격리 확인 |
| G5 Execution | 필수 Case 완료와 미실행 근거 완결 |
| G6 Evidence | Assertion·원시 결과·Artifact·Trace 연결 |
| G7 Reliability | Flaky·Oracle·Tolerance·재현성 판정 완결 |
| G8 Defect | 결함·Severity·Owner·상태·재검사 조건 완결 |
| G9 Release | 차단 결함 0건, Waiver 유효, 잔여 위험 승인 |
| G10 Record | QA Record·Evidence Package·Handoff 해시 완결 |

Critical 결함, 필수 Evidence 누락, 만료 Waiver, 필수 Gate의 NOT_TESTABLE·INCONCLUSIVE가 있으면 Release를 PASS로 표시하지 않는다.

# 17. 실행 규칙 (AUT-121 ~ AUT-150)

## 17.A 요청과 기준 (AUT-121 ~ AUT-125)

### AUT-121 - QA 대상 식별
- **Statement:** QA Request는 target_id·version·hash·status·purpose를 고정해야 한다.
- **Verification:** Target Manifest와 실제 대상을 대조한다.
- **Exceptions:** Mutable Target은 Snapshot 시점과 변경 감지 규칙을 기록한다.

### AUT-122 - Authority Set 고정
- **Statement:** 적용 기준의 ID·버전·상태·우선순위를 검사 전에 고정해야 한다.
- **Verification:** Authority Manifest와 Target Binding을 검사한다.
- **Exceptions:** 기준 충돌은 COR-008에 따라 BLOCKED로 상승한다.

### AUT-123 - Risk 기반 Profile
- **Statement:** QA Profile은 Artifact 유형·변경 영역·위험·부작용으로 선택해야 한다.
- **Verification:** Change Impact와 required_suites 매핑을 검사한다.
- **Exceptions:** 신규 유형은 가장 보수적인 승인 Profile을 적용한다.

### AUT-124 - 필수 입력 완전성
- **Statement:** Target·Profile·Environment·Fixture·Oracle·Evidence·Budget 필수 필드가 완결되어야 한다.
- **Verification:** QA Request Schema와 Manifest 참조를 검사한다.
- **Exceptions:** 비적용 항목은 NOT_APPLICABLE 근거를 가진다.

### AUT-125 - 사전 차단
- **Statement:** Authority·Integrity·Safety Preflight 실패 시 부작용 검사를 시작하지 않아야 한다.
- **Verification:** Preflight 결과와 실행 로그를 대조한다.
- **Exceptions:** 격리된 비변경 정적 검사는 별도 계획으로 수행할 수 있다.

## 17.B Plan과 Oracle (AUT-126 ~ AUT-130)

### AUT-126 - Test Plan 추적성
- **Statement:** 각 Case는 규칙·위험·Oracle·Assertion·Evidence·Gate에 연결되어야 한다.
- **Verification:** Trace Map의 단절과 중복을 검사한다.
- **Exceptions:** 탐색 Case는 목적과 판정 제한을 표시한다.

### AUT-127 - Fixture 버전 고정
- **Statement:** Fixture는 ID·버전·해시·출처·민감도·초기화 규칙을 가져야 한다.
- **Verification:** Fixture Manifest와 실제 입력 해시를 대조한다.
- **Exceptions:** 실시간 데이터는 Snapshot·as_of·재현 제한을 기록한다.

### AUT-128 - Oracle 승인
- **Statement:** Oracle은 유형·버전·Owner·승인·Tolerance·적용 범위를 가져야 한다.
- **Verification:** Oracle Manifest와 Case Binding을 검사한다.
- **Exceptions:** Oracle 없는 필수 Case는 NOT_TESTABLE로 판정한다.

### AUT-129 - 자체 평가 제한
- **Statement:** 대상을 생성한 동일 시스템의 자체 점수만으로 Critical Gate를 통과시키지 않아야 한다.
- **Verification:** Evaluator 계보와 독립 근거를 검사한다.
- **Exceptions:** 정형 Schema·해시 같은 결정적 검사는 적용할 수 있다.

### AUT-130 - Tolerance 통제
- **Statement:** Tolerance는 비교 차원별 근거·버전·승인을 가져야 한다.
- **Verification:** 실행 중 변경과 임계 우회를 검사한다.
- **Exceptions:** 적응형 임계는 계산 규칙·범위·상한·하한을 고정한다.

## 17.C 환경과 실행 (AUT-131 ~ AUT-135)

### AUT-131 - 환경 Manifest
- **Statement:** Runtime·Locale·Time Zone·Clock·Seed·Font·Adapter·Dependency·Resource Limit을 기록해야 한다.
- **Verification:** Manifest와 실제 환경을 대조한다.
- **Exceptions:** 증명 불가 정보는 UNKNOWN 잔여 위험으로 남긴다.

### AUT-132 - 검사 격리
- **Statement:** 생산 부작용·Secret·사용자 데이터를 최소화하는 격리 범위에서 실행해야 한다.
- **Verification:** Namespace·Credential·Target·Cleanup Evidence를 검사한다.
- **Exceptions:** 생산 검증은 승인된 Read-only 또는 제한 작업만 수행한다.

### AUT-133 - Assertion 독립 결과
- **Statement:** 각 Assertion은 예상값·관찰값·비교·Severity·Evidence를 개별 기록해야 한다.
- **Verification:** 점수 집계 전 원시 판정 보존을 검사한다.
- **Exceptions:** 복합 판정은 하위 Assertion과 집계 규칙을 모두 남긴다.

### AUT-134 - Timeout·중단 투명성
- **Statement:** Timeout·Cancel·Kill·Resource Exhaustion을 검사 실패와 대상 실패로 분리해야 한다.
- **Verification:** Runner·Target·Dependency Event와 종료 상태를 대조한다.
- **Exceptions:** 원인 불명은 INCONCLUSIVE로 AUT-004에 인계한다.

### AUT-135 - Cleanup 검증
- **Statement:** 임시 자원·계정·파일·외부 부작용의 종료 상태를 검증해야 한다.
- **Verification:** Cleanup Record와 실제 외부 상태를 대조한다.
- **Exceptions:** 삭제 금지 증거는 보존 위치·기간·Owner를 기록한다.

## 17.D 증거와 결함 (AUT-136 ~ AUT-140)

### AUT-136 - Evidence 완전성
- **Statement:** PASS·FAIL은 재현 가능한 원시 결과와 Evidence Pointer를 가져야 한다.
- **Verification:** 참조, 해시, 접근 가능성을 검사한다.
- **Exceptions:** 보호정보는 비식별 해시·Redaction Evidence를 남긴다.

### AUT-137 - Trace Coverage
- **Statement:** 필수 규칙·위험·Gate는 Case·Assertion·Evidence에 연결되어야 한다.
- **Verification:** 미연결 항목을 Coverage Gap으로 집계한다.
- **Exceptions:** NOT_APPLICABLE은 적용조건과 근거를 유지한다.

### AUT-138 - Defect 고유성
- **Statement:** Defect는 ID·Rule·Case·Expected·Actual·Evidence·Severity·Owner·Status를 가져야 한다.
- **Verification:** 병합 시 원본 증거와 영향 보존을 검사한다.
- **Exceptions:** 신규 원인 의심은 별도 Defect로 유지한다.

### AUT-139 - Severity 비축소
- **Statement:** 낮은 빈도·재현 난이도·점수로 안전·권한·데이터·외부 부작용 심각도를 낮추지 않아야 한다.
- **Verification:** Severity 차원과 영향 근거를 검사한다.
- **Exceptions:** Project 조정은 상위 심각도를 낮추지 않는다.

### AUT-140 - 잔여 위험 표시
- **Statement:** 미검사·NOT_TESTABLE·INCONCLUSIVE·Flaky·Waived 항목을 잔여 위험으로 보존해야 한다.
- **Verification:** Summary와 세부 결과의 누락을 검사한다.
- **Exceptions:** 해소 항목은 재검사 Evidence와 종료 시점을 남긴다.

## 17.E 신뢰성과 회귀 (AUT-141 ~ AUT-145)

### AUT-141 - Flaky 검사 격리
- **Statement:** 불안정 Case는 최초 실패를 삭제하지 않고 격리·Owner·해소 조건을 가져야 한다.
- **Verification:** 모든 Attempt·환경·변동과 Gate 영향을 검사한다.
- **Exceptions:** 외부 변동이 증명되면 의존성 실패로 재분류한다.

### AUT-142 - 오탐·미탐 교정
- **Statement:** 오탐·미탐은 Oracle·Fixture·Tolerance·Environment·Assertion 원인을 분리해 검사 Defect로 관리해야 한다.
- **Verification:** 규칙 비활성화 전 원인·영향·대체 통제를 검사한다.
- **Exceptions:** 긴급 격리는 만료 시점과 사후 승인을 가진다.

### AUT-143 - Regression Baseline 무결성
- **Statement:** Baseline은 승인 상태·버전·Target·Environment·해시와 연결되어야 한다.
- **Verification:** Baseline Manifest와 실제 참조를 대조한다.
- **Exceptions:** Baseline 미존재 시 최초 결과를 자동 승인하지 않는다.

### AUT-144 - Difference 분류
- **Statement:** 회귀 차이를 EXPECTED·APPROVED_CHANGE·DEFECT·UNKNOWN으로 분류해야 한다.
- **Verification:** Change Reference·Evidence·Approver를 검사한다.
- **Exceptions:** 분류 불가는 INCONCLUSIVE로 Gate에 반영한다.

### AUT-145 - 회귀 선택 투명성
- **Statement:** Suite를 축소하면 제외 영역·근거·잔여 위험을 기록해야 한다.
- **Verification:** Changed Area·Dependency·Rule·Suite 매핑을 검사한다.
- **Exceptions:** 전체 회귀 불가 시 BLOCKED 또는 승인 Waiver로 인계한다.

## 17.F Gate·Release·인계 (AUT-146 ~ AUT-150)

### AUT-146 - Gate 비상쇄
- **Statement:** 총점·평균·통과율로 Critical 결함·Evidence 누락·필수 Gate 실패를 상쇄하지 않아야 한다.
- **Verification:** Gate 계산과 원시 결과 보존을 검사한다.
- **Exceptions:** 없음.

### AUT-147 - Waiver 유효성
- **Statement:** Waiver는 범위·사유·영향·대체 통제·Owner·Approver·Expiry·재검사 조건을 가져야 한다.
- **Verification:** 만료·범위 초과·승인 권한·Critical 금지 조건을 검사한다.
- **Exceptions:** 만료 Waiver는 없는 것으로 간주한다.

### AUT-148 - Release 판정 결합
- **Statement:** Release Decision은 Gate·Defect·Coverage·Waiver·잔여 위험·승인자와 결합되어야 한다.
- **Verification:** Candidate 상태와 QA Record·Release Record를 대조한다.
- **Exceptions:** QA PASS는 사용자 승인·LOCKED 전환을 대체하지 않는다.

### AUT-149 - QA Record 불변성
- **Statement:** Request·Plan·Environment·Result·Evidence·Defect·Gate·Decision·Handoff를 해시 추적 기록으로 결합해야 한다.
- **Verification:** Manifest·Artifact·Hash·Timestamp·Lineage를 검사한다.
- **Exceptions:** 보존 제한 증거는 Retention·Redaction·검증 대체값을 기록한다.

### AUT-150 - 후속 인계
- **Statement:** FAIL·BLOCKED·INCONCLUSIVE는 AUT-004 Recovery, 운영 조치는 AUT-006 Runbook, 승인 후보는 COR-007 상태 계약으로 인계해야 한다.
- **Verification:** Handoff의 필드·Owner·상태·증거·다음 조치를 검사한다.
- **Exceptions:** 자동 인계 불가 시 수동 패키지와 전달 확인을 남긴다.

# 18. AI용 압축 QA Automation

1. target_id·version·hash·status와 Authority Set·QA Profile을 검사 전에 고정한다.
2. 위험·변경 영향으로 필수 Suite를 선택하고 제외 근거를 남긴다.
3. Fixture·Oracle·Baseline·Tolerance의 ID·버전·해시·승인을 고정한다.
4. Runtime·Locale·Time Zone·Clock·Seed·Adapter·Dependency를 기록한다.
5. Authority·Integrity·Safety Preflight 실패 시 부작용 검사를 차단한다.
6. Case를 Rule·Risk·Oracle·Assertion·Evidence·Gate에 연결해 격리 실행한다.
7. 각 Assertion의 예상값·관찰값·비교·Severity·Evidence를 보존한다.
8. Timeout·Runner·Dependency·Target 실패를 분리하고 Cleanup을 검증한다.
9. Flaky·오탐·미탐·NOT_TESTABLE·INCONCLUSIVE를 PASS로 축소하지 않는다.
10. Regression 차이를 EXPECTED·APPROVED_CHANGE·DEFECT·UNKNOWN으로 분류한다.
11. Critical 결함·증거 누락·만료 Waiver·필수 Gate 실패를 점수로 상쇄하지 않는다.
12. QA Record에 Plan·Environment·Result·Evidence·Defect·Coverage·Gate·Decision·Handoff 해시를 결합한다.

이 압축 블록은 상세 QA Automation의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- AUT-005는 검사 계약·실행 증거·결함·회귀·Gate 판정만 정의한다.
- 실제 CI·Test Framework·Dashboard·Provider 구현은 Adapter 또는 Project 책임이다.
- 실패 복구는 AUT-004, 운영자 명령·수동 조치·연락 순서는 AUT-006이 정의한다.
- QA PASS는 콘텐츠·법무·안전·사용자 승인 또는 LOCKED 전환을 대체하지 않는다.
- Project 고유 필수 Suite·임계값·SLA·승인자는 Project Rules·Project QA가 구체화한다.

## 19.2 알려진 제한

- 모든 의미·사실·시각 품질을 완전히 자동 판정할 수 있다고 가정하지 않는다.
- 자동 평가자와 모델은 버전·입력·환경에 따라 변동하며 독립 Oracle이 아니다.
- 실시간 외부 시스템은 완전한 재현과 관찰을 제공하지 않을 수 있다.
- 통과율·Coverage 숫자·점수는 미연결 규칙, 오류 Oracle, Critical 결함을 숨길 수 있다.
- 테스트 환경의 PASS가 생산 환경의 동일 결과를 보장하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 5 순서에 따라 범용 QA Request·Profile·Plan·Fixture·Oracle·Environment·Assertion·Evidence·Defect·Coverage·Flaky·Regression·Waiver·Release Gate와 AUT-121~150 작성·QA·사용자 승인 완료 |
