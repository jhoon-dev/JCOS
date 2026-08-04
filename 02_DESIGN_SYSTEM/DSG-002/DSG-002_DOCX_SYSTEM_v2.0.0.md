# JCOS v2.0.0 - DSG-002 DOCX SYSTEM

## Word 문서 디자인 원칙

| Field | Value |
|---|---|
| Document ID | DSG-002 |
| Title | DOCX SYSTEM |
| Korean Title | Word 문서 디자인 원칙 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS가 생성·관리하는 DOCX와 그 DOCX에서 내보낸 PDF |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / FULL_DOCUMENT |
| Depends On | FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 잠금된 참조 프로젝트 DOCX·PDF에서 실제 검증된 공통 문서 조판 원칙만 분리해 사용자 승인과 명시적 잠금 승인을 받은 `LOCKED` 기준본이다. 프로젝트별 페이지 수·색상·표 수·콘텐츠 구조를 공통 필수값으로 추가하지 않는다.

# 문서 목적

DSG-002는 JCOS DOCX 산출물이 프로젝트와 문서 유형이 달라도 편집 가능성, 읽기 흐름, 글꼴 안정성, 표와 상자의 안전한 배치, 페이지네이션과 PDF 변환 검수를 일관되게 유지하도록 공통 문서 디자인 계약을 정의한다.

DOCX는 사람용 상세 문서 또는 편집 가능한 Delivery다. 논리 콘텐츠와 프로젝트별 시각 표현은 승인된 Content Schema와 MASTER가 정하며, DSG-002는 이를 Word 문서로 구현할 때 지켜야 할 공통 하한선과 검증 기준만 제공한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. 페이지와 Section
5. 글꼴과 문자 체계
6. 제목과 정보 계층
7. 본문·목록·간격
8. 표
9. 상자·코드·이미지
10. 머리글·바닥글·페이지 번호
11. 페이지네이션과 밀도
12. 편집성·접근성·호환성
13. PDF 변환 계약
14. 데이터 가변성과 템플릿
15. 검증과 품질 게이트
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 DOCX System
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- DOCX의 페이지 크기·여백·Section·열과 방향 설정
- 문서 기본 글꼴, 문자 스타일, 제목 단계, 본문과 목록 리듬
- 표·강조 상자·코드 블록·이미지의 안전한 조판
- 머리글·바닥글·페이지 번호와 페이지 분할
- 편집 가능성, 접근성, 호환성과 DOCX 재개봉
- 같은 DOCX에서 내보낸 PDF의 페이지·정보·시각 연속성

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| 문서에 들어갈 사실·해석·필드·순서 | 승인 Content Schema와 Project MASTER |
| 프로젝트별 색상·로고·브랜드 표현 | DSG-007 BRAND SYSTEM과 Project MASTER |
| HTML 구조와 모바일 반응형 | DSG-001 HTML SYSTEM |
| CSS 토큰과 변경 동결 | DSG-003 CSS GOVERNANCE |
| 재사용 UI 구성요소의 세부 명세 | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·대체 텍스트 정책 | DSG-005 IMAGE SYSTEM |
| 게시·배포·수정·삭제 절차 | CNT-006 PUBLISHING SYSTEM |
| 자동 생성·내보내기·재시도 구현 | AUT 문서 |

## 1.3 금지되는 확장

- 참조 프로젝트의 A4·10~11페이지·파란 제목 체계를 모든 DOCX에 강제
- 특정 Word 버전, 운영체제, AI, 문서 생성 라이브러리를 유일한 실행 환경으로 지정
- 페이지 수를 맞추기 위해 글꼴을 과도하게 축소하거나 내용을 누락
- DOCX 규칙에서 프로젝트 콘텐츠 필드나 카드 수를 새로 정의

# 2. 계층과 권한

## 2.1 권한 순서

DOCX 구현은 다음 순서로 해석한다.

1. 안전·법률·접근성·파일 무결성 필수 제한
2. 사용자의 현재 명시적 요청
3. 승인된 Content Schema와 Project MASTER
4. DSG-002 DOCX SYSTEM
5. DSG-004 구성요소 계약과 DSG-007 브랜드 기준
6. Execution과 날짜별 입력
7. 참고 DOCX와 과거 Output

