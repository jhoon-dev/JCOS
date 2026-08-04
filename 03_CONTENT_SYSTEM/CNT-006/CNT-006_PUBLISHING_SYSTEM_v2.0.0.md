# JCOS v2.0.0 - CNT-006 PUBLISHING SYSTEM

## 범용 채널 패키징·승인·게시·검증·실패 대응 절차

| Field | Value |
|---|---|
| Document ID | CNT-006 |
| Title | PUBLISHING SYSTEM |
| Korean Title | 범용 채널 패키징·승인·게시·검증·실패 대응 절차 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CONTENT SYSTEM |
| Applies To | SEO Candidate와 승인된 채널 Variant의 공개·제한 공개·배포 실행 |
| Priority | CRITICAL |
| Created | 2026-08-03 |
| Last Updated | 2026-08-03 |
| Inherits | JCOS Foundation v2.0, COR-001~008 v2.0.0 LOCKED, DSG-001~007 v2.0.0 LOCKED, CNT-001~005 v2.0.0 LOCKED |
| Extends | COR-006 FILE DELIVERY FILE-001~050 |
| Depends On | COR-005 QUALITY GATE, COR-006 FILE DELIVERY, COR-007 VERSION POLICY, CNT-005 SEO SYSTEM |

> 상태 알림: 이 문서는 사용자 승인과 2026-08-03 명시적 잠금 승인에 따라 LOCKED로 전환된 CNT-006 기준본이다. 변경은 COR-007 VERSION POLICY와 승인 절차를 따른다.

# 1. 문서 목적

CNT-006은 CNT-005가 인계한 SEO Candidate를 정확한 채널·대상·시점·권한으로 게시하고 실제 공개 결과를 검증하는 표준 절차를 정의한다. 결과는 게시 전 기준본, 승인, 실행, 공개 상태와 실패 대응을 재현할 수 있는 Publication Record여야 한다.

게시 명령이 성공했다는 응답만으로 완료하지 않는다. 승인된 콘텐츠가 의도한 대상에게 실제로 접근 가능하고, 표시·링크·자산·권한이 올바르며, 실패와 잔여 위험이 기록됐을 때 게시 실행이 완료된다.

# 2. 범위와 비범위

## 2.1 포함 범위

- Publishing Request와 SEO Candidate Binding
- Release Baseline과 Channel Release Brief 생성
- 채널별 본문·필드·자산·링크 패키징
- 권리·개인정보·기밀·엠바고·공개 범위 확인
- 접근성·Preview·호환성·링크·표시 검사
- 승인자·역할 분리·게시 창·예약 조건 확인
- 수동 또는 승인된 실행 경로의 게시
- 실제 URL·상태·시간·가시성·표시 결과 검증
- 실패·부분 게시·Rollback·Correction 인계
- Publication Record와 Lifecycle Handoff

## 2.2 비범위

- 새 조사·작성·Fact Verdict·SEO 의미의 임의 변경
- 채널 계정 생성·계약·결제·광고 집행
- 서비스별 API·UI·Credential·Webhook 구현
- 무인 예약 실행·재시도·모니터링 Automation 구축
- 장기 성과 분석·갱신 주기·통합·폐기 결정
- 법률·보안·개인정보 전문 승인 대체

## 2.3 책임 경계

