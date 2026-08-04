# JCOS v2.0.0 - AUT-001 AUTOMATION ARCHITECTURE

## 범용 자동화 책임·실행 경계·상태·통제 구조

| Field | Value |
|---|---|
| Document ID | AUT-001 |
| Title | AUTOMATION ARCHITECTURE |
| Korean Title | 범용 자동화 책임·실행 경계·상태·통제 구조 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | AUTOMATION |
| Applies To | 승인된 JCOS 기준과 Project 계약을 반복 가능하게 실행하는 자동화 구조 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~007 v2.0.0 LOCKED |
| Extends | JCOS Rule ID System의 AUT 영역 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, COR-008 DECISION RULES, CNT-007 CONTENT LIFECYCLE |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 AUT-001 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

AUT-001은 자동화가 어떤 입력을 신뢰하고, 어느 구성요소가 무엇을 책임지며, 어디에서 사람의 승인과 안전 통제가 필요한지 정의한다. 결과는 같은 Binding과 입력으로 실행의 시작·판단·산출물·상태·증거·인계를 재현할 수 있는 Automation Run Record여야 한다.

자동화는 승인된 기준을 빠르게 반복하는 실행 수단이지 기준을 새로 만들거나 사람의 권한을 대신하는 주체가 아니다. 도구 응답이 성공했다는 사실만으로 완료하지 않으며, 승인된 상태 전이와 증거·산출물 검증이 충족돼야 한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Automation Request, Binding과 실행 계약
- Trigger·Orchestrator·Worker·Adapter·State Store·Evidence Store의 책임
- Control Plane과 Execution Plane 분리
- 상태 모델, 전이 권한과 불변 조건
- 사람 승인 지점과 권한 있는 중지
- Credential·Secret·최소 권한·환경 분리 원칙
- Idempotency·중복 실행·Concurrency 통제
- 입력·출력·로그·Metric·Trace·Artifact 계보
- 변경·버전·Release·Rollback 준비 구조
- 수동 대체 경로와 공급자 교체 가능성
- Automation Architecture QA와 후속 문서 인계

## 2.2 비범위

- 구체적 예약 시각·주기·시간대·Calendar 계산
- 실제 Prompt 본문·모델 선택·Token·Sampling 설정
- 실패 유형별 재시도 횟수·Backoff·복구 절차
- 자동 QA 검사식·Threshold·CI 구성
- 운영자별 명령·화면·장애 대응 순서
- 서비스별 API·SDK·Webhook·Credential 저장 방식
- Project 고유 SLA·비용 한도·승인자·채널·환경 값

## 2.3 후속 문서 책임

| 판단 | 책임 문서 |
|---|---|
| 자동화 전체 책임·경계·상태·통제 구조 | AUT-001 AUTOMATION ARCHITECTURE |
| 예약·시간대·중복 Schedule·지연 정책 | AUT-002 SCHEDULE POLICY |
| 실행 Prompt·Context·출력 계약 | AUT-003 PROMPT SYSTEM |
| 실패 분류·재시도·복구·보상 | AUT-004 FAILURE RECOVERY |
| 자동 검사·Threshold·Gate 구현 | AUT-005 QA AUTOMATION |
| 실제 운영·수동 전환·Escalation 순서 | AUT-006 RUNBOOK |
| 콘텐츠 판단·Publishing·Lifecycle | CNT-001~007 해당 System |
| Project 고유 값 | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Automation Request | 목적·범위·입력·Trigger·환경·완료 조건을 지정한 실행 요청 |
| Automation Binding | 적용할 Core·Design·Content·Project·Runtime의 ID·버전·상태·해시 묶음 |
| Execution Contract | 입력·출력·상태·권한·실패·증거·완료 조건의 실행 계약 |
| Trigger | 시간·사건·수동 요청 등 실행 검토를 시작하는 신호 |
| Orchestrator | 실행 계획·의존성·상태 전이·승인 지점을 조정하는 역할 |
| Worker | 한정된 작업 계약을 수행하고 결과와 증거를 반환하는 역할 |
| Adapter | 외부 시스템의 차이를 내부 표준 계약으로 변환하는 경계 구성요소 |
| Control Plane | 정책·Binding·권한·승인·배포·중지·상태 정의를 관리하는 영역 |
| Execution Plane | 승인된 계약에 따라 실제 작업과 데이터 이동을 수행하는 영역 |
| State Store | 현재 실행 상태와 전이 이력을 보존하는 논리 저장소 |
| Evidence Store | 입력 Snapshot·로그·Trace·산출물·검증 결과를 보존하는 논리 저장소 |
| Run ID | 하나의 자동화 실행을 고유하게 식별하는 값 |
| Idempotency Key | 같은 의도의 중복 실행을 식별하고 부작용을 통제하는 키 |
| Human Gate | 사람이 승인·거부·수정·중지해야 다음 상태로 갈 수 있는 지점 |
| Kill Switch | 권한 있는 사용자가 신규 실행과 진행 중 실행을 안전하게 중지하는 통제 |
| Run Record | 요청부터 종료·증거·인계까지 연결한 실행 기록 |

