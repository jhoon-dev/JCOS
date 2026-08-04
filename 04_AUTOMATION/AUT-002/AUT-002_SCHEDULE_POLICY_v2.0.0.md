# JCOS v2.0.0 - AUT-002 SCHEDULE POLICY

## 범용 예약·시간대·실행 창·중복·지연·Backfill 통제 원칙

| Field | Value |
|---|---|
| Document ID | AUT-002 |
| Title | SCHEDULE POLICY |
| Korean Title | 범용 예약·시간대·실행 창·중복·지연·Backfill 통제 원칙 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | AUTOMATION |
| Applies To | 승인된 Automation Architecture에서 시간·Calendar·사건 조건으로 시작하는 반복·예약 실행 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~007 v2.0.0 LOCKED, AUT-001 v2.0.0 LOCKED |
| Extends | AUT-001~AUT-030 |
| Depends On | COR-007 VERSION POLICY, COR-008 DECISION RULES, CNT-007 CONTENT LIFECYCLE, AUT-001 AUTOMATION ARCHITECTURE |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 AUT-002 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

AUT-002는 같은 예약 정의가 환경과 도구가 달라도 동일한 시간 의미와 실행 의도를 유지하도록 표준 Schedule 계약을 정의한다. 결과는 언제 실행이 예정됐고, 어떤 Calendar와 시간대가 적용됐으며, 실제 Trigger와 지연·누락·중복 처리가 어떻게 결정됐는지 재현할 수 있는 Schedule Record여야 한다.

Scheduler가 작업을 호출했다는 사실만으로 실행이 허용되거나 완료되지 않는다. AUT-001 Preflight, Binding, 권한, Human Gate와 Idempotency를 통과한 새 Run으로 인계돼야 한다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Schedule Request와 승인된 Automation Binding
- IANA 또는 동등한 명시적 Time Zone과 기준 시각
- Calendar, 영업일·휴일·제외일·포함일 계약
- 일회성·주기·Calendar·사건 기반 Schedule 정의
- Trigger Time·Execution Window·Deadline·유효 기간
- Jitter·동시 시작·Overlap·Concurrency Key 통제
- 선행 조건·Dependency·데이터 준비 시점
- Misfire·지연·누락·Catch-up·Backfill 정책
- Schedule 변경·Pause·Resume·Expire·대체 관계
- Next Run 계산·실제 Trigger·Run 인계와 Schedule Record

## 2.2 비범위

- 서비스별 Cron 표현식·UI·API·Queue 설정
- Prompt 본문·모델·Context 구성
- 실패 유형별 재시도·Backoff·복구·보상 실행
- 자동 QA 검사식·Threshold·CI 구성
- 실제 운영자의 명령·화면·Escalation 절차
- Project 고유 게시 시각·휴일표·SLA·비용 한도 임의 결정
- 외부 데이터의 도착·정확성·가용성 보증

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 자동화 책임·Binding·상태·권한·Idempotency 구조 | AUT-001 AUTOMATION ARCHITECTURE |
| 시간대·Calendar·Window·Overlap·Misfire·Backfill | AUT-002 SCHEDULE POLICY |
| 실행 Prompt와 출력 계약 | AUT-003 PROMPT SYSTEM |
| 실행 후 실패·재시도·복구 | AUT-004 FAILURE RECOVERY |
| 자동 검사와 Gate 구현 | AUT-005 QA AUTOMATION |
| 운영자 절차와 수동 실행 | AUT-006 RUNBOOK |
| 콘텐츠 만료·재검토 Trigger | CNT-007 CONTENT LIFECYCLE |
| Project 고유 시간·Calendar·SLA | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Schedule Request | 대상 자동화·시간 의도·기간·Owner·승인자를 지정한 요청 |
| Schedule Binding | schedule_id가 참조하는 AUT-001 Contract와 Project 기준본 |
| Time Zone | Local Time을 UTC Instant로 해석하는 명시적 지역 시간 규칙 |
| Schedule Calendar | 영업일·휴일·포함일·제외일과 적용 기간의 계약 |
| Recurrence Rule | 반복 주기와 종료 조건을 도구 중립적으로 표현한 규칙 |
| Nominal Time | Schedule 정의상 실행돼야 하는 의도된 시각 |
| Trigger Time | Scheduler가 실행 후보 Event를 실제 생성한 시각 |
| Execution Window | 실행을 시작할 수 있는 허용 시간 구간 |
| Deadline | 해당 발생분이 유효하게 완료 또는 인계돼야 하는 한계 시점 |
| Jitter | 동시 부하를 분산하기 위한 승인된 시작 시각 변동 범위 |
| Overlap | 이전 발생분이 종료되기 전에 다음 발생분이 도래한 상태 |
| Misfire | Nominal Time에 Trigger 또는 시작이 이루어지지 않은 상태 |
| Catch-up | 누락된 최근 발생분을 정책에 따라 제한적으로 실행하는 처리 |
| Backfill | 과거 기간의 복수 발생분을 명시적 범위와 승인으로 재생성하는 작업 |
| Schedule Instance | 하나의 Nominal Time에 대응하는 고유 예약 발생분 |
| Schedule Record | 정의·계산·변경·Trigger·누락·Run 인계를 연결한 기록 |