## 2.2 MASTER 우선

승인 MASTER가 페이지 크기, 여백, 글꼴, 색상, 제목 체계와 구성요소를 더 구체적으로 정하면 그 값을 따른다. 단, 잘림·겹침·편집 불가·접근성 저하·검증 불가 상태는 허용하지 않는다.

## 2.3 참고 구현의 역할

`PROJECT_REFERENCE_FIXTURE` v1.0.1은 Noto Sans KR 명시, 실제 데이터 기반 유동 밀도, 표 뒤 간격, 긴 제목 줄바꿈, 내용 밀착형 상자와 전 페이지 렌더 검수를 실제로 통과한 참조 구현이다. A4, 색상, 페이지 수와 프로젝트 전용 표 구조는 공통 규칙이 아니다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| DOCX Source | 편집 가능한 WordprocessingML 패키지 |
| Rendered PDF | 동일 DOCX에서 승인된 경로로 내보낸 고정 레이아웃 표현 |
| Style Contract | 제목·본문·목록·표 등 역할별 이름과 속성의 일관된 정의 |
| Direct Formatting | Style과 별개로 개별 문단·Run에 직접 적용한 서식 |
| Section | 페이지 크기·여백·방향·머리글·바닥글 범위를 제어하는 단위 |
| Flow Content | 텍스트 길이에 따라 자연스럽게 늘고 페이지를 넘는 본문 |
| Fixed Geometry | 표 너비·셀 여백처럼 계산 가능한 명시적 배치 값 |
| Render Evidence | 최종 파일의 모든 페이지를 이미지로 확인한 검수 기록 |
| Font Substitution | 지정 글꼴 부재로 다른 글꼴이 대신 사용되는 현상 |

# 4. 페이지와 Section

## 4.1 페이지 형식 명시

페이지 크기, 방향과 상·하·좌·우 여백은 Project MASTER 또는 문서 유형 기준에 명시한다. 값이 없으면 생성 환경의 우연한 기본값을 운영 기준으로 기록하지 않고 합리적인 기본값과 근거를 QA에 남긴다.

## 4.2 Section 최소화

하나의 페이지 설정으로 표현 가능한 문서는 단일 Section을 우선한다. 방향·머리글·번호 체계가 실제로 달라질 때만 Section을 추가하고, 빈 페이지나 번호 초기화가 생기지 않는지 검수한다.

## 4.3 사용 가능 폭

표, 이미지, 상자와 코드 블록은 페이지 폭에서 좌우 여백과 필요한 들여쓰기를 뺀 사용 가능 폭 안에 둔다. 회전·축소·가로 방향 전환은 내용 가독성을 보존하는 경우에만 사용한다.

# 5. 글꼴과 문자 체계

## 5.1 설치 이름 명시

문서 기본값, 일반 Style과 필요한 Run에 실제 설치된 글꼴 이름을 명시한다. 한글·영문·숫자의 East Asia, ASCII와 High ANSI 매핑을 함께 확인한다.

## 5.2 글꼴 역할 분리

본문·제목·표·머리글·바닥글은 승인된 본문 계열을 일관되게 사용한다. 고정폭 글꼴은 코드·명령·정렬 보존이 필요한 역할에만 제한한다.

## 5.3 대체 글꼴 검수

최종 렌더에서 명조·고딕 혼용, Calibri·Cambria 등 의도하지 않은 대체, 누락 글리프와 폭 변화가 없는지 확인한다. 글꼴이 없으면 무음 대체하지 않고 승인된 Fallback 또는 환경 제한을 기록한다.

# 6. 제목과 정보 계층

## 6.1 Style 기반 제목

제목은 역할에 맞는 Word Style과 논리 단계를 사용한다. 글자 크기만 키운 일반 문단을 제목으로 사용하거나 시각 크기 때문에 단계를 건너뛰지 않는다.

## 6.2 단일 문서 제목

