# JCOS v2.0.0 - CNT-007 CONTENT LIFECYCLE

## 범용 콘텐츠 등록·모니터링·재검토·갱신·통합·폐기·보관 절차

| Field | Value |
|---|---|
| Document ID | CNT-007 |
| Title | CONTENT LIFECYCLE |
| Korean Title | 범용 콘텐츠 등록·모니터링·재검토·갱신·통합·폐기·보관 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | CNT-006이 LIVE로 검증하고 인계한 콘텐츠의 운영 수명주기 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~006 v2.0.0 LOCKED |
| Extends | COR-007 VERSION POLICY VER-001~050 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, CNT-006 PUBLISHING SYSTEM |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-007 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-007은 CNT-006이 인계한 LIVE 콘텐츠를 단발성 산출물이 아닌 추적 가능한 운영 자산으로 관리하는 표준 절차를 정의한다. 결과는 현재 상태, 소유자, 기준 시점, 재검토 조건, 수행 조치와 보관 계보를 재현할 수 있는 Lifecycle Record여야 한다.

게시 당시 정확했다는 사실만으로 영구 유효성을 가정하지 않는다. 실제 접근 상태와 내용의 최신성, 링크·자산·권리, 대체 콘텐츠와 보존 의무를 검토하고 승인된 조치가 검증·기록됐을 때 해당 수명주기 단계가 완료된다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Lifecycle Request와 LIVE Content Binding
- Live Baseline, Content Inventory와 Content Owner 등록
- 정기·조건·사건 기반 Review Trigger 관리
- 접근성·정확성·최신성·링크·자산·권리 상태 평가
- KEEP·UPDATE·CORRECT·CONSOLIDATE·DEPRECATE·UNPUBLISH·ARCHIVE 판정
- 승인된 상위 작성·검수·게시 경로를 통한 유지보수
- Canonical Content와 Variant 관계 관리
- 폐기 안내, 공개 중단, Redirect와 대체 경로 확인
- Retention Schedule, Legal Hold와 Archive Package 관리
- Lifecycle Record, 현재 상태 Registry와 계보 보존

## 2.2 비범위

- 신규 조사·초안·Fact Verdict·SEO·게시 실행 자체
- 서비스별 API·UI·Credential·Webhook·Crawler 구현
- 무인 스케줄러·알림·재시도·상태 수집 Automation 구축
- 채널 알고리즘·성과 예측·광고·전환 최적화
- 법률·보안·개인정보·기록 보존 전문 판단 대체
- Project 고유 SLA·보존 기간·승인자·채널 정책의 임의 결정

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 품질 Gate와 결함 등급 | COR-005 QUALITY GATE |
| 파일·전달·Manifest·무결성 | COR-006 FILE DELIVERY |
| 버전·상태·승인·잠금·보관 | COR-007 VERSION POLICY |
| 실제 게시·Live Verification·Rollback | CNT-006 PUBLISHING SYSTEM |
| 장기 등록·검토·갱신·통합·폐기·보관 | CNT-007 CONTENT LIFECYCLE |
| 신규 사실·내용·검색 변경 | CNT-001~005 해당 System |
| 예약·수집·알림·재시도 구현 | Phase 5 Automation Documents |
| 보존 기간·승인자·SLA | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Lifecycle Request | 대상 콘텐츠·현재 상태·검토 목적·범위·기한을 지정한 요청 |
| Live Baseline | Lifecycle 등록 시 실제 공개 결과와 승인 기준본을 고정한 기준 |
| Content Inventory | 콘텐츠 ID·URL·상태·Owner·기준 시점·관계를 관리하는 목록 |
| Content Owner | 검토 시작과 판정·조치 인계를 책임지는 지정 역할 |
| Review Policy | 검토 주기·Trigger·범위·증거·승인 Route를 정한 계약 |
| Review Trigger | 시간·조건·사건 변화로 검토를 시작하게 하는 신호 |
| Freshness Condition | 사실·날짜·가격·인물·정책 등 재확인이 필요한 조건 |
| Health Assessment | 접근·정확성·링크·자산·권리·중복 상태를 증거로 평가한 기록 |
| Maintenance Action | KEEP·UPDATE·CORRECT·CONSOLIDATE·DEPRECATE·UNPUBLISH·ARCHIVE 조치 |
| Canonical Content | 중복·파생 콘텐츠군에서 현재 기준으로 지정된 콘텐츠 |
| Deprecation Notice | 사용 중단 이유·대체 경로·효력 시점을 알리는 기록 |
| Retention Record | 보존 근거·기간·위치·접근권한·처분 조건의 기록 |
| Legal Hold | 통상 삭제·처분을 중지하는 권한 있는 보존 지시 |
| Lifecycle Record | 요청부터 평가·판정·조치·검증·보관까지 연결한 감사 기록 |