| 판단 | 책임 문서 |
|---|---|
| 품질 Gate와 결함 등급 | COR-005 QUALITY GATE |
| 파일·패키지·전달·무결성 | COR-006 FILE DELIVERY |
| 버전·승인·잠금·Rollback 기준 | COR-007 VERSION POLICY |
| 검색 필드·Topic·내부 탐색 | CNT-005 SEO SYSTEM |
| 채널 패키징·승인·게시·공개 검증 | CNT-006 PUBLISHING SYSTEM |
| 장기 성과·갱신·통합·폐기 | CNT-007 LIFECYCLE SYSTEM |
| 예약·재시도·모니터링 구현 | Phase 5 Automation Documents |
| 프로젝트 고유 계정·채널·승인자·SLA | 해당 Project Schema·Rules·MASTER |

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Publishing Request | 대상 콘텐츠·채널·대상·일정·공개 범위·승인자를 지정한 요청 |
| Release Baseline | 게시 준비 시작 시 버전과 해시를 고정한 SEO Candidate |
| Channel Release Brief | 채널·대상·필드·자산·일정·권한·완료 조건의 계약 |
| Release Package | 채널에 게시할 본문·필드·자산·링크·설정·매니페스트 묶음 |
| Publication Target | 게시가 적용될 정확한 계정·사이트·공간·경로·언어·지역 |
| Release Window | 게시 가능한 시작·종료 시점과 시간대 |
| Embargo | 지정 시점 전 공개·전달을 금지하는 조건 |
| Release Approval | 지정 승인자가 정확한 Baseline·Package·Target·Window를 승인한 기록 |
| Publication Attempt | 하나의 실행 ID로 식별되는 게시 시도 |
| Live Verification | 실제 공개 결과의 URL·상태·표시·자산·링크·권한 확인 |
| Rollback | 잘못된 공개를 중지·숨김·복구하거나 이전 안전 상태로 되돌리는 조치 |
| Publication Record | 요청·Baseline·승인·시도·결과·검증·실패·조치를 묶은 기록 |

# 4. 입력 계약과 게시 상태

## 4.1 필수 입력

| 입력 | 최소 내용 |
|---|---|
| publishing_request_id | 게시 실행 고유 식별자 |
| target_content_ref | SEO Candidate 위치·버전·해시 |
| seo_handoff_ref | CNT-005 Publishing Handoff 위치 |
| publication_targets | 계정·사이트·공간·경로·언어·지역 |
| audience_and_visibility | 대상 독자와 PUBLIC·RESTRICTED·PRIVATE 범위 |
| release_window | 날짜·시간·시간대·마감 |
| channel_contracts | 필드·형식·자산·링크·접근성 제약 |
| approval_route | 작성·검수·승인·실행 책임자 |
| rollback_route | 중지·복구·정정 책임자와 연락 경로 |
| binding | 적용 기준본 ID·버전·상태 |

대상 Candidate·Target·가시성·일정·승인자가 하나로 식별되지 않으면 추정으로 게시하지 않는다. 공개 범위를 바꿀 수 있는 누락은 `BLOCKED`로 처리한다.

## 4.2 게시 상태

| 상태 | 의미 |
|---|---|
| READY | 요청·Binding·Baseline 확인 완료 |
| PACKAGING | 채널 Release Package 준비 중 |
| APPROVAL_REVIEW | Package·Target·Window 승인 대기 |
| SCHEDULED | 승인 후 게시 창 또는 예약 대기 |
| PUBLISHING | 승인된 실행 경로로 게시 중 |
| VERIFYING | 실제 공개 결과 검증 중 |
| LIVE | 필수 Live Verification 통과 |
| PARTIAL | 일부 Target·필드·자산만 성공 |
| ROLLBACK | 공개 중지·복구·정정 조치 중 |
| BLOCKED | 필수 입력·권한·승인·안전 조건 부재 |
| SUPERSEDED | 새 Release 또는 정정본으로 대체됨 |

# 5. 표준 Publishing 수명주기

1. Publishing Request를 등록하고 대상 SEO Candidate를 식별한다.
2. 적용 기준본·Target·가시성·채널 계약을 Binding한다.
3. CNT-005 Handoff와 SEO QA를 확인한다.
4. Candidate 버전·해시를 Release Baseline으로 고정한다.
5. Target별 Channel Release Brief와 Package를 만든다.
6. 권리·개인정보·기밀·엠바고·접근성 조건을 확인한다.
7. 본문·필드·자산·링크·표시를 Preview에서 검사한다.
8. Release Package·Target·Window·Rollback Route를 승인받는다.
9. 게시 창과 시간대, 중복 실행 방지 조건을 확인한다.
10. 승인된 실행 경로로 Publication Attempt를 시작한다.
11. 응답·생성 ID·URL·시간·오류를 Attempt Record에 남긴다.
12. 실제 공개 결과를 대상 환경에서 Live Verification한다.
13. 실패·부분 게시를 중지·복구·정정하고 상태를 기록한다.
14. Publication Record와 Lifecycle Handoff를 CNT-007에 전달한다.

