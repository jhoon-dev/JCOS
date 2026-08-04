# JCOS v2.0.0 - COR-001 CORE INSTRUCTIONS

## JCOS 공통 운영 지침

| 항목 | 값 |
|---|---|
| Document ID | COR-001 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | CORE |
| Applies To | JCOS를 상속하는 모든 프로젝트 |
| Priority | CRITICAL |
| Created | 2026-07-30 |
| Last Updated | 2026-07-30 |
| Depends On | JCOS v2.0 Foundation |

> **상태 알림:** 이 문서는 범용성·내용·형식 QA와 사용자 승인을 통과한 v2.0.0 `LOCKED` 기준본이다. 변경은 COR-007에 따른 새 버전·QA·승인 절차로만 수행한다.

---

## 문서 목적

이 문서는 JCOS를 상속하는 모든 프로젝트의 공통 운영 헌법이다. 프로젝트별 세부 규칙은 이 문서를 복사하지 않고 참조하며, 충돌 시 본 문서와 별도 Decision Rules의 우선순위를 따른다.

## 목차

1. 목적과 비목적
2. 적용 범위와 대상
3. 규범 언어와 용어
4. 운영 아키텍처
5. 핵심 운영 원칙
6. 요청 해석과 변경 경계
7. 근거와 출처
8. 글쓰기와 편집
9. MASTER와 디자인
10. 파일과 전달
11. 품질 게이트
12. 자동화와 실행
13. 오류와 실패 처리
14. 버전과 변경 관리
15. 보안·개인정보·권리
16. 준수와 감사
17. 규칙 카탈로그
18. 표준 실행 수명주기
19. 준수 체크리스트
20. 부록

---

# 1. 목적과 비목적

## 1.1 목적

본 문서는 JCOS를 상속하는 모든 프로젝트가 공통으로 따라야 할 최상위 운영 규칙을 정의한다. JCOS는 매번 새 형식을 고안하는 제작 지침이 아니라, 승인된 기준을 반복적으로 적용해 안정적인 콘텐츠를 만드는 운영체제다.

## 1.2 핵심 목표

JCOS Core의 목표는 일관성, 사실성, 재현성, 유지보수성, 전달 가능성을 보장하는 것이다. 결과물의 화려함보다 같은 기준을 다시 적용할 수 있는지가 중요하다.

## 1.3 비목적

본 문서는 특정 프로젝트의 세부 뉴스 선정, 디자인 값, 섹션 이름, 예약 시각을 정의하지 않는다. 이러한 세부사항은 Project Module, MASTER, Automation 문서에서 정의한다.

# 2. 적용 범위와 대상

## 2.1 적용 프로젝트

콘텐츠, 교육, 데이터, 도구 안내 및 향후 JCOS를 상속하는 모든 프로젝트에 적용한다.

## 2.2 적용 활동

조사, 작성, 편집, 디자인 적용, 파일 생성, 렌더링, 검수, 발행, 자동화, 오류 복구, 버전 관리를 포함한다.

## 2.3 적용 주체

사람, 대화형·생성형 AI 시스템, 외부 자동화, 스크립트, 에이전트 등 결과물을 생성하거나 변경하는 모든 실행 주체에 적용한다.

# 3. 규범 언어와 용어

## 3.1 규범 언어

“해야 한다”는 필수, “하지 않는다”는 금지, “권장한다”는 기본적으로 따라야 하나 정당한 사유로 예외가 가능한 규칙을 뜻한다.

## 3.2 핵심 용어

CORE는 공통 규칙, Project Module은 프로젝트 특수 규칙, MASTER는 승인된 디자인·구조 기준, Execution은 특정 시점의 실행 명령, Output은 실제 결과물이다.

## 3.3 상태 용어

DRAFT는 초안, REVIEW는 사용자 검토 대기, APPROVED는 내용 승인, LOCKED는 운영 기준 동결, DEPRECATED는 대체됨, ARCHIVED는 이력 보존을 뜻한다.

# 4. 운영 아키텍처

## 4.1 계층

JCOS CORE → Project Module → MASTER → Execution Prompt → Output의 순서로 상속한다.

## 4.2 책임 분리

CORE는 공통 판단, Project Module은 프로젝트 특수성, MASTER는 디자인, Execution은 오늘의 작업, QA는 검증을 담당한다.

## 4.3 단일 기준원

각 판단과 디자인 영역은 현재 활성 상태인 하나의 LOCKED 기준만 가져야 한다.

# 5. 핵심 운영 원칙

## 5.1 안정성

새로움보다 안정성을 우선한다. 2.0 범위를 완료하기 전 새로운 아이디어는 실행하지 않고 후속 버전 Backlog로 분리한다.

## 5.2 품질

자동화보다 품질을 우선한다. 산출물 생성은 검수와 실제 전달까지 포함한다.

## 5.3 정직성

확인하지 못한 사실, 링크, 파일 상태를 확인한 것처럼 말하지 않는다.

# 6. 요청 해석과 변경 경계

## 6.1 현재 요청

현재 사용자의 명시적 요청을 최우선으로 해석한다.

## 6.2 범위 관리

요청하지 않은 개선과 재설계를 작업 범위에 추가하지 않는다.

## 6.3 디자인 승인

내용 수정과 디자인 변경을 분리하며 디자인은 명시적 승인 후 새 버전에서 적용한다.

# 7. 근거와 출처

## 7.1 출처 우선순위

공식 원문, 원 논문, 원 데이터, 공식 저장소를 우선하고 필요한 경우 독립 보도를 보강한다.

## 7.2 사실 검증

중요 주장과 수치는 출처가 실제로 뒷받침하는지 문장 단위로 확인한다.

## 7.3 최신성

시간에 따라 변할 수 있는 사실은 실행 시점에 다시 확인한다.

# 8. 글쓰기와 편집

## 8.1 독자 효용

대상 독자가 무엇이 바뀌었고 왜 중요하며 무엇을 해야 하는지 이해하도록 쓴다.

## 8.2 사실과 해석

사실, 해석, 전망, 권고를 구분한다.

## 8.3 편집 품질

과장, 반복, 상투어, 무의미한 서론을 제거한다.

# 9. MASTER와 디자인

## 9.1 MASTER 보호

MASTER는 일일 Output과 분리하며 승인 없이 덮어쓰지 않는다.

## 9.2 콘텐츠 삽입

일일 작업은 MASTER 슬롯에 오늘의 콘텐츠를 삽입하는 방식으로 수행한다.

## 9.3 포맷 정합

HTML, DOCX, PDF 등 형식이 달라도 핵심 원고와 결론은 일치해야 한다.

# 10. 파일과 전달

## 10.1 실재성

파일 요청은 실제 파일을 생성하고 존재, 크기, 경로를 확인해야 한다.

## 10.2 렌더링

레이아웃 파일은 렌더링 화면을 모든 페이지 기준으로 검수한다.

## 10.3 전달

사용자에게 제공하는 링크는 확인된 실제 경로만 사용한다.

# 11. 품질 게이트

## 11.1 완료 정의

완료는 작성, 생성, 검수, 링크 확인, 전달의 전체 과정을 뜻한다.

## 11.2 차단 조건

Critical 항목이 하나라도 실패하면 완료 또는 LOCKED로 표시하지 않는다.

## 11.3 정합성

다중 형식 산출물과 목차·섹션·링크 간 대응 관계를 검사한다.

# 12. 자동화와 실행

## 12.1 예약 역할

예약은 규칙을 새로 정의하지 않고 승인된 규칙을 호출하는 실행 명령이다.

## 12.2 중복 방지

같은 목적과 시각의 중복 예약을 방지한다.

## 12.3 복구 가능성

실패 시 마지막 성공 상태를 보호하고 수동 복구 절차를 유지한다.

# 13. 오류와 실패 처리

## 13.1 상태 구분

성공, 부분 성공, 실패를 구분하여 보고한다.

## 13.2 원인 기록

오류의 단계, 입력, 사용 버전, 영향 범위, 재처리 결과를 기록한다.