# 4. 입력 계약과 상태 모델

## 4.1 필수 입력

| 입력 | 필수 내용 |
|---|---|
| Lifecycle Request | lifecycle_request_id, 목적, 범위, 요청자, 기한 |
| Publication Handoff | content_id, release_id, 실제 URL, 공개 시점, Owner, 제한 |
| Live Baseline | 승인 콘텐츠 ID·버전·해시, Live Snapshot, 기준 시점 |
| Binding | Core·Content·Project 기준본 ID·버전·상태 |
| Review Policy | 주기, Trigger, 증거, 승인 Route, 예외 |
| Relationship Map | Variant, Canonical, 후속·대체 콘텐츠 관계 |
| Retention Input | 보존 근거, 기간, 위치, 접근권한, Legal Hold 여부 |

필수 입력이 없으면 추정으로 채우지 않고 `BLOCKED` 또는 `UNKNOWN`과 해소 책임을 기록한다.

## 4.2 콘텐츠 상태

| 상태 | 의미 |
|---|---|
| REGISTERED | Inventory와 Baseline 등록 완료 |
| ACTIVE | 현재 제공 중이며 다음 검토 조건이 설정됨 |
| REVIEW_DUE | 정기 또는 조건 Trigger가 도래함 |
| UNDER_REVIEW | 범위와 증거가 고정되어 검토 중 |
| UPDATE_REQUIRED | 최신성·구조·표현 갱신 필요 |
| CORRECTION_REQUIRED | 사실·의미·안전 오류의 우선 정정 필요 |
| CONSOLIDATION_REQUIRED | 중복·분산 콘텐츠의 통합 필요 |
| DEPRECATED | 신규 사용은 중지하되 안내와 대체 경로 유지 |
| UNPUBLISHED | 공개 접근이 승인 경로로 중단됨 |
| ARCHIVED | 보존 Package와 Record가 등록됨 |
| LEGAL_HOLD | 권한 있는 지시에 따라 처분이 중지됨 |
| SUPERSEDED | 승인된 후속 콘텐츠가 기준을 대체함 |

문서 관리 상태 `REVIEW`, `APPROVED`, `LOCKED`와 콘텐츠 운영 상태를 혼용하지 않는다.

# 5. 표준 Lifecycle 절차

| 단계 | 작업 | 필수 산출물 |
|---|---|---|
| 1 | Lifecycle Request 식별 | 요청 ID·범위·목적·기한 |
| 2 | LIVE 콘텐츠와 Binding 고정 | content_id·release_id·URL·Binding |
| 3 | Publication Handoff 검증 | Publication Record 참조·제한 |
| 4 | Live Baseline 생성 | 승인본 해시·Live Snapshot·기준 시점 |
| 5 | Inventory·Owner·Review Policy 등록 | Registry 항목·책임·Trigger |
| 6 | 시간·조건·사건 Trigger 확인 | Trigger Event·시각·근거 |
| 7 | 접근·정확성·링크·자산·권리 평가 | Health Assessment |
| 8 | 단일 Maintenance Verdict 결정 | 판정·영향·우선순위·승인 Route |
| 9 | 승인된 상위 절차로 조치 실행 | Change·Correction·Release 참조 |
| 10 | 실제 결과 재검증 | 접근·내용·링크·권한 결과 |
| 11 | Canonical·Variant·Redirect 정리 | Relationship Map 갱신 |
| 12 | 폐기·공개 중단·보관 조건 적용 | Notice·승인·Archive Package |
| 13 | QA와 Lifecycle Record 완결 | Gate·결함·잔여 위험 |
| 14 | 현재 상태와 다음 검토 조건 인계 | Registry·next_review·Automation 요구 |