승인 후 Baseline·Target·가시성·Window가 바뀌면 기존 승인을 재사용하지 않는다. 새 Package와 영향 범위를 검수하고 다시 승인받는다.

# 6. Preflight와 Release Baseline

## 6.1 SEO Candidate 확인

CNT-005가 `PUBLISHING_READY`로 인계한 하나의 SEO Candidate를 확인한다. Content ID·버전·해시·언어·Variant와 게시 전 재확인 조건을 기록한다.

## 6.2 인계물 확인

- SEO Request와 적용 Binding
- Baseline Content와 SEO Candidate
- Search Brief와 SEO Field Set
- Link Map과 Change·Query Log
- SEO QA와 재확인 조건
- 채널별 Variant·자산·접근성 정보

## 6.3 Release Snapshot

게시 준비 전 Candidate와 필드를 덮어쓰지 않고 보존한다. Release Package와 공개 결과는 이 Baseline을 기준으로 비교할 수 있어야 한다.

# 7. Channel Release Brief와 Target

## 7.1 Release Brief

| 필드 | 내용 |
|---|---|
| target_id | 게시 Target 고유 ID |
| channel_and_account | 채널·사이트·계정·공간 |
| audience | 대상 독자·지역·언어 |
| visibility | PUBLIC·RESTRICTED·PRIVATE |
| content_variant | 게시할 Canonical 또는 Variant |
| release_window | 시작·종료·시간대 |
| owner_roles | 작성·검수·승인·실행·Rollback 책임자 |
| completion_criteria | LIVE 판정 조건 |

## 7.2 Target 단일성

표시 이름만으로 계정이나 공간을 선택하지 않는다. 내부 ID·경로·도메인·조직과 환경을 확인해 시험·운영·개인 계정을 구분한다.

## 7.3 공개 범위

PUBLIC·RESTRICTED·PRIVATE를 명시하고 실제 권한 설정과 대조한다. 제한 공개 콘텐츠를 링크 비공개만으로 보호된 것으로 간주하지 않는다.

# 8. Release Package와 Manifest

## 8.1 Package 구성

- 채널별 본문과 제목·설명·Category·Tag
- URL 또는 경로 제안과 Canonical 관계
- 이미지·썸네일·첨부·대체 텍스트
- 내부·외부 링크와 Anchor
- 공개 범위·일정·엠바고·지역·언어 설정
- 버전·해시·필수 파일·의존성을 적은 Manifest

## 8.2 Candidate 일치

Package의 본문·필드·자산이 승인된 SEO Candidate와 일치하는지 해시 또는 구조 비교로 확인한다. 채널 UI에 붙여넣는 과정의 자동 변환·잘림·문자 치환도 변경으로 검사한다.

## 8.3 Variant 분리

Target별 Variant를 물리적·논리적으로 구분한다. 다른 계정·언어·지역의 파일이나 필드를 혼합하지 않고 Package ID와 Target ID를 연결한다.

# 9. 권리·개인정보·기밀·엠바고

## 9.1 권리와 라이선스

본문·이미지·폰트·인용·데이터의 공개·배포 권리와 필요한 귀속을 확인한다. 권리 상태가 불명확한 자산은 임의로 공개하지 않는다.

## 9.2 개인정보와 기밀

공개 불필요한 개인정보, Credential, 내부 URL, Prompt, 댓글, 추적 변경, 문서 메타데이터와 미승인 대안을 제거한다. 제한 공개에도 최소 권한을 적용한다.

## 9.3 Embargo

엠바고 시점과 시간대, 사전 공유 허용 대상, 해제 승인자를 기록한다. 예약 기능이 있다는 이유로 게시 전 노출 가능성을 무시하지 않는다.

# 10. Preview·접근성·호환성

## 10.1 Preview

