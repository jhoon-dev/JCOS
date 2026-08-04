# JCOS v2.0.0 - AUT-004 FAILURE RECOVERY

## 범용 실패 분류·재시도·재실행·복구·보상·종료 원칙

| Field | Value |
|---|---|
| Document ID | AUT-004 |
| Title | FAILURE RECOVERY |
| Korean Title | 범용 실패 분류·재시도·재실행·복구·보상·종료 원칙 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | AUTOMATION |
| Applies To | AUT-001 Run과 AUT-002 Schedule Instance, AUT-003 Prompt 실행에서 발생한 실패·부분 완료·미확인 상태 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~007 v2.0.0 LOCKED, AUT-001~003 v2.0.0 LOCKED |
| Extends | AUT-001~AUT-090 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, AUT-001 AUTOMATION ARCHITECTURE, AUT-002 SCHEDULE POLICY, AUT-003 PROMPT SYSTEM |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 AUT-004 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

AUT-004는 실패를 단순히 다시 실행하는 문제가 아니라 현재 외부 상태와 부작용, 입력 유효성, 시간 제한과 복구 가능성을 판정하는 절차로 정의한다. 결과는 무엇이 실패했고, 무엇이 이미 완료됐으며, 어떤 재시도·복구·보상·종료 결정이 어떤 증거로 수행됐는지 재현할 수 있는 Recovery Record여야 한다.

오류 응답이 없다는 사실만으로 성공을 가정하지 않는다. 실제 외부 상태가 불명확하면 `UNKNOWN`을 유지하고, 중복 부작용 가능성을 제거하기 전 재시도하지 않는다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Failure Event 수집·정규화·상관관계
- 입력·권한·정책·Dependency·Provider·Tool·Output·Delivery 실패 분류
- Transient·Persistent·Unknown과 Retry Eligibility 판정
- Retry Budget·Delay·Backoff·Jitter·Retry-After 계약
- 동일 Attempt Retry와 새 Run Re-execution 구분
- Idempotency·중복 부작용·원격 상태 확인
- Checkpoint·Resume·Restart·Rollback·Compensation
- PARTIAL·UNKNOWN·고립된 외부 상태 처리
- Quarantine·Dead Letter·수동 검토·Escalation
- Recovery Verification·Closure·재발 방지 인계

## 2.2 비범위

- 서비스별 Queue·Retry 설정·명령·API 문법
- Schedule 시각·Calendar·Misfire·Backfill 정의
- Prompt 조립·Context·모델·Tool Schema 정의
- 자동 QA 검사식·Threshold·CI 구현
- 운영자별 화면·명령·연락망·당직 순서
- 법률·보안·개인정보 Incident 전문 대응 대체
- Project 고유 RTO·RPO·SLA·Retry 횟수·비용 한도 임의 결정

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| Run·상태·Idempotency·Human Gate·Kill Switch | AUT-001 AUTOMATION ARCHITECTURE |
| Schedule Misfire·Catch-up·Backfill | AUT-002 SCHEDULE POLICY |
| Prompt·Tool·Output Validation 실패 입력 | AUT-003 PROMPT SYSTEM |
| 실패 분류·Retry·Recovery·Compensation·Closure | AUT-004 FAILURE RECOVERY |
| 자동 검사와 Release Gate 구현 | AUT-005 QA AUTOMATION |
| 운영자 명령·수동 복구·Escalation 절차 | AUT-006 RUNBOOK |
| 콘텐츠 정정·게시 Rollback·Lifecycle | CNT-003~007 해당 System |
| RTO·RPO·SLA·비용·연락망 | 해당 Project Rules·Runbook |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Failure Event | 실패·부분·미확인 상태를 나타내는 정규화된 사건 |
| Failure Class | 실패 원인과 처리 성질을 구분한 분류 |
| Attempt | 하나의 Run Step을 한 번 실행한 기록 |
| Retry | 같은 Run·Step·입력 계약 안에서 새 Attempt를 수행하는 것 |
| Re-execution | 변경된 조건 또는 Recovery Plan으로 새 Run을 시작하는 것 |
| Retry Eligibility | 재시도가 안전·유효·허용되는지에 대한 판정 |
| Retry Budget | 횟수·시간·비용·Deadline·부하를 제한하는 계약 |
| Backoff | 연속 Attempt 사이의 승인된 지연 증가 규칙 |
| Retry-After | 외부 시스템이 제공하거나 승인 정책이 정한 최소 재시도 시점 |
| Checkpoint | 안전하게 재개할 수 있는 검증된 중간 상태 |
| Resume | Checkpoint 이후 남은 단계만 수행하는 것 |
| Rollback | 이전의 검증된 상태로 되돌리는 조치 |
| Compensation | 되돌릴 수 없는 부작용을 상쇄하는 별도 조치 |
| Quarantine | 자동 처리를 중단하고 입력·Artifact·상태를 격리하는 것 |
| Dead Letter | 자동 복구 불가 작업을 증거와 함께 수동 검토 경로로 보내는 것 |
| Recovery Record | 실패부터 판정·Attempt·복구·검증·종료까지 연결한 기록 |