# 6. 등록과 Live Baseline

## 6.1 Publication Handoff 검증

CNT-006의 Publication Record에서 승인 Candidate, 실제 Target, 공개 URL, 공개 시각, Live Verification, Owner, 알려진 제한과 재확인 조건을 확인한다. 요청 응답이나 계획 URL만으로 LIVE를 등록하지 않는다.

## 6.2 Live Baseline

Live Baseline에는 다음을 포함한다.

- content_id, lifecycle_request_id, release_id
- 승인 파일 ID·버전·해시
- 실제 URL·Target·언어·지역·가시성
- 기준 시점과 Live Snapshot 또는 동등한 증거
- 공개 시 Owner와 알려진 제한
- Canonical·Variant·대체 콘텐츠 관계

새 Release가 검증되면 이전 Baseline을 덮어쓰지 않고 새 Baseline과 교체 관계를 기록한다.

# 7. Inventory와 소유권

Content Inventory는 콘텐츠마다 현재 상태, 실제 위치, Owner, 마지막 검토, 다음 검토, Trigger, Canonical 관계와 Retention 참조를 가진다. 하나의 콘텐츠에 현재 상태 항목은 하나만 둔다.

Owner가 바뀌면 이전 책임 이력과 효력 시점을 보존한다. Owner 부재는 검토 면제 사유가 아니며 `BLOCKED`와 지정 책임자를 기록한다.

# 8. Review Policy와 Trigger

## 8.1 Review Policy

Review Policy는 콘텐츠 위험과 변화 가능성에 맞춰 다음을 정의한다.

- 시간 기반 검토 주기와 시간대
- 날짜·만료·재고·가격·인물·정책 등 조건 Trigger
- 오류 신고·권리 변경·보안 사건·채널 변경 등 사건 Trigger
- 검토 범위, 필수 증거, 승인자와 완료 조건
- 지연·미검증·외부 접근 불가 처리

## 8.2 Trigger 처리

Trigger가 발생하면 event_id, 발생 시각, 출처, 영향 콘텐츠와 우선순위를 기록한다. 신호 자체를 오류나 변경 확정으로 간주하지 않고 검토를 시작하는 근거로 사용한다.

기한을 넘긴 검토는 숨기지 않고 `REVIEW_DUE`와 경과 기간, 사유, Owner, 다음 조치를 표시한다.

# 9. Health와 Freshness 평가

## 9.1 평가 축

| 축 | 확인 내용 |
|---|---|
| Access | 실제 URL·가시성·상태·Redirect·권한 |
| Accuracy | 핵심 주장·수치·날짜·명칭과 최신 근거 |
| Freshness | 기준 시점·변경 가능성·만료 조건 |
| Links | 내부·외부 링크의 목적지·상태·안전성 |
| Assets | 이미지·첨부·대체 텍스트·표시·무결성 |
| Rights and Privacy | 사용 권리·귀속·개인정보·기밀의 현재 유효성 |
| Relationships | Canonical·Variant·중복·대체 관계 |
| Records | 승인·Release·변경·보관 계보의 완결성 |

## 9.2 증거 원칙

검토 시점, 출처, 접근 조건과 관찰 결과를 기록한다. 확인할 수 없는 항목은 통과로 간주하지 않고 `NOT_TESTABLE` 또는 `UNKNOWN`으로 표시한다.

# 10. Assessment와 Verdict

