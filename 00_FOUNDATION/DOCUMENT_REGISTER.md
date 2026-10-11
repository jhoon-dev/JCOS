# JCOS Public Document Register

| 항목 | 값 |
|---|---|
| Document ID | FND-003 |
| Version | 2.1.0 |
| Status | REVIEW |
| Owner | JCOS Maintainers |

## 공개 문서군

| Prefix | 영역 | 공개 상태 |
|---|---|---|
| COR | Core 공통 원칙 | 포함 |
| DSG | Design System | 포함 |
| CNT | Content System | 포함 |
| AUT | Automation System | 포함 |
| PRJ | 개별 Project Module | 제외 |

## 현재 공개 패키지

- `COR-001`~`COR-008`
- `DSG-001`~`DSG-007`
- `CNT-001`~`CNT-007`
- `AUT-001`~`AUT-006`
- `06_LIBRARY/PROMPTS/CORE/JCOS_CORE_COMPACT_v2.0.0.md`
- `06_LIBRARY/PROMPTS/CORE/RUNTIME_MANIFEST.md`

## 등록 원칙

1. 문서 ID는 하나의 책임 영역에만 연결합니다.
2. 같은 ID와 Version의 승인 문서를 조용히 덮어쓰지 않습니다.
3. 파생 Runtime은 원문 문서, 섹션, Version과 해시를 Manifest에 기록합니다.
4. 공개 등록부에는 개별 프로젝트명, 전용 경로, 실행 결과와 내부 승인 기록을 넣지 않습니다.
5. 공개판에서 제외된 문서를 참조해야 하는 경우 구체적인 이름 대신 `Project Module` 또는 `Project Fixture` 역할만 표시합니다.

## 공개 Foundation 경로

| ID | 문서 | 상태 |
|---|---|---|
| FND-001 | [Foundation 안내](README.md) | REVIEW |
| FND-002 | [Architecture](ARCHITECTURE.md) | REVIEW |
| FND-003 | [Document Register](DOCUMENT_REGISTER.md) | REVIEW |
| FND-004 | [Rule ID System](RULE_ID_SYSTEM.md) | REVIEW |
| FND-005 | [Roadmap](ROADMAP.md) | REVIEW |
| FND-006 | [Application Profiles](APPLICATION_PROFILES.md) | REVIEW, 검토 후보 |

FND-002·003·005 참조는 위 공개 경로로 해석합니다. 등록부 자체는 승인 근거가 아니며, Foundation REVIEW와 하위 LOCKED 기록의 관계는 통합 검토가 남아 있습니다.

## 기계 판독 등록부와 기준본 선택

[document_registry.json](document_registry.json)은 문서별 ID, 정확한 버전·상태·경로·SHA-256, 의존 ID와 활성 여부를 기록합니다. JSON의 `active`는 문서군에서 현재 선택된 파일이라는 뜻이며 승인 또는 운영 적합성을 뜻하지 않습니다. REVIEW 상태도 반드시 따로 확인합니다.

- Core·Design·Content·Automation의 기존 28종은 v2.0.0 LOCKED 기준본을 유지합니다. 상태는 기존 파일의 기록이며 비공개 승인 증거를 재검증한 결과가 아닙니다.
- AUT-003 v2.0.1-rc.1과 FND-006 v0.1.0-rc.1은 REVIEW 후보이며 `active: false`입니다.
- Core Runtime은 v2.0.0 REVIEW 파생본입니다. 원문과 해시가 일치해도 승인·운영 승격을 의미하지 않습니다.
- 사람이 읽는 모듈 README는 탐색 안내입니다. 메타데이터와 무결성 검사는 상세 파일과 JSON 등록 항목을 대조합니다.

승격은 대상 버전·QA·승인·호환성 기록을 확인한 뒤 활성 항목을 명시적으로 전환합니다. 기존 승인본을 덮어쓰거나 후보를 자동 활성화하지 않습니다. JSON 해시는 실제 공개 파일 바이트를 기준으로 계산합니다.

## 공개 학습 자료

`examples/`의 가상 프로젝트·요청·예상 결과는 범용 학습 자료입니다. 실제 개별 프로젝트명·전용 MASTER·실행 증거는 계속 제외합니다. 정적 검사와 예제 입력 검사는 내용 승인, 실제 AI 실행 또는 프로젝트 QA가 아닙니다.