# 4. Failure 분류 모델

## 4.1 원인 분류

| Class | 예 | 기본 방향 |
|---|---|---|
| INPUT | 누락·형식·만료·해시 불일치 | 입력 교정 전 Retry 금지 |
| POLICY | 승인·Binding·권한·Gate 불충족 | 사람 결정 또는 정책 해소 |
| DEPENDENCY | 선행 Run·데이터·서비스 준비 안 됨 | Window 안에서 재평가 |
| CAPABILITY | 필수 Context·Tool·형식 능력 부족 | Adapter·환경 변경 또는 BLOCKED |
| PROVIDER | Rate Limit·일시 장애·Timeout | Eligibility와 Budget 안에서 Retry |
| TOOL | Tool 오류·권한·응답 불일치 | 원격 상태·부작용 확인 후 결정 |
| OUTPUT | Parse·Schema·Meaning·Safety 실패 | Prompt·입력·검증 경로 재평가 |
| DELIVERY | 게시·전송·저장·권한·검증 실패 | 실제 Target 상태 확인 후 복구 |
| INTERNAL | Orchestrator·State·Code·Resource 오류 | 격리·수정·새 Release 검토 |
| UNKNOWN | 원인·외부 상태 확인 불가 | 자동 Retry 보류·증거 수집 |

## 4.2 성질 분류

- `TRANSIENT`: 조건 변화 없이 제한된 재시도로 회복 가능
- `PERSISTENT`: 입력·정책·구현·환경 변경 전 반복될 가능성이 높음
- `INTERMITTENT`: 간헐적으로 재현되며 상관관계 분석 필요
- `UNKNOWN`: 원인 또는 부작용 상태를 판단할 수 없음

원인 Class와 성질을 별도로 기록한다. HTTP 코드나 Exception 이름 하나만으로 Retry 가능성을 확정하지 않는다.

# 5. 필수 입력 계약

| 입력 | 필수 내용 |
|---|---|
| Failure Event | event_id, run_id, step_id, attempt_id, observed_at |
| Run Binding | 기준·Project·Schedule·Prompt·환경·해시 |
| State Snapshot | 이전·현재 상태, Checkpoint, 외부 Target 상태 |
| Side Effect Record | 실행된 쓰기·공개·전송·삭제·결제와 remote_ref |
| Error Evidence | class 후보, code, message, trace, provider status |
| Recovery Contract | retry·resume·restart·rollback·compensation 허용 범위 |
| Budget Contract | attempts, elapsed, cost, deadline, load 한도 |
| Authority | 자동·사람 결정 권한, Human Gate, Kill Switch |

입력·상태·부작용 중 하나라도 불명확하면 무조건 Retry하지 않고 `UNKNOWN` 또는 `BLOCKED`와 해소 책임을 기록한다.