| Verdict | 적용 조건 | 다음 경로 |
|---|---|---|
| KEEP | 핵심 상태가 유효하고 변경 불필요 | 다음 Review 설정 |
| UPDATE | 최신성·구조·표현 개선 필요 | CNT-001~006 해당 승인 경로 |
| CORRECT | 사실·의미·안전 오류 존재 | 우선 정정 및 새 Release |
| CONSOLIDATE | 중복·분산으로 기준이 불명확 | Canonical 지정·통합 계획 |
| DEPRECATE | 신규 사용 중지, 안내·대체 필요 | Notice·대체 링크·기한 |
| UNPUBLISH | 공개 유지가 부적절하거나 승인 취소 | CNT-006 중지·복구 경로 |
| ARCHIVE | 운영 종료 후 보존 필요 | Archive Package·Retention |

한 번의 Assessment에는 현재 주된 Verdict 하나를 지정하고 부수 조치와 우선순위를 별도로 기록한다. Critical 오류·민감정보 노출·권리 철회는 `CORRECT` 또는 `UNPUBLISH`를 우선 검토한다.

# 11. 유지·갱신·정정

Lifecycle은 무엇을 바꿔야 하는지 판정하지만 승인 없이 공개 콘텐츠를 직접 변경하지 않는다. 사실·내용·SEO·디자인 변경은 해당 CNT·DSG 절차로 돌아가 검수하고 CNT-006을 통해 새 Release로 게시·검증한다.

정정은 영향 범위, 오류 노출 기간, 관련 Variant, 공지 필요성과 복구 우선순위를 기록한다. 조치 후에는 계획본이 아니라 실제 공개 결과를 다시 검증한다.

# 12. 통합과 Canonical 관리

중복 또는 분산 콘텐츠는 Canonical Content를 하나 지정하고 통합 대상, 보존 내용, Redirect·대체 링크, Variant 전파와 종료 시점을 정한다. 근거 없이 조회 수만으로 삭제하거나 서로 다른 대상·언어·법적 목적의 콘텐츠를 합치지 않는다.

Canonical 변경은 이전·새 기준, 효력 시점, 승인, 영향을 받는 링크와 Sitemap·Index 등 Project 적용 항목을 기록한다.

# 13. 폐기와 공개 중단

## 13.1 Deprecation

DEPRECATED 콘텐츠에는 가능할 때 중단 이유, 효력 시점, 현재 대체 콘텐츠와 문의 경로를 제공한다. 대체가 없으면 그 사실을 명시한다.

## 13.2 Unpublish

공개 중단은 정확한 Target, 승인자, 영향, 보존 필요성과 복구 가능성을 확인하고 CNT-006의 실행·Live Verification 경로를 따른다. 삭제 명령 성공만으로 완료하지 않으며 실제 접근과 Redirect·캐시·Variant 상태를 확인한다.

# 14. Archive, Retention과 Legal Hold

Archive Package는 최종 콘텐츠, 주요 이전 버전, Manifest, 승인·Release·Lifecycle Record, 해시, 접근권한과 Retention Record를 포함한다. 보관 위치와 공개 위치를 구분한다.

Retention Schedule은 Project 또는 권한 있는 정책이 정한 근거·기간·처분 조건을 참조한다. CNT-007은 임의의 법정 기간을 만들지 않는다.

Legal Hold가 확인되면 통상 삭제·처분보다 우선하며 적용 범위, 지시자, 시작 시각, 해제 권한을 기록한다. 공개 차단과 증거 보존은 별개로 판단한다.

# 15. Lifecycle Record와 인계

## 15.1 필수 기록

