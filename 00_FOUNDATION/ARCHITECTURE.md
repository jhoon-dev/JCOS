# JCOS Architecture v2.0

Version: 2.0  
Status: REVIEW

---

## 1. 설계 철학

JCOS는 문서 모음이 아니라 계층형 운영 시스템이다.

공통 규칙을 한 곳에서 관리하고, 각 프로젝트는 필요한 부분만 확장한다. 동일한 규칙을 여러 프로젝트에 복사하지 않는다.

---

## 2. 다섯 개의 실행 계층

### L1. CORE

모든 프로젝트에 적용되는 공통 규칙이다.

예:

- 사실성
- 출처 검증
- MASTER 보호
- 파일 전달
- 품질 게이트
- 버전 관리
- 실패 보고

### L2. PROJECT MODULE

특정 프로젝트의 목적과 특성을 정의한다.

예:

- 뉴스 프로젝트의 선정 기준
- 교육 프로젝트의 초보자 설명 원칙
- 데이터 프로젝트의 수치 검증 기준

### L3. MASTER

승인된 결과물 디자인과 구조다.

예:

- HTML 구조와 CSS
- Word 제목 계층과 표 스타일
- 썸네일 안전 영역과 비율

### L4. EXECUTION

예약 작업이나 사용자 요청에서 실행할 구체적인 지시다.

Execution Prompt는 공통 규칙을 다시 길게 복사하지 않는다. 참조 대상과 오늘 수행할 작업만 명시한다.

### L5. OUTPUT

실제 날짜별 결과물이다.

일일 결과물은 MASTER가 아니며 다음 실행의 디자인 기준으로 자동 승격되지 않는다.

## 2.1 상세 기준본과 AI Runtime

CORE, PROJECT MODULE, MASTER와 EXECUTION의 상세 문서는 사람이 작성·검토·승인하는 규범적 기준본이다.

AI Runtime은 별도의 여섯 번째 규칙 계층이 아니라, 승인된 상세 기준본에서 AI 실행에 필요한 지침만 추출·통합한 배포 표현이다. Runtime은 `06_LIBRARY/PROMPTS`에 두며 원본 문서 ID, 버전, 상태, 경로와 해시를 Manifest로 추적한다.

Runtime과 상세 기준본이 충돌하거나 Runtime에 필요한 판단이 없으면 상세 기준본이 우선한다. Project Runtime은 해당 Project Module이 승인되기 전에는 운영용으로 생성하지 않는다.

---

## 3. 책임 분리

| 질문 | 담당 문서 |
|---|---|
| 모든 콘텐츠에 공통으로 지켜야 할 것은? | CORE |
| 이 프로젝트만의 규칙은? | PROJECT MODULE |
| 디자인과 문서 구조는? | MASTER |
| 오늘 무엇을 실행할 것인가? | EXECUTION |
| 결과가 기준을 통과했는가? | QA |
| 무엇이 언제 바뀌었는가? | CHANGELOG |

---

## 4. 충돌 처리

규칙 충돌 시 기본 우선순위:

1. 안전·법률·플랫폼 필수 규칙
2. 사용자의 현재 명시적 요청
3. LOCKED PROJECT 규칙
4. LOCKED CORE 규칙
5. LOCKED MASTER
6. 실행 프롬프트
7. 참고 문서와 과거 산출물

단, 사용자의 단순 콘텐츠 수정 요청을 디자인 변경 승인으로 해석하지 않는다.

---

## 5. 참조 방식

각 프로젝트 모듈은 다음을 명시한다.

```yaml
project:
  name: Example Project
  inherits:
    - JCOS CORE v2.0
  masters:
    html: MASTER_EXAMPLE_v1.0.html
    docx: MASTER_EXAMPLE_v1.0.docx
  qa:
    - CORE Quality Gate
    - Project Quality Gate
```

---

## 6. 변경 전파

CORE 변경은 모든 프로젝트에 영향을 줄 수 있다.

따라서 CORE 변경은 다음 절차를 따른다.

1. 변경 제안
2. 영향 프로젝트 식별
3. 호환성 검토
4. 사용자 승인
5. 버전 증가
6. 프로젝트별 적용 확인
7. CHANGELOG 기록

PROJECT MODULE 변경은 해당 프로젝트에만 적용한다.

MASTER 변경은 해당 MASTER를 사용하는 결과물 디자인에만 적용한다.

---

## 7. 금지되는 구조

- 프로젝트마다 CORE 규칙을 복사하여 별도로 수정
- 일일 HTML을 MASTER로 자동 간주
- 하나의 파일에 조사·디자인·예약·QA 규칙을 모두 혼합
- 과거 산출물을 현재 MASTER보다 우선
- 실행 프롬프트에 수천 자의 중복 규칙 삽입
- 상세 기준본과 연결되지 않은 독립 AI 프롬프트를 운영 기준으로 사용
- Runtime 파일에서 원본에 없는 규칙을 추가하거나 의미를 변경