하나의 DOCX는 주 문서 제목을 하나만 가진다. Cover의 Series·Subtitle·날짜는 제목을 대체하지 않으며 Project MASTER가 정한 관계를 유지한다.

## 6.3 제목 분할 안전

제목은 다음 문단과 함께 유지하고 페이지 마지막 줄에 홀로 남기지 않는다. 긴 제목은 의미를 보존한 자연스러운 줄바꿈을 허용하며 폭 이탈이나 잘림을 허용하지 않는다.

# 7. 본문·목록·간격

## 7.1 본문 리듬

본문 크기, 줄 간격, 문단 전후 간격은 Style로 정의한다. 연속 항목 사이 간격은 너무 넓거나 붙지 않도록 같은 역할에서 일관되게 유지한다.

## 7.2 실제 목록

순서와 집합을 표현하는 항목은 Word 목록 구조를 사용한다. 수동 숫자·문자 Bullet로 목록을 흉내 내지 않으며 줄바꿈된 문장이 Marker 아래가 아니라 본문 시작점에 정렬되게 한다.

## 7.3 인접 요소 간격

표·상자·이미지 다음에 일반 문단이 이어질 때는 역할에 맞는 명시적 간격을 둔다. 빈 문단의 개수로 간격을 조절하지 않고 Style 또는 요소 뒤 문단의 간격으로 제어한다.

# 8. 표

## 8.1 표 사용 조건

표는 여러 행이 같은 열 의미를 공유해 비교·조회가 쉬워질 때만 사용한다. 일반 설명이나 한 문장짜리 상태를 반복해서 표로 감싸지 않는다.

## 8.2 너비와 셀 여백

표 너비, 열 너비, 들여쓰기와 셀 여백을 사용 가능 폭 안에서 명시한다. 긴 설명 열은 넓게, 날짜·상태·번호 등 짧은 열은 필요한 만큼만 배정한다.

## 8.3 행과 머리글

행은 내용에 따라 확장되며 고정 높이로 텍스트를 자르지 않는다. 여러 페이지에 걸치는 표는 머리행을 반복하고 가능한 범위에서 한 행의 페이지 간 분할을 막는다.

## 8.4 표 전후 흐름

표 제목·설명과 표는 함께 유지하되 큰 빈 공간을 만들지 않는다. 표 직후 문단에는 충분한 간격을 두고 표 머리만 페이지 끝에 남거나 변경 이력 머리행과 본문이 분리되지 않게 한다.

# 9. 상자·코드·이미지

## 9.1 상자 역할

강조·요약·경고·프롬프트 상자는 역할이 있을 때만 사용한다. 상자 높이는 내용에 맞게 늘어나며 고정 높이나 빈 문단으로 과도한 내부 여백을 만들지 않는다.

## 9.2 코드 블록

코드·명령·프롬프트는 줄바꿈과 공백을 보존하는 별도 Style을 사용한다. 페이지 폭을 넘는 긴 줄은 승인된 줄바꿈 또는 글꼴·여백 조정으로 해결하고 내용 자체를 임의로 생략하지 않는다.

## 9.3 이미지

이미지는 사용 가능 폭 안에서 비율을 유지한다. 본문과 겹치는 부동 배치보다 안정적인 인라인 배치를 우선하고, 캡션·출처·대체 설명은 전담 정책과 MASTER를 따른다.

# 10. 머리글·바닥글·페이지 번호

## 10.1 일관된 페이지 가구

머리글과 바닥글은 문서 식별과 탐색에 필요한 최소 정보만 담는다. 본문과 충돌하지 않는 거리와 대비를 유지하며 홀수·짝수·첫 페이지 Variant를 사용하면 모두 검수한다.

## 10.2 페이지 번호

페이지 번호는 필드 또는 동등하게 갱신 가능한 구조를 사용한다. Section 전환에서 의도하지 않은 초기화·누락·잘림이 없는지 DOCX와 PDF 모두 확인한다.

# 11. 페이지네이션과 밀도

## 11.1 페이지 수보다 가독성