# 4. Architecture 원칙

1. 승인된 기준과 실행 구현을 분리한다.
2. Trigger 수신과 실행 허용을 구분한다.
3. Control Plane과 Execution Plane의 권한을 최소화한다.
4. 모든 외부 서비스는 교체 가능한 Adapter 뒤에 둔다.
5. 상태 전이는 명시적이고 단방향 기록으로 남긴다.
6. 중요한 외부 부작용은 사람 승인 또는 명시적 권한 계약을 요구한다.
7. 중복·재시작·부분 실행을 정상 설계 조건으로 다룬다.
8. 성공·실패·미확인을 증거와 함께 분리한다.
9. 자동화가 불가하면 기록 가능한 수동 경로로 전환할 수 있어야 한다.
10. 산출물은 최초 입력부터 최종 전달까지 계보를 재현할 수 있어야 한다.

# 5. 논리 Architecture

| 구성요소 | 책임 | 금지되는 책임 |
|---|---|---|
| Request Interface | 요청 정규화·요청자·범위 식별 | 승인 없는 실행 허용 |
| Trigger Gateway | Trigger 수신·중복 후보 식별 | Schedule 정책 임의 결정 |
| Policy and Binding Resolver | 승인 기준·환경·권한 확인 | 기준 내용 임의 수정 |
| Orchestrator | 실행 계획·의존성·상태·Gate 조정 | 전문 판단을 무근거 대체 |
| Worker | 한정 작업 수행·결과 반환 | 계약 밖 데이터 접근 |
| Adapter | 외부 서비스 변환·응답 정규화 | 내부 상태를 단독 확정 |
| State Store | 현재 상태·전이·Lock 보존 | 증거 없는 상태 변경 |
| Evidence Store | 입력·로그·Trace·Artifact·QA 보존 | Secret 원문 기록 |
| Human Gate | 승인·거부·수정·중지 | 승인 대상을 불명확하게 처리 |
| Delivery Interface | 검증된 산출물과 Record 인계 | 실패를 성공으로 변환 |

구성요소는 논리 역할이다. 하나의 구현이 여러 역할을 수행할 수 있지만 책임·권한·기록은 구분해야 한다.

# 6. 입력 계약과 Preflight

## 6.1 필수 입력

| 입력 | 필수 내용 |
|---|---|
| Automation Request | request_id, 목적, 범위, 요청자, 우선순위 |
| Binding | 기준 문서·Project·Runtime ID·버전·상태·해시 |
| Execution Contract | 입력·출력·상태·Gate·실패·증거·완료 조건 |
| Environment | environment_id, 격리 수준, 허용 Target |
| Authority | 실행·승인·중지·Credential 사용 권한 |
| Input Snapshot | 실제 입력 위치·버전·해시·기준 시점 |
| Handoff | CNT-007 또는 선행 단계의 상태·Trigger·제한·Owner |

필수 입력이 없거나 승인 상태를 확인할 수 없으면 실행하지 않고 `BLOCKED`와 해소 책임을 기록한다.

## 6.2 Preflight

Preflight는 Binding, 입력 무결성, 환경, 권한, 의존성, Idempotency, 활성 중지 지시와 Human Gate 요구를 확인한다. 외부 연결이 가능하다는 사실은 실행 권한을 의미하지 않는다.

# 7. 표준 Automation 수명주기