## 13.3 재실행

재실행은 멱등성, 중복 출력, 기존 성공 파일 보존을 확인한 뒤 수행한다.

# 14. 버전과 변경 관리

## 14.1 버전 체계

Major.Minor.Patch를 사용해 호환성 파괴, 하위 호환 기능, 버그 수정을 구분한다.

## 14.2 승인

APPROVED와 LOCKED 전환에는 명시적 승인 기록이 필요하다.

## 14.3 롤백

이전 LOCKED 버전과 변경 이력을 보존하여 롤백 가능성을 유지한다.

# 15. 보안·개인정보·권리

## 15.1 최소 수집

목적에 필요하지 않은 개인정보와 민감정보를 포함하지 않는다.

## 15.2 비밀 보호

비밀번호, 토큰, API 키, 내부 접속정보를 출력이나 로그에 남기지 않는다.

## 15.3 저작권

외부 자료는 필요한 범위에서 요약하고 인용 한도와 출처를 준수한다.

# 16. 준수와 감사

## 16.1 준수 책임

각 Project Module은 상속하는 CORE 버전과 예외를 명시한다.

## 16.2 감사

Phase 종료와 정식 운영 후 핵심 프로젝트의 준수 상태를 검토한다.

## 16.3 개선

감사 결과는 현재 2.0 결함 수정과 2.1 Backlog를 구분해 기록한다.

# 17. 규칙 카탈로그

이 장의 규칙은 규범적이다. 각 Project Module은 적용되는 CORE Rule ID를 참조하고, 예외가 필요한 경우 프로젝트 전용 Rule ID와 근거를 기록해야 한다.

## 17.A 목적과 운영 철학 (CORE-001 ~ CORE-010)

### CORE-001 - JCOS 목적 우선

- **Priority:** Critical
- **Statement:** 모든 실행은 반복 가능한 콘텐츠 운영 품질을 높이는 방향으로 수행해야 한다.
- **Rationale:** JCOS는 단발성 결과물보다 일관성, 재현성, 유지보수성을 우선하는 운영체제다.
- **Verification:** 실행 결과가 프로젝트 목적, MASTER, 품질 게이트와 일치하는지 검토한다.
- **Exceptions:** 사용자가 명시적으로 일회성 실험을 요청한 경우에도 기존 MASTER는 변경하지 않고 별도 실험 결과로 구분한다.

### CORE-002 - 안정성 우선

- **Priority:** Critical
- **Statement:** 새로운 아이디어나 기능은 현재 운영의 안정성을 훼손하지 않는 경우에만 도입할 수 있다.
- **Rationale:** 중간에 좋은 아이디어를 즉시 반영하면 구조와 포맷이 반복적으로 흔들릴 수 있다.
- **Verification:** 변경 전후의 규칙, MASTER, 산출물 호환성을 비교한다.
- **Exceptions:** 승인된 버전 업그레이드 계획에 포함된 변경은 허용한다.

### CORE-003 - 품질 우선

- **Priority:** Critical
- **Statement:** 자동화 속도나 생산량보다 사실성, 완결성, 전달 가능성을 우선한다.
- **Rationale:** 빠른 자동화가 오류 파일이나 검증되지 않은 정보를 반복 생산하면 운영 가치가 낮아진다.
- **Verification:** QA 결과와 실패 항목을 확인한다.
- **Exceptions:** 긴급 속보 등 시간 우선 상황은 프로젝트 규칙에서 명시적으로 정의해야 한다.

### CORE-004 - 재현 가능성

- **Priority:** High
- **Statement:** 동일한 입력, 규칙, MASTER를 사용한 실행은 구조적으로 동등한 결과를 생성해야 한다.
- **Rationale:** 재현성이 있어야 오류 원인 분석과 자동화가 가능하다.
- **Verification:** 동일 조건의 샘플 실행 간 구조, 파일 구성, 필수 섹션을 비교한다.
- **Exceptions:** 외부 데이터 변화로 인한 내용 차이는 허용한다.

### CORE-005 - 단일 기준원

- **Priority:** Critical
- **Statement:** 각 판단 영역에는 하나의 승인된 기준 문서 또는 MASTER만 존재해야 한다.
- **Rationale:** 복수의 기준이 경쟁하면 오래된 파일이 잘못 적용될 수 있다.
- **Verification:** Document Register와 Project Module의 참조 대상을 대조한다.
- **Exceptions:** 마이그레이션 기간에는 구버전과 신버전을 병기하되 활성 기준을 명확히 표시한다.

### CORE-006 - 중복 규칙 금지

- **Priority:** High
- **Statement:** 공통 규칙은 CORE에서 한 번만 정의하고 프로젝트 문서에서는 복사하지 않고 참조해야 한다.
- **Rationale:** 중복 규칙은 업데이트 누락과 충돌을 만든다.
- **Verification:** 프로젝트 문서에서 동일 문장 또는 의미의 중복 규칙을 검색한다.
- **Exceptions:** 프로젝트 특수 예외는 별도 Rule ID로 정의할 수 있다.

### CORE-007 - 검증 가능성

- **Priority:** High
- **Statement:** 모든 필수 규칙은 사람이거나 자동화가 통과 여부를 판단할 수 있게 작성해야 한다.
- **Rationale:** 모호한 규칙은 실행과 QA에서 서로 다른 해석을 낳는다.
- **Verification:** Rule Catalog의 verification 항목 존재 여부를 확인한다.
- **Exceptions:** 순수 철학 선언은 검증 항목을 운영 지표로 연결할 수 있다.

### CORE-008 - 명시적 상태

- **Priority:** High
- **Statement:** 모든 운영 문서와 MASTER는 DRAFT, REVIEW, APPROVED, LOCKED, DEPRECATED, ARCHIVED 중 하나의 상태를 표시해야 한다.
- **Rationale:** 상태가 없으면 초안이 운영 기준으로 오인될 수 있다.
- **Verification:** 문서 헤더와 등록부를 확인한다.
- **Exceptions:** 일일 산출물은 OUTPUT 상태 체계를 별도로 사용할 수 있다.

### CORE-009 - 운영과 실험 분리

- **Priority:** High
- **Statement:** 실험 결과는 운영 MASTER와 물리적 또는 논리적으로 분리해야 한다.
- **Rationale:** 실험 파일이 기준 폴더에 섞이면 다음 실행에 잘못 참조될 수 있다.
- **Verification:** 파일 경로, 파일명, 상태 라벨을 검사한다.
- **Exceptions:** 승인 후 실험 결과를 정식 버전으로 승격할 수 있다.

### CORE-010 - 완결된 단계 진행

- **Priority:** High
- **Statement:** 현재 버전의 합의된 범위를 완료하기 전에는 신규 아이디어를 실행 범위에 추가하지 않는다.
- **Rationale:** 스코프 확장은 완성 지연과 문서 구조 변경을 유발한다.
- **Verification:** Roadmap과 현재 릴리스 범위를 대조한다.
- **Exceptions:** 치명적 결함 수정과 안전상 필수 변경은 즉시 처리한다.

## 17.B 계층, 책임, 기준원 (CORE-011 ~ CORE-020)

### CORE-011 - 계층 상속

- **Priority:** Critical
- **Statement:** 모든 프로젝트는 CORE, Project Module, MASTER, Execution Prompt, Output의 계층을 따라야 한다.
- **Rationale:** 계층은 공통 규칙과 프로젝트 특수 규칙을 분리한다.
- **Verification:** 프로젝트 메타데이터의 inherits와 masters를 확인한다.
- **Exceptions:** 비콘텐츠 프로젝트는 적용 가능한 계층만 사용하되 이유를 기록한다.

### CORE-012 - 상위 규칙 준수

- **Priority:** Critical
- **Statement:** 하위 계층은 상위 계층의 LOCKED 규칙을 임의로 무효화할 수 없다.
- **Rationale:** 상속 체계가 유지되어야 공통 품질을 보장할 수 있다.
- **Verification:** 충돌 규칙을 Decision Matrix로 검토한다.
- **Exceptions:** 사용자의 명시적 변경 승인과 필수 안전 규칙은 예외다.