# 6. 표준 Failure Recovery 수명주기

| 단계 | 작업 | 필수 산출물 |
|---|---|---|
| 1 | Failure Event 식별·상관관계 | event_id·run·step·attempt |
| 2 | 실행·입력·외부 상태 Snapshot | binding·checkpoint·remote state |
| 3 | 영향·부작용·Critical 여부 확인 | scope·targets·exposure |
| 4 | 원인 Class·성질·확신도 판정 | classification·confidence |
| 5 | Retry Eligibility와 금지 조건 판정 | eligible·blocked reasons |
| 6 | Budget·Deadline·Retry-After 확인 | remaining·next_allowed_at |
| 7 | Retry·Resume·Restart·Rollback·Compensation 선택 | recovery decision |
| 8 | Human Gate·Kill Switch·Owner 확인 | approval_ref·authority |
| 9 | Recovery Plan과 입력 Snapshot 고정 | plan_id·version·hash |
| 10 | 새 Attempt 또는 Run 실행 | attempt_id·parent_ref |
| 11 | 실제 외부 결과·부작용 재검증 | verification·remote refs |
| 12 | 반복 실패 시 Quarantine·Dead Letter·Escalation | quarantine_ref·incident_ref |
| 13 | Recovery Gate와 최종 상태 판정 | recovered·failed·unknown |
| 14 | Record 완결·재발 방지·QA·Runbook 인계 | record·follow-up refs |

# 7. 감지, Triage와 영향

Failure Event는 원 오류, Run·Step·Attempt, 시각, 환경, Target, 입력·출력 참조와 관찰자를 가진다. 같은 원인의 중복 Event는 하나의 Recovery Case에 연결하되 원본을 보존한다.

Triage는 다음을 우선 확인한다.

1. 민감정보·권한·잘못된 Target·비가역 부작용 여부
2. 실제 외부 상태와 부분 완료 범위
3. 진행 중 추가 부작용을 막을 Kill Switch 필요성
4. 영향받는 Run·Schedule Instance·Variant·사용자
5. Deadline·SLA·승인자와 증거 보존 필요성

Critical이면 자동 Retry보다 중지·격리·권한 있는 Escalation을 우선한다.

# 8. Retry Eligibility

Retry는 다음 조건을 모두 확인한다.

- 입력·Binding·Target이 여전히 유효함
- 같은 작업을 다시 해도 중복 부작용이 없거나 차단됨
- 실제 외부 상태가 확인됐거나 안전한 조회 경로가 있음
- 오류 성질이 TRANSIENT이거나 승인된 재평가 조건이 충족됨
- Window·Deadline·Budget·Rate·비용 한도 안에 있음
- Retry 금지·Pause·Kill Switch·Human Gate가 없음

INPUT·POLICY·CAPABILITY·PERSISTENT·UNKNOWN 실패는 원칙적으로 조건 변경 또는 사람 결정 전 자동 Retry하지 않는다.

# 9. Retry Budget와 Delay

Retry Budget는 다음 한도를 함께 관리한다.

| 한도 | 의미 |
|---|---|
| Attempt | Step·Run·Target별 최대 횟수 |
| Elapsed | 최초 실패부터 허용되는 총 시간 |
| Deadline | Schedule·Delivery·업무상 최종 유효 시각 |
| Cost | 금액·Token·Compute·외부 호출 한도 |
| Load | 동시성·Rate·Queue·Provider 보호 한도 |
| Error | 같은 Class·Signature의 반복 허용 한도 |

Backoff·Jitter·Retry-After는 다음 Attempt의 최소 가능 시점을 계산한다. 외부 Retry-After가 내부 정책보다 늦으면 더 보수적인 시점을 적용한다. 구체적 수치는 Project 계약이 정의한다.

Budget 소진을 성공으로 축소하지 않고 `FAILED`, `BLOCKED` 또는 `ESCALATED`로 전환한다.