# 4. Schedule 유형과 시간 모델

## 4.1 Schedule 유형

| 유형 | 의미 | 필수 조건 |
|---|---|---|
| ONCE | 한 번의 지정 Instant | 정확한 시각·Time Zone·만료 |
| INTERVAL | 기준점부터 일정 간격 반복 | anchor·interval·종료 조건 |
| CALENDAR | Local Calendar 규칙에 따른 반복 | Time Zone·Calendar·DST 정책 |
| EVENT_WINDOW | 사건 후 허용 Window 안에서 실행 | event_id·중복·Window |
| MANUAL_SCHEDULED | 승인된 미래 수동 실행 예약 | 요청자·승인·유효기간 |

서비스별 표현식은 위 의미 모델의 Adapter 표현일 뿐 기준 정의가 아니다.

## 4.2 시각 표현

모든 시각 기록은 가능한 경우 UTC Instant와 원 Local Time, Time Zone ID, Offset, 계산 규칙 버전을 함께 가진다. `KST`, `EST` 같은 모호한 약어만 사용하지 않는다.

기간은 시작 포함·종료 제외 `[start, end)`를 기본으로 하며 다른 경계는 명시한다. 현재 시각은 승인된 Clock Source에서 읽고 시스템 간 Clock 차이를 기록한다.

# 5. 필수 입력 계약

| 입력 | 필수 내용 |
|---|---|
| Schedule Request | request_id, 목적, 대상 automation_ref, Owner, 승인자 |
| Schedule Binding | AUT-001 Contract·Project ID·버전·상태·해시 |
| Time Contract | schedule_type, Time Zone, anchor, recurrence, Calendar |
| Window Contract | earliest_start, latest_start, deadline, jitter |
| Overlap Contract | concurrency_key, overlap decision, max active |
| Misfire Contract | detect_after, skip·catch-up·hold 결정, 최대 처리량 |
| Effective Period | starts_at, ends_at, pause 조건 |
| Evidence Contract | 계산 결과·Trigger·Run·변경 기록과 보존 위치 |

필수 입력이 없거나 Time Zone·Calendar·Overlap·Misfire 의미가 불명확하면 등록하지 않고 `BLOCKED`와 해소 책임을 기록한다.

# 6. 표준 Schedule 수명주기

| 단계 | 작업 | 필수 산출물 |
|---|---|---|
| 1 | Schedule Request 식별 | request_id·automation_ref·Owner |
| 2 | AUT-001 Binding 고정 | Contract·Project·환경·해시 |
| 3 | 유형·Time Zone·Clock 고정 | type·zone_id·anchor·clock_ref |
| 4 | Calendar·Recurrence 정의 | calendar_ref·rule·종료 조건 |
| 5 | Window·Deadline·Jitter 정의 | earliest·latest·deadline·range |
| 6 | Overlap·Concurrency 정책 정의 | key·max active·decision |
| 7 | Dependency·Data Readiness 정의 | dependency refs·cutoff·timeout class |
| 8 | Misfire·Catch-up·Backfill 계약 정의 | decision·limit·approval route |
| 9 | Schedule 승인·등록 | approval_ref·effective period |
| 10 | Next Instance 계산·검증 | nominal time·UTC·Local·calendar result |
| 11 | Trigger 시 Preflight·중복 확인 | instance_id·idempotency·eligibility |
| 12 | 승인된 Run 생성·인계 | run_id·schedule_instance_ref |
| 13 | 실제 시각·지연·결과 기록 | trigger·start·handoff·status |
| 14 | 다음 Instance·변경·Pause 상태 갱신 | next_run·state·Schedule Record |

