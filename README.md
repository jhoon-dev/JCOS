# JCOS

JCOS는 AI 기반 콘텐츠와 문서 작업을 일관되게 설계·실행·검수하기 위한 문서 중심 운영 시스템입니다.

이 공개판은 특정 개인 프로젝트와 실행 결과를 제외하고, 여러 프로젝트에서 재사용할 수 있는 공통 원칙과 워크플로만 제공합니다.

## 공개 범위

- `00_FOUNDATION` — 구조, 아키텍처, 문서 등록 원칙, 규칙 ID 체계, 공개 로드맵
- `01_CORE` — 공통 운영·작성·조사·출처·품질·전달·버전·의사결정 원칙
- `02_DESIGN_SYSTEM` — HTML, DOCX, CSS, 구성요소, 이미지, 썸네일, 브랜드 원칙
- `03_CONTENT_SYSTEM` — 조사부터 작성·편집·검증·게시·수명주기까지의 워크플로
- `04_AUTOMATION` — 자동화 책임, 일정, 프롬프트, 복구, QA, 운영 원칙
- `06_LIBRARY/PROMPTS/CORE` — Core 문서에서 파생된 AI Runtime Compact와 Manifest

## 포함하지 않는 항목

개별 프로젝트 모듈, 프로젝트 전용 템플릿과 프롬프트, 실행 결과, 내부 QA 증거, 과거 버전, 임시 빌드 데이터는 공개판에 포함하지 않습니다.

현재 공개판은 검토와 변경 추적이 쉬운 Markdown을 기준 형식으로 제공합니다. DOCX와 PDF 배포본은 문서 메타데이터와 공개 범위를 별도로 검수한 뒤 릴리스 자산으로 제공할 수 있습니다.

## 시작하기

1. `00_FOUNDATION/ARCHITECTURE.md`에서 JCOS 계층과 책임 분리를 확인합니다.
2. `01_CORE`의 공통 원칙을 프로젝트 기본 규칙으로 사용합니다.
3. 필요한 Design, Content, Automation 문서를 선택해 프로젝트 규칙에 연결합니다.
4. 프로젝트 전용 규칙과 자산은 공개 Core와 분리된 별도 공간에서 관리합니다.

## 라이선스

별도 표시가 없는 문서는 [Creative Commons Attribution 4.0 International](LICENSE.md)에 따라 이용할 수 있습니다.

## 기여와 보안

기여 방법은 [CONTRIBUTING.md](CONTRIBUTING.md), 민감정보 신고 방법은 [SECURITY.md](SECURITY.md)를 참고하세요.