| 단계 | 작업 | 필수 산출물 |
|---|---|---|
| 1 | Automation Request 식별 | request_id·목적·범위·요청자 |
| 2 | Binding과 Input Snapshot 고정 | ID·버전·상태·해시·as_of |
| 3 | Execution Contract 검증 | 입력·출력·상태·Gate·완료 조건 |
| 4 | 환경·권한·Secret 참조 Preflight | environment_id·authority·secret_ref |
| 5 | Run ID와 Idempotency Key 생성 | run_id·중복 판정 근거 |
| 6 | 실행 계획과 의존성 구성 | step graph·owner·timeout class |
| 7 | Human Gate 또는 실행 허용 확인 | approval_ref·scope·expiry |
| 8 | Worker·Adapter 작업 실행 | step record·정규화 응답 |
| 9 | 상태·로그·Trace·Artifact 기록 | state transition·evidence refs |
| 10 | 출력 계약과 필수 QA 확인 | validation result·결함 |
| 11 | 외부 부작용 또는 Delivery 승인 | target·baseline·approval |
| 12 | 실제 결과와 최종 상태 확인 | delivered ref·verification |
| 13 | Run Record·계보·잔여 위험 완결 | record·lineage·risk |
| 14 | 후속 Schedule·Recovery·QA·Runbook 인계 | next trigger·handoff refs |

# 8. Control Plane과 Execution Plane

Control Plane은 승인된 정책·Binding·환경·권한·배포 버전·Kill Switch를 관리한다. Execution Plane은 고정된 계약을 실행하며 Control Plane의 승인 범위를 확대할 수 없다.

Production과 비Production 환경은 식별자, Credential, Target, State와 Evidence를 논리적으로 분리한다. Test 결과를 Production 성공으로 승격하지 않는다.

Control Plane 변경은 누가, 무엇을, 언제, 왜 변경했는지와 승인·효력 시점을 기록한다. 실행 중 변경은 새 Binding 또는 명시적 재승인 없이 적용하지 않는다.

# 9. 상태 모델과 전이

| 상태 | 의미 |
|---|---|
| RECEIVED | 요청 수신·실행 미허용 |
| VALIDATING | Binding·입력·환경·권한 검증 중 |
| BLOCKED | 필수 조건 부족·외부 의존성 대기 |
| READY | Preflight 통과·실행 가능 |
| WAITING_APPROVAL | Human Gate 승인 대기 |
| RUNNING | 승인 범위 안에서 실행 중 |
| VERIFYING | 출력·외부 결과·QA 검증 중 |
| SUCCEEDED | 필수 Gate와 완료 조건 충족 |
| PARTIAL | 일부 단계·Target만 완료 |
| FAILED | 완료 조건 미충족·실패 확정 |
| CANCELLED | 권한 있는 중지로 종료 |
| UNKNOWN | 실제 외부 상태를 확인할 수 없음 |

상태 전이는 이전 상태, 새 상태, actor, 시각, 근거와 증거를 가진다. `PARTIAL`, `FAILED`, `UNKNOWN`을 `SUCCEEDED`로 축소하지 않는다. 세부 재시도·복구 상태는 AUT-004에서 확장한다.

# 10. Human Gate와 권한

다음과 같은 작업은 기본적으로 Human Gate 후보로 분류한다.

- 공개·배포·삭제·비가역 변경
- 외부 사용자·고객·구독자에게 영향을 주는 전송
- 비용·계약·권한·Credential 범위 확대
- 개인정보·기밀·권리·법률 영향이 있는 처리
- 승인 Baseline·Target·가시성·Schedule의 의미 변경
- Critical 결함 상태에서의 강제 진행

승인은 정확한 Run·Binding·입력·Target·행위·유효기간에 결속한다. 포괄 승인이나 과거 승인으로 변경된 실행을 허용하지 않는다.

# 11. Identity, Credential과 환경 격리

자동화 주체와 사람 주체를 구분하고 각 작업에 actor_id를 기록한다. 권한은 작업에 필요한 최소 범위와 기간만 부여한다.

Run Record에는 Secret 값 대신 secret_ref와 version_ref만 기록한다. Prompt·로그·오류·Artifact에 Credential을 복사하지 않는다. Secret 노출이 의심되면 실행을 중지하고 AUT-004와 AUT-006 경로로 인계한다.

개발·시험·운영 환경의 Target과 Credential을 분리하고, 환경 간 산출물 승격은 승인된 Release와 검증을 요구한다.

# 12. Idempotency와 Concurrency

