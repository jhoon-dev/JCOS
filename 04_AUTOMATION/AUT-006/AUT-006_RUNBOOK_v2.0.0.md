# JCOS v2.0.0 - AUT-006 RUNBOOK

## 범용 자동화 운영·감시·중단·복구·인계 절차

| Field | Value |
|---|---|
| Document ID | AUT-006 |
| Title | RUNBOOK |
| Korean Title | 범용 자동화 운영·감시·중단·복구·인계 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | AUTOMATION |
| Applies To | 승인된 JCOS Automation Run·Schedule·Prompt·Recovery·QA의 운영 실행과 사람 개입 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~007 v2.0.0 LOCKED, AUT-001~005 v2.0.0 LOCKED |
| Extends | AUT-001~AUT-150 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, COR-008 DECISION RULES, AUT-001~005 |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 AUT-006 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

AUT-006은 자동화 기준을 실제 운영 행동으로 연결하는 마지막 절차 문서다. 운영자는 어떤 명령을 외우는 사람이 아니라 승인된 Runbook Binding, 권한, 대상, 상태, 증거와 중단 조건을 확인하고 검증 가능한 조치를 수행하는 책임자다.

Runbook은 정상 실행뿐 아니라 준비 불완전, 상태 불명, 부분 완료, 도구 장애, 긴급 중단과 교대 인계를 다룬다. 화면의 성공 표시만으로 완료를 선언하지 않고 실제 Target, 산출물, QA Gate와 외부 부작용을 확인한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Operator Session·Runbook Request·Binding·Authority 확인
- 시작 전 Preflight와 Go·Hold·Abort 판정
- Start·Observe·Pause·Resume·Cancel·Kill Switch 절차
- Schedule·Prompt·Tool·Output·Delivery 상태 감시
- Failure·PARTIAL·UNKNOWN 탐지와 Recovery 인계
- Incident·Escalation·Human Gate·Decision Log
- 배포·변경·Rollback·Compensation 운영 순서
- Evidence Capture·Run Record·Shift Handoff·Closure
- 수동 대체 경로와 자동화 불가 시 안전 종료

## 2.2 비범위

- 특정 Shell·CLI·API·Dashboard 버튼·Provider 문법
- 조직 고유 연락처·당직표·Ticket Queue·비밀값
- Project 고유 SLA·RTO·RPO·Budget·승인자 임의 결정
- AUT-001~005의 Architecture·Schedule·Prompt·Recovery·QA 계약 재정의
- 보안·개인정보·법률 Incident 전문 절차 대체
- 승인되지 않은 Production 변경·데이터 삭제·외부 게시 허용

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 권한·상태·Human Gate·Kill Switch | AUT-001 AUTOMATION ARCHITECTURE |
| 일정·Window·Misfire·Backfill·Pause | AUT-002 SCHEDULE POLICY |
| Prompt Package·Tool·Output Contract | AUT-003 PROMPT SYSTEM |
| Failure Class·Retry·Recovery·Compensation | AUT-004 FAILURE RECOVERY |
| QA Plan·Evidence·Defect·Release Gate | AUT-005 QA AUTOMATION |
| 실제 운영 순서·확인·중단·인계 | AUT-006 RUNBOOK |
| Project 고유 Target·SLA·연락망·승인자 | Project Rules·Project Runbook Binding |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Operator Session | 운영자·역할·시간·환경·권한·목적이 고정된 작업 단위 |
| Runbook Request | 대상 Run·행동·사유·우선순위·승인 요구를 지정한 요청 |
| Runbook Binding | 기준·Project·환경·Adapter·Schedule·Run·Target을 결합한 운영 참조 |
| Action Contract | 조치의 목적·전제·권한·Target·부작용·확인·Rollback 계약 |
| Command Adapter | 추상 Action을 특정 운영 도구의 검증된 명령으로 변환하는 경계 |
| Observation | 상태·로그·Metric·Artifact·외부 Target에서 수집한 시점 고정 사실 |
| Decision Point | Go·Hold·Abort·Escalate 등 사람 또는 정책 판정이 필요한 지점 |
| Safe State | 추가 부작용 없이 관찰·인계·복구할 수 있는 검증된 상태 |
| Shift Handoff | 현재 상태·증거·위험·미완료 조치·다음 Owner의 공식 인계 |
| Operational Record | Session·Action·Observation·Decision·Evidence·Closure를 연결한 기록 |