페이지 목표는 Project MASTER의 운영 범위일 수 있으나 고정 요구가 아니다. 콘텐츠 양이 변하면 페이지 수를 유동적으로 허용하고, 글꼴 축소·여백 압축·내용 삭제로 목표 수를 강제하지 않는다.

## 11.2 고아·과부 방지

제목, 짧은 설명, 표 머리와 관련 콘텐츠는 가능한 범위에서 함께 유지한다. 한 줄만 다음 페이지로 넘어가거나 큰 빈 페이지가 생기면 Style의 Keep·Page Break와 구성요소 크기를 조정한다.

## 11.3 전체 페이지 검수

첫 페이지, 중간 표·상자, Section 경계와 마지막 변경 이력을 포함해 모든 페이지를 실제 렌더로 확인한다. 페이지 수 통계만으로 시각 QA를 대신하지 않는다.

# 12. 편집성·접근성·호환성

## 12.1 편집 가능한 구조

본문을 이미지로 평면화하거나 하나의 거대한 텍스트 상자에 넣지 않는다. 제목·목록·표·링크·대체 텍스트는 가능한 한 Word의 의미 구조로 유지한다.

## 12.2 최소 접근성

제목 단계, 표 머리, 의미 있는 링크 텍스트, 색상 외 상태 단서와 이미지 대체 설명을 제공한다. 장식 이미지는 보조 기술에서 불필요하게 반복되지 않도록 처리한다.

## 12.3 범용성

문서 규칙은 특정 AI, 생성 라이브러리, 운영체제 또는 Word 버전에 종속되지 않는다. 구현 도구가 달라도 최종 OOXML 구조와 렌더 결과가 계약을 충족해야 한다.

# 13. PDF 변환 계약

## 13.1 단일 기준 DOCX

PDF는 승인된 최종 DOCX에서 생성하며 별도 편집본으로 취급하지 않는다. PDF에서 발견된 결함은 가능하면 DOCX 또는 내보내기 설정에서 수정하고 두 형식을 다시 검수한다.

## 13.2 정보와 순서 일치

DOCX와 PDF는 내용, 제목 순서, 표·이미지·상자, 페이지 가구와 페이지 수가 의도된 범위에서 일치해야 한다. PDF 변환 과정에서 누락·재배치·글꼴 대체가 발생하면 Delivery FAIL이다.

## 13.3 PDF 상자와 글꼴

상자 내부 여백과 높이, 글꼴 모양과 줄바꿈은 PDF에서도 자연스러워야 한다. DOCX에서 정상이라는 이유로 PDF의 과도한 빈 공간·잘림·글꼴 혼용을 허용하지 않는다.

# 14. 데이터 가변성과 템플릿

## 14.1 실제 Cardinality 반영

반복 Item·Summary·Insight·Action·Source의 수는 실제 데이터에 따른다. 템플릿 예시 수를 고정 페이지나 빈 구성요소 유지 근거로 사용하지 않는다.

## 14.2 미사용 슬롯 제거

값이 없는 표 행·카드·제목·상자와 Placeholder는 완전히 제거한다. 제거 후 제목 단계, 요소 사이 간격과 페이지 흐름을 다시 검수한다.

## 14.3 독자용 본문 경계

QA 상태, Binding 해시, 검수 추적과 템플릿 운영 메모는 독자에게 필요한 내용이 아니면 DOCX 본문에 노출하지 않고 패키지 README·QA Report에 기록한다.

# 15. 검증과 품질 게이트

## 15.1 구조 QA

- DOCX ZIP 패키지가 손상 없이 열리고 필요한 Part가 존재한다.
- 제목·본문·목록·표·머리글·바닥글이 역할별 Style과 구조를 사용한다.
- 댓글·추적 변경·의도하지 않은 Placeholder가 남지 않는다.
- 표 너비와 페이지 설정이 문서 사용 가능 폭에 맞는다.

## 15.2 렌더 QA

- DOCX를 최종 대상 환경 또는 승인된 대체 경로에서 재개봉·재페이지네이션했다.
- 동일 DOCX에서 PDF를 생성하고 페이지 수와 정보 순서를 비교했다.
- 모든 PDF 페이지를 이미지로 렌더링해 잘림·겹침·글리프·글꼴·간격을 확인했다.
- 첫 페이지, Section 경계, 긴 제목, 넓은 표, 상자와 마지막 페이지를 확인했다.