### CORE-013 - 책임 단일화

- **Priority:** High
- **Statement:** 각 규칙, MASTER, 자동화에는 관리 책임자 또는 승인 주체를 표시해야 한다.
- **Rationale:** 책임이 불명확하면 변경과 오류 대응이 지연된다.
- **Verification:** 문서 메타데이터의 owner 필드를 확인한다.
- **Exceptions:** 개인 운영에서는 Owner를 JCOS Maintainers으로 통일할 수 있다.

### CORE-014 - 참조 명시

- **Priority:** High
- **Statement:** Project Module은 상속하는 CORE 버전과 사용하는 MASTER 버전을 명시해야 한다.
- **Rationale:** 암묵적 참조는 버전 교체 시 예측하지 못한 결과를 만든다.
- **Verification:** 프로젝트 헤더의 dependencies를 확인한다.
- **Exceptions:** 없음으로 표기할 수 있으나 빈 값은 허용하지 않는다.

### CORE-015 - Output 비승격

- **Priority:** Critical
- **Statement:** 일일 Output은 사용자 승인 없이 MASTER로 자동 승격되지 않는다.
- **Rationale:** 우연히 잘 나온 결과가 검증 없이 다음 기준이 되는 것을 막는다.
- **Verification:** MASTER 등록부와 Output 경로를 비교한다.
- **Exceptions:** 사용자가 해당 Output을 신규 MASTER 후보로 지정할 수 있다.

### CORE-016 - Execution 최소화

- **Priority:** Medium
- **Statement:** Execution Prompt는 오늘 수행할 작업과 참조 대상만 포함하고 공통 규칙을 장문으로 복제하지 않는다.
- **Rationale:** 중복 프롬프트는 유지보수와 토큰 비용을 증가시킨다.
- **Verification:** Prompt에서 CORE 문구 중복률을 점검한다.
- **Exceptions:** 독립 실행 환경에서 참조 문서를 읽을 수 없을 때 필수 요약 규칙을 포함할 수 있다.

### CORE-017 - Project 특수성 분리

- **Priority:** High
- **Statement:** 프로젝트에만 적용되는 조사, 문체, 섹션, 산출물 규칙은 Project Module에서 정의해야 한다.
- **Rationale:** CORE가 프로젝트 세부사항으로 비대해지는 것을 방지한다.
- **Verification:** 규칙 적용 범위를 검토한다.
- **Exceptions:** 다수 프로젝트에 반복되면 CORE 또는 공통 확장 문서로 승격을 검토한다.

### CORE-018 - MASTER 역할 제한

- **Priority:** High
- **Statement:** MASTER는 승인된 디자인과 구조를 정의하며 조사 정책이나 일일 내용 자체를 기준으로 사용하지 않는다.
- **Rationale:** 디자인 파일에 운영 정책이 섞이면 변경 범위가 불명확해진다.
- **Verification:** MASTER 내용과 MASTER Map을 검토한다.
- **Exceptions:** 필드 설명이나 플레이스홀더는 포함할 수 있다.

### CORE-019 - QA 독립성

- **Priority:** High
- **Statement:** QA 기준은 생성 프롬프트와 분리된 문서 또는 명시적 검수 단계로 유지해야 한다.
- **Rationale:** 생성 과정이 스스로 누락을 알아차리지 못할 수 있으므로 독립 검수가 필요하다.
- **Verification:** Quality Gate 실행 기록을 확인한다.
- **Exceptions:** 단순한 일회성 작업에서는 동일 실행 안에서 별도 단계로 수행할 수 있다.

### CORE-020 - 변경 이력 보존

- **Priority:** High
- **Statement:** 승인된 문서와 MASTER의 변경은 CHANGELOG에 기록해야 한다.
- **Rationale:** 변경 원인을 추적해야 회귀와 책임을 관리할 수 있다.
- **Verification:** 버전 파일과 Changelog 항목을 대조한다.
- **Exceptions:** 오탈자라도 의미나 출력에 영향을 주면 기록한다.

## 17.C 요청 해석과 변경 통제 (CORE-021 ~ CORE-030)

### CORE-021 - 현재 요청 우선 해석

- **Priority:** Critical
- **Statement:** 사용자의 현재 명시적 요청은 기존 선호보다 우선하되 필수 안전 규칙과 충돌할 수 없다.
- **Rationale:** 현재 의도는 과거 설정보다 정확한 실행 기준이다.
- **Verification:** 요청과 결과를 직접 대조한다.
- **Exceptions:** 요청이 모호하면 연결된 자료나 프로젝트 문서로 해결하고 필요한 경우에만 확인 질문을 한다.

### CORE-022 - 범위 확대 금지

- **Priority:** High
- **Statement:** 사용자가 요청하지 않은 구조, 디자인, 플랫폼 또는 기능 변경으로 작업 범위를 확대하지 않는다.
- **Rationale:** 선의의 개선이 기존 운영 안정성을 훼손할 수 있다.
- **Verification:** 변경 목록을 요청 범위와 비교한다.
- **Exceptions:** 명백한 오류 수정은 별도 고지 후 포함할 수 있다.

### CORE-023 - 콘텐츠-디자인 분리

- **Priority:** Critical
- **Statement:** 날짜, 기사, 제목, 문장, 데이터 변경 요청을 디자인 변경으로 해석하지 않는다.
- **Rationale:** 가장 빈번한 포맷 흔들림을 방지하는 핵심 규칙이다.
- **Verification:** HTML/CSS/Word 스타일 diff를 수행한다.
- **Exceptions:** 사용자가 색상, 여백, 구조 등 디자인 요소를 명시한 경우는 제외한다.

### CORE-024 - 명시적 디자인 승인

- **Priority:** Critical
- **Statement:** MASTER 디자인 변경은 사용자가 변경 대상과 방향을 명시적으로 승인한 경우에만 수행한다.
- **Rationale:** 암묵적 선호 추정으로 MASTER를 변경하지 않는다.
- **Verification:** 승인 기록과 변경 diff를 확인한다.
- **Exceptions:** 치명적 렌더링 결함은 버그 수정 버전으로 제안할 수 있다.

### CORE-025 - 모호성 최소 질문

- **Priority:** Medium
- **Statement:** 파일, 연결 데이터, 기존 지침으로 해결할 수 있는 모호성은 먼저 조회하고 불필요한 확인 질문을 하지 않는다.
- **Rationale:** 사용자의 작업 흐름을 끊지 않으면서 정확도를 높인다.
- **Verification:** 조회 가능 자료 사용 여부를 확인한다.
- **Exceptions:** 필수 값이 실제로 없을 때는 질문한다.

### CORE-026 - 추정 표시

- **Priority:** High
- **Statement:** 근거가 부족한 판단이나 예측은 사실과 분리해 추정 또는 해석임을 명시한다.
- **Rationale:** 독자가 사실과 의견을 혼동하지 않게 한다.
- **Verification:** 주장별 근거와 표현을 검토한다.
- **Exceptions:** 일반적인 편집 연결 문장은 별도 라벨이 필요하지 않을 수 있다.

### CORE-027 - 미지원 사항 정직 보고

- **Priority:** Critical
- **Statement:** 수행하지 못한 작업, 확인하지 못한 링크, 생성 실패를 완료한 것처럼 보고하지 않는다.
- **Rationale:** 신뢰는 그럴듯한 설명보다 실제 상태의 정확한 보고에서 나온다.
- **Verification:** 파일 존재, 링크, 도구 결과를 확인한다.
- **Exceptions:** 부분 완료는 완료 항목과 실패 항목을 분리해 보고한다.

### CORE-028 - 기존 결정 존중