# 4. 운영 원칙과 우선순위

## 4.1 행동 우선순위

| 순서 | 원칙 | 운영 의미 |
|---|---|---|
| 1 | Safety | 사람·데이터·권한·외부 부작용 보호 |
| 2 | Authority | 승인 범위와 Human Gate 준수 |
| 3 | State Truth | UI 표시보다 실제 Target·Evidence 우선 |
| 4 | Containment | 불명 상태와 확산 가능성 우선 격리 |
| 5 | Recoverability | 되돌림·보상·재현 가능성 보존 |
| 6 | Continuity | 승인 범위 안에서 서비스 연속성 유지 |
| 7 | Efficiency | 안전·증거를 훼손하지 않는 범위에서 최적화 |

## 4.2 운영 판정

- GO: 전제·권한·Window·Target·Rollback·Evidence가 완결됨
- HOLD: 변경 없이 대기하며 추가 정보·승인·Dependency를 기다림
- ABORT: 시작 전 요청을 종료하거나 진행 중 조치를 안전 중단함
- PAUSE: 재개 가능한 Checkpoint에서 실행을 일시 정지함
- ESCALATE: 현재 권한·정보·시간·위험 한계를 넘어 상위 판정이 필요함
- MANUAL: 승인된 수동 대체 경로로 전환함

# 5. 필수 입력 계약

| 입력 | 필수 내용 |
|---|---|
| Runbook Request | request_id, action, reason, priority, requested_by |
| Operator Context | operator_id, role, shift, environment, authentication |
| Runbook Binding | foundation·project·automation·adapter·target 참조와 해시 |
| Run Context | run_id, schedule_instance, prompt_package, current_state |
| Action Contract | action_id, preconditions, authority, side_effect, verification |
| Window Contract | time zone, window, deadline, freeze, blackout |
| Recovery Contract | safe state, checkpoint, rollback, compensation, retry limits |
| QA Contract | required gates, evidence, severity, release condition |
| Communication Plan | owner, approver, escalation level, update cadence |
| Handoff Contract | destination, required fields, acknowledgement, deadline |

필수 Target, 권한, 현재 상태, Action Contract 또는 Recovery 경로가 없으면 변경 조치를 시작하지 않고 HOLD 또는 BLOCKED로 기록한다.

# 6. 표준 운영 수명주기

| 단계 | 운영 작업 | 필수 산출물 |
|---|---|---|
| 1 | Runbook Request와 Operator Session 식별 | request_id·session_id·operator |
| 2 | Binding·Target·Authority·상태 고정 | binding·target·authority·snapshot |
| 3 | Window·Dependency·Freeze 확인 | window·dependencies·constraints |
| 4 | Risk·Side Effect·Blast Radius 검토 | risk·impact·containment |
| 5 | Recovery·Rollback·Evidence 준비 | checkpoint·rollback·capture plan |
| 6 | Human Gate와 Go·Hold·Abort 판정 | decision·approver·timestamp |
| 7 | Action Adapter와 Dry Run 검증 | adapter·translated action·preview |
| 8 | 최소 범위 실행과 상관관계 ID 기록 | action_id·attempt_id·started_at |
| 9 | 상태·로그·Artifact·외부 Target 감시 | observations·alerts·evidence |
| 10 | 이상 시 Pause·Contain·Cancel·Escalate | control action·safe state |
| 11 | Recovery·Rollback·Compensation 수행 | recovery_case·actual state |
| 12 | QA Gate와 실제 결과 검증 | gates·defects·residual risk |
| 13 | 종료·정리·권한 회수·기록 고정 | closure·cleanup·hashes |
| 14 | Shift·Owner·후속 문서 인계 | handoff·acknowledgement·next action |

# 7. Operator Session과 접근 통제

Operator Session은 운영자 ID, 역할, 인증 시각, 환경, 승인 범위, 작업 목적, 만료 시각을 가진다. 공유 계정이나 출처 불명 Credential을 사용하지 않으며 Secret 값은 Record·화면 캡처·명령 인수에 불필요하게 남기지 않는다.