외부 부작용이 있는 작업은 request intent, Target, 기준 입력과 허용 Window를 반영한 Idempotency Key를 가진다. 같은 Key의 완료·진행 상태를 확인하기 전 새 실행을 시작하지 않는다.

동일 자원에 충돌 가능한 Run은 Lock, Queue, Version Check 또는 동등한 통제로 직렬화한다. Lock 만료와 소유권 상실을 성공으로 간주하지 않는다.

재실행은 새 Run ID를 갖되 원 Run과 원인·재사용 입력·변경 내용을 연결한다. 구체적 재시도와 Backoff는 AUT-004가 정의한다.

# 13. 관찰 가능성과 증거

## 13.1 필수 관찰 정보

| 정보 | 최소 내용 |
|---|---|
| Event | event_id, run_id, step_id, type, timestamp |
| Log | 구조화된 action·result·error class·redaction 상태 |
| Metric | 이름·단위·집계 구간·환경·상태 |
| Trace | 요청부터 Worker·Adapter·Delivery까지 상관관계 |
| Artifact | ID·버전·해시·위치·생성 단계·검증 상태 |
| State Transition | from·to·actor·reason·evidence_ref |
| Approval | approver·scope·baseline·decision·time·expiry |

로그 양보다 재현성과 판정 가능성을 우선한다. 민감정보는 수집 전 최소화하고 불필요한 원문·Prompt·응답을 보존하지 않는다.

## 13.2 Run Record

Run Record는 Request, Binding, Input Snapshot, Contract, Plan, State, Approval, Step Result, Artifact, QA, Delivery, Error, 잔여 위험과 후속 Handoff를 연결한다.

# 14. 변경, Release와 교체 가능성

Automation 구현, Adapter, Contract, Binding 또는 상태 전이 변경은 버전과 영향 검토를 가진다. 승인된 Release 단위를 넘어 암묵적으로 동작을 바꾸지 않는다.

외부 제공자 고유 형식은 Adapter 내부에 제한하고 내부 Contract는 공급자 중립 형식을 유지한다. 제공자를 교체할 때 입력·출력·오류·권한·관찰 정보의 동등성을 검증한다.

새 버전은 제한된 환경과 승인된 입력에서 검증한 뒤 승격한다. Rollback 가능 기준본과 이전 Adapter 계약을 보존하되 구체적 배포·복구 절차는 AUT-004·006이 정의한다.

# 15. 수동 경로와 Degraded Mode

자동 실행 불가, 외부 장애, 권한 부족 또는 안전 불확실성이 발생하면 임의 우회하지 않는다. 입력 Snapshot, 현재 상태, 완료 단계, 열린 위험과 필요한 권한을 보존하고 승인된 수동 경로로 인계한다.

수동 수행도 동일한 Binding·Approval·Evidence·QA·Run Record 계약을 따른다. Degraded Mode는 검증을 생략하는 상태가 아니라 기능과 Target을 제한한 명시적 운영 상태다.

# 16. Automation Architecture QA Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | 목적·범위·요청자·Trigger 추적 가능 |
| G2 Binding | 승인 기준·입력 Snapshot·환경·해시 고정 |
| G3 Contract | 입력·출력·상태·권한·증거·완료 조건 완결 |
| G4 Controls | Human Gate·최소 권한·Secret·환경 격리 확인 |
| G5 Execution | Run·Idempotency·Concurrency·구성요소 책임 확인 |
| G6 Observability | 상태·로그·Trace·Artifact·Approval 추적 가능 |
| G7 Verification | 출력 계약·외부 결과·필수 QA 확인 |
| G8 Record | Run Record·계보·잔여 위험·후속 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. Critical 결함이 열려 있으면 Production Release 또는 `SUCCEEDED` 판정을 허용하지 않는다.

Critical 결함의 예는 승인되지 않은 외부 부작용, Production Target 혼동, Secret 노출, Binding 무시, 중복 결제·게시·삭제, 실제 실패의 성공 보고, Kill Switch 무력화다.

# 17. 실행 규칙 (AUT-001 ~ AUT-030)

## 17.A 기준과 책임 (AUT-001 ~ AUT-005)

### AUT-001 - 승인 기준 우선
- **Statement:** 자동화는 승인된 Core·Design·Content·Project·Runtime Binding만 실행 기준으로 사용해야 한다.
- **Verification:** Run Binding의 ID·버전·상태·해시를 실제 기준본과 대조한다.
- **Exceptions:** 없음.