가능하면 실제 Target과 같은 렌더링 경로에서 Desktop·Mobile 또는 계약된 환경을 확인한다. 제목 잘림, 줄바꿈, 표·이미지 이탈, 문자 깨짐과 빈 필드를 검사한다.

## 10.2 접근성

제목 계층, 대체 텍스트, 링크 설명, 표 구조, 자막·대본과 키보드 접근 등 적용 가능한 접근성 정보를 유지한다. 채널 제약으로 손실되면 대체 수단과 제한을 기록한다.

## 10.3 링크와 자산

모든 공개 링크의 목적지·상태·권한·지역·언어와 자산 로딩을 확인한다. Preview 성공만으로 게시 후 URL이 동일하게 작동한다고 가정하지 않는다.

# 11. 승인·역할 분리·일정

## 11.1 Release Approval

승인 기록은 Baseline ID·버전·해시, Package ID, Target, 가시성, Window, 알려진 제한과 Rollback Route를 포함한다. 모호한 “게시해도 됨”을 다른 Package에 재사용하지 않는다.

## 11.2 역할 분리

고위험 공개는 작성·검수·승인·실행 중 적용 가능한 역할을 분리한다. 동일 인물이 여러 역할을 맡으면 Project 정책의 허용 근거와 추가 검사를 기록한다.

## 11.3 게시 창

Release Window의 시간대, 선행 조건, 금지 시간, 의존 게시물과 담당자 가용성을 확인한다. 창이 지나면 새 확인 없이 게시하지 않는다.

# 12. Publication Attempt

## 12.1 실행 전 최종 확인

실행 직전에 Target·계정·환경·Package·가시성·Window·승인 상태를 다시 확인한다. 화면이나 세션이 바뀌었으면 이전 확인을 재사용하지 않는다.

## 12.2 실행 기록

| 필드 | 내용 |
|---|---|
| attempt_id | 게시 시도 고유 ID |
| package_id | 실행한 Release Package |
| target_id | 정확한 Publication Target |
| actor | 실행 주체와 권한 |
| started_at | 시작 시각·시간대 |
| result | SUCCESS·PARTIAL·FAILED·UNKNOWN |
| remote_ref | 생성 ID·URL·응답 참조 |
| error | 오류 코드·메시지·영향 범위 |

## 12.3 중복 실행 방지

재시도 전에 이전 Attempt의 원격 상태를 확인한다. 응답 손실이나 Timeout을 실패로 단정해 같은 콘텐츠를 중복 게시하지 않는다.

# 13. Live Verification

## 13.1 실제 접근

게시 요청 응답이 아니라 실제 공개 URL·Target에서 권한이 다른 적절한 관점으로 접근한다. 존재, 가시성, 상태 코드 또는 채널 상태와 기준 시각을 기록한다.

## 13.2 내용·표시 검증

제목·본문·설명·태그·이미지·첨부·대체 텍스트·링크·날짜·작성자·언어·지역을 Release Package와 대조한다. 자동 변환·잘림·순서 변경을 포함한다.

## 13.3 전파 지연

채널 전파가 지연되면 `UNKNOWN` 또는 `VERIFYING`으로 유지하고 확인 시점·재확인 조건을 기록한다. 아직 확인되지 않은 결과를 LIVE로 표시하지 않는다.

# 14. 실패·부분 게시·Rollback

## 14.1 실패와 PARTIAL

Target별 성공·실패·미확인을 분리한다. 일부 성공을 전체 성공으로 보고하지 않으며 영향받는 공개 URL과 독자를 기록한다.

## 14.2 Rollback

허위·민감정보 노출·잘못된 Target·중대한 표시 오류는 승인된 Route에 따라 중지·숨김·복구한다. 삭제가 증거와 법적 보존 의무를 훼손하면 보존 정책을 우선한다.

## 14.3 Correction 인계

사실·의미 오류는 CNT-003~005 책임 경로로 반환하고 승인된 정정본을 새 Release로 처리한다. 공개 정정 공지의 형식과 위치는 Project 정책과 승인자가 결정한다.

# 15. Publication Record와 Lifecycle Handoff

## 15.1 필수 기록