권한은 Action에 필요한 최소 범위와 시간으로 제한한다. 승인 범위를 넘어서는 권한이 발견되면 작업 편의를 위해 사용하지 않고 권한 차이를 기록한다. Session 종료 시 임시 Credential·Token·승격 권한을 회수하고 확인한다.

# 8. 시작 전 Preflight

Preflight는 다음을 모두 확인한다.

1. 대상 Project·환경·Run·Schedule·Artifact ID와 해시
2. 현재 상태와 마지막 검증 Observation 시각
3. Window·Deadline·Freeze·Blackout·Dependency 상태
4. Action Contract·Adapter 버전·Capability·권한
5. 예상 부작용·Blast Radius·Kill Switch·Safe State
6. Checkpoint·Backup·Rollback·Compensation 준비
7. QA Gate·Evidence Capture·로그·상관관계 ID
8. Human Gate·Owner·Escalation·Handoff 경로

Dry Run이나 Preview가 가능하면 실제 Target 변경 전에 수행하고, 실제 Action과 의미가 동일한지 Adapter 계약으로 확인한다. Preview 통과는 실제 실행 승인을 대신하지 않는다.

# 9. Start와 정상 감시

Start는 승인된 Action Contract를 변경 없이 Adapter에 전달하고, action_id·run_id·attempt_id·operator_session을 기록한 후 수행한다. 운영자는 복사한 과거 명령이나 화면 기본값으로 Target·환경·버전을 추정하지 않는다.

감시는 Heartbeat, 상태 전이, 처리량, 오류, 비용·시간 Budget, Artifact, 외부 Target과 QA Signal을 포함한다. 단일 Dashboard의 녹색 표시보다 서로 독립된 상태와 실제 결과를 대조한다.

# 10. Pause·Resume·Cancel·Kill Switch

Pause는 Checkpoint와 재개 전제를 확인한 뒤 새 부작용 생성을 멈추는 조치다. Resume은 현재 상태, Binding, Window, Dependency, Budget, Checkpoint 무결성을 다시 확인한 뒤 수행한다.

Cancel은 추가 작업을 중단하지만 이미 발생한 부작용을 되돌리지 않을 수 있다. Kill Switch는 급박한 확산을 막는 비상 통제이며 실행 직후 격리 범위, 미완료 작업, 외부 상태, Recovery 필요성을 기록한다.

# 11. Failure·PARTIAL·UNKNOWN 대응

Failure Event가 발생하면 원인 추정보다 먼저 Target·Run·Attempt·Checkpoint·외부 상태를 Snapshot으로 고정한다. 동일 Action을 반복하기 전에 AUT-004 Retry Eligibility와 Idempotency를 확인한다.

PARTIAL은 성공한 단위와 실패·미확인 단위를 분리하고 전체 성공으로 보고하지 않는다. UNKNOWN은 확인 가능한 조회와 Evidence Capture를 수행하되, 실제 부작용이 없다고 증명되기 전 재시도·삭제·덮어쓰기를 금지한다.

# 12. Recovery·Rollback·Compensation

Recovery Plan은 현재 상태, 목표 Safe State, Action 순서, 권한, 위험, 중단 조건, Verification을 가진다. 계획을 승인받은 뒤 각 단계의 전후 Snapshot을 남긴다.

Rollback은 이전 검증 상태로 복귀할 수 있을 때만 사용한다. 되돌릴 수 없는 외부 전송·게시·결제·삭제는 Compensation으로 처리하며 원래 작업과 별개의 action_id·승인·Evidence를 가진다.

# 13. Escalation과 Communication

Escalation은 Severity, 영향, 긴급도, 현재 상태, 수행 조치, 증거, 필요한 권한·판정, Owner, 다음 Update 시점을 포함한다. 특정 연락 도구가 아니라 Communication Plan의 승인된 채널 Adapter를 사용한다.

상태 Update는 새 사실, 변경된 위험, 결정, 다음 조치와 예상 시점을 구분한다. 추정은 사실처럼 쓰지 않으며 UNKNOWN과 가정을 명시한다. Critical Incident에서는 조사보다 Containment와 사람 안전을 우선한다.