- **Priority:** High
- **Statement:** LOCKED된 결정과 사용자가 반복적으로 확인한 선호는 새 명시적 변경 요청이 없는 한 유지한다.
- **Rationale:** 반복 수정 비용과 포맷 회귀를 줄인다.
- **Verification:** Project Changelog와 사용자 승인 기록을 검토한다.
- **Exceptions:** 새로운 상위 정책이나 안전 요구가 생기면 재검토한다.

### CORE-029 - 불필요한 재설계 금지

- **Priority:** High
- **Statement:** 작업을 시작하기 전에 이미 승인된 구조를 다시 제안하거나 재설계하지 않는다.
- **Rationale:** 계획 반복이 실제 산출물 생성을 지연하는 것을 방지한다.
- **Verification:** 응답과 실행 로그에서 제안 반복 여부를 확인한다.
- **Exceptions:** 사용자가 구조 검토를 직접 요청한 경우는 허용한다.

### CORE-030 - 완료 중심 실행

- **Priority:** Critical
- **Statement:** 산출물 생성 요청을 받으면 설명보다 실제 결과물 생성과 검증을 우선한다.
- **Rationale:** 운영 시스템은 계획이 아니라 전달 가능한 결과로 평가된다.
- **Verification:** 요청한 파일과 실제 전달물을 대조한다.
- **Exceptions:** 필수 입력이 없거나 안전상 수행 불가한 경우 이유를 명확히 설명한다.

## 17.D 조사, 근거, 출처 (CORE-031 ~ CORE-040)

### CORE-031 - 근거 우선

- **Priority:** Critical
- **Statement:** 외부 사실을 포함하는 콘텐츠는 확인 가능한 근거를 기반으로 작성해야 한다.
- **Rationale:** 근거 없는 정보는 브랜드 신뢰와 독자 판단을 훼손한다.
- **Verification:** 중요 주장과 출처의 연결을 검사한다.
- **Exceptions:** 순수 창작물이나 개인 의견문은 적용 범위를 별도로 표시한다.

### CORE-032 - 공식 원천 우선

- **Priority:** High
- **Statement:** 가능한 경우 공식 발표, 공식 문서, 원 논문, 원 데이터, 공식 저장소를 우선 사용한다.
- **Rationale:** 1차 자료는 전달 과정의 왜곡을 줄인다.
- **Verification:** Source List의 출처 유형을 분류한다.
- **Exceptions:** 공식 원천이 불충분하면 신뢰도 높은 직접 취재와 독립 분석을 병행한다.

### CORE-033 - 최신성 확인

- **Priority:** High
- **Statement:** 시간에 따라 변할 수 있는 사실은 실행 시점의 최신 상태를 확인해야 한다.
- **Rationale:** 가격, 일정, 제품, 인물, 정책은 빠르게 바뀔 수 있다.
- **Verification:** 출처 날짜와 실행 날짜를 비교한다.
- **Exceptions:** 역사적 분석은 대상 시점을 명시한다.

### CORE-034 - 다중 검증

- **Priority:** High
- **Statement:** 중요하거나 논쟁적인 주장은 가능한 경우 독립적인 복수 근거로 교차 확인한다.
- **Rationale:** 단일 자료의 오류와 편향 위험을 줄인다.
- **Verification:** 출처 도메인과 원천 독립성을 확인한다.
- **Exceptions:** 공식 발표 자체가 분석 대상이면 공식 원문 하나로 사실 확인이 가능하다.

### CORE-035 - 출처-주장 정합성

- **Priority:** Critical
- **Statement:** 인용한 출처는 해당 문장의 주장 전체를 실제로 뒷받침해야 한다.
- **Rationale:** 관련성만 있는 출처를 붙이면 검증된 것처럼 오해하게 한다.
- **Verification:** 문장 단위로 출처 내용을 대조한다.
- **Exceptions:** 한 문장에 여러 주장이 있으면 문장을 분리하거나 복수 출처를 사용한다.

### CORE-036 - URL 검증

- **Priority:** Critical
- **Statement:** 결과물에 포함하는 링크는 실제 원문을 가리키며 접근 가능한 형식인지 확인해야 한다.
- **Rationale:** 가짜 URL과 깨진 링크는 콘텐츠 신뢰와 사용성을 직접 훼손한다.
- **Verification:** HTTP 접근 또는 브라우저 확인을 수행한다.
- **Exceptions:** 로그인 필요 링크는 접근 조건을 표시한다.

### CORE-037 - 중복 통합

- **Priority:** Medium
- **Statement:** 같은 사건을 다룬 여러 기사는 하나의 주제로 통합하고 출처를 보강하는 데 사용한다.
- **Rationale:** 중복 뉴스가 콘텐츠 양을 부풀리는 것을 막는다.
- **Verification:** 주제별 사건 식별자를 비교한다.
- **Exceptions:** 서로 다른 관점 자체가 핵심이면 비교 구조로 분리할 수 있다.

### CORE-038 - 불확실성 공개

- **Priority:** High
- **Statement:** 정보가 미확정, 제한 공개, 루머, 전망일 경우 그 상태와 한계를 명시한다.
- **Rationale:** 독자가 확정 사실로 오해하지 않도록 한다.
- **Verification:** 표현과 출처의 확정 수준을 검토한다.
- **Exceptions:** 미확인 루머는 원칙적으로 핵심 기사에서 제외한다.

### CORE-039 - 수치 맥락 제공

- **Priority:** High
- **Statement:** 중요 수치에는 단위, 기준 시점, 비교 대상, 측정 조건을 함께 제공한다.
- **Rationale:** 수치는 맥락이 없으면 과장되거나 잘못 해석될 수 있다.
- **Verification:** 수치 주변의 단위와 기준을 검사한다.
- **Exceptions:** 널리 통용되는 단순 카운트는 문맥상 명확하면 축약할 수 있다.

### CORE-040 - 출처 목록 완결

- **Priority:** High
- **Statement:** 본문에 사용한 핵심 출처는 최종 Sources 또는 References에 누락 없이 정리한다.
- **Rationale:** 독자가 근거를 다시 확인할 수 있어야 한다.
- **Verification:** 본문 링크와 출처 목록을 비교한다.
- **Exceptions:** 채널 특성상 별도 목록이 없으면 본문 링크가 명확해야 한다.

## 17.E 글쓰기와 편집 (CORE-041 ~ CORE-050)

### CORE-041 - 독자 중심

- **Priority:** High
- **Statement:** 콘텐츠는 제작자가 아는 내용을 나열하지 않고 대상 독자가 이해하고 행동할 수 있게 구성한다.
- **Rationale:** 정보량보다 독자 효용이 콘텐츠 품질을 결정한다.
- **Verification:** Target Audience와 설명 수준을 대조한다.
- **Exceptions:** 전문가 대상 문서는 용어 설명을 축약할 수 있다.

### CORE-042 - 사실-해석 분리

- **Priority:** Critical
- **Statement:** 사실, 해석, 권고, 전망을 문장 구조나 라벨을 통해 구분한다.
- **Rationale:** 분류가 섞이면 의견이 사실처럼 보일 수 있다.
- **Verification:** 문단별 주장 유형을 점검한다.
- **Exceptions:** 간단한 서술에서는 접속 표현으로 구분할 수 있다.

### CORE-043 - 핵심 흐름 우선

- **Priority:** High
- **Statement:** 각 콘텐츠는 세부 항목 전에 전체를 연결하는 핵심 흐름 또는 중심 질문을 가져야 한다.
- **Rationale:** 독자가 여러 정보를 하나의 의미로 이해하게 한다.
- **Verification:** 제목, 리드, 결론의 일관성을 확인한다.
- **Exceptions:** 짧은 단일 사실 알림은 제외할 수 있다.

### CORE-044 - 구조적 서술

- **Priority:** High
- **Statement:** 설명형 콘텐츠는 원칙적으로 사실, 중요성, 영향, 한계, 다음 행동 순서를 사용한다.
- **Rationale:** 재현 가능한 구조는 누락을 줄이고 이해를 돕는다.
- **Verification:** 필수 요소 존재 여부를 확인한다.
- **Exceptions:** 프로젝트 특성에 따라 순서와 명칭을 조정할 수 있다.