# 10. Retry와 Re-execution

Retry는 같은 Run·Step·Input Snapshot·Contract를 유지하며 새 attempt_id를 만든다. 입력·Prompt·Tool·Target·권한·코드·Adapter가 의미 있게 바뀌면 같은 Retry가 아니라 새 Run Re-execution이다.

Re-execution은 새 run_id와 Binding·Recovery Plan·변경 Diff를 가지며 원 Run과 계보를 연결한다. Schedule 재실행은 AUT-002 Catch-up·Backfill 계약도 확인한다.

재실행 전에 이전 Attempt가 늦게 성공했거나 외부 부작용을 만들었는지 다시 확인한다.

# 11. Checkpoint, Resume와 Restart

Checkpoint는 단계 완료, 산출물 해시, 외부 상태, 검증 결과와 다음 허용 단계를 포함한다. 응답 수신이나 로그 한 줄만으로 Checkpoint를 확정하지 않는다.

Resume는 Checkpoint 이후 남은 단계만 수행하며 이미 완료된 부작용을 반복하지 않는다. Checkpoint의 Binding·입력·Artifact·권한이 현재도 유효한지 검증한다.

안전한 Checkpoint가 없거나 상태가 손상됐으면 전체 Restart보다 먼저 격리·Rollback·사람 결정을 검토한다.

# 12. Rollback과 Compensation

Rollback은 이전 검증 상태, 정확한 Target, 영향 범위, 실행 순서, 승인과 Rollback 후 검증을 가진다. 단순히 이전 파일을 다시 올리는 행위가 아니다.

되돌릴 수 없는 전송·알림·결제·외부 노출은 Compensation을 정의한다. Compensation은 정정·취소·환불·차단·후속 통지처럼 부작용을 상쇄하지만 원 행위를 삭제하지 않으며 별도 결과와 증거를 가진다.

Rollback 또는 Compensation이 더 큰 위험을 만들 수 있으면 자동 실행하지 않고 Human Gate로 인계한다.

# 13. PARTIAL과 UNKNOWN

PARTIAL은 Target·Variant·Step·Artifact별 성공과 실패를 분리한다. 성공 부분을 무조건 되돌리거나 실패 부분만 무조건 재시도하지 않고 일관성·사용자 영향·중복을 평가한다.

UNKNOWN은 외부 시스템 Timeout, 응답 유실, 상태 조회 불가처럼 실제 부작용을 알 수 없는 상태다. 조회·대조·사람 확인으로 상태를 확정하기 전 같은 쓰기를 반복하지 않는다.

상태 확정 불가가 Deadline을 넘으면 UNKNOWN을 유지한 채 Quarantine·Escalation하고 성공으로 종료하지 않는다.

# 14. Quarantine, Dead Letter와 Escalation

Quarantine은 의심 입력·Artifact·응답·Credential 참조·현재 상태를 운영 경로와 분리하고 접근권한·보존 기간을 기록한다. 보호정보를 격리 로그에 다시 노출하지 않는다.

Dead Letter에는 다음을 포함한다.

- Recovery Case·Run·Step·Attempt 참조
- Failure Class·Signature·횟수·최종 증거
- 입력·Binding·Checkpoint·부작용 상태
- 시도한 Recovery와 실패 이유
- 필요한 사람 결정·Owner·기한
- 재처리 조건과 중복 방지 Key

Escalation은 Severity, 영향, 긴급도, Owner, 필요한 권한과 다음 업데이트 시점을 가진다. 실제 연락·당직 절차는 AUT-006이 정의한다.

# 15. Recovery Verification과 Closure

복구 후에는 원 오류가 사라졌는지만 보지 않고 다음을 검증한다.

- 기대 출력·Artifact·Schema·해시
- 실제 외부 Target·가시성·권한·부작용
- 중복·누락·부분 상태·Variant 일관성
- Schedule의 다음 Instance와 활성 상태
- Prompt·Tool·Adapter·Credential의 현재 Binding
- 열린 결함·잔여 위험·사람 후속 조치