# 14. 변경·배포·Release 운영

변경 실행 전 Candidate 버전, 변경 목록, 승인 상태, Baseline, Rollback Target, Release Window와 QA Record를 확인한다. APPROVED는 LOCKED와 같지 않으며 명시적 잠금 또는 Release 승인이 필요한 경우 별도 Gate를 통과한다.

점진 적용이 가능하면 승인된 최소 범위부터 수행하고 관찰 지점을 둔다. 각 단계는 다음 단계로 넘어가기 전에 Target 상태, Error Budget, QA Signal, 사용자 영향과 Rollback 가능성을 확인한다.

# 15. Evidence·Record·Handoff

Operational Record에는 Session, Request, Binding, Action, Adapter, Target, 전후 Snapshot, Observation, Decision, Approval, Failure·Recovery, QA Gate, Cleanup, Closure를 연결한다.

Shift Handoff는 현재 상태, 완료·미완료 조치, 열린 Defect·Incident, 잔여 Budget, 다음 Deadline, 필요한 승인, 증거 위치, 다음 Owner를 포함한다. 수신자는 acknowledgement와 이해되지 않은 항목을 기록한다.

# 16. Runbook Gate와 결함 처리

| Gate | 통과 조건 |
|---|---|
| G1 Session | Operator·Role·Environment·Expiry·목적 완결 |
| G2 Binding | 기준·Project·Run·Adapter·Target·해시 일치 |
| G3 Preflight | Window·Dependency·권한·상태·Freeze 확인 |
| G4 Safety | Side Effect·Blast Radius·Kill Switch·Safe State 확인 |
| G5 Recovery | Checkpoint·Rollback·Compensation·Evidence 준비 |
| G6 Approval | Human Gate·Go/Hold/Abort·Approver 기록 |
| G7 Execution | Action ID·최소 범위·Adapter·Attempt 추적 |
| G8 Observation | 상태·로그·Artifact·외부 Target 교차 확인 |
| G9 Verification | QA Gate·실제 결과·잔여 위험 판정 |
| G10 Closure | Cleanup·권한 회수·Record·Handoff 확인 |

Target 불일치, 승인 누락, 상태 UNKNOWN, Recovery 불가, Critical QA 결함, Evidence 누락이 있으면 정상 종료 또는 Release 완료로 표시하지 않는다.

# 17. 실행 규칙 (AUT-151 ~ AUT-180)

## 17.A Session과 Binding (AUT-151 ~ AUT-155)

### AUT-151 - Operator Session 식별
- **Statement:** 모든 운영 조치는 operator_id·role·environment·purpose·issued_at·expires_at을 가진 Session 안에서 수행해야 한다.
- **Verification:** 인증 기록과 Operational Record를 대조한다.
- **Exceptions:** 비상 접근은 사유·범위·만료·사후 승인을 기록한다.

### AUT-152 - Runbook Request 고정
- **Statement:** request_id·action·reason·priority·requested_by·target을 실행 전에 고정해야 한다.
- **Verification:** Request와 Action Contract를 대조한다.
- **Exceptions:** 긴급 중단은 사후 Request를 생성하되 최초 Event를 보존한다.

### AUT-153 - Binding 무결성
- **Statement:** Foundation·Project·Automation·Adapter·Run·Target의 ID·버전·상태·해시를 결합해야 한다.
- **Verification:** Runbook Binding과 실제 참조를 검사한다.
- **Exceptions:** Mutable Target은 Snapshot과 변경 감지를 기록한다.

### AUT-154 - 최소 권한
- **Statement:** Action에 필요한 최소 권한·환경·시간 범위만 사용해야 한다.
- **Verification:** Granted Scope와 Action Contract를 대조한다.
- **Exceptions:** 비상 승격은 만료·감사·회수 조건을 가진다.

### AUT-155 - Secret 비기록
- **Statement:** Secret·Token·개인정보를 명령·로그·화면 캡처·Handoff에 불필요하게 남기지 않아야 한다.
- **Verification:** Redaction과 Evidence Manifest를 검사한다.
- **Exceptions:** 검증용 값은 비식별 reference·hash·vault pointer를 사용한다.

