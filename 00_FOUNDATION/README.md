# JCOS Foundation

| 항목 | 값 |
|---|---|
| Document ID | FND-001 |
| Version | 2.1.0 |
| Status | REVIEW |
| Owner | JCOS Maintainers |

Foundation은 JCOS의 구조와 문서 관리 원칙을 설명하는 시작점입니다.

## 문서

- `ARCHITECTURE.md` — 실행 계층, 책임 분리, 충돌 처리와 변경 전파
- `DOCUMENT_REGISTER.md` — 공개 문서군과 상태 관리 원칙
- `RULE_ID_SYSTEM.md` — 문서 및 규칙 식별자 체계
- `ROADMAP.md` — 공통 시스템 공개 로드맵

## 기본 원칙

JCOS는 특정 AI 도구나 콘텐츠 유형에 종속되지 않습니다. 공통 규칙은 Core에서 관리하고, 프로젝트별 규칙·기준 자산·실행 지침·결과물은 공통 시스템과 분리합니다.

이 공개판은 공통 시스템만 제공합니다. 개별 프로젝트 모듈, 전용 템플릿, 실행 결과, 내부 QA 증거와 History는 공개 범위에서 제외합니다.

## 문서 계층

1. `00_FOUNDATION` — 구조와 관리 원칙
2. `01_CORE` — 모든 프로젝트의 공통 규칙
3. `02_DESIGN_SYSTEM` — 형식과 시각 시스템
4. `03_CONTENT_SYSTEM` — 콘텐츠 제작 워크플로
5. `04_AUTOMATION` — 자동화 실행과 통제
6. `06_LIBRARY/PROMPTS/CORE` — 승인 Core에서 파생한 실행용 Compact

프로젝트 구현은 이 계층을 상속하지만 공개 Core와 독립된 저장 위치에서 관리합니다.