# 7. Calendar와 Time Zone

Schedule Calendar에는 적용 지역, 버전, 유효 기간, 영업일, 휴일, 포함일, 제외일과 충돌 우선순위를 기록한다. 휴일 이름만 기록하지 않고 실제 Local Date를 고정한다.

Calendar가 바뀌면 이미 확정된 Instance에 소급 적용하지 않는다. 영향 범위와 재계산 기준 시점을 정하고 미래 Instance를 새 Schedule 버전으로 계산한다.

Daylight Saving Time 전환으로 Local Time이 존재하지 않거나 두 번 존재하면 `SKIP`, `SHIFT_FORWARD`, `FIRST_OCCURRENCE`, `SECOND_OCCURRENCE` 또는 Project가 승인한 동등한 결정을 사전에 명시한다. 도구 기본값에 맡기지 않는다.

# 8. Window, Deadline과 Jitter

Nominal Time은 의도된 기준점이고 Trigger Time과 실제 Start Time은 관찰값이다. 세 값을 분리 기록한다.

Execution Window 밖에서는 기본적으로 새 Run을 시작하지 않는다. Deadline 이후 결과가 무의미하거나 위험하면 `EXPIRED`로 처리하고 AUT-004 또는 AUT-006에 인계한다.

Jitter는 승인된 범위 안에서만 적용하며 Deadline·Dependency·순서·외부 약속을 위반하지 않아야 한다. 실제 적용된 jitter value와 계산 근거를 기록한다.

# 9. Overlap과 Concurrency

## 9.1 Overlap 결정

| 결정 | 의미 |
|---|---|
| FORBID | 이전 Instance가 활성 상태면 새 Instance를 시작하지 않음 |
| QUEUE | 도래 순서대로 대기하되 Window·Deadline을 다시 검증 |
| REPLACE | 권한 있는 취소·보상 후 최신 Instance로 대체 |
| PARALLEL | 독립성이 검증된 Instance를 제한된 수만큼 병렬 실행 |
| MERGE | 여러 발생분을 하나의 승인된 범위로 통합 |

기본값은 `FORBID`이며 다른 결정은 데이터·Target·외부 부작용 독립성과 최대 활성 수를 근거로 승인한다.

## 9.2 Schedule Instance와 중복

각 Instance는 schedule_id, schedule_version, nominal_time과 scope로 고유하게 식별한다. 같은 Instance에서 복수 Trigger가 발생해도 AUT-001 Idempotency 확인 전 새 Run을 만들지 않는다.

# 10. Dependency와 Data Readiness

시간 도래는 입력 준비를 보장하지 않는다. 필요한 선행 Run·파일·데이터 기준 시점·승인·외부 상태를 Dependency로 정의한다.

Dependency가 준비되지 않으면 `WAITING_DEPENDENCY`, `MISFIRED` 또는 `BLOCKED`로 기록하고 승인된 Window 안에서만 다시 평가한다. 구체적인 재시도 간격과 복구는 AUT-004가 정의한다.

데이터 Cutoff 이후 도착한 입력을 현재 Instance에 포함할지 다음 Instance로 넘길지 Project 계약으로 정한다. 입력 Snapshot과 as_of를 Run에 인계한다.

# 11. Misfire와 Catch-up

Misfire 판정은 nominal_time, 허용 지연, Window, Dependency와 실제 Trigger 상태를 기준으로 한다.

| 결정 | 적용 |
|---|---|
| SKIP | 해당 Instance를 실행하지 않고 누락 이유 기록 |
| CATCH_UP_LATEST | 허용 범위에서 가장 최근 Instance 하나 실행 |
| CATCH_UP_ALL | 승인된 최대 수까지 순서대로 실행 |
| HOLD_FOR_APPROVAL | 영향 검토와 사람 승인 전 실행 보류 |
| MERGE | 복수 누락분을 하나의 승인된 입력 범위로 통합 |

Catch-up은 오래된 사실·중복 게시·반복 전송·중복 결제 같은 부작용을 만들 수 있으므로 Target과 콘텐츠 유효성을 다시 확인한다. 누락을 성공으로 표시하지 않는다.