### AUT-002 - Automation Request 식별
- **Statement:** 모든 실행은 고유 request_id, 목적, 범위, 요청자와 우선순위를 가져야 한다.
- **Verification:** Automation Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### AUT-003 - 책임 구성요소 분리
- **Statement:** Request·Trigger·Policy·Orchestrator·Worker·Adapter·State·Evidence·Delivery 책임을 식별해야 한다.
- **Verification:** Architecture Map과 실제 실행 역할을 대조한다.
- **Exceptions:** 한 구현의 복수 역할은 권한·로그·경계를 분리한다.

### AUT-004 - Control과 Execution 분리
- **Statement:** 정책·승인·중지 권한과 실제 작업·데이터 이동 권한을 구분해야 한다.
- **Verification:** Control Plane과 Execution Plane 권한표를 검사한다.
- **Exceptions:** 단일 사용자 환경도 논리적 경계를 기록한다.

### AUT-005 - 후속 책임 보존
- **Statement:** Schedule·Prompt·Recovery·QA·Runbook 세부사항은 AUT-002~006의 승인 계약으로 인계해야 한다.
- **Verification:** Architecture 문서의 Handoff와 비범위를 확인한다.
- **Exceptions:** 없음.

## 17.B 입력과 실행 계약 (AUT-006 ~ AUT-010)

### AUT-006 - Binding 고정
- **Statement:** 실행 전 기준 문서·Project·Runtime·입력의 ID·버전·상태·해시를 고정해야 한다.
- **Verification:** Binding과 Input Snapshot을 검사한다.
- **Exceptions:** 동적 입력은 조회 시점과 결과 해시를 기록한다.

### AUT-007 - Execution Contract
- **Statement:** 입력·출력·상태·권한·실패·증거·완료 조건을 실행 전에 정의해야 한다.
- **Verification:** Contract 필수 항목과 실제 Plan을 대조한다.
- **Exceptions:** 탐색 실행은 외부 부작용을 금지하고 제한을 명시한다.

### AUT-008 - Preflight Gate
- **Statement:** Binding·입력·환경·권한·의존성·중지 지시를 확인한 뒤 실행해야 한다.
- **Verification:** Preflight Evidence와 READY 전이를 확인한다.
- **Exceptions:** 없음.

### AUT-009 - Run 고유성
- **Statement:** 각 실행은 고유 run_id와 시작 주체·시각·환경·Contract를 가져야 한다.
- **Verification:** Run Record 식별 필드를 확인한다.
- **Exceptions:** 없음.

### AUT-010 - 입력 불변성
- **Statement:** 실행 중 의미 있는 입력·Binding 변경은 새 Snapshot과 영향 검토·재승인을 요구한다.
- **Verification:** 시작 이후 Diff와 Approval을 검사한다.
- **Exceptions:** Contract가 허용한 비의미 Metadata 갱신은 기록 후 적용할 수 있다.

## 17.C 상태와 사람 통제 (AUT-011 ~ AUT-015)

### AUT-011 - 명시적 상태 전이
- **Statement:** 모든 상태 변경은 from·to·actor·시각·근거·증거를 가져야 한다.
- **Verification:** State Transition Log를 검사한다.
- **Exceptions:** 없음.

### AUT-012 - 불확실성 보존
- **Statement:** PARTIAL·FAILED·BLOCKED·UNKNOWN을 SUCCEEDED 또는 전체 완료로 축소하지 않아야 한다.
- **Verification:** Step 결과·외부 상태·최종 상태를 대조한다.
- **Exceptions:** 없음.

### AUT-013 - Human Gate 결속
- **Statement:** 승인은 정확한 Run·Binding·입력·Target·행위·유효기간에 결속돼야 한다.
- **Verification:** Approval Record와 실행 입력을 대조한다.
- **Exceptions:** 없음.

### AUT-014 - 비가역 행위 통제
- **Statement:** 공개·삭제·결제·외부 전송·권한 확대 등 중요한 부작용은 명시적 승인 계약을 가져야 한다.
- **Verification:** Side Effect 분류와 Human Gate를 검사한다.
- **Exceptions:** 사전 승인된 저위험 반복 행위는 범위·한도·만료를 가져야 한다.

