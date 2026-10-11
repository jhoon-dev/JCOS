# JCOS Rule ID System v2.0.1-rc.1

| 항목 | 값 |
|---|---|
| Document ID | FND-004 |
| Version | 2.0.1-rc.1 |
| Status | REVIEW |
| Owner | JCOS Maintainers |

---

## 1. 목적

규칙 ID는 긴 문장을 반복하지 않고 규칙을 정확히 참조하고 변경 이력을 관리하기 위해 사용한다.

---

## 2. 형식

```text
[영역]-[세 자리 번호]
```

예:

```text
CORE-001
SRC-004
HTML-012
EXM-021
QA-006
```

---

## 3. 영역 코드

| 코드 | 영역 |
|---|---|
| CORE | 공통 운영 원칙 |
| WRT | 글쓰기 |
| RSH | 조사 |
| SRC | 출처 |
| QA | 품질 검수 |
| FILE | 파일 전달 |
| VER | 버전 관리 |
| DEC | 의사결정 |
| HTML | HTML |
| DOCX | Word |
| CSS | CSS |
| CMP | 구성요소 |
| IMG | 이미지 |
| THM | 썸네일 |
| BRD | 브랜드 |
| SEO | 검색·제목·태그 |
| AUT | 자동화 |
| EXM | Example Project |
| EDU | Education Project |
| DAT | Data Project |

---

## 4. 규칙 작성 형식

```yaml
id: CORE-001
title: MASTER 우선
status: LOCKED
statement: 승인된 MASTER를 현재 프로젝트의 유일한 디자인 기준으로 사용한다.
applies_to:
  - all_projects
exceptions:
  - 사용자가 디자인 변경을 명시적으로 승인한 경우
verification:
  - 결과물 구조와 MASTER 비교
owner: project_owner
version: 2.0
```

---

## 5. 규칙 작성 원칙

- 하나의 ID에는 하나의 판단 가능한 규칙만 둔다.
- “가능하면”, “적절히”처럼 검증하기 어려운 표현을 피한다.
- 적용 범위와 예외를 함께 기록한다.
- 검수 가능한 규칙에는 verification을 둔다.
- 폐기한 ID를 다른 규칙에 재사용하지 않는다.
- 문구 수정만으로 의미가 달라지지 않으면 같은 ID를 유지한다.
- 의미나 적용 범위가 크게 달라지면 새 ID를 만든다.

---

## 6. 상태

| 상태 | 의미 |
|---|---|
| DRAFT | 초안 |
| REVIEW | 검토 중 |
| APPROVED | 승인 |
| LOCKED | 운영 기준 |
| DEPRECATED | 대체됨 |
| ARCHIVED | 이력 보관 |

---

## 7. 변경 예시

기존:

```text
CORE-001: MASTER를 변경하지 않는다.
```

변경 제안:

```text
CORE-001: 사용자 승인 없이 MASTER를 변경하지 않는다.
```

의미가 명확해지는 경미한 변경이면 동일 ID와 부 버전을 유지할 수 있다.

MASTER의 정의나 적용 범위 자체가 바뀌면 새로운 규칙 ID 또는 주 버전을 사용한다.

## 8. 공개 문서 ID와 규칙 ID

FND·COR·DSG·CNT·AUT 문서 ID는 파일과 책임 영역을 식별합니다. CORE·WRT·RSH 등 규칙 ID는 문서 내부 판단 항목을 식별합니다. 문서 ID와 규칙 ID를 혼용하지 않습니다. FND-001~006의 공개 경로는 DOCUMENT_REGISTER와 document_registry.json에서 확인합니다.

동일 규칙의 과거·후보 버전은 같은 규칙 ID를 유지할 수 있습니다. 고유성 검사는 선택한 활성 기준본 집합 안에서 수행합니다.