| 기록 | 최소 내용 |
|---|---|
| Publishing Request | 대상·Target·가시성·Window |
| Binding | 적용 기준본 ID·버전·상태 |
| Release Baseline | 게시 전 Candidate·버전·해시 |
| Release Package | 본문·필드·자산·Manifest·해시 |
| Approval Record | 승인 Package·Target·Window·제한 |
| Attempt Records | 실행 ID·주체·시각·응답·오류 |
| Live Verification | URL·가시성·표시·링크·자산 결과 |
| Incident and Rollback Log | 실패·영향·조치·잔여 위험 |
| Publication QA | Gate 판정·제한·재확인 조건 |

## 15.2 Lifecycle Handoff

LIVE 콘텐츠의 Content ID, 실제 URL, 공개 시점, Owner, 기준 시점, 재확인·만료 조건, 알려진 제한과 관련 Publication Record를 CNT-007에 인계한다.

`LIVE`는 장기 정확성, 검색 성과, 자동 모니터링, 향후 접근 가능성 또는 Lifecycle 완료를 의미하지 않는다.

# 16. Publishing QA Gate와 결함 처리

## 16.1 Gate

| Gate | 통과 조건 |
|---|---|
| G1 Request | Candidate·Target·가시성·Window·Owner 추적 가능 |
| G2 Baseline | SEO Candidate·버전·해시 고정 |
| G3 Package | 본문·필드·자산·링크·Manifest 정합 |
| G4 Safety | 권리·개인정보·기밀·엠바고·권한 확인 |
| G5 Preview | 표시·접근성·호환성·링크 검사 완료 |
| G6 Approval | Package·Target·Window·Rollback 승인 완결 |
| G7 Live | 실제 URL·가시성·내용·자산·링크 검증 |
| G8 Record | Attempt·실패·조치·QA·Lifecycle 인계 완결 |

각 Gate는 `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` 또는 `NOT_TESTABLE`과 증거를 가진다. 게시 전 G7은 `NOT_TESTABLE`일 수 있으나 LIVE 판정에서는 반드시 PASS여야 한다.

## 16.2 Critical 결함

- 승인되지 않은 Candidate·Package·Target·가시성·Window로 게시함
- 개인정보·Credential·기밀·엠바고 콘텐츠가 잘못 공개됨
- 권리가 확인되지 않은 핵심 자산을 공개함
- 실제 공개 결과가 승인본과 의미·사실·언어·지역에서 다름
- 잘못된 계정·사이트·환경에 게시함
- 실패·부분 게시를 LIVE 또는 전체 성공으로 보고함

Critical 결함이 열려 있으면 `LIVE`로 표시하지 않는다.

# 17. 실행 규칙 (FILE-051 ~ FILE-080)

## 17.A 요청과 Baseline (FILE-051 ~ FILE-055)

### FILE-051 - 게시 요청 식별
- **Statement:** 모든 게시 실행은 고유 publishing_request_id, Candidate, Target, 가시성과 Window를 가져야 한다.
- **Verification:** Publishing Request 필수 필드를 확인한다.
- **Exceptions:** 없음.

### FILE-052 - 기준본 Binding
- **Statement:** 게시 준비 전에 적용할 Core·Content·Project 기준본의 ID·버전·상태를 고정해야 한다.
- **Verification:** Binding과 실제 기준 파일을 대조한다.
- **Exceptions:** 없음.

### FILE-053 - Release Baseline 단일성
- **Statement:** 하나의 SEO Candidate를 ID·버전·해시로 Release Baseline에 고정해야 한다.
- **Verification:** target_content_ref와 실제 파일 해시를 확인한다.
- **Exceptions:** 병렬 언어본은 각 Baseline과 관계를 명시한다.

### FILE-054 - SEO Handoff
- **Statement:** CNT-005 Handoff의 Candidate·Field Set·Link Map·Change·QA를 확인해야 한다.
- **Verification:** seo_handoff_ref와 manifest를 검사한다.
- **Exceptions:** 없음.

### FILE-055 - Target 정확성
- **Statement:** 게시 Target은 계정·사이트·공간·경로·환경·언어·지역으로 정확히 식별해야 한다.
- **Verification:** target_id와 실제 채널 식별자를 대조한다.
- **Exceptions:** 없음.

