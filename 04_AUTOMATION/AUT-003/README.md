# AUT-003 PROMPT SYSTEM

- Document ID: `AUT-003`
- Version: `2.0.0`
- Status: `LOCKED` — 기존 문서에 기록된 승인 상태
- Owner: JCOS Maintainers

## 현재 공개 파일

- [AUT-003_PROMPT_SYSTEM_v2.0.0.md](AUT-003_PROMPT_SYSTEM_v2.0.0.md) — 기존 규범 기준본

DOCX·PDF, 내부 QA 보고서·체크섬 패키지와 승인 History는 이 공개판에 포함하지 않습니다. 공개 배포가 검증된 문서 형식은 별도 릴리스 자산으로 제공할 수 있습니다.

## 문서 범위

Binding·Runtime Compact·Instruction Layer·Input Slot·Context Budget·Capability·Adapter·Tool·Injection·Secret·Output·Validation

## 상태와 검증 범위

현재 기준본은 기존 v2.0.0 LOCKED 문서입니다. 이전 REVIEW·APPROVED 단계 설명은 현재 상태로 사용하지 않습니다. 승인 근거와 내부 이력은 공개판에서 독립적으로 확인할 수 없습니다.

공개 파일의 경로·메타데이터·SHA-256은 [공개 등록부](../../00_FOUNDATION/DOCUMENT_REGISTER.md)와 자동 검사로 확인합니다. 정적 검사 PASS는 내용 승인, 실제 프로젝트 QA 또는 LOCKED 승격을 의미하지 않습니다.

Runtime 반영은 별도 원문 연결·통합 검증을 요구합니다. 이 README 수정은 기준본 내용을 변경하지 않습니다.

## 과거 내부 QA 요약

다음은 기존 내부 검증의 요약입니다. 공개판에는 검증 원자료가 없어 이번 공개 패키지에서 재현된 결과로 해석하지 않습니다.

- AUT-061~AUT-090 연속성·고유성 및 AUT-001~060과의 연속 확장 확인
- 특정 AI·모델·역할명·Tokenizer·Tool Calling 문법·SDK·Workflow 서비스 비종속성 확인
- 사람용 상세 원본과 AI Runtime Compact·Execution Prompt의 계보 분리 확인
- DOCX 1 Section·269 Paragraphs·10 Tables, 수정 이력·댓글 구조 검사 완료
- PDF 15페이지 전수 시각 검사 완료
- 열린 Critical·Major·Minor 결함 0건

## 검토 후보

- [v2.0.1-rc.1 우선순위 명확화](AUT-003_PROMPT_SYSTEM_v2.0.1-rc.1.md) — REVIEW, 현재 LOCKED 기준본을 자동 대체하지 않습니다.