### AUT-015 - Kill Switch
- **Statement:** 권한 있는 사용자가 신규 실행과 진행 중 부작용을 중지할 수 있어야 한다.
- **Verification:** 중지 권한·전파·확인·기록 경로를 검사한다.
- **Exceptions:** 원자적 단계는 완료 후 추가 단계 차단과 결과 격리를 적용한다.

## 17.D 보안과 실행 안전 (AUT-016 ~ AUT-020)

### AUT-016 - 최소 권한
- **Statement:** 자동화 주체는 작업·환경·기간에 필요한 최소 권한만 가져야 한다.
- **Verification:** actor_id와 권한 Scope·Expiry를 검사한다.
- **Exceptions:** 긴급 권한은 별도 승인·만료·사후 검토를 요구한다.

### AUT-017 - Secret 비기록
- **Statement:** Secret 원문을 Prompt·로그·오류·Artifact·Run Record에 저장하지 않아야 한다.
- **Verification:** Redaction 검사와 secret_ref 사용을 확인한다.
- **Exceptions:** 없음.

### AUT-018 - 환경 격리
- **Statement:** 개발·시험·운영의 Target·Credential·State·Evidence를 분리해야 한다.
- **Verification:** environment_id와 실제 연결·권한을 대조한다.
- **Exceptions:** 공유 자원은 격리 한계와 추가 통제를 승인받는다.

### AUT-019 - Idempotency 통제
- **Statement:** 외부 부작용 작업은 의도·Target·입력·Window를 반영한 Idempotency Key를 가져야 한다.
- **Verification:** 중복 Key와 원격 상태 확인을 검사한다.
- **Exceptions:** 읽기 전용 작업은 중복 허용 근거를 기록할 수 있다.

### AUT-020 - Concurrency 통제
- **Statement:** 동일 자원에 충돌 가능한 Run을 Lock·Queue·Version Check 또는 동등한 방식으로 통제해야 한다.
- **Verification:** 자원 Key·Lock Owner·만료·충돌 결과를 검사한다.
- **Exceptions:** 독립성이 증명된 작업은 병렬 실행할 수 있다.

## 17.E 증거와 검증 (AUT-021 ~ AUT-025)

### AUT-021 - 구조화 Event
- **Statement:** 주요 단계는 run_id·step_id·event_id·type·timestamp를 가진 Event를 남겨야 한다.
- **Verification:** Event Schema와 누락 구간을 검사한다.
- **Exceptions:** 없음.

### AUT-022 - Artifact 계보
- **Statement:** 생성·변환·전달 Artifact는 ID·버전·해시·입력·생성 단계·검증 상태를 가져야 한다.
- **Verification:** Artifact Manifest와 실제 파일을 대조한다.
- **Exceptions:** 외부 원격 객체는 remote_ref와 가능한 무결성 증거를 기록한다.

### AUT-023 - 실제 결과 검증
- **Statement:** 성공 판정은 Worker 응답뿐 아니라 출력 계약과 실제 외부 결과 확인을 포함해야 한다.
- **Verification:** Validation·Delivery Verification과 상태를 대조한다.
- **Exceptions:** 확인 불가는 VERIFYING 또는 UNKNOWN으로 남긴다.

### AUT-024 - 민감 정보 최소화
- **Statement:** 로그·Trace·Evidence는 판정에 필요한 최소 데이터만 수집하고 보호정보를 제거해야 한다.
- **Verification:** 수집 필드·Redaction·접근권한·보존 정책을 검사한다.
- **Exceptions:** 승인된 조사 보존은 목적·범위·기간을 기록한다.

### AUT-025 - Run Record 완결성
- **Statement:** Request부터 Binding·Plan·State·Approval·Step·Artifact·QA·Delivery·위험·Handoff를 연결해야 한다.
- **Verification:** Run Record 필수 참조와 무결성을 검사한다.
- **Exceptions:** 범위 밖 단계는 제외 사유와 Owner를 기록한다.

## 17.F 변경·이식·인계 (AUT-026 ~ AUT-030)

### AUT-026 - Adapter 경계
- **Statement:** 외부 제공자 고유 형식과 오류는 Adapter에서 내부 표준 Contract로 변환해야 한다.
- **Verification:** Provider 의존 필드가 Orchestrator·Record에 누출되는지 검사한다.
- **Exceptions:** 불가피한 고유 기능은 Capability와 대체 경로를 명시한다.