## 15.3 판정

Critical 또는 Major 결함이 하나라도 열려 있으면 PASS나 운영 Release를 선언하지 않는다. REVIEW 문서는 사용자 검토와 실제 프로젝트 적용 전까지 APPROVED 또는 LOCKED로 표시하지 않는다.

# 16. 변경·승인·LOCK 수명주기

1. 잠금된 실제 DOCX·PDF에서 공통 후보 원칙을 추출한다.
2. 프로젝트 전용 콘텐츠·브랜드·페이지 목표를 전담 문서에 남긴다.
3. Markdown·DOCX·PDF와 QA·해시 패키지를 `REVIEW`로 작성한다.
4. 사용자 검토와 수정 후 `APPROVED`로 전환한다.
5. 참조 프로젝트 DOCX와 PDF에 회귀 적용해 조판·편집성·렌더링을 검증한다.
6. 다른 프로젝트 또는 두 번째 문서 유형에서 재사용 가능성을 확인한다.
7. 명시적 잠금 승인 후 `LOCKED`로 전환한다.

책임·적용 범위·필수 QA가 바뀌면 버전을 증가시킨다. 승인된 파일은 History에 원형 보존하며 조용히 덮어쓰지 않는다.

# 17. 규칙 카탈로그

## 17.A 권한과 페이지

### DOCX-001 - Project MASTER 우선
- **Priority:** Critical
- **Statement:** 프로젝트별 페이지·시각 구조는 승인 Content Schema와 MASTER를 우선한다.
- **Verification:** Binding과 문서 속성을 대조한다.
- **Exceptions:** 안전·접근성·파일 무결성 또는 사용자 명시적 변경 승인.

### DOCX-002 - 단일 책임
- **Priority:** High
- **Statement:** DOCX SYSTEM은 공통 조판 계약만 정의하고 콘텐츠·브랜드·게시 규칙을 새로 만들지 않는다.
- **Verification:** 규칙별 전담 문서와 중복을 확인한다.
- **Exceptions:** 책임 경계를 설명하는 참조.

### DOCX-003 - 페이지 형식 명시
- **Priority:** High
- **Statement:** 페이지 크기·방향·여백과 Section 수를 명시한다.
- **Verification:** Section 속성과 MASTER를 대조한다.
- **Exceptions:** 없음.

### DOCX-004 - Section 최소화
- **Priority:** Medium
- **Statement:** 실제 페이지 설정 변화가 없으면 불필요한 Section을 추가하지 않는다.
- **Verification:** Section 경계와 속성 차이를 검사한다.
- **Exceptions:** 첫 페이지·홀짝 페이지 가구를 위한 승인 구조.

### DOCX-005 - 사용 가능 폭 준수
- **Priority:** Critical
- **Statement:** 표·이미지·상자·코드는 페이지 여백 안의 사용 가능 폭을 넘지 않는다.
- **Verification:** 요소 너비와 페이지 Geometry를 비교한다.
- **Exceptions:** 승인된 가로 방향 Section.

## 17.B 글꼴과 계층

### DOCX-006 - 실제 글꼴 이름
- **Priority:** Critical
- **Statement:** 문서 기본값과 역할별 Style에 실제 설치된 글꼴 이름을 명시한다.
- **Verification:** Style·Run의 ASCII·High ANSI·East Asia Font를 감사한다.
- **Exceptions:** 승인 Fallback Stack.

### DOCX-007 - 글꼴 역할 제한
- **Priority:** High
- **Statement:** 고정폭 글꼴은 코드·명령 등 정렬 보존 역할에만 사용한다.
- **Verification:** 글꼴별 Run과 문맥을 대조한다.
- **Exceptions:** Project MASTER가 승인한 특수 표기.