## 17.B Preflight와 승인 (AUT-156 ~ AUT-160)

### AUT-156 - Target 재확인
- **Statement:** Action 직전에 Project·Environment·Run·Target·Version·Hash를 재확인해야 한다.
- **Verification:** Preflight Snapshot과 Adapter Target을 대조한다.
- **Exceptions:** Alias는 해석된 불변 ID를 함께 기록한다.

### AUT-157 - Window와 Freeze 준수
- **Statement:** Time Zone·Window·Deadline·Freeze·Blackout·Dependency 조건을 확인해야 한다.
- **Verification:** Schedule Instance와 운영 시각을 대조한다.
- **Exceptions:** 긴급 예외는 승인·영향·종료 시점을 가진다.

### AUT-158 - Side Effect와 Blast Radius
- **Statement:** 외부 변경·전송·게시·삭제·비용과 최대 영향 범위를 실행 전에 명시해야 한다.
- **Verification:** Action Contract와 실제 권한·Target 범위를 검사한다.
- **Exceptions:** 범위 불명은 HOLD 또는 제한된 Dry Run으로 전환한다.

### AUT-159 - Recovery 준비
- **Statement:** Checkpoint·Safe State·Rollback·Compensation·Kill Switch·Evidence Capture를 시작 전에 준비해야 한다.
- **Verification:** Recovery Contract와 접근 가능성을 검사한다.
- **Exceptions:** 되돌릴 수 없는 작업은 강화 Human Gate와 Compensation을 요구한다.

### AUT-160 - Go·Hold·Abort 기록
- **Statement:** 실행 전 Go·Hold·Abort 판정과 기준·Approver·Timestamp를 기록해야 한다.
- **Verification:** Decision Log와 Human Gate를 대조한다.
- **Exceptions:** 자동 Go는 승인 정책과 적용 조건이 고정된 경우에만 허용한다.

## 17.C 실행과 감시 (AUT-161 ~ AUT-165)

### AUT-161 - Adapter 검증
- **Statement:** 추상 Action을 실제 명령으로 변환한 Adapter의 ID·버전·Target·Parameter·부작용을 검증해야 한다.
- **Verification:** Preview와 실제 Invocation Manifest를 대조한다.
- **Exceptions:** 수동 명령은 동일 Action Contract와 검토 기록을 가진다.

### AUT-162 - 최소 범위 실행
- **Statement:** 승인된 최소 Target·Batch·Concurrency·권한 범위에서 시작해야 한다.
- **Verification:** 실제 실행 범위와 Blast Radius를 대조한다.
- **Exceptions:** 원자적 전체 실행은 원자성 근거와 중단 조건을 기록한다.

### AUT-163 - 상관관계 추적
- **Statement:** request_id·session_id·run_id·action_id·attempt_id를 모든 로그·Artifact·외부 Event에 연결해야 한다.
- **Verification:** Operational Trace의 단절을 검사한다.
- **Exceptions:** 외부 시스템 제약은 mapping record를 둔다.

### AUT-164 - 독립 상태 관찰
- **Statement:** UI 상태만으로 성공을 판단하지 않고 로그·Artifact·외부 Target·QA Signal을 교차 확인해야 한다.
- **Verification:** Observation Source와 시점을 검사한다.
- **Exceptions:** 단일 Source만 가능하면 잔여 위험과 추가 확인 조건을 기록한다.

### AUT-165 - Budget·Deadline 감시
- **Statement:** 시간·비용·Attempt·Load·Deadline Budget을 실행 중 감시해야 한다.
- **Verification:** 현재 소비량·잔여량·예측과 Alert를 검사한다.
- **Exceptions:** 한도 변경은 새 승인과 Decision Record를 요구한다.

## 17.D 중단과 복구 (AUT-166 ~ AUT-170)

### AUT-166 - Pause 안전성
- **Statement:** Pause는 새 부작용을 멈추고 재개 가능한 Checkpoint와 미완료 작업을 기록해야 한다.
- **Verification:** Pause 전후 상태와 Queue·Target을 대조한다.
- **Exceptions:** 안전 Pause 불가는 Cancel 또는 Kill Switch로 상승한다.

