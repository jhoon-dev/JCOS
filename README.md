# JCOS

JCOS는 AI 기반 콘텐츠와 문서 작업을 일관되게 설계·실행·검수하기 위한 문서 중심 운영 시스템입니다.

이 공개판은 여러 프로젝트에서 재사용할 수 있는 공통 원칙·워크플로와 가상의 학습 예제를 제공합니다. 실제 개인 프로젝트와 실행 결과는 제외합니다.

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

1. [빠른 시작](QUICKSTART.md)에서 작업별 문서를 선택합니다.
2. [가상 로컬 편집 예제](examples/README.md)로 입력과 결과 계약을 확인합니다.
   자신의 설정으로 시작하려면 [로컬 계약 초기화](templates/README.md)를 사용합니다.
   다음으로 [로컬 dry-run](examples/DRY_RUN.md)에서 작업 패키지와 검사 기록을 준비합니다.
3. [공개 등록부](00_FOUNDATION/DOCUMENT_REGISTER.md)에서 기준본 상태·버전·경로·해시를 확인합니다.
4. [Architecture](00_FOUNDATION/ARCHITECTURE.md)에 따라 프로젝트 전용 규칙과 자산을 별도 공간에서 관리합니다.

## 현재 상태

기존 공통 문서 28종은 v2.0.0 `LOCKED` 기록을 유지합니다. Foundation과 Core Runtime은 `REVIEW`이며, 공개판에는 내부 승인 근거와 실제 프로젝트 QA 증거가 포함되지 않습니다. 상태 기록과 공개 파일 무결성 검사는 운영 승인이나 실전 검증을 대신하지 않습니다.

[AUT-003 우선순위 명확화](04_AUTOMATION/AUT-003/AUT-003_PROMPT_SYSTEM_v2.0.1-rc.1.md)와 [작업별 적용 수준](00_FOUNDATION/APPLICATION_PROFILES.md)은 검토 후보입니다. 기존 승인본이나 필수 절차를 자동 대체하지 않습니다.

## 공개 패키지 검사

Python 3.12 이상에서 외부 패키지 없이 실행할 수 있습니다.

```text
python scripts/validate_docs.py
python scripts/validate_example.py examples/request.json
python -m unittest discover -s tests -v
```

검사 범위와 제한은 [검사 안내](scripts/README.md), 업데이트 내용은 [변경 이력](CHANGELOG.md), 후속 계획은 [로드맵](00_FOUNDATION/ROADMAP.md)을 참고하세요.

## 라이선스

별도 표시가 없는 문서는 [Creative Commons Attribution 4.0 International](LICENSE.md)에 따라 이용할 수 있습니다.

## 기여와 보안

기여 방법은 [CONTRIBUTING.md](CONTRIBUTING.md), 민감정보 신고 방법은 [SECURITY.md](SECURITY.md)를 참고하세요.