# 12. Backfill

Backfill은 일반 Catch-up과 분리된 명시적 요청으로 수행한다. 다음을 고정한다.

- backfill_request_id와 승인자
- 정확한 시작·종료 Instant와 포함 경계
- 생성할 Schedule Instance 목록과 최대 수
- 입력 기준 시점·현재 데이터 사용 여부
- 외부 부작용 차단 또는 허용 범위
- Rate·Concurrency·비용·Deadline 한도
- Dry Run·샘플 검증·중지 조건
- 기존 Run과 중복 판정·계보

Backfill이 현재 Live 상태를 덮어쓰거나 과거 알림·게시를 재발송할 가능성이 있으면 Human Gate를 요구한다.

# 13. 변경, Pause와 Resume

Schedule 변경은 새 schedule_version, 변경 이유, 영향받는 미래 Instance, 승인과 효력 시점을 가진다. Time Zone·Calendar·Recurrence·Window·Overlap·Misfire 변경은 의미 변경으로 취급한다.

`PAUSED`는 새 Instance의 Run 생성을 막지만 기존 진행 Run의 자동 취소를 의미하지 않는다. 진행 Run의 중지 여부는 별도로 결정한다.

Resume 전에는 Pause 기간의 누락분, 현재 Binding, 다음 Nominal Time, Catch-up 필요성과 Deadline을 재평가한다. Pause 기간 전체를 자동 Backfill하지 않는다.

# 14. 상태와 Schedule Record

## 14.1 Schedule 상태

| 상태 | 의미 |
|---|---|
| DRAFT | 정의 중·등록 불가 |
| REVIEW | 시간·Calendar·영향 검토 중 |
| APPROVED | 승인 완료·아직 비활성 가능 |
| ACTIVE | 유효 기간 안에서 Instance 계산·Trigger 가능 |
| PAUSED | 새 Run 생성 중지 |
| EXPIRED | 유효 기간 종료 |
| SUPERSEDED | 새 Schedule 버전으로 대체 |
| REVOKED | 권한 있는 취소로 사용 금지 |

## 14.2 Schedule Record

Schedule Record는 Request, Binding, Time Contract, Calendar, Window, Overlap, Dependency, Misfire, Approval, Version, Instance, Trigger, Run, 변경, Pause·Resume와 다음 실행 계산을 연결한다.

# 15. Handoff 계약

Scheduler에서 AUT-001 Run으로 인계할 때 다음을 포함한다.

- schedule_id, schedule_version, schedule_instance_id
- nominal_time_utc, nominal_time_local, zone_id, offset
- trigger_time, window, deadline, jitter_applied
- Calendar·Dependency·Overlap·Misfire 판정
- Idempotency·Concurrency Key
- Binding·Input Snapshot·approval_ref
- Schedule Record와 알려진 제한

Prompt 내용은 AUT-003, 실패 복구는 AUT-004, 자동 QA는 AUT-005, 운영자 수동 조치는 AUT-006 계약으로 별도 인계한다.

# 16. Schedule QA Gate와 결함 처리

| Gate | 통과 조건 |
|---|---|
| G1 Request | 대상·목적·Owner·승인자 추적 가능 |
| G2 Binding | AUT-001 Contract·Project·환경·해시 고정 |
| G3 Time | 유형·Time Zone·Clock·Calendar·DST 결정 명확 |
| G4 Window | Nominal·Window·Deadline·Jitter·유효 기간 완결 |
| G5 Safety | Overlap·Idempotency·Concurrency·Dependency 확인 |
| G6 Misfire | 지연·누락·Catch-up·Backfill 결정과 한도 명확 |
| G7 Handoff | Instance·Trigger·Run·입력·승인 참조 완결 |
| G8 Record | 변경·Pause·Resume·다음 실행·계보 기록 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. Critical 결함이 열려 있으면 Schedule을 `ACTIVE`로 전환하지 않는다.

Critical 결함의 예는 Time Zone 누락, Production Schedule의 무단 활성화, 중복 외부 부작용, Deadline 이후 위험 실행, 무승인 Backfill, Pause 무시, 서로 다른 Calendar 버전의 암묵적 혼합이다.

# 17. 실행 규칙 (AUT-031 ~ AUT-060)

## 17.A 요청과 시간 기준 (AUT-031 ~ AUT-035)