### AUT-167 - Resume 재검증
- **Statement:** Resume 전 Binding·Window·Dependency·Budget·Checkpoint·권한을 다시 확인해야 한다.
- **Verification:** 원 Session과 Resume Decision을 비교한다.
- **Exceptions:** 의미 있는 변경은 Resume이 아니라 새 Run Re-execution으로 처리한다.

### AUT-168 - Cancel·Kill Switch 구분
- **Statement:** 정상 Cancel과 비상 Kill Switch의 범위·권한·효과·후속 Recovery를 구분해야 한다.
- **Verification:** Control Action과 실제 중단 상태를 검사한다.
- **Exceptions:** 즉시 Kill은 사후 Evidence·승인·영향 평가를 요구한다.

### AUT-169 - UNKNOWN 재실행 금지
- **Statement:** 실제 외부 상태가 UNKNOWN이면 중복 부작용 가능성을 제거하기 전 동일 Action을 반복하지 않아야 한다.
- **Verification:** Remote State Evidence와 AUT-004 Eligibility를 검사한다.
- **Exceptions:** 읽기 전용·멱등성이 증명된 조회는 허용한다.

### AUT-170 - Recovery 단계 검증
- **Statement:** Recovery·Rollback·Compensation의 각 단계는 전후 Snapshot·Action ID·Verification을 가져야 한다.
- **Verification:** Recovery Plan과 실제 상태 전이를 대조한다.
- **Exceptions:** 긴급 Containment는 후속 상세 검증과 Owner를 남긴다.

## 17.E Incident와 Communication (AUT-171 ~ AUT-175)

### AUT-171 - PARTIAL 분리
- **Statement:** 성공·실패·미확인 Target·Step·Artifact를 분리해 전체 성공으로 보고하지 않아야 한다.
- **Verification:** Partial Map과 실제 Target을 대조한다.
- **Exceptions:** 없음.

### AUT-172 - Escalation 완결성
- **Statement:** Escalation은 Severity·영향·긴급도·현재 상태·증거·필요 판정·Owner·다음 Update를 가져야 한다.
- **Verification:** Escalation Record와 acknowledgement를 검사한다.
- **Exceptions:** 채널 장애는 승인된 대체 경로와 전달 증거를 남긴다.

### AUT-173 - 사실과 추정 분리
- **Statement:** Observation·추정·가정·결정을 운영 Update에서 구분해야 한다.
- **Verification:** Source·Timestamp·Confidence·Decision Reference를 검사한다.
- **Exceptions:** 긴급 요약도 UNKNOWN을 성공·실패로 단정하지 않는다.

### AUT-174 - Update Cadence
- **Statement:** 열린 Critical·Major Incident는 승인된 주기와 상태 변화 시점에 Update해야 한다.
- **Verification:** Communication Plan과 실제 Update 시간을 대조한다.
- **Exceptions:** 안전 조치 중 지연은 사유와 다음 시점을 기록한다.

### AUT-175 - 전문 대응 인계
- **Statement:** 보안·개인정보·법률·사람 안전 Incident는 해당 전문 절차와 Owner로 즉시 인계해야 한다.
- **Verification:** Incident Class·Handoff·수신 확인을 검사한다.
- **Exceptions:** 초기 Containment는 최소 범위에서 수행할 수 있다.

## 17.F 검증·종료·인계 (AUT-176 ~ AUT-180)

### AUT-176 - 실제 결과 검증
- **Statement:** 완료 선언 전 내부 상태뿐 아니라 Artifact·외부 Target·부작용·QA Gate를 검증해야 한다.
- **Verification:** Expected State와 실제 Observation을 대조한다.
- **Exceptions:** 검증 불가는 INCONCLUSIVE 또는 UNKNOWN으로 유지한다.

### AUT-177 - Cleanup과 권한 회수
- **Statement:** 임시 자원·파일·세션·Credential·승격 권한·Lock을 종료하고 회수를 검증해야 한다.
- **Verification:** Cleanup Record와 실제 상태를 대조한다.
- **Exceptions:** 보존 자원은 Owner·위치·기간·삭제 조건을 기록한다.