### CORE-045 - 과장 금지

- **Priority:** Critical
- **Statement:** 근거 없이 최고, 혁명적, 완전한, 반드시와 같은 단정적·과장적 표현을 사용하지 않는다.
- **Rationale:** 과장은 신뢰를 낮추고 위험한 판단을 유도할 수 있다.
- **Verification:** 강한 형용사와 단정 표현을 검색한다.
- **Exceptions:** 공식 명칭이나 직접 인용은 출처와 함께 사용할 수 있다.

### CORE-046 - 상투어 제거

- **Priority:** Medium
- **Statement:** AI가 자주 생성하는 공허한 서론, 반복 결론, 의미 없는 전환 문구를 제거한다.
- **Rationale:** 문장 밀도를 높이고 사람다운 편집 품질을 만든다.
- **Verification:** 중복 문장과 일반론을 편집 검토한다.
- **Exceptions:** 브랜드의 고정 인사말은 허용한다.

### CORE-047 - 용어 일관성

- **Priority:** High
- **Statement:** 동일 문서와 프로젝트에서 같은 개념은 승인된 동일 용어로 표현한다.
- **Rationale:** 용어 변화는 독자 혼란과 검색 오류를 만든다.
- **Verification:** Glossary와 본문 용어를 대조한다.
- **Exceptions:** 직접 인용에서는 원문 용어를 병기할 수 있다.

### CORE-048 - 초보자 설명 원칙

- **Priority:** Medium
- **Statement:** 대상이 초보자인 경우 용어를 처음 사용할 때 쉬운 정의와 맥락을 제공한다.
- **Rationale:** 전문용어는 정보 접근 장벽이 된다.
- **Verification:** 대상 독자와 Glossary를 확인한다.
- **Exceptions:** 전문가용 콘텐츠는 생략 가능하다.

### CORE-049 - 실행 가능성

- **Priority:** High
- **Statement:** 실무형 콘텐츠의 권고와 Action Item은 구체적이고 수행 가능한 형태로 작성한다.
- **Rationale:** 모호한 조언은 독자의 행동으로 이어지지 않는다.
- **Verification:** 주체, 행동, 입력, 결과가 명확한지 확인한다.
- **Exceptions:** 전망 중심 콘텐츠에는 관찰 항목으로 대체할 수 있다.

### CORE-050 - 결론 정합성

- **Priority:** High
- **Statement:** 제목, 요약, 본문, Editor’s Insight 또는 결론은 서로 모순되지 않아야 한다.
- **Rationale:** 섹션별로 따로 작성할 때 메시지가 흔들리는 것을 방지한다.
- **Verification:** 핵심 주장과 권고를 교차 비교한다.
- **Exceptions:** 의도적으로 상반된 시나리오를 제시하면 조건을 명시한다.

## 17.F MASTER와 디자인 (CORE-051 ~ CORE-060)

### CORE-051 - MASTER 고정

- **Priority:** Critical
- **Statement:** 승인된 MASTER의 구조, 스타일, 클래스, 색상, 여백, 구성 요소를 사용자의 디자인 변경 승인 없이 수정하지 않는다.
- **Rationale:** 일일 콘텐츠마다 포맷이 흔들리는 문제를 차단한다.
- **Verification:** MASTER와 결과물의 구조 및 스타일 diff를 수행한다.
- **Exceptions:** 버그 수정은 버전 정책과 승인 절차를 따른다.

### CORE-052 - 내용만 교체

- **Priority:** Critical
- **Statement:** 정기 산출물 생성은 MASTER를 새로 설계하는 작업이 아니라 승인된 슬롯에 당일 콘텐츠를 삽입하는 작업으로 수행한다.
- **Rationale:** 디자인 재생성을 원천적으로 방지한다.
- **Verification:** MASTER Map의 슬롯과 결과물을 대조한다.
- **Exceptions:** 기사 수 변화에 따른 승인된 반복 블록 증감은 허용한다.

### CORE-053 - 신규 스타일 금지

- **Priority:** High
- **Statement:** 필요성이 검증되고 승인되지 않은 새 CSS 클래스, Word 스타일, 카드, 표 디자인을 임의로 추가하지 않는다.
- **Rationale:** 작은 스타일 추가가 장기적으로 디자인 파편화를 만든다.
- **Verification:** 스타일 목록을 MASTER와 비교한다.
- **Exceptions:** MASTER에 표현 수단이 전혀 없으면 변경 제안을 별도로 작성한다.

### CORE-054 - 구조-수량 정합

- **Priority:** Critical
- **Statement:** 목차, 요약, 반복 섹션, 내부 링크 등 서로 대응하는 요소의 수와 순서를 일치시킨다.
- **Rationale:** Deep Dive 수 변화 시 가장 자주 발생하는 결함을 방지한다.
- **Verification:** DOM, 문서 헤딩, 링크 대상을 자동 또는 수동 검사한다.
- **Exceptions:** 비표시 조건부 섹션은 목차에서 함께 제거한다.

### CORE-055 - 반응형 보존

- **Priority:** High
- **Statement:** HTML MASTER의 모바일 규칙과 안전 영역을 유지해야 한다.
- **Rationale:** 데스크톱에서 정상인 결과가 모바일에서 잘리는 것을 방지한다.
- **Verification:** 지정 뷰포트에서 렌더링을 검사한다.
- **Exceptions:** 프로젝트가 모바일을 지원하지 않으면 적용 범위를 명시한다.

### CORE-056 - Word 구조 보존

- **Priority:** High
- **Statement:** DOCX MASTER의 페이지 설정, 제목 계층, 표, 강조 박스, 헤더·푸터, 스타일 체계를 유지해야 한다.
- **Rationale:** Word 재생성 과정에서 포맷이 점차 변하는 것을 방지한다.
- **Verification:** 렌더링 페이지와 MASTER를 비교한다.
- **Exceptions:** 내용 길이에 따른 자연스러운 페이지 증가는 허용한다.

### CORE-057 - 채널 간 내용 일치

- **Priority:** Critical
- **Statement:** 같은 발행물의 HTML, DOCX, PDF 등 채널별 산출물은 핵심 사실, 수치, 순서, 결론, 출처가 일치해야 한다.
- **Rationale:** 서로 다른 원고를 병렬 작성할 때 생기는 불일치를 방지한다.
- **Verification:** 정합성 체크리스트를 수행한다.
- **Exceptions:** 채널에 맞춘 축약은 가능하나 새로운 사실이나 반대 결론을 추가할 수 없다.

### CORE-058 - 플레이스홀더 제거

- **Priority:** Critical
- **Statement:** 최종 산출물에는 템플릿 토큰, 샘플 날짜, TODO, 내부 메모, 빈 링크를 남기지 않는다.
- **Rationale:** 미완성 상태가 발행되는 것을 막는다.
- **Verification:** 정규식으로 플레이스홀더 패턴을 검색한다.
- **Exceptions:** 의도적인 예제 코드의 플레이스홀더는 예제임을 표시한다.

### CORE-059 - 접근성 기본 준수

- **Priority:** Medium
- **Statement:** 제목 계층, 표 헤더, 링크 텍스트, 이미지 대체 설명 등 기본 접근성을 고려한다.
- **Rationale:** 다양한 환경과 독자가 콘텐츠를 이용할 수 있게 한다.
- **Verification:** 접근성 감사 도구와 수동 검토를 수행한다.
- **Exceptions:** 플랫폼이 지원하지 않는 항목은 가능한 대안을 적용한다.

### CORE-060 - 디자인 변경 버전화

- **Priority:** Critical
- **Statement:** 구조 또는 디자인 변경은 새 MASTER 버전으로 복제하고 기존 MASTER를 덮어쓰지 않는다.
- **Rationale:** 롤백과 비교 가능성을 보장한다.
- **Verification:** 파일명, 버전, Changelog를 확인한다.
- **Exceptions:** 의미 없는 파일 메타데이터 수정은 동일 버전에서 처리할 수 있다.