### DOCX-008 - 대체 글꼴 금지
- **Priority:** Critical
- **Statement:** 최종 렌더에 의도하지 않은 명조·고딕 혼용이나 대체 글꼴을 남기지 않는다.
- **Verification:** DOCX 글꼴 감사와 PDF 전 페이지 시각 검수를 결합한다.
- **Exceptions:** 기록된 환경 제한과 승인 Fallback.

### DOCX-009 - Style 기반 제목
- **Priority:** High
- **Statement:** 제목은 논리 단계에 맞는 Word Style을 사용한다.
- **Verification:** Heading Outline Level과 시각 계층을 비교한다.
- **Exceptions:** 독립 Cover의 승인 Title Style.

### DOCX-010 - 긴 제목 안전
- **Priority:** Critical
- **Statement:** 긴 제목은 의미를 보존해 줄바꿈하고 잘림·폭 이탈·고아 제목을 허용하지 않는다.
- **Verification:** 최장 제목과 페이지 끝 제목을 렌더한다.
- **Exceptions:** 없음.

## 17.C 본문·목록·표

### DOCX-011 - 본문 리듬 일관성
- **Priority:** High
- **Statement:** 본문 크기·줄 간격·전후 간격은 역할별 Style에서 일관된다.
- **Verification:** Style 정의와 직접 서식 예외를 감사한다.
- **Exceptions:** 명시적 Lead·Caption·Source Style.

### DOCX-012 - 실제 목록 구조
- **Priority:** High
- **Statement:** 목록은 수동 Marker가 아니라 Word 목록 구조를 사용한다.
- **Verification:** Numbering 관계와 줄바꿈 들여쓰기를 확인한다.
- **Exceptions:** 코드 예시 안의 문자 목록.

### DOCX-013 - 빈 문단 간격 금지
- **Priority:** High
- **Statement:** 요소 사이 간격을 반복 빈 문단으로 만들지 않는다.
- **Verification:** 연속 빈 문단과 Style 간격을 검사한다.
- **Exceptions:** 승인된 단일 Spacer 역할이 문서 전체에서 일관된 경우.

### DOCX-014 - 비교 가능한 표
- **Priority:** Medium
- **Statement:** 표는 행이 같은 열 의미를 공유하는 비교·조회 데이터에 사용한다.
- **Verification:** 행·열 관계와 대체 표현을 검토한다.
- **Exceptions:** 승인 Form 또는 Key-Value 메타데이터 표.

### DOCX-015 - 표 Geometry 일치
- **Priority:** Critical
- **Statement:** 표·열·셀 너비와 들여쓰기는 사용 가능 폭 안에서 일치한다.
- **Verification:** Table Width·Grid·Cell Width를 대조한다.
- **Exceptions:** 없음.

### DOCX-016 - 표 행 안전
- **Priority:** Critical
- **Statement:** 표 행은 내용에 따라 확장되고 텍스트를 자르는 고정 높이를 사용하지 않는다.
- **Verification:** Row Height Rule과 최장 셀 렌더를 확인한다.
- **Exceptions:** 내용 길이가 고정되고 잘림을 검증한 승인 Control Row.

### DOCX-017 - 표 머리 반복
- **Priority:** High
- **Statement:** 여러 페이지 표는 머리행을 반복하고 행 분할을 가능한 범위에서 막는다.
- **Verification:** 다중 페이지 표의 각 페이지 시작을 확인한다.
- **Exceptions:** 머리행이 없는 의도된 단일 Key-Value 표.

### DOCX-018 - 표 뒤 간격
- **Priority:** High
- **Statement:** 표 다음 일반 문단은 읽기 가능한 명시적 간격을 가진다.
- **Verification:** 모든 표의 후속 요소를 렌더에서 확인한다.
- **Exceptions:** 연속 표가 하나의 논리 데이터셋인 경우.

## 17.D 상자·페이지 가구·흐름

### DOCX-019 - 내용 밀착형 상자
- **Priority:** High
- **Statement:** 강조·코드·프롬프트 상자는 내용 높이에 맞게 확장하고 과도한 빈 공간을 만들지 않는다.
- **Verification:** DOCX와 PDF의 상자 내부 여백과 마지막 줄을 비교한다.
- **Exceptions:** 승인된 고정 크기 Form Field.