| 기록 | 필수 내용 |
|---|---|
| Request and Binding | 요청·콘텐츠·Release·Core·Project 기준 |
| Live Baseline | 승인 해시·실제 URL·Snapshot·기준 시점 |
| Inventory Record | 상태·Owner·검토일·Trigger·관계 |
| Health Assessment | 평가 축·증거·결함·미검증 항목 |
| Verdict and Approval | 단일 판정·근거·우선순위·승인 Route |
| Action References | Change·Correction·Release·Redirect·Archive 참조 |
| Verification | 조치 후 실제 결과와 시각 |
| Retention Record | 보존 근거·기간·위치·권한·Hold |
| Lifecycle QA | Gate·잔여 위험·다음 검토 조건 |

## 15.2 Automation Handoff

자동 수집·예약·알림·재시도 구현이 필요한 항목은 Trigger, 입력, 예상 상태, 실패 처리, 사람 승인 지점과 증거 요구를 명세하여 Phase 5에 인계한다. CNT-007 자체는 특정 Automation 구현을 지정하지 않는다.

# 16. Lifecycle QA Gate와 결함 처리

| Gate | 통과 조건 |
|---|---|
| G1 Request | 대상·목적·범위·기한 추적 가능 |
| G2 Baseline | 승인본·실제 URL·Snapshot·Binding 고정 |
| G3 Registry | Inventory·Owner·상태·Review Policy 등록 |
| G4 Assessment | 접근·정확성·Freshness·링크·자산·권리 평가 |
| G5 Verdict | 단일 Verdict·영향·우선순위·승인 Route 완결 |
| G6 Action | 승인된 상위 절차와 실제 조치 참조 |
| G7 Verification | 실제 결과·Canonical·Variant·접근 재검증 |
| G8 Record | Lifecycle·Retention·다음 검토·인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. Critical 결함이 열려 있으면 `HEALTHY`, `ACTIVE` 또는 완료로 축소 보고하지 않는다.

Critical 결함의 예는 민감정보의 지속 노출, 중대한 허위의 방치, 권리 철회 무시, 승인 없는 삭제, Legal Hold 대상 처분, 실제 결과 미확인, 잘못된 Canonical로의 대량 전환이다.

# 17. 실행 규칙 (VER-051 ~ VER-080)

## 17.A 등록과 Baseline (VER-051 ~ VER-055)

### VER-051 - Lifecycle 요청 식별
- **Statement:** 모든 Lifecycle 작업은 고유 lifecycle_request_id, 대상 콘텐츠, 목적, 범위와 기한을 가져야 한다.
- **Verification:** Lifecycle Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### VER-052 - LIVE Binding
- **Statement:** content_id, release_id, 실제 URL과 적용 Core·Content·Project 기준본을 고정해야 한다.
- **Verification:** Binding과 Publication Record를 대조한다.
- **Exceptions:** 없음.

### VER-053 - Live Baseline 단일성
- **Statement:** 현재 LIVE 기준은 승인본 ID·버전·해시와 실제 Snapshot으로 하나만 지정해야 한다.
- **Verification:** Inventory의 현재 Baseline과 실제 공개 결과를 확인한다.
- **Exceptions:** 언어·지역·채널 Variant는 각각의 Baseline과 관계를 가진다.

### VER-054 - Publication Handoff 검증
- **Statement:** CNT-006의 Live Verification, Owner, 제한, 재확인·만료 조건을 확인해야 한다.
- **Verification:** Publication Record와 Handoff 필드를 검사한다.
- **Exceptions:** 즉시 중단된 Release는 중단 상태와 기록 위치를 등록한다.

### VER-055 - Inventory 등록
- **Statement:** LIVE 콘텐츠는 현재 상태·URL·Owner·기준 시점·관계와 함께 Inventory에 등록해야 한다.
- **Verification:** Content Inventory 필수 필드를 검사한다.
- **Exceptions:** 없음.

## 17.B 소유권과 Review Trigger (VER-056 ~ VER-060)

### VER-056 - Owner 지정
- **Statement:** 각 콘텐츠는 Lifecycle 검토와 인계를 책임지는 Owner를 가져야 한다.
- **Verification:** 현재 Owner와 효력 시점을 확인한다.
- **Exceptions:** Owner 미정은 BLOCKED와 지정 책임자를 기록한다.