## 17.B Package와 채널 (FILE-056 ~ FILE-060)

### FILE-056 - Channel Contract
- **Statement:** Release Package는 Target의 필드·형식·자산·링크·접근성 계약을 따라야 한다.
- **Verification:** Package와 channel_contract를 대조한다.
- **Exceptions:** 지원되지 않는 필드는 승인된 대체 방식과 제한을 기록한다.

### FILE-057 - Package Manifest
- **Statement:** 각 Release Package는 본문·필드·자산·의존성·버전·해시를 적은 Manifest를 가져야 한다.
- **Verification:** Manifest와 실제 Package 항목을 대조한다.
- **Exceptions:** 단일 필드 게시도 Candidate·Target·버전 참조는 유지한다.

### FILE-058 - Candidate 내용 일치
- **Statement:** Package의 본문과 검색 필드는 승인된 SEO Candidate와 의미·값이 일치해야 한다.
- **Verification:** 구조 비교·해시·Field Diff를 검사한다.
- **Exceptions:** 채널 축약은 승인된 Variant와 Change Record를 가져야 한다.

### FILE-059 - 자산과 링크 결속
- **Statement:** 이미지·첨부·대체 텍스트·링크는 정확한 Package와 Target에 결속돼야 한다.
- **Verification:** Asset·Link Map과 Preview를 대조한다.
- **Exceptions:** 채널이 자산을 재인코딩하면 원본과 원격 식별자를 함께 기록한다.

### FILE-060 - Variant 분리
- **Statement:** 서로 다른 계정·언어·지역·채널 Variant를 한 Package에서 혼합하지 않아야 한다.
- **Verification:** Package ID·Target ID·Variant Map을 검사한다.
- **Exceptions:** 다중 Target Package는 Target별 파일·필드·결과를 분리 기록한다.

## 17.C 안전·권한·Preview (FILE-061 ~ FILE-065)

### FILE-061 - 공개 권리 확인
- **Statement:** 본문·이미지·폰트·인용·데이터의 공개·배포 권리와 귀속을 확인해야 한다.
- **Verification:** Rights Record와 Package 자산을 대조한다.
- **Exceptions:** 권리 불명확 자산은 공개 Package에서 제외한다.

### FILE-062 - 보호정보 제거
- **Statement:** 공개 Package에 불필요한 개인정보·Credential·기밀·내부 메모·숨은 데이터가 없어야 한다.
- **Verification:** 본문·첨부·메타데이터·권한을 검사한다.
- **Exceptions:** 승인된 제한 공개 정보는 최소 권한과 목적을 기록한다.

### FILE-063 - 가시성 최소화
- **Statement:** Publication Target의 실제 권한은 승인된 audience_and_visibility보다 넓지 않아야 한다.
- **Verification:** 익명·일반 사용자·승인 사용자 관점의 접근을 확인한다.
- **Exceptions:** PUBLIC은 공개 승인 기록을 요구한다.

### FILE-064 - Embargo 준수
- **Statement:** Embargo 콘텐츠는 지정 시점과 승인 전 공개·색인·외부 공유되지 않아야 한다.
- **Verification:** 예약·Preview·권한·시간대와 해제 기록을 검사한다.
- **Exceptions:** 승인된 사전 검토자는 명단과 범위를 기록한다.

### FILE-065 - Preview 완결성
- **Statement:** 게시 전 Preview에서 표시·접근성·링크·자산·언어·지역을 검사해야 한다.
- **Verification:** Preview QA와 Release Package를 대조한다.
- **Exceptions:** Preview가 없는 채널은 제한을 기록하고 게시 후 즉시 검증한다.

## 17.D 승인·일정·실행 (FILE-066 ~ FILE-070)

### FILE-066 - Release Approval 결속
- **Statement:** 승인은 Baseline·Package·Target·가시성·Window·제한에 결속돼야 한다.
- **Verification:** Approval Record와 실행 입력을 대조한다.
- **Exceptions:** 없음.