### AUT-178 - Operational Record
- **Statement:** Request·Session·Binding·Action·Observation·Decision·Approval·Recovery·QA·Closure를 해시 추적 기록으로 결합해야 한다.
- **Verification:** Manifest·Timestamp·Lineage·Evidence Pointer를 검사한다.
- **Exceptions:** 보호정보는 Redaction·Retention·검증 대체값을 사용한다.

### AUT-179 - Handoff 수신 확인
- **Statement:** Shift·Owner 인계는 현재 상태·미완료 조치·위험·Deadline·Evidence·다음 Action과 수신 확인을 가져야 한다.
- **Verification:** Handoff Contract와 acknowledgement를 검사한다.
- **Exceptions:** 수신 실패는 상위 Escalation으로 전환한다.

### AUT-180 - Runbook Closure
- **Statement:** Safe State·QA 판정·잔여 위험·Cleanup·Record·Handoff가 완결된 후에만 CLOSED를 표시해야 한다.
- **Verification:** G1~G10과 Closure Record를 검사한다.
- **Exceptions:** 이관 종료는 TRANSFERRED 상태와 새 Owner를 가져야 한다.

# 18. AI용 압축 Runbook

1. operator_id·role·environment·purpose·expiry가 있는 Operator Session을 연다.
2. Request와 Foundation·Project·Automation·Adapter·Run·Target Binding의 버전·상태·해시를 고정한다.
3. Target·Window·Freeze·Dependency·권한·현재 상태를 Action 직전에 재확인한다.
4. Side Effect·Blast Radius·Safe State·Checkpoint·Rollback·Compensation·Kill Switch를 준비한다.
5. Human Gate에서 Go·Hold·Abort와 Approver·Timestamp를 기록한다.
6. Adapter Preview와 실제 Target을 검증하고 승인된 최소 범위에서 action_id·attempt_id로 실행한다.
7. UI뿐 아니라 로그·Artifact·외부 Target·QA Signal과 Budget·Deadline을 감시한다.
8. 이상 시 Pause·Cancel·Kill Switch를 구분하고 Snapshot·Containment·Escalation을 수행한다.
9. PARTIAL·UNKNOWN을 성공으로 축소하지 않고 중복 부작용 확인 전 재실행하지 않는다.
10. Recovery·Rollback·Compensation 각 단계의 전후 상태와 Verification을 기록한다.
11. 완료 전 실제 결과·외부 부작용·QA Gate를 확인하고 임시 자원·권한을 회수한다.
12. Operational Record와 현재 상태·위험·Deadline·Evidence·다음 Action을 수신 확인과 함께 인계한다.

이 압축 블록은 상세 Runbook의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- AUT-006은 범용 운영 순서와 필수 확인·증거·중단·인계를 정의한다.
- 실제 명령·버튼·Endpoint·연락처는 승인된 Project Runbook Binding과 Adapter가 제공한다.
- 운영자는 AUT-001~005의 계약을 임의 변경하지 않으며 예외는 승인·만료·잔여 위험을 가진다.
- QA PASS는 사용자 승인, Release 승인, LOCKED 전환을 자동으로 의미하지 않는다.
- Project 고유 SLA·RTO·RPO·Budget·연락망·당직은 Project Rules가 구체화한다.

## 19.2 알려진 제한

- 모든 외부 시스템이 원자적 Pause·Rollback·상태 조회를 제공한다고 가정하지 않는다.
- Dashboard·로그·Provider 응답은 지연·누락·상충할 수 있어 실제 Target 확인이 필요하다.
- 비상 Kill Switch는 확산을 막지만 이미 발생한 부작용을 되돌리지 않을 수 있다.
- 수동 대체 경로는 자동화와 동일한 추적·권한·증거 수준을 유지하지 못할 수 있다.
- 조직 고유 연락·규제·보안 절차는 이 범용 Runbook만으로 완성되지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 5 순서에 따라 범용 Operator Session·Binding·Preflight·Start·Observe·Pause·Resume·Cancel·Kill Switch·Recovery·Escalation·Evidence·Handoff·Closure와 AUT-151~180 작성·QA·사용자 승인 완료 |