### VER-057 - Review Policy 등록
- **Statement:** 주기·Trigger·검토 범위·증거·승인 Route를 Review Policy로 정해야 한다.
- **Verification:** 콘텐츠 위험과 Policy 항목을 대조한다.
- **Exceptions:** 일회성 콘텐츠도 만료·폐기 조건을 가져야 한다.

### VER-058 - 시간·조건 Trigger
- **Statement:** 검토 시점과 만료·날짜·가격·정책 등 조건 Trigger를 명시해야 한다.
- **Verification:** next_review_at과 조건 목록을 확인한다.
- **Exceptions:** 변화가 드문 콘텐츠는 근거 있는 장기 주기를 사용할 수 있다.

### VER-059 - 사건 Trigger
- **Statement:** 오류 신고·권리 변경·보안 사건·채널 변경은 정기 주기와 별개로 검토를 시작해야 한다.
- **Verification:** event_id, 출처, 영향 콘텐츠와 처리 상태를 검사한다.
- **Exceptions:** 중복 신호는 연결하되 최초 사건을 보존한다.

### VER-060 - 지연 투명성
- **Statement:** 기한을 넘긴 검토와 미확인 항목을 ACTIVE 또는 PASS로 숨기지 않아야 한다.
- **Verification:** REVIEW_DUE, 경과 기간, 사유와 다음 조치를 확인한다.
- **Exceptions:** 없음.

## 17.C Health와 Assessment (VER-061 ~ VER-065)

### VER-061 - 실제 접근 확인
- **Statement:** 현재 상태는 요청 응답이 아니라 실제 URL·가시성·Redirect·권한으로 확인해야 한다.
- **Verification:** 적절한 접근 관점의 관찰 결과를 검사한다.
- **Exceptions:** 외부 장애는 UNKNOWN과 재확인 조건을 기록한다.

### VER-062 - 사실과 Freshness
- **Statement:** 핵심 주장·수치·날짜·명칭을 현재 근거와 기준 시점으로 재확인해야 한다.
- **Verification:** Claim·Source·as_of와 공개 내용을 대조한다.
- **Exceptions:** 검증 불가는 NOT_TESTABLE과 영향도를 기록한다.

### VER-063 - 링크와 자산 Health
- **Statement:** 내부·외부 링크와 이미지·첨부·대체 텍스트의 접근·표시·무결성을 확인해야 한다.
- **Verification:** Link·Asset 결과와 Live Snapshot을 검사한다.
- **Exceptions:** 일시적 오류는 재검사 시점과 임시 조치를 기록한다.

### VER-064 - 권리·개인정보 유효성
- **Statement:** 공개 권리·귀속·개인정보·기밀 조건이 현재도 유효한지 확인해야 한다.
- **Verification:** Rights·Privacy Record와 현재 Package를 대조한다.
- **Exceptions:** 불명확하면 공개 유지 위험과 승인 Route를 기록한다.

### VER-065 - 단일 Verdict
- **Statement:** Assessment는 KEEP·UPDATE·CORRECT·CONSOLIDATE·DEPRECATE·UNPUBLISH·ARCHIVE 중 주된 Verdict 하나를 가져야 한다.
- **Verification:** 증거, 영향도, 우선순위와 Verdict를 대조한다.
- **Exceptions:** 부수 조치는 별도 목록으로 기록한다.

## 17.D 유지보수와 통합 (VER-066 ~ VER-070)

### VER-066 - 승인된 상위 경로
- **Statement:** 사실·내용·SEO·디자인·게시 변경은 해당 CNT·DSG·CNT-006 승인 경로를 통해 수행해야 한다.
- **Verification:** Change, QA, Approval과 Release 참조를 확인한다.
- **Exceptions:** 없음.

### VER-067 - Correction 우선
- **Statement:** 중대한 사실·안전 오류는 일반 갱신보다 우선하여 영향과 노출 기간을 기록하고 정정해야 한다.
- **Verification:** 결함 등급, 조치 시각, 승인과 실제 결과를 검사한다.
- **Exceptions:** 공개 차단이 먼저 필요한 경우 차단과 정정을 분리 기록한다.