### AUT-027 - 버전된 변경
- **Statement:** 구현·Contract·Adapter·Binding·상태 전이 변경은 버전·영향·승인·효력 시점을 가져야 한다.
- **Verification:** Release Record와 실행 Binding을 대조한다.
- **Exceptions:** 의미 없는 문서 정리는 변경 기록만 남길 수 있다.

### AUT-028 - 수동 대체 경로
- **Statement:** 자동 실행 불가 시 현재 상태·입력·완료 단계·위험을 보존해 승인된 수동 경로로 전환할 수 있어야 한다.
- **Verification:** Manual Handoff와 동일 QA·Record 적용을 검사한다.
- **Exceptions:** 안전하지 않은 수동 우회는 허용하지 않는다.

### AUT-029 - Architecture Gate
- **Statement:** G1~G8 필수 Gate가 PASS일 때만 Production Architecture 후보로 승인해야 한다.
- **Verification:** Gate Evidence와 열린 Critical 결함을 검사한다.
- **Exceptions:** NOT_APPLICABLE은 승인 근거가 있어야 한다.

### AUT-030 - 후속 문서 인계
- **Statement:** Trigger·시간·Prompt·실패·QA·운영 요구를 AUT-002~006의 입력 계약으로 분리 인계해야 한다.
- **Verification:** Handoff Map과 각 책임 문서의 입력을 확인한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Automation Architecture

```text
1. request_id, 승인 Binding, Input Snapshot, environment_id와 Execution Contract를 고정한다.
2. Trigger 수신과 실행 허용을 구분하고 Preflight 전 작업을 시작하지 않는다.
3. Request·Policy·Orchestrator·Worker·Adapter·State·Evidence·Delivery 책임을 분리한다.
4. Control Plane의 정책·승인·중지 권한이 Execution Plane에서 확대되지 않게 한다.
5. 고유 run_id와 Idempotency Key를 만들고 충돌 Run을 Lock·Queue·Version Check로 통제한다.
6. 공개·삭제·결제·외부 전송·권한 확대는 정확한 대상에 결속된 Human Gate를 요구한다.
7. 최소 권한과 환경 격리를 적용하고 Secret 원문을 Prompt·로그·Artifact에 기록하지 않는다.
8. 모든 상태 전이에 actor·시각·근거·증거를 남기고 PARTIAL·FAILED·UNKNOWN을 숨기지 않는다.
9. Worker 응답뿐 아니라 출력 계약과 실제 외부 결과를 검증한다.
10. Event·Trace·Artifact·Approval·QA를 Run Record로 연결하고 민감정보 수집을 최소화한다.
11. 제공자 고유 형식은 Adapter에 제한하고 자동화 불가 시 동일 계약의 수동 경로로 인계한다.
12. Schedule·Prompt·Recovery·QA·Runbook 세부 요구를 AUT-002~006에 분리 인계한다.
```

이 압축 블록은 상세 Architecture의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- AUT-001은 자동화 책임·경계·상태·권한·증거와 실행 통제 구조만 정의한다.
- 구체적인 Schedule·Prompt·Recovery·QA·Runbook은 AUT-002~006이 정의한다.
- 콘텐츠 의미·게시·Lifecycle 판단은 CNT-001~007을 따른다.
- Project 고유 환경·Target·SLA·비용·승인자는 Project 문서가 구체화한다.
- 서비스별 구현은 승인된 Adapter와 Project 운영 계약의 책임이다.

## 19.2 알려진 제한

- 모든 자동화에 같은 구성요소 수·배포 방식·저장소·관찰 도구를 강제하지 않는다.
- 외부 서비스의 가용성·정확성·Rate Limit·정책 변경·데이터 보존을 보장하지 않는다.
- Architecture 적합성이 콘텐츠 품질·법률 적합성·보안 인증을 자동 보증하지 않는다.
- 비용·성능·지연·재시도 Threshold의 구체적 값은 현재 범위에 포함하지 않는다.
- 완전 무인 운영을 기본값으로 가정하지 않으며 사람 승인과 수동 경로를 제거하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 5 순서에 따라 범용 Automation 책임·Control/Execution Plane·Binding·Contract·상태·Human Gate·권한·Secret·Idempotency·Concurrency·Evidence·Adapter·수동 경로와 AUT-001~030 작성; 사용자 명시적 승인 반영 |