Closure 상태는 `RECOVERED`, `COMPENSATED`, `FAILED_FINAL`, `CANCELLED`, `QUARANTINED`, `ESCALATED`, `UNKNOWN` 중 하나와 근거를 가진다. `RECOVERED`는 Recovery QA Gate 통과를 요구한다.

# 16. Recovery QA Gate와 결함 처리

| Gate | 통과 조건 |
|---|---|
| G1 Event | Run·Step·Attempt·시각·오류 증거 추적 가능 |
| G2 State | 입력·Binding·Checkpoint·외부 부작용 Snapshot 고정 |
| G3 Classification | 원인·성질·확신도·영향·Critical 판정 완결 |
| G4 Eligibility | Retry 금지·Idempotency·Window·Budget·권한 확인 |
| G5 Plan | Retry·Resume·Restart·Rollback·Compensation 결정 승인 |
| G6 Execution | 새 Attempt·Run·Plan·상태 전이·증거 추적 가능 |
| G7 Verification | 출력·외부 상태·중복·일관성·잔여 위험 확인 |
| G8 Record | Closure·Quarantine·Escalation·후속 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. Critical 결함이 열려 있으면 자동 Retry나 `RECOVERED` 판정을 허용하지 않는다.

Critical 결함의 예는 UNKNOWN 쓰기 재시도, 중복 결제·게시·전송, 무승인 Rollback, Secret 재노출, 잘못된 Production Target 복구, 부분 실패의 전체 성공 보고다.

# 17. 실행 규칙 (AUT-091 ~ AUT-120)

## 17.A 감지와 분류 (AUT-091 ~ AUT-095)

### AUT-091 - Failure Event 식별
- **Statement:** 모든 실패는 고유 event_id와 run_id·step_id·attempt_id·observed_at을 가져야 한다.
- **Verification:** Failure Event 필수 필드를 확인한다.
- **Exceptions:** 없음.

### AUT-092 - 상태 Snapshot
- **Statement:** 분류 전 입력·Binding·Checkpoint·외부 Target·부작용 상태를 고정해야 한다.
- **Verification:** State Snapshot과 Run Record를 대조한다.
- **Exceptions:** 확인 불가는 UNKNOWN과 조회 제한을 기록한다.

### AUT-093 - 영향 우선 Triage
- **Statement:** 민감정보·권한·잘못된 Target·비가역 부작용·진행 중 영향부터 확인해야 한다.
- **Verification:** Impact Assessment와 Kill Switch 결정을 검사한다.
- **Exceptions:** 없음.

### AUT-094 - 이중 분류
- **Statement:** 실패는 원인 Class와 TRANSIENT·PERSISTENT·INTERMITTENT·UNKNOWN 성질을 별도로 가져야 한다.
- **Verification:** Error Evidence·외부 상태·분류 근거를 대조한다.
- **Exceptions:** 초기 분류는 confidence와 재평가 조건을 기록한다.

### AUT-095 - 오류 코드 비단독 판정
- **Statement:** 상태 코드·Exception·메시지 하나만으로 Retry 가능성을 확정하지 않아야 한다.
- **Verification:** 입력·부작용·Window·Budget·정책 근거를 함께 확인한다.
- **Exceptions:** 승인된 명확한 읽기 전용 Transient Signature는 단축 판정할 수 있다.

## 17.B Retry Eligibility와 Budget (AUT-096 ~ AUT-100)

### AUT-096 - Retry Eligibility
- **Statement:** 입력·Binding·Target·Idempotency·외부 상태·Window·Budget·권한을 통과한 경우만 Retry해야 한다.
- **Verification:** Eligibility Checklist와 Attempt를 대조한다.
- **Exceptions:** 없음.