### VER-068 - Canonical과 통합
- **Statement:** 통합 시 Canonical 하나, 통합 대상, 보존 내용, 대체·Redirect와 효력 시점을 정해야 한다.
- **Verification:** Relationship Map과 실제 링크·접근 결과를 확인한다.
- **Exceptions:** 독립 목적의 Variant는 통합하지 않고 관계만 기록한다.

### VER-069 - Variant 전파
- **Statement:** 변경 영향이 있는 언어·지역·채널 Variant를 식별하고 적용 또는 제외 근거를 기록해야 한다.
- **Verification:** Variant Map과 Release 결과를 대조한다.
- **Exceptions:** 범위 밖 Variant는 Owner와 후속 기한을 지정한다.

### VER-070 - 조치 후 검증
- **Statement:** 유지보수 완료는 실제 URL의 내용·가시성·링크·자산·관계 재검증을 요구한다.
- **Verification:** 새 Live Verification과 승인 Baseline을 대조한다.
- **Exceptions:** 전파 지연은 VERIFYING 또는 UNKNOWN으로 남긴다.

## 17.E 폐기·보관·Retention (VER-071 ~ VER-075)

### VER-071 - Deprecation 안내
- **Statement:** DEPRECATED 콘텐츠는 가능한 경우 중단 이유·효력 시점·대체 콘텐츠를 알려야 한다.
- **Verification:** Notice와 실제 표시·대체 링크를 확인한다.
- **Exceptions:** 안전·법적 사유로 안내할 수 없으면 승인 근거를 기록한다.

### VER-072 - Unpublish 승인
- **Statement:** 공개 중단은 정확한 Target·영향·보존 필요성과 권한 있는 승인을 가져야 한다.
- **Verification:** Approval, CNT-006 Attempt와 실제 접근 결과를 검사한다.
- **Exceptions:** 긴급 차단은 지정 Route와 사후 승인을 요구한다.

### VER-073 - Archive 완결성
- **Statement:** Archive Package는 최종본·주요 버전·Manifest·승인·Release·Lifecycle Record·해시를 포함해야 한다.
- **Verification:** Package 목록과 실제 보관 파일을 대조한다.
- **Exceptions:** 제외 항목은 사유와 대체 위치를 기록한다.

### VER-074 - Retention Schedule
- **Statement:** 보존 기간·근거·위치·접근권한·처분 조건을 권한 있는 정책에서 참조해야 한다.
- **Verification:** Retention Record와 Project 정책을 확인한다.
- **Exceptions:** 기간 미정은 임의 삭제하지 않고 Owner와 결정 기한을 기록한다.

### VER-075 - Legal Hold 우선
- **Statement:** Legal Hold 대상은 해제 권한의 확인 전 통상 삭제·처분하지 않아야 한다.
- **Verification:** Hold 범위·지시자·시작·상태와 Archive를 검사한다.
- **Exceptions:** 공개 차단은 증거 보존을 유지하며 별도 승인할 수 있다.

## 17.F QA·기록·인계 (VER-076 ~ VER-080)

### VER-076 - Lifecycle Gate
- **Statement:** G1~G8 필수 Gate가 PASS일 때만 해당 Lifecycle 조치를 완료로 표시해야 한다.
- **Verification:** Gate Evidence와 최종 상태를 대조한다.
- **Exceptions:** NOT_APPLICABLE은 승인 근거가 있어야 한다.

### VER-077 - Lifecycle Record 완결성
- **Statement:** Request·Baseline·Inventory·Assessment·Verdict·Approval·Action·Verification·Retention을 연결해야 한다.
- **Verification:** 필수 기록과 참조 무결성을 검사한다.
- **Exceptions:** 범위 밖 항목은 제외 사유와 Owner를 기록한다.