### AUT-031 - Schedule 요청 식별
- **Statement:** 모든 Schedule은 고유 schedule_request_id, 대상 automation_ref, 목적, Owner와 승인자를 가져야 한다.
- **Verification:** Schedule Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### AUT-032 - Schedule Binding
- **Statement:** AUT-001 Contract·Project·환경의 ID·버전·상태·해시를 Schedule에 고정해야 한다.
- **Verification:** Schedule Binding과 승인 기준본을 대조한다.
- **Exceptions:** 없음.

### AUT-033 - Time Zone 명시
- **Statement:** Local Time 기반 Schedule은 명시적 zone_id와 UTC 변환 결과를 가져야 한다.
- **Verification:** zone_id·offset·UTC·Local Time을 대조한다.
- **Exceptions:** UTC 전용 Schedule은 zone_id를 UTC로 기록한다.

### AUT-034 - Clock Source
- **Statement:** 계산과 관찰에 사용하는 Clock Source와 허용 Clock 차이를 정의해야 한다.
- **Verification:** Scheduler·Orchestrator Event의 시각 차이를 검사한다.
- **Exceptions:** 없음.

### AUT-035 - Calendar 버전
- **Statement:** 영업일·휴일·포함일·제외일은 버전과 유효 기간이 있는 Calendar로 관리해야 한다.
- **Verification:** nominal date와 적용 Calendar 버전을 확인한다.
- **Exceptions:** Calendar 미적용은 명시적으로 기록한다.

## 17.B Recurrence와 Window (AUT-036 ~ AUT-040)

### AUT-036 - 도구 중립 Recurrence
- **Statement:** Schedule 의미를 유형·anchor·간격·Calendar·종료 조건으로 정의하고 서비스 문법과 분리해야 한다.
- **Verification:** 표준 Time Contract와 Adapter 표현을 대조한다.
- **Exceptions:** 공급자 고유 기능은 Capability와 대체 경로를 기록한다.

### AUT-037 - DST 결정
- **Statement:** 존재하지 않거나 중복되는 Local Time의 처리 결정을 사전에 정의해야 한다.
- **Verification:** DST 경계 Test Case와 계산 결과를 검사한다.
- **Exceptions:** DST가 없는 Time Zone은 NOT_APPLICABLE 근거를 기록한다.

### AUT-038 - Window 경계
- **Statement:** Execution Window의 시작·종료·포함 경계와 Time Zone을 명시해야 한다.
- **Verification:** earliest_start·latest_start와 경계 Test를 확인한다.
- **Exceptions:** 즉시 Event는 최대 지연 또는 만료를 가져야 한다.

### AUT-039 - Deadline 준수
- **Statement:** Deadline 이후 무의미하거나 위험한 Instance를 새로 시작하지 않아야 한다.
- **Verification:** start_time·deadline·최종 결정을 대조한다.
- **Exceptions:** 승인된 Late Run은 영향·승인·새 완료 조건을 기록한다.

### AUT-040 - Jitter 한도
- **Statement:** Jitter는 승인 범위 안에서 Window·Deadline·Dependency·순서를 위반하지 않아야 한다.
- **Verification:** nominal_time·jitter_applied·actual_start를 검사한다.
- **Exceptions:** Jitter 미적용은 0으로 기록할 수 있다.

## 17.C Instance·Overlap·Dependency (AUT-041 ~ AUT-045)

### AUT-041 - Instance 고유성
- **Statement:** 각 발생분은 schedule_id·version·nominal_time·scope로 고유하게 식별해야 한다.
- **Verification:** schedule_instance_id 중복을 검사한다.
- **Exceptions:** 없음.

### AUT-042 - Trigger와 실행 분리
- **Statement:** Trigger Event 수신을 Run 허용 또는 성공으로 간주하지 않아야 한다.
- **Verification:** Trigger·Preflight·Run 전이를 대조한다.
- **Exceptions:** 없음.

### AUT-043 - Overlap 정책
- **Statement:** FORBID·QUEUE·REPLACE·PARALLEL·MERGE 중 승인된 Overlap 결정을 가져야 한다.
- **Verification:** 활성 Run과 새 Instance 처리 결과를 검사한다.
- **Exceptions:** 없음.