### FILE-067 - 변경 시 재승인
- **Statement:** 승인 후 의미·Package·Target·가시성·Window가 바뀌면 영향 검수와 재승인을 받아야 한다.
- **Verification:** Approval 시점 이후 diff와 decision_ref를 검사한다.
- **Exceptions:** 의미 없는 실행 시각의 허용 범위는 사전 승인 계약을 따른다.

### FILE-068 - 게시 창 확인
- **Statement:** 실행 직전에 Release Window·시간대·선행 조건·담당자 가용성을 확인해야 한다.
- **Verification:** 현재 시각과 Window·승인·Dependency를 대조한다.
- **Exceptions:** 긴급 게시도 별도 승인 Route와 사후 기록을 요구한다.

### FILE-069 - Attempt 고유성
- **Statement:** 각 게시 시도는 고유 attempt_id와 actor·Package·Target·시작 시각을 가져야 한다.
- **Verification:** Attempt Record 필수 필드를 확인한다.
- **Exceptions:** 없음.

### FILE-070 - 중복 실행 방지
- **Statement:** 재시도 전에 이전 Attempt의 원격 상태를 확인해 중복 게시를 방지해야 한다.
- **Verification:** remote_ref·Target 검색·Attempt 상태를 검사한다.
- **Exceptions:** 없음.

## 17.E Live 검증과 실패 대응 (FILE-071 ~ FILE-075)

### FILE-071 - 실제 공개 접근
- **Statement:** 성공 판정은 요청 응답이 아니라 실제 공개 URL·Target의 접근 결과를 포함해야 한다.
- **Verification:** 적절한 권한 관점에서 URL·상태·가시성을 확인한다.
- **Exceptions:** 전파 지연은 VERIFYING 또는 UNKNOWN으로 기록한다.

### FILE-072 - 공개 내용 대조
- **Statement:** 실제 제목·본문·필드·자산·링크·언어·지역을 Release Package와 대조해야 한다.
- **Verification:** Live Verification Snapshot과 Package를 비교한다.
- **Exceptions:** 채널 표시 전용 비의미 변환은 차이와 근거를 기록한다.

### FILE-073 - 부분 성공 분리
- **Statement:** Target·필드·자산 일부만 성공하면 전체 성공이 아닌 PARTIAL로 기록해야 한다.
- **Verification:** Target별 Attempt와 Live 결과를 집계한다.
- **Exceptions:** 없음.

### FILE-074 - Critical Rollback
- **Statement:** 잘못된 Target·민감정보 노출·중대한 허위·권리 위반은 승인 Route에 따라 즉시 중지·숨김·복구해야 한다.
- **Verification:** Incident 시각·영향·조치·승인과 현재 공개 상태를 확인한다.
- **Exceptions:** 삭제 금지 의무가 있으면 공개 차단과 증거 보존을 분리한다.

### FILE-075 - Correction 새 Release
- **Statement:** 사실·의미 교정은 승인된 정정본과 새 Release ID로 재게시해야 한다.
- **Verification:** Correction·Baseline·Approval·Attempt 계보를 검사한다.
- **Exceptions:** 비의미 표기 수정은 Project 정책이 허용하면 동일 Release의 패치 기록으로 남길 수 있다.

## 17.F 기록과 인계 (FILE-076 ~ FILE-080)

### FILE-076 - Publication Record 완결성
- **Statement:** 게시 기록은 Request·Baseline·Package·Approval·Attempt·Live Verification·Incident·QA를 포함해야 한다.
- **Verification:** 필수 기록 목록과 Publication Record를 검사한다.
- **Exceptions:** 범위 밖 Target은 제외 사유를 기록한다.

### FILE-077 - LIVE Gate
- **Statement:** G1~G8의 필수 Gate와 실제 Live Verification이 PASS일 때만 LIVE로 표시해야 한다.
- **Verification:** Gate Evidence와 Publication 상태를 대조한다.
- **Exceptions:** NOT_APPLICABLE은 승인 근거가 있어야 하며 NOT_TESTABLE은 LIVE에서 허용하지 않는다.