### VER-078 - 현재 상태 Registry
- **Statement:** Content Inventory는 콘텐츠별 현재 상태 하나와 전체 상태 이력을 제공해야 한다.
- **Verification:** 중복 현재 상태, 전이 시각과 이전 상태 보존을 검사한다.
- **Exceptions:** 동시 Variant는 각각 상태를 갖고 상위 관계를 기록한다.

### VER-079 - Automation 인계 분리
- **Statement:** 자동화 요구는 Trigger·입력·상태·실패·사람 승인·증거 계약으로 인계하고 구현과 분리해야 한다.
- **Verification:** Phase 5 Handoff와 CNT-007 책임 경계를 확인한다.
- **Exceptions:** 수동 운영은 동일한 기록 계약을 따른다.

### VER-080 - Lifecycle 계보 보존
- **Statement:** 최초 Candidate부터 Live Baseline, 변경 Release, 폐기와 Archive까지 ID·버전·해시·승인·시각 계보를 재현할 수 있어야 한다.
- **Verification:** Lifecycle Record의 참조 연결과 변경 이력을 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Content Lifecycle

```text
1. lifecycle_request_id, content_id, release_id, 실제 URL과 적용 기준본을 고정한다.
2. CNT-006 Publication Record와 Live Verification, Owner, 제한, 재확인 조건을 검증한다.
3. 승인본 해시·Live Snapshot·기준 시점을 Live Baseline으로 보존한다.
4. Inventory에 현재 상태·Owner·Review Policy·Trigger·Canonical·Variant 관계를 등록한다.
5. 시간·조건·사건 Trigger를 추적하고 지연·미확인을 숨기지 않는다.
6. 실제 접근, 사실·Freshness, 링크·자산, 권리·개인정보, 관계와 기록을 평가한다.
7. KEEP·UPDATE·CORRECT·CONSOLIDATE·DEPRECATE·UNPUBLISH·ARCHIVE 중 주된 Verdict 하나를 정한다.
8. 변경은 해당 CNT·DSG 승인 경로와 CNT-006 새 Release를 통해 수행한다.
9. 조치 후 실제 URL의 내용·가시성·링크·자산·Canonical·Variant를 재검증한다.
10. 폐기에는 안내·대체·승인이 필요하며 Archive와 공개 위치를 구분한다.
11. Retention 정책과 Legal Hold를 우선 적용하고 임의 보존 기간이나 삭제를 만들지 않는다.
12. Lifecycle Record, 현재 상태, 다음 검토 조건과 Automation 요구를 인계한다.
```

이 압축 블록은 상세 System의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-007은 LIVE 콘텐츠의 등록·검토·판정·유지보수 인계·폐기·보관과 기록 계약만 정의한다.
- 새 조사·사실·내용·SEO·디자인 변경은 CNT-001~005와 DSG 절차로 반환한다.
- 실제 게시·공개 중단·Rollback은 CNT-006을 따른다.
- 버전·승인·잠금·Archive 공통 정책은 COR-007을 따른다.
- 스케줄·수집·알림·재시도·상태 동기화 구현은 Phase 5가 맡는다.

## 19.2 알려진 제한

- 모든 콘텐츠에 같은 검토 주기·보존 기간·폐기 방식을 강제하지 않는다.
- 외부 플랫폼의 장애·정책·색인·캐시·Redirect 전파 또는 분석 정확성을 보장하지 않는다.
- 트래픽 감소만으로 부정확성이나 폐기 필요를 확정하지 않는다.
- 법정 보존·삭제·개인정보 권리·증거 보존의 전문 판단을 대체하지 않는다.
- Project 고유 SLA·Owner·승인자·Risk Threshold·Retention은 해당 Project 문서가 구체화한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 Lifecycle 등록·Baseline·Inventory·Owner·Review Trigger·Health·Verdict·Update·Correction·Consolidation·Deprecation·Unpublish·Archive·Retention·Legal Hold와 VER-051~080 작성; 사용자 명시적 승인 반영 |