## 17.G 파일과 산출물 전달 (CORE-061 ~ CORE-070)

### CORE-061 - 실제 파일 생성

- **Priority:** Critical
- **Statement:** 파일 산출물 요청은 파일 경로에 실재하고 크기가 0보다 큰 파일을 생성해야 충족된다.
- **Rationale:** 텍스트로 생성했다고 말하는 것과 실제 파일 전달은 다르다.
- **Verification:** 파일 시스템 stat과 해시를 확인한다.
- **Exceptions:** 파일 형식을 지원하지 못하면 즉시 알리고 가능한 대체물을 제시한다.

### CORE-062 - 렌더링 검수

- **Priority:** Critical
- **Statement:** DOCX, PDF, 슬라이드처럼 레이아웃이 중요한 파일은 렌더링한 화면을 검수한 뒤 전달한다.
- **Rationale:** 텍스트 구조만으로는 잘림, 겹침, 글꼴 오류를 알 수 없다.
- **Verification:** 모든 페이지 또는 슬라이드 이미지를 검토한다.
- **Exceptions:** 순수 텍스트 파일은 구조 검증으로 대체한다.

### CORE-063 - 파일명 규칙

- **Priority:** High
- **Statement:** 파일명은 프로젝트, 날짜 또는 문서 ID, 버전, 형식을 식별할 수 있어야 한다.
- **Rationale:** 명확한 파일명은 자동화와 이력 관리를 돕는다.
- **Verification:** Naming Convention을 검사한다.
- **Exceptions:** 채널의 파일명 제한이 있으면 축약 규칙을 따른다.

### CORE-064 - 다운로드 경로 확인

- **Priority:** Critical
- **Statement:** 사용자에게 제공하는 다운로드 링크는 실제 런타임 경로와 정확히 일치해야 한다.
- **Rationale:** 실행 환경에서 접근할 수 없는 경로나 유효하지 않은 파일 참조 제공을 방지한다.
- **Verification:** 링크 전에 파일 존재를 확인한다.
- **Exceptions:** 외부 서비스가 관리하는 파일은 해당 서비스가 검증한 파일 참조 방식을 사용한다.

### CORE-065 - 요청 산출물 완결

- **Priority:** Critical
- **Statement:** 요청된 모든 파일 형식과 부속 결과를 제공하거나 누락 사유를 명시해야 한다.
- **Rationale:** 일부 파일만 만들어 놓고 전체 완료로 보고하는 것을 막는다.
- **Verification:** 요청 목록과 전달 목록을 대조한다.
- **Exceptions:** 사용자가 범위를 축소한 경우 최신 요청을 따른다.

### CORE-066 - 원본과 파생본 구분

- **Priority:** High
- **Statement:** Markdown 원본, DOCX 렌더링, PDF 배포본, HTML 발행본의 역할과 생성 관계를 명시해야 한다.
- **Rationale:** 어느 파일을 수정해야 하는지 혼동하지 않게 한다.
- **Verification:** 패키지 README와 파일 메타데이터를 확인한다.
- **Exceptions:** 한 형식만 사용하는 프로젝트는 생략 가능하다.

### CORE-067 - 중간 산출물 비노출

- **Priority:** Medium
- **Statement:** 사용자가 요청하지 않은 렌더링 이미지, 로그, 임시 파일은 최종 전달물에 포함하지 않는다.
- **Rationale:** 최종 패키지의 혼란과 불필요한 용량을 줄인다.
- **Verification:** Deliverables 폴더의 파일을 검토한다.
- **Exceptions:** 진단 요청이나 검토 과정에서는 별도 폴더로 제공할 수 있다.

### CORE-068 - 무결성 기록

- **Priority:** Medium
- **Statement:** 정식 릴리스 패키지는 파일 목록과 해시 또는 동등한 무결성 정보를 포함하는 것을 권장한다.
- **Rationale:** 전달 후 파일 변조와 누락을 확인할 수 있다.
- **Verification:** Manifest의 해시를 재계산한다.
- **Exceptions:** 소규모 일일 산출물에서는 생략할 수 있다.

### CORE-069 - 메타데이터 관리

- **Priority:** Medium
- **Statement:** 배포 파일에서 불필요한 개인정보, 임시 작성자, 내부 경로 메타데이터를 제거해야 한다.
- **Rationale:** 개인정보와 내부 환경 노출을 줄인다.
- **Verification:** 문서 속성과 PDF 메타데이터를 감사한다.
- **Exceptions:** Owner 등 의도적으로 표시한 정보는 유지한다.

### CORE-070 - 패키지 설명 포함

- **Priority:** Medium
- **Statement:** 여러 파일을 묶어 전달할 때 README 또는 간결한 적용 안내를 포함해야 한다.
- **Rationale:** 사용자가 각 파일의 용도를 바로 이해하게 한다.
- **Verification:** 패키지 루트의 안내 문서를 확인한다.
- **Exceptions:** 파일이 하나뿐이면 생략할 수 있다.

## 17.H 품질 게이트와 릴리스 (CORE-071 ~ CORE-080)

### CORE-071 - 완료 정의

- **Priority:** Critical
- **Statement:** 완료는 콘텐츠 작성, 파일 생성, 품질 검수, 링크 확인, 전달이 모두 끝난 상태를 의미한다.
- **Rationale:** 작성만 끝난 상태를 완료로 오인하지 않는다.
- **Verification:** Release Checklist의 모든 필수 항목을 확인한다.
- **Exceptions:** 사용자가 초안만 요청한 경우 완료 정의를 초안 범위로 조정한다.

### CORE-072 - 필수 게이트 통과

- **Priority:** Critical
- **Statement:** Critical 품질 게이트가 하나라도 실패하면 결과를 정식 완료 또는 LOCKED로 표시하지 않는다.
- **Rationale:** 치명적 오류가 있는 결과의 발행을 차단한다.
- **Verification:** QA 결과에서 Critical 실패 수를 확인한다.
- **Exceptions:** 긴급 임시본은 명확한 경고와 만료 조건을 붙여 별도 상태로 제공할 수 있다.

### CORE-073 - 독립 검수 단계

- **Priority:** High
- **Statement:** 생성 직후 동일한 내용을 그대로 신뢰하지 말고 별도의 검수 단계에서 누락과 불일치를 확인한다.
- **Rationale:** 생성 관성으로 인한 자기 검증 실패를 줄인다.
- **Verification:** 작성 로그와 QA 로그의 단계 분리를 확인한다.
- **Exceptions:** 아주 짧은 단순 파일도 최소한 존재와 내용 검사를 수행한다.

### CORE-074 - Critical-High-Medium 분류

- **Priority:** Medium
- **Statement:** 검수 항목은 실패 영향에 따라 Critical, High, Medium으로 분류한다.
- **Rationale:** 오류 대응 우선순위를 일관되게 정한다.
- **Verification:** QA Matrix의 심각도 필드를 확인한다.
- **Exceptions:** 프로젝트별로 추가 등급을 사용할 수 있다.

### CORE-075 - 회귀 검수

- **Priority:** High
- **Statement:** MASTER 또는 규칙 변경 후에는 이전에 정상 동작했던 핵심 항목의 회귀 여부를 검사한다.
- **Rationale:** 한 문제를 고치며 다른 형식을 깨뜨리는 것을 방지한다.
- **Verification:** 이전 승인 샘플과 렌더링 또는 구조 diff를 수행한다.
- **Exceptions:** 초기 버전에는 기준 샘플을 먼저 생성한다.

### CORE-076 - 정합성 검사

- **Priority:** Critical
- **Statement:** 다중 형식 산출물의 제목, 날짜, 핵심 수치, 섹션 순서, 출처, 결론을 교차 검증한다.
- **Rationale:** 채널 간 사실 불일치는 심각한 신뢰 문제다.
- **Verification:** 필드별 비교표를 생성하거나 수동 확인한다.
- **Exceptions:** 의도적 축약 항목은 Mapping 문서에 표시한다.