### AUT-044 - Idempotency 재사용
- **Statement:** 같은 Schedule Instance의 중복 Trigger는 AUT-001 Idempotency 확인 전 새 Run을 만들지 않아야 한다.
- **Verification:** instance_id·idempotency_key·run_id 관계를 검사한다.
- **Exceptions:** 없음.

### AUT-045 - Dependency Readiness
- **Statement:** 선행 Run·입력·승인·외부 상태의 준비를 Window 안에서 확인해야 한다.
- **Verification:** dependency_ref·cutoff·readiness 결과를 검사한다.
- **Exceptions:** 독립 실행은 Dependency 미적용 근거를 기록한다.

## 17.D Misfire와 Backfill (AUT-046 ~ AUT-050)

### AUT-046 - Misfire 판정
- **Statement:** Nominal Time·허용 지연·Window·Dependency를 기준으로 Misfire를 명시적으로 판정해야 한다.
- **Verification:** expected·trigger·start 시각과 상태를 대조한다.
- **Exceptions:** 없음.

### AUT-047 - Catch-up 한도
- **Statement:** Catch-up 결정은 대상 Instance·최대 수·순서·Window·부작용 검증을 가져야 한다.
- **Verification:** 누락 목록과 생성된 Run을 대조한다.
- **Exceptions:** SKIP은 이유와 다음 Instance를 기록한다.

### AUT-048 - 무승인 Backfill 금지
- **Statement:** 과거 복수 발생분 재실행은 별도 backfill_request_id·범위·한도·승인을 요구한다.
- **Verification:** Backfill Request와 Run 계보를 검사한다.
- **Exceptions:** 없음.

### AUT-049 - Backfill 중복·부작용 통제
- **Statement:** Backfill은 기존 Run·현재 Live 상태·외부 전송·게시·결제와 중복 영향을 확인해야 한다.
- **Verification:** Dry Run·중복 Map·Human Gate를 검사한다.
- **Exceptions:** 읽기 전용 재계산은 부작용 없음 근거를 기록한다.

### AUT-050 - 누락 투명성
- **Statement:** MISFIRED·SKIPPED·EXPIRED·BLOCKED Instance를 성공 또는 무발생으로 숨기지 않아야 한다.
- **Verification:** Instance Registry와 상태 보고를 대조한다.
- **Exceptions:** 없음.

## 17.E 변경·Pause·Resume (AUT-051 ~ AUT-055)

### AUT-051 - Schedule 버전 변경
- **Statement:** 시간대·Calendar·Recurrence·Window·Overlap·Misfire 변경은 새 버전·영향·승인·효력 시점을 가져야 한다.
- **Verification:** Schedule Diff와 미래 Instance 재계산을 검사한다.
- **Exceptions:** 설명 문구 수정은 의미 불변 근거를 기록한다.

### AUT-052 - 미래 적용
- **Statement:** Schedule 변경을 이미 확정·실행된 Instance에 암묵적으로 소급 적용하지 않아야 한다.
- **Verification:** effective_at과 Instance 버전을 대조한다.
- **Exceptions:** 승인된 Backfill 또는 교정은 별도 계보를 가진다.

### AUT-053 - Pause 효력
- **Statement:** PAUSED 상태에서는 새 Run 생성을 막고 진행 Run의 처리 결정을 별도로 기록해야 한다.
- **Verification:** pause_at 이후 Instance·Run과 진행 Run 결정을 검사한다.
- **Exceptions:** 없음.

### AUT-054 - Resume 재평가
- **Statement:** Resume 전 Binding·누락분·다음 Nominal Time·Catch-up·Deadline을 재평가해야 한다.
- **Verification:** Resume Approval과 Next Instance 계산을 확인한다.
- **Exceptions:** 없음.

### AUT-055 - Schedule 대체 계보
- **Statement:** SUPERSEDED·REVOKED·EXPIRED Schedule은 대체 버전·효력·마지막 Instance와 이유를 보존해야 한다.
- **Verification:** Schedule Registry의 상태 전이와 참조를 검사한다.
- **Exceptions:** 대체가 없으면 그 사실을 기록한다.

## 17.F 기록·QA·인계 (AUT-056 ~ AUT-060)

### AUT-056 - Next Run 검증
- **Statement:** 활성 Schedule은 다음 nominal_time의 UTC·Local·zone·Calendar 결과를 계산·검증해야 한다.
- **Verification:** 독립 계산 또는 승인 Test Vector와 대조한다.
- **Exceptions:** 종료된 Schedule은 종료 이유를 기록한다.