### DOCX-020 - 코드 공백 보존
- **Priority:** High
- **Statement:** 코드·명령·프롬프트는 공백과 줄바꿈을 보존하면서 페이지 폭 안에서 읽힌다.
- **Verification:** 최장 코드 줄과 PDF 변환 결과를 확인한다.
- **Exceptions:** 단어 수준 Inline Code.

### DOCX-021 - 이미지 비율 보존
- **Priority:** High
- **Statement:** 이미지는 사용 가능 폭 안에서 원본 비율과 본문 흐름을 유지한다.
- **Verification:** Image Extent와 페이지 폭을 비교한다.
- **Exceptions:** 승인 Crop 규칙이 있는 썸네일·장식 자산.

### DOCX-022 - 페이지 가구 일관성
- **Priority:** High
- **Statement:** 머리글·바닥글은 Section Variant별로 의도된 식별 정보를 일관되게 표시한다.
- **Verification:** 첫·홀수·짝수·Section 경계 페이지를 확인한다.
- **Exceptions:** 승인된 Cover의 페이지 가구 생략.

### DOCX-023 - 페이지 번호 연속성
- **Priority:** Critical
- **Statement:** 페이지 번호는 갱신 가능한 필드로 표시하고 누락·중복·잘림·의도하지 않은 초기화를 허용하지 않는다.
- **Verification:** DOCX와 PDF 전체 페이지 번호를 대조한다.
- **Exceptions:** 번호를 표시하지 않는 승인 단일 페이지 문서.

### DOCX-024 - 페이지 수 유동성
- **Priority:** Critical
- **Statement:** 실제 콘텐츠 양에 따라 페이지 수를 유동적으로 허용하고 목표 수를 위해 가독성이나 내용을 훼손하지 않는다.
- **Verification:** 글꼴·여백·내용 삭제와 목표 페이지 수의 관계를 검토한다.
- **Exceptions:** 법정 양식 등 외부 고정 페이지 제한.

### DOCX-025 - 페이지 분할 안전
- **Priority:** High
- **Statement:** 제목·짧은 설명·표 머리·관련 상자는 부자연스럽게 분리되지 않는다.
- **Verification:** 모든 페이지 끝과 시작을 전수 확인한다.
- **Exceptions:** 단일 구성요소가 한 페이지보다 긴 경우의 안전한 분할.

## 17.E 편집·PDF·검수

### DOCX-026 - 편집 가능한 의미 구조
- **Priority:** Critical
- **Statement:** 제목·목록·표·링크와 본문을 편집 가능한 Word 의미 구조로 유지한다.
- **Verification:** DOCX 재개봉과 요소 유형을 확인한다.
- **Exceptions:** 승인된 배경·장식 이미지.

### DOCX-027 - 접근성 하한선
- **Priority:** Critical
- **Statement:** 제목 단계·표 머리·링크 목적·색상 외 상태 단서·이미지 대체 설명을 유지한다.
- **Verification:** 구조 감사와 렌더 검수를 함께 수행한다.
- **Exceptions:** 장식 이미지의 명시적 제외.

### DOCX-028 - PDF 단일 원본
- **Priority:** Critical
- **Statement:** PDF는 승인된 최종 DOCX에서 생성하고 별도 내용 편집본으로 운영하지 않는다.
- **Verification:** 생성 경로·해시·내용 순서를 연결한다.
- **Exceptions:** 외부 서명·보안 후처리가 필요한 승인 배포 단계.

### DOCX-029 - 전 페이지 렌더 검수
- **Priority:** Critical
- **Statement:** 최종 DOCX와 PDF의 모든 페이지를 렌더해 잘림·겹침·글리프·간격·페이지 가구를 확인한다.
- **Verification:** 페이지 수와 Render Evidence를 대조한다.
- **Exceptions:** 렌더 환경이 없으면 미검증 범위를 명시하고 Release하지 않는다.