### CORE-077 - 링크 검사

- **Priority:** Critical
- **Statement:** 최종 발행 전 모든 외부 링크와 내부 앵커의 존재, 대상, 접근성을 검사한다.
- **Rationale:** 깨진 출처와 목차 링크를 차단한다.
- **Verification:** 링크 검증 도구와 DOM 검사를 사용한다.
- **Exceptions:** 일시적 서버 오류는 재확인 후 상태를 표시한다.

### CORE-078 - 빈값 검사

- **Priority:** Critical
- **Statement:** 필수 필드, 표 셀, 제목, 출처, 파일 링크에 의도하지 않은 빈값이 없어야 한다.
- **Rationale:** 템플릿이 미완성 상태로 전달되는 것을 막는다.
- **Verification:** 스키마와 결과의 필수 필드를 검사한다.
- **Exceptions:** 조건부 필드는 명시적 미표시 규칙을 따른다.

### CORE-079 - 사용자 검토 상태

- **Priority:** High
- **Statement:** 사용자 승인 전 문서는 REVIEW 또는 APPROVED 상태이며 실제 운영 검증 전 LOCKED로 표시하지 않는다.
- **Rationale:** 파일 생성과 운영 검증을 구분한다.
- **Verification:** Status와 승인 기록을 확인한다.
- **Exceptions:** 사용자가 사전 승인한 자동 갱신 문서는 정의된 절차에 따른다.

### CORE-080 - 릴리스 기록

- **Priority:** High
- **Statement:** 정식 릴리스에는 버전, 날짜, 변경 요약, 검수 결과, 알려진 제한을 기록해야 한다.
- **Rationale:** 운영자가 나중에 해당 버전의 상태를 이해할 수 있다.
- **Verification:** Release Note와 QA Summary를 확인한다.
- **Exceptions:** 일일 Output은 간소화된 로그를 사용할 수 있다.

## 17.I 자동화와 실패 복구 (CORE-081 ~ CORE-090)

### CORE-081 - 예약은 실행 명령

- **Priority:** High
- **Statement:** 예약 작업은 새로운 운영 규칙을 정의하지 않고 승인된 CORE, Project Module, MASTER를 참조해 실행해야 한다.
- **Rationale:** 예약마다 규칙이 복제되는 것을 막는다.
- **Verification:** 예약 프롬프트와 참조 문서를 검토한다.
- **Exceptions:** 참조 접근이 제한되면 압축 Core를 포함할 수 있다.

### CORE-082 - 중복 예약 방지

- **Priority:** Critical
- **Statement:** 같은 프로젝트와 시간에 동일 목적의 활성 예약이 중복되지 않도록 확인해야 한다.
- **Rationale:** 중복 산출물과 알림을 방지한다.
- **Verification:** 활성 예약 목록과 일정 키를 비교한다.
- **Exceptions:** 의도적인 A/B 실행은 실험 ID를 사용한다.

### CORE-083 - 시간대 명시

- **Priority:** High
- **Statement:** 시간 기반 자동화는 기준 시간대와 휴일 또는 예외 일정을 명시해야 한다.
- **Rationale:** 서버 시간과 사용자 현지 시간의 차이로 오작동하는 것을 막는다.
- **Verification:** 스케줄의 TZID와 프로젝트 설정을 확인한다.
- **Exceptions:** 상대 시간 알림은 실행 시스템 규칙을 따른다.

### CORE-084 - 멱등성

- **Priority:** High
- **Statement:** 재실행 가능한 작업은 동일 실행 키에서 중복 파일이나 중복 발행을 만들지 않도록 설계한다.
- **Rationale:** 실패 후 재시도 시 결과가 중복되는 것을 방지한다.
- **Verification:** 실행 ID와 파일명, 발행 상태를 확인한다.
- **Exceptions:** 의도적 재발행은 새 revision을 부여한다.

### CORE-085 - 실패 상태 보존

- **Priority:** Critical
- **Statement:** 자동화 실패 시 마지막 성공 상태를 훼손하거나 MASTER를 변경하지 않는다.
- **Rationale:** 오류가 정상 운영 기준까지 오염시키는 것을 방지한다.
- **Verification:** 실패 전후의 MASTER 해시와 출력 경로를 비교한다.
- **Exceptions:** 승인된 복구 절차가 있는 경우에만 변경한다.

### CORE-086 - 재시도 제한

- **Priority:** High
- **Statement:** 자동 재시도는 횟수, 간격, 중단 조건을 명시해야 한다.
- **Rationale:** 무한 재시도와 과도한 비용을 방지한다.
- **Verification:** 스케줄 또는 Runbook 설정을 확인한다.
- **Exceptions:** 사람의 승인으로 추가 재시도를 수행할 수 있다.

### CORE-087 - 부분 실패 분리

- **Priority:** High
- **Statement:** 다중 산출물 중 일부가 실패하면 성공 파일과 실패 항목을 분리해 보고하고 전체 성공으로 처리하지 않는다.
- **Rationale:** Word 성공, HTML 실패 같은 상황을 정확히 다룬다.
- **Verification:** 산출물별 상태를 확인한다.
- **Exceptions:** 사용자가 성공 파일만 우선 전달받기를 요청할 수 있다.

### CORE-088 - 관찰 가능성

- **Priority:** Medium
- **Statement:** 자동화는 실행 시각, 입력, 사용 버전, 출력, QA 결과, 오류를 추적 가능하게 기록해야 한다.
- **Rationale:** 문제 발생 시 원인을 재현할 수 있다.
- **Verification:** Execution Log 필드를 확인한다.
- **Exceptions:** 개인정보와 비밀 값은 로그에 남기지 않는다.

### CORE-089 - 알림 정확성

- **Priority:** High
- **Statement:** 알림은 실제 성공, 부분 실패, 실패 상태를 구분해 표현해야 한다.
- **Rationale:** 사용자가 잘못된 완료 알림을 받지 않게 한다.
- **Verification:** 알림 문구와 실행 상태를 대조한다.
- **Exceptions:** 조용한 실패 정책은 사용자가 승인한 경우에만 사용한다.

### CORE-090 - 수동 복구 가능성

- **Priority:** High
- **Statement:** 자동화는 사람이 이해하고 재실행할 수 있는 Runbook과 원본 입력을 유지해야 한다.
- **Rationale:** 자동화 도구가 바뀌어도 운영을 지속할 수 있다.
- **Verification:** Runbook 존재와 최근 검증일을 확인한다.
- **Exceptions:** 완전히 관리형인 단순 예약도 최소한의 비활성화·재생성 절차를 기록한다.

## 17.J 버전, 보안, 준수 (CORE-091 ~ CORE-100)

### CORE-091 - 시맨틱 버전

- **Priority:** High
- **Statement:** JCOS 문서와 MASTER는 의미 변화에 따라 Major.Minor.Patch 버전을 사용한다.
- **Rationale:** 변경 규모와 호환성을 파일명만으로 이해할 수 있게 한다.
- **Verification:** 버전 증가와 변경 내용을 대조한다.
- **Exceptions:** 일일 Output 번호는 프로젝트별 별도 규칙을 사용할 수 있다.

### CORE-092 - Major 변경

- **Priority:** Critical
- **Statement:** 계층, 필수 구조, 호환되지 않는 규칙 또는 MASTER 디자인 변경은 Major 버전을 증가시킨다.
- **Rationale:** 호환성 파괴를 명확히 표시한다.
- **Verification:** 이전 버전과 구조 diff를 검토한다.
- **Exceptions:** 없음.

### CORE-093 - Minor 변경

- **Priority:** High
- **Statement:** 하위 호환되는 기능, 선택 규칙, 새 프로젝트 모듈 추가는 Minor 버전을 증가시킨다.
- **Rationale:** 기존 운영을 유지하면서 기능이 늘어났음을 표시한다.
- **Verification:** 호환성 테스트를 수행한다.
- **Exceptions:** 프로젝트 자체 버전 정책이 더 엄격할 수 있다.

### CORE-094 - Patch 변경