### AUT-057 - Schedule Record 완결성
- **Statement:** Request·Binding·Time·Calendar·Window·Overlap·Misfire·Approval·Instance·Run·변경을 연결해야 한다.
- **Verification:** Schedule Record 필수 참조를 검사한다.
- **Exceptions:** 범위 밖 항목은 제외 근거를 기록한다.

### AUT-058 - 실제 시각 기록
- **Statement:** nominal_time, trigger_time, start_time과 run_handoff_time을 분리 기록해야 한다.
- **Verification:** Event Timeline의 순서와 지연을 검사한다.
- **Exceptions:** Run 미생성은 원인 상태를 기록한다.

### AUT-059 - Schedule Gate
- **Statement:** G1~G8 필수 Gate가 PASS일 때만 Production Schedule을 ACTIVE로 전환해야 한다.
- **Verification:** Gate Evidence와 열린 Critical 결함을 검사한다.
- **Exceptions:** NOT_APPLICABLE은 승인 근거가 있어야 한다.

### AUT-060 - 후속 실행 인계
- **Statement:** Schedule Instance·시간·Window·Deadline·중복·입력·승인 정보를 AUT-001 Run과 AUT-003~006에 인계해야 한다.
- **Verification:** Handoff 필수 필드와 수신 Record를 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Schedule Policy

```text
1. schedule_request_id, automation_ref, 승인 Binding, Owner와 승인자를 고정한다.
2. ONCE·INTERVAL·CALENDAR·EVENT_WINDOW 등 유형과 anchor·종료 조건을 도구 중립적으로 정의한다.
3. UTC와 Local Time, 명시적 zone_id·offset·Clock Source를 함께 기록한다.
4. 버전된 Calendar와 DST 중복·누락 시각 처리 결정을 고정한다.
5. Nominal Time, Execution Window, Deadline, Jitter와 유효 기간을 구분한다.
6. Instance ID와 Idempotency Key를 만들고 Trigger 수신을 실행 허용으로 간주하지 않는다.
7. FORBID·QUEUE·REPLACE·PARALLEL·MERGE 중 Overlap 정책과 최대 활성 수를 정한다.
8. 선행 Run·입력·승인·데이터 Cutoff의 준비를 Window 안에서 확인한다.
9. Misfire는 SKIP·CATCH_UP·HOLD·MERGE 중 승인된 결정과 한도로 처리한다.
10. Backfill은 별도 요청·기간·Instance 목록·중복·부작용·승인·중지 조건을 요구한다.
11. 변경은 새 버전으로 미래 적용하고 Pause·Resume 시 누락분과 다음 실행을 재평가한다.
12. nominal·trigger·start·handoff 시각과 Schedule Record를 Run·Recovery·QA·Runbook에 인계한다.
```

이 압축 블록은 상세 Schedule Policy의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- AUT-002는 시간 의미·Calendar·Window·Overlap·Misfire·Backfill·Schedule Record만 정의한다.
- 실행 책임·권한·상태·Idempotency 구조는 AUT-001을 따른다.
- Prompt·Recovery·자동 QA·운영 절차는 AUT-003~006이 정의한다.
- Project 고유 게시 시각·영업일·휴일·SLA는 Project 문서가 구체화한다.
- 서비스별 Cron·UI·API 표현은 Adapter 구현 책임이다.

## 19.2 알려진 제한

- 모든 프로젝트에 같은 실행 시각·주기·Calendar·Catch-up 방식을 강제하지 않는다.
- 운영체제와 공급자의 Clock 정확성·Trigger 지연·가용성을 보장하지 않는다.
- DST·법정 시간·휴일 변경은 Calendar·Time Zone 데이터 갱신과 재검토가 필요하다.
- Schedule 활성화가 입력 준비·콘텐츠 품질·외부 전달 성공을 보장하지 않는다.
- 구체적인 재시도 간격·Backoff·실패 보상은 현재 범위에 포함하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 5 순서에 따라 범용 Schedule 요청·Time Zone·Calendar·DST·Window·Deadline·Jitter·Overlap·Dependency·Misfire·Catch-up·Backfill·Pause·Resume·Record와 AUT-031~060 작성; 사용자 명시적 승인 반영 |