### AUT-097 - UNKNOWN 쓰기 금지
- **Statement:** 외부 쓰기 결과가 UNKNOWN이면 실제 상태 확인 전 같은 부작용을 반복하지 않아야 한다.
- **Verification:** remote_ref 조회·대조와 후속 Attempt를 검사한다.
- **Exceptions:** 원자적 Idempotency가 증명된 경로는 근거를 기록한다.

### AUT-098 - Retry Budget
- **Statement:** Attempt·Elapsed·Deadline·Cost·Load·Error 한도를 함께 관리해야 한다.
- **Verification:** Budget 소비와 remaining 값을 검사한다.
- **Exceptions:** 긴급 확대는 Human Gate·만료·비용 영향을 요구한다.

### AUT-099 - Delay 준수
- **Statement:** Backoff·Jitter·Retry-After 중 적용되는 가장 보수적인 다음 시점 전 Retry하지 않아야 한다.
- **Verification:** failure_at·next_allowed_at·attempt_at을 대조한다.
- **Exceptions:** 안전·법적 긴급 조치는 별도 승인 경로를 따른다.

### AUT-100 - Budget 소진 투명성
- **Statement:** Retry Budget 소진을 성공으로 숨기지 않고 FAILED·BLOCKED·ESCALATED 중 적절한 상태로 전환해야 한다.
- **Verification:** Budget과 최종 상태·Escalation을 검사한다.
- **Exceptions:** 없음.

## 17.C Retry·Resume·재실행 (AUT-101 ~ AUT-105)

### AUT-101 - Attempt 고유성
- **Statement:** 각 Retry는 같은 Run·Step 안에서 고유 attempt_id와 이전 Attempt 참조를 가져야 한다.
- **Verification:** Attempt Chain과 입력 해시를 검사한다.
- **Exceptions:** 없음.

### AUT-102 - Retry와 Re-execution 분리
- **Statement:** 입력·Prompt·Tool·Target·권한·Code·Adapter 의미가 바뀌면 새 Run Re-execution으로 처리해야 한다.
- **Verification:** Diff·run_id·parent_run_ref를 확인한다.
- **Exceptions:** 의미 없는 전송 Metadata 변경은 같은 Run에 기록할 수 있다.

### AUT-103 - Checkpoint 검증
- **Statement:** Resume에 사용할 Checkpoint는 완료 단계·Artifact·외부 상태·검증·다음 단계가 완결돼야 한다.
- **Verification:** Checkpoint Manifest와 실제 상태를 대조한다.
- **Exceptions:** 불완전 Checkpoint는 사용하지 않는다.

### AUT-104 - 완료 단계 비반복
- **Statement:** Resume는 검증된 완료 단계와 외부 부작용을 다시 실행하지 않아야 한다.
- **Verification:** Checkpoint 이후 Plan과 Tool Timeline을 검사한다.
- **Exceptions:** 승인된 재검증 읽기 작업은 허용한다.

### AUT-105 - 늦은 성공 확인
- **Statement:** 새 Attempt·Run 전에 이전 Timeout 작업이 늦게 성공했는지 원격 상태를 확인해야 한다.
- **Verification:** remote_ref·idempotency_key·actual state를 검사한다.
- **Exceptions:** 읽기 전용 무부작용 작업은 재실행 근거를 기록한다.

## 17.D Rollback·Compensation·부분 상태 (AUT-106 ~ AUT-110)

### AUT-106 - Rollback Baseline
- **Statement:** Rollback은 이전 검증 상태·정확한 Target·순서·승인·완료 검증을 가져야 한다.
- **Verification:** Rollback Plan과 실제 결과를 대조한다.
- **Exceptions:** Baseline 불명확 시 자동 Rollback하지 않는다.

### AUT-107 - Compensation 분리
- **Statement:** 비가역 부작용은 원 행위를 삭제한 것으로 표시하지 않고 별도 Compensation과 결과를 기록해야 한다.
- **Verification:** 원 Side Effect와 Compensation Record를 연결한다.
- **Exceptions:** 없음.

