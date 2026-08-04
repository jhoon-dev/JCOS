# AUT-004 FAILURE RECOVERY

- Version: 2.0.0
- Status: `LOCKED`
- Owner: JCOS Maintainers
- Scope: Failure Event·Classification·Retry Eligibility·Budget·Backoff·Checkpoint·Resume·Re-execution·Rollback·Compensation·Partial·Unknown·Quarantine·Dead Letter·Escalation·Closure
- Rule IDs: AUT-091~AUT-120
- Reference: AUT-001~003 v2.0.0 LOCKED, COR-005~007 v2.0.0 LOCKED

## Package

- `AUT-004_FAILURE_RECOVERY_v2.0.0.md`
- `AUT-004_FAILURE_RECOVERY_v2.0.0.docx`
- `AUT-004_FAILURE_RECOVERY_v2.0.0.pdf`
- `QA_REPORT.md`
- `SHA256SUMS.txt`

## QA Summary

- AUT-091~AUT-120 연속성·고유성 및 AUT-001~090과의 연속 확장 확인
- 특정 AI·모델·Provider·Scheduler·Queue·Workflow·SDK 비종속성 확인
- 재시도·재실행·재개·롤백·보상의 구분과 안전 게이트 확인
- DOCX 1 Section·252 Paragraphs·9 Tables, 수정 이력·댓글 구조 검사 완료
- PDF 15페이지 전수 시각 검사 완료
- 열린 Critical·Major·Minor 결함 0건

사용자 승인과 QA를 완료한 `APPROVED` 기준본이다. 변경 전 REVIEW 패키지는 History에 보존했으며 명시적 잠금 승인 전 `LOCKED`로 표시하지 않는다. 다음 문서는 AUT-005 QA AUTOMATION이다.

## 잠금 기록

- Lock Date: `2026-08-03`
- Lock Evidence: 사용자의 승인 항목 전체 LOCKED 전환 지시
- Preserved Baseline: `08_HISTORY`의 `AUT-004/v2.0.0_APPROVED_PRE_LOCK/`
- 변경은 새 버전과 승인 절차를 통해서만 수행한다.