### DOCX-030 - 변경 후 재검수
- **Priority:** Critical
- **Statement:** 내용·Style·MASTER·글꼴·내보내기 경로가 바뀌면 최종 파일과 해시를 다시 검증한다.
- **Verification:** QA 대상 해시와 최종 패키지 해시를 비교한다.
- **Exceptions:** 해시에 영향을 주지 않는 외부 전달 메타데이터.

# 18. AI용 압축 DOCX System

## 18.1 압축 지침

다음 블록은 DSG-002가 `APPROVED` 또는 `LOCKED`된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 `LOCKED`이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-002 DOCX SYSTEM v2.0을 따른다.
1. 승인 Content Schema와 Project MASTER가 콘텐츠·페이지·시각 구조를 결정하며 DOCX SYSTEM은 공통 조판 하한선만 제공한다.
2. 페이지 크기·방향·여백·Section을 명시하고 표·이미지·상자·코드는 사용 가능 폭 안에 둔다.
3. 실제 설치 글꼴을 문서 기본값과 역할별 Style에 명시하고 코드 외 의도하지 않은 글꼴 혼용·대체를 허용하지 않는다.
4. 제목·본문·목록은 Word 의미 Style과 연속 계층을 사용하고 긴 제목·목록 줄바꿈·요소 간격을 안전하게 유지한다.
5. 표는 비교 데이터에만 사용하고 명시적 열 너비·셀 여백·자동 행 높이·반복 머리행·표 뒤 간격을 적용한다.
6. 상자와 코드 블록은 내용 높이에 맞게 확장하며 이미지 비율과 본문 흐름을 보존한다.
7. 머리글·바닥글·페이지 번호는 모든 Section Variant에서 누락·중복·잘림 없이 일관된다.
8. 실제 데이터 Cardinality에 따라 페이지 수를 유동적으로 허용하고 빈 슬롯·Placeholder·독자에게 불필요한 QA 메타데이터를 제거한다.
9. PDF는 최종 DOCX에서 생성하며 내용·순서·페이지·글꼴·상자와 페이지 가구가 의도대로 유지되어야 한다.
10. DOCX 재개봉과 PDF 변환 후 모든 페이지를 렌더하고 Critical 또는 Major 결함이 열려 있으면 Release하지 않는다.
```

## 18.2 추출 조건

- DSG-002가 `APPROVED` 또는 `LOCKED` 상태다.
- 실제 Project MASTER와 충돌하지 않는지 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| DOCX의 공통 조판·편집·페이지·PDF 하한선은? | DSG-002 DOCX SYSTEM |
| HTML 의미 구조와 모바일 안전은? | DSG-001 HTML SYSTEM |
| 색상·간격 토큰의 동결과 변경은? | DSG-003 CSS GOVERNANCE |
| 재사용 상자·카드·표의 세부 사양은? | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·대체 설명은? | DSG-005 IMAGE SYSTEM |
| 프로젝트 색상·로고·브랜드는? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 게시·수정·삭제와 전달은? | CNT-006 PUBLISHING SYSTEM과 COR-006 |
| 자동 생성·내보내기·복구는? | AUT 문서 |

## 19.2 알려진 제한

- 현재 기준은 정적 보고서·가이드·운영 기준 문서와 그 PDF 변환에서 추출했다.
- 복잡한 양식, 매크로, 수식 편집기, 다단 학술 조판과 서명 워크플로는 실제 적용 검증 전이다.
- 글꼴 가용성과 Word·대체 렌더러의 줄바꿈 차이는 대상 환경별 검수가 필요하다.
- Project MASTER가 A4·Letter, 페이지 목표·색상·제목 체계를 구체화할 수 있다.
- 이 문서는 사용자 승인을 받은 `APPROVED` 기준본이지만 실제 DOCX·PDF 회귀 적용과 명시적 잠금 승인 전에는 `LOCKED` 또는 운영 Release로 자동 전환하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | LOCKED `PROJECT_REFERENCE_FIXTURE` v1.0.1 FULL_DOCUMENT와 JCOS 기준 문서 검수에서 글꼴·Style·표·상자·페이지네이션·PDF 변환·전 페이지 QA 원칙을 분리하고 사용자 승인·잠금 승인 완료 |