### FILE-078 - 실패 투명성
- **Statement:** FAILED·PARTIAL·UNKNOWN·ROLLBACK과 잔여 위험을 성공으로 축소하거나 숨기지 않아야 한다.
- **Verification:** Attempt·Incident·상태 보고를 대조한다.
- **Exceptions:** 없음.

### FILE-079 - Lifecycle Handoff
- **Statement:** LIVE 콘텐츠의 URL·공개 시점·Owner·기준 시점·재확인·만료 조건을 CNT-007에 인계해야 한다.
- **Verification:** Lifecycle Handoff 필수 필드를 검사한다.
- **Exceptions:** 즉시 폐기된 Release는 폐기 상태와 기록 위치를 인계한다.

### FILE-080 - 게시 계보 보존
- **Statement:** SEO Candidate부터 공개 결과와 Rollback까지 ID·버전·해시·승인·시각 계보를 재현할 수 있어야 한다.
- **Verification:** Publication Record의 참조 연결과 변경 이력을 검사한다.
- **Exceptions:** 없음.

# 18. AI용 압축 Publishing System

```text
1. publishing_request_id, SEO Candidate ID·버전·해시, Target·가시성·Window·Binding을 고정한다.
2. CNT-005 Handoff의 Field Set·Link Map·Variant·QA와 재확인 조건을 확인한다.
3. Release Baseline을 보존하고 Target별 Brief·Package·Manifest를 만든다.
4. 본문·필드·자산·링크가 승인 Candidate와 일치하고 Variant가 섞이지 않았는지 확인한다.
5. 권리·개인정보·기밀·Credential·Embargo·최소 권한을 검사한다.
6. 실제 채널과 같은 Preview에서 표시·접근성·링크·자산·언어·지역을 확인한다.
7. Baseline·Package·Target·가시성·Window·Rollback Route에 결속된 승인을 받는다.
8. 실행 직전 Target·계정·Window·승인을 재확인하고 고유 Attempt ID로 게시한다.
9. 응답·생성 ID·URL·시각·오류를 기록하고 재시도 전 원격 상태를 확인한다.
10. 실제 공개 URL에서 가시성·내용·필드·자산·링크를 Package와 대조한다.
11. 실패·부분 성공은 숨기지 말고 Critical이면 중지·복구하며 정정은 새 Release로 처리한다.
12. Publication Record와 URL·Owner·기준 시점·재확인·만료 조건을 CNT-007에 인계한다.
```

이 압축 블록은 상세 System의 파생본이다. 충돌하면 본문과 상위 LOCKED·APPROVED 기준본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

- CNT-006은 승인된 콘텐츠의 채널 패키징·승인·게시·공개 검증·실패 대응과 기록 계약만 정의한다.
- 사실·의미·SEO 변경은 CNT-003~005의 승인 경로로 반환한다.
- 파일 생성·전달의 공통 규칙은 COR-006, 버전·Rollback은 COR-007을 따른다.
- 장기 모니터링·갱신·통합·폐기는 CNT-007이 맡는다.
- 예약 실행·재시도·알림·상태 수집 구현은 Phase 5 Automation이 맡는다.

## 19.2 알려진 제한

- 모든 채널에 같은 승인 역할·게시 창·Preview·Rollback 방식을 강제하지 않는다.
- 외부 플랫폼의 장애·지연·정책 변경·색인·알고리즘·계정 제재를 보장하지 않는다.
- 게시 성공은 장기 접근성·정확성·검색 성과·전환 또는 규제 적합성을 보증하지 않는다.
- 서비스별 API·UI·Credential 저장·Webhook·Rate Limit은 현재 범위에 포함하지 않는다.
- Project 고유 계정 ID·SLA·긴급 승인·정정 공지 형식은 해당 Project 문서가 구체화한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-03 | LOCKED | Foundation Phase 4 순서에 따라 범용 Publishing 입력·Baseline·Target·Package·Rights·Privacy·Embargo·Preview·Approval·Attempt·Live Verification·Rollback·Lifecycle Handoff와 FILE-051~080 작성; 사용자 명시적 승인 반영 |