### AUT-108 - 위험 증가 금지
- **Statement:** Rollback·Compensation이 더 큰 영향·손실·법적 위험을 만들 수 있으면 Human Gate 전 실행하지 않아야 한다.
- **Verification:** Risk Assessment와 Approval을 검사한다.
- **Exceptions:** 즉시 차단은 증거 보존과 별도로 수행할 수 있다.

### AUT-109 - PARTIAL 분해
- **Statement:** 부분 완료는 Target·Variant·Step·Artifact별 성공·실패·UNKNOWN을 분리해야 한다.
- **Verification:** Partial Map과 전체 상태를 대조한다.
- **Exceptions:** 없음.

### AUT-110 - 일관성 복구
- **Statement:** 부분 상태의 Retry·Rollback·Compensation은 전체 관계와 사용자 영향을 검증해야 한다.
- **Verification:** 전후 Consistency Check와 Variant Map을 검사한다.
- **Exceptions:** 독립 Target은 독립성 근거를 기록한다.

## 17.E 격리와 Escalation (AUT-111 ~ AUT-115)

### AUT-111 - Quarantine
- **Statement:** 의심 입력·Artifact·응답·상태를 운영 경로와 분리하고 접근·보존·해제 조건을 기록해야 한다.
- **Verification:** quarantine_ref와 권한·Retention을 검사한다.
- **Exceptions:** 없음.

### AUT-112 - Dead Letter 완결성
- **Statement:** 자동 복구 불가 작업은 원인·증거·시도·부작용·Owner·재처리 조건과 함께 Dead Letter로 인계해야 한다.
- **Verification:** Dead Letter 필수 필드를 검사한다.
- **Exceptions:** 즉시 폐기 금지 입력은 Quarantine을 유지한다.

### AUT-113 - 중복 재처리 방지
- **Statement:** Dead Letter 재처리는 새 승인·Run·Idempotency 확인과 이전 상태 검증을 요구한다.
- **Verification:** reprocess_ref와 parent Recovery Case를 검사한다.
- **Exceptions:** 없음.

### AUT-114 - Escalation 계약
- **Statement:** Escalation은 Severity·영향·긴급도·Owner·필요 권한·다음 업데이트 시점을 가져야 한다.
- **Verification:** Escalation Record와 AUT-006 Handoff를 확인한다.
- **Exceptions:** 없음.

### AUT-115 - 보호정보 격리
- **Statement:** Quarantine·Dead Letter·Incident 기록에 Secret·개인정보·기밀을 불필요하게 복사하지 않아야 한다.
- **Verification:** Redaction·접근권한·보존 정책을 검사한다.
- **Exceptions:** 승인된 증거 보존은 최소 범위와 기간을 기록한다.

## 17.F 검증·종료·인계 (AUT-116 ~ AUT-120)

### AUT-116 - 실제 복구 검증
- **Statement:** Recovery 성공은 내부 응답뿐 아니라 출력·Artifact·외부 Target·부작용·일관성 확인을 포함해야 한다.
- **Verification:** Recovery Verification과 실제 상태를 대조한다.
- **Exceptions:** 확인 불가는 UNKNOWN을 유지한다.

### AUT-117 - Closure 상태
- **Statement:** Recovery Case는 RECOVERED·COMPENSATED·FAILED_FINAL·CANCELLED·QUARANTINED·ESCALATED·UNKNOWN 중 하나와 근거를 가져야 한다.
- **Verification:** Gate 결과와 Closure를 대조한다.
- **Exceptions:** 없음.

### AUT-118 - Recovery Record
- **Statement:** Event·Snapshot·Class·Eligibility·Budget·Plan·Attempt·Side Effect·Verification·Closure를 연결해야 한다.
- **Verification:** Recovery Record 필수 참조와 무결성을 검사한다.
- **Exceptions:** 범위 밖 항목은 제외 근거를 기록한다.