- **Priority:** Medium
- **Statement:** 의미를 바꾸지 않는 오탈자, 링크 수정, 경미한 렌더링 버그는 Patch 버전을 증가시킨다.
- **Rationale:** 작은 수정도 추적 가능하게 한다.
- **Verification:** 변경 diff를 확인한다.
- **Exceptions:** 내부 빌드 메타데이터만 바뀌면 버전을 유지할 수 있다.

### CORE-095 - 승인 기록

- **Priority:** Critical
- **Statement:** APPROVED와 LOCKED 전환에는 사용자 또는 지정 승인자의 명시적 승인 기록이 있어야 한다.
- **Rationale:** 암묵적 동의로 기준 문서가 고정되는 것을 막는다.
- **Verification:** 승인 날짜와 메시지 또는 변경 요청을 기록한다.
- **Exceptions:** 자동 승인 정책은 별도 거버넌스 문서에서 정의해야 한다.

### CORE-096 - 롤백 가능성

- **Priority:** High
- **Statement:** 정식 변경은 이전 LOCKED 버전으로 롤백할 수 있도록 파일과 변경 이력을 보존해야 한다.
- **Rationale:** 새 버전 결함 발생 시 운영 중단을 줄인다.
- **Verification:** Archive와 복원 테스트를 확인한다.
- **Exceptions:** 법적 또는 보안상 삭제가 필요한 파일은 예외다.

### CORE-097 - 개인정보 최소화

- **Priority:** Critical
- **Statement:** 콘텐츠, 프롬프트, 로그, 파일에는 목적에 필요하지 않은 개인정보와 민감정보를 포함하지 않는다.
- **Rationale:** 개인정보 노출과 오용 위험을 줄인다.
- **Verification:** 메타데이터 및 본문 감사 도구를 실행한다.
- **Exceptions:** 사용자가 명시적으로 필요성을 승인하고 적법한 경우에만 최소 범위로 사용한다.

### CORE-098 - 비밀정보 보호

- **Priority:** Critical
- **Statement:** 비밀번호, API 키, 토큰, 내부 접속정보를 산출물이나 로그에 노출하지 않는다.
- **Rationale:** 계정 침해와 시스템 위험을 방지한다.
- **Verification:** Secret pattern 스캔을 수행한다.
- **Exceptions:** 마스킹된 예시는 허용한다.

### CORE-099 - 저작권·인용 준수

- **Priority:** Critical
- **Statement:** 외부 자료는 필요한 범위에서 요약하고 인용 한도와 출처 표시를 준수한다.
- **Rationale:** 법적 위험과 원저작물 대체를 방지한다.
- **Verification:** 인용 길이와 출처를 검토한다.
- **Exceptions:** 퍼블릭 도메인 또는 사용 허가가 명확한 자료는 해당 조건을 따른다.

### CORE-100 - 정기 준수 감사

- **Priority:** High
- **Statement:** JCOS v2.0 정식 운영 후에는 핵심 프로젝트를 대상으로 규칙 준수와 문서 유효성을 정기 검토해야 한다.
- **Rationale:** 규칙이 현실과 달라지거나 사용되지 않는 상태를 방지한다.
- **Verification:** Audit Report와 개선 항목을 확인한다.
- **Exceptions:** 초기 구축 단계에서는 각 Phase 종료 검토로 대체한다.

# 18. 표준 실행 수명주기

모든 반복 콘텐츠 작업은 아래 수명주기를 기본으로 한다.

1. **Resolve** - 현재 요청, 적용 프로젝트, 활성 CORE, Project Module, MASTER 버전을 확정한다.
2. **Research** - 필요한 원천을 수집하고 최신성·출처 정합성을 검증한다.
3. **Draft** - 단일 확정 원고를 만든다.
4. **Render** - MASTER에 원고를 삽입해 필요한 형식의 파일을 생성한다.
5. **Verify** - 사실, 링크, 구조, 렌더링, 형식 간 정합성을 검사한다.
6. **Deliver** - 실제 파일과 정확한 다운로드 경로를 제공한다.
7. **Record** - 버전, 사용 기준, QA 결과, 실패와 변경을 기록한다.

Critical 게이트가 실패하면 Deliver 단계에서 완료를 선언하지 않고 실패 또는 부분 완료 상태로 전환한다.

# 19. 준수 체크리스트

## 19.1 실행 전
- [ ] 적용 프로젝트와 요청 범위가 명확하다.
- [ ] 활성 CORE, Project Module, MASTER 버전을 확인했다.
- [ ] 구버전 또는 과거 Output을 MASTER로 오인하지 않았다.
- [ ] 신규 아이디어가 현재 2.0 범위에 유입되지 않았다.

## 19.2 작성·생성
- [ ] 중요한 사실과 수치에 근거가 있다.
- [ ] 사실과 해석이 구분된다.
- [ ] MASTER 구조와 스타일을 변경하지 않았다.
- [ ] 필수 슬롯과 반복 블록 수가 일치한다.
- [ ] 플레이스홀더와 내부 메모가 없다.

## 19.3 검수·전달
- [ ] 모든 요청 파일이 실제로 생성되었다.
- [ ] 레이아웃 파일의 모든 페이지를 렌더링 검수했다.
- [ ] 링크와 내부 앵커가 유효하다.
- [ ] 다중 형식의 핵심 내용이 일치한다.
- [ ] 다운로드 경로가 실제 파일과 일치한다.
- [ ] Critical 실패가 0건이다.

## 19.4 변경·운영
- [ ] 변경이 버전 정책에 맞게 기록되었다.
- [ ] 승인 전 REVIEW, 운영 검증 전 LOCKED 미사용 원칙을 지켰다.
- [ ] 이전 LOCKED 버전을 보존했다.

# 20. 부록

## 20.1 AI용 압축 Core Instructions

다음 블록은 프로젝트 지침이나 독립 실행 환경에서 사용할 수 있는 압축본이다. 상세 규칙과 충돌하면 상세 규칙이 우선한다.

```text
JCOS CORE v2.0을 따른다.
1. 현재 요청을 정확히 수행하고 요청하지 않은 재설계는 하지 않는다.
2. 승인된 MASTER를 유일한 디자인 기준으로 사용하고 내용만 교체한다.
3. 중요한 사실은 실제 근거와 최신 상태를 확인한다.
4. 사실, 해석, 전망, 권고를 구분하고 과장과 상투어를 제거한다.
5. 요청된 모든 파일을 실제 생성하고 레이아웃을 렌더링 검수한다.
6. 링크, 목차, 섹션 수, 형식 간 핵심 내용의 정합성을 검사한다.
7. 확인하지 못한 사항과 실패를 숨기지 않는다.
8. Critical 품질 게이트가 실패하면 완료라고 말하지 않는다.
9. 사용자 승인 없이 MASTER나 LOCKED 문서를 변경하지 않는다.
10. 신규 아이디어는 현재 버전에 넣지 않고 다음 버전 Backlog로 분리한다.
```

## 20.2 규칙 우선순위 요약

1. 필수 안전·법률·플랫폼 규칙
2. 사용자의 현재 명시적 요청
3. LOCKED Project Module
4. LOCKED JCOS CORE
5. LOCKED MASTER
6. Execution Prompt
7. 참고 문서와 과거 Output

단, 콘텐츠 수정 요청은 디자인 변경 승인으로 간주하지 않는다.

## 20.3 알려진 제한

- COR-001은 공통 최상위 규칙을 정의하며 세부 조사·글쓰기·파일 정책은 후속 CORE 문서에서 확장한다.
- 상태는 LOCKED이며 변경은 COR-007에 따른 새 버전·QA·승인 절차의 대상이다.
- v2.0 완성 전 새 기능 제안은 2.1 Backlog로 분리한다.

## 20.4 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-07-30 | LOCKED | COR-001 전체 본문, 100개 규칙, 실행 수명주기와 준수 체크리스트 작성; AI·벤더 범용성 QA와 사용자 승인 후 기준본 확정 |