### AUT-119 - Recovery Gate
- **Statement:** G1~G8 필수 Gate가 PASS일 때만 RECOVERED로 표시해야 한다.
- **Verification:** Gate Evidence와 열린 Critical 결함을 검사한다.
- **Exceptions:** NOT_APPLICABLE은 승인 근거가 있어야 한다.

### AUT-120 - QA·Runbook 인계
- **Statement:** Failure Class·Plan·Attempt·잔여 위험·수동 조치를 AUT-005·006의 입력 계약으로 인계해야 한다.
- **Verification:** Handoff 필수 필드와 수신 Record를 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Failure Recovery

```text
1. failure event를 run·step·attempt와 연결하고 입력·Binding·Checkpoint·외부 상태를 고정한다.
2. 민감정보·잘못된 Target·비가역 부작용·진행 중 영향을 먼저 확인하고 필요하면 중지한다.
3. INPUT·POLICY·DEPENDENCY·CAPABILITY·PROVIDER·TOOL·OUTPUT·DELIVERY·INTERNAL·UNKNOWN 원인과 성질을 분리한다.
4. 오류 코드 하나로 Retry를 결정하지 말고 입력·부작용·Idempotency·Window·Budget·권한을 검사한다.
5. UNKNOWN 쓰기는 실제 원격 상태 확인 전 반복하지 않는다.
6. Attempt·Elapsed·Deadline·Cost·Load·Error Budget과 Backoff·Jitter·Retry-After를 지킨다.
7. 같은 계약은 Retry, 입력·Prompt·Tool·Target·Code 변경은 새 Run Re-execution으로 분리한다.
8. 검증된 Checkpoint 이후만 Resume하고 완료 단계와 외부 부작용을 반복하지 않는다.
9. Rollback은 이전 Baseline과 검증을 요구하고 비가역 행위는 별도 Compensation으로 기록한다.
10. PARTIAL은 Target별로 분해하고 UNKNOWN·Budget 소진·반복 실패를 성공으로 숨기지 않는다.
11. 자동 복구 불가는 Quarantine·Dead Letter·Escalation으로 Owner와 재처리 조건을 인계한다.
12. 실제 출력·외부 상태·중복·일관성을 검증하고 Recovery Record를 AUT-005·006에 인계한다.
```

이 압축 블록은 상세 Failure Recovery의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- AUT-004는 실패 감지 이후 분류·Retry·Resume·Re-execution·Rollback·Compensation·격리·Closure 계약만 정의한다.
- 실행 권한·상태·Idempotency는 AUT-001, Schedule 누락은 AUT-002, Prompt 검증 실패 입력은 AUT-003을 따른다.
- 자동 검사 구현은 AUT-005, 실제 운영자 명령·연락·수동 복구 순서는 AUT-006이 정의한다.
- 콘텐츠 정정·게시 Rollback·Lifecycle 처리는 CNT-003~007을 따른다.
- Project 고유 RTO·RPO·SLA·Budget·Severity·연락망은 Project 문서가 구체화한다.

## 19.2 알려진 제한

- 모든 오류에 같은 Retry 횟수·Backoff·Rollback·Compensation을 강제하지 않는다.
- 외부 시스템의 실제 상태·원자성·Idempotency·가용성을 보장하지 않는다.
- Recovery 성공이 원인 제거·재발 방지·법률·보안 적합성을 자동 보증하지 않는다.
- 분산 시스템의 동시성·지연·응답 유실로 UNKNOWN 상태가 장기간 유지될 수 있다.
- 실제 Incident 연락망·명령·서비스별 복구 절차는 현재 범위에 포함하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 5 순서에 따라 범용 Failure Event·분류·Retry Eligibility·Budget·Backoff·Checkpoint·Resume·Re-execution·Rollback·Compensation·Partial·Unknown·Quarantine·Dead Letter·Escalation·Closure와 AUT-091~120 작성·QA·사용자 승인 완료 |
