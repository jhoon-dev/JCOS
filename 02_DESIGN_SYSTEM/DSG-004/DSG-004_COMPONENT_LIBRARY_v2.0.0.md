# JCOS v2.0.0 - DSG-004 COMPONENT LIBRARY

## 승인된 UI 구성요소 계약

| Field | Value |
|---|---|
| Document ID | DSG-004 |
| Title | COMPONENT LIBRARY |
| Korean Title | 승인된 UI 구성요소 계약 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS HTML에 반복 사용되는 정보·탐색·행동·상태 구성요소 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001·DSG-002·DSG-003 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / BLOG_SUMMARY_HTML |
| Depends On | FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 재사용 UI 구성요소의 식별·구조·상태·조합·접근성·검수 계약을 분리해 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이다. 실제 색상·서체 값, CSS 선언, 이미지 생성, 썸네일 규칙과 게시 운영은 각 담당 문서가 정한다.

# 문서 목적

DSG-004는 프로젝트와 게시 채널이 달라도 같은 이름의 구성요소가 같은 의미와 구조로 생성되도록 공통 계약을 정의한다. 구성요소가 받을 데이터, 필수와 선택 Slot, Variant와 State, 반복 수, 중첩 가능 범위, 읽기 순서와 접근성 검증 방법을 명시한다.

이 문서는 완성된 화면의 실제 색·간격·서체 값을 고정하지 않는다. HTML 의미 구조는 DSG-001, DOCX 변환은 DSG-002, CSS 선언과 변경 통제는 DSG-003, 실제 브랜드 값은 DSG-007과 Project MASTER가 소유한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. 구성요소 식별과 유형
5. Anatomy와 Slot
6. Variant와 State
7. 데이터·Cardinality·빈 상태
8. 조합과 중첩
9. 의미 구조와 접근성
10. 반응형과 Overflow
11. 콘텐츠·출처·행동 패턴
12. CSS·브랜드·이미지 경계
13. 등록·버전·폐기
14. 변경 영향과 회귀
15. 검증과 품질 Gate
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 Component Library
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- Header, Navigation, Hero, Summary, Card, Insight, Action, Source, Table, Code, Callout, Footer 등 재사용 가능한 구성요소
- 구성요소의 이름, 목적, 필수·선택 Slot, Variant, State, Cardinality와 중첩 규칙
- 의미 있는 DOM 순서, 키보드·스크린리더·대체 경로를 포함한 접근성 계약
- 최소·대표·최대 데이터에서의 반응형·가변 콘텐츠 안전 조건
- 등록, 버전, 변경 영향, 폐기, 회귀 검수와 승인 상태

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| 문서의 HTML 의미 구조와 제목 계층 | DSG-001 HTML SYSTEM |
| DOCX 조판과 PDF 변환 | DSG-002 DOCX SYSTEM |
| CSS Token·Scope·Cascade·변경 통제 | DSG-003 CSS GOVERNANCE |
| 이미지 생성·선정·대체 설명 | DSG-005 IMAGE SYSTEM |
| 썸네일 비율·안전 영역·텍스트 배치 | DSG-006 THUMBNAIL RULES |
| 실제 색상·로고·서체 조합 | DSG-007 BRAND SYSTEM과 Project MASTER |
| 게시·수정·삭제·채널 운영 | CNT-006 PUBLISHING SYSTEM |
| 자동 빌드·배포·실패 복구 | AUT 문서 |

## 1.3 금지되는 확장

- 특정 프로젝트의 카드 수, 문구, 색상이나 장식 외형을 공통 필수값으로 고정
- 특정 Framework, CMS, 브라우저 또는 AI 도구를 유일한 구현 방식으로 지정
- 페이지 높이나 고정 수를 맞추기 위해 콘텐츠를 숨기거나 의미 순서를 변경
- 구성요소 계약으로 Content Schema, Brand, CSS 또는 게시 정책을 우회

# 2. 계층과 권한

## 2.1 권한 순서

구성요소 해석은 다음 순서를 따른다.

1. 안전·법률·접근성·플랫폼 필수 제한
2. 사용자의 현재 명시적 요청
3. 승인 Content Schema와 Project MASTER
4. DSG-007 Brand System과 DSG-004 Component Library
5. DSG-003 CSS Governance와 DSG-001 HTML System
6. 실제 입력 데이터와 게시 채널의 검증된 제한
7. 참고 구현과 과거 Output

## 2.2 상위 기준 우선

Project MASTER가 구성요소의 데이터 Slot, Variant 또는 지원 State를 구체적으로 승인하면 그 값을 따른다. 단, 의미 구조 훼손, 접근성 저하, 핵심 정보 누락이나 검증 불가 상태는 승인된 예외와 근거 없이 허용하지 않는다.

## 2.3 참고 구현의 역할

PROJECT_REFERENCE_FIXTURE v1.0.1은 Hero, Executive Summary, Editor's Insight, Action Items, Source와 코드 블록의 실제 조합을 검수한 참고 구현이다. 구성요소 수와 실제 문구는 그날의 데이터와 Project MASTER가 정하며 공통 규칙이 아니다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Component | 하나의 목적과 경계를 가지며 재사용 가능한 UI 단위 |
| Anatomy | 구성요소를 이루는 구조적 부분과 순서 |
| Slot | 데이터나 하위 구성요소가 들어가는 명명된 위치 |
| Required Slot | 누락되면 의미나 동작이 성립하지 않는 위치 |
| Optional Slot | 없어도 핵심 목적이 유지되는 위치 |
| Variant | 같은 목적을 유지하며 구조 또는 표현 선택지가 달라진 형태 |
| State | 데이터·동작·진행 상황에 따라 변하는 현재 조건 |
| Cardinality | 구성요소나 Slot이 허용하는 최소·대표·최대 개수 |
| Composition | 여러 구성요소를 승인된 관계로 결합하는 방식 |
| Empty State | 표시할 데이터가 없을 때의 명시적 대체 상태 |
| Registry | 구성요소 ID, 버전, 상태, 소유자와 계약을 기록한 목록 |

# 4. 구성요소 식별과 유형

## 4.1 식별자

각 등록 구성요소는 안정적인 Component ID와 의미 이름을 가진다. 이름은 `Blue Box`처럼 외형이 아니라 `Executive Summary`, `Source List`, `Action Item`처럼 역할을 드러낸다. 구현 Class는 프로젝트 또는 구성요소 Prefix를 사용한다.

## 4.2 기본 유형

| 유형 | 목적 | 예시 |
|---|---|---|
| Landmark | 페이지 영역과 탐색 경계 | Header, Main, Footer, Navigation |
| Information | 핵심 정보 전달 | Hero, Summary, Card, Table, Code |
| Editorial | 해석·강조·권고 | Editor's Insight, Callout, Action Item |
| Reference | 근거와 외부 연결 | Source, Citation, Related Link |
| Status | 현재 조건 전달 | Notice, Empty, Error, Loading |
| Control | 사용자 행동 수집 | Link, Button, Disclosure, Tab |

## 4.3 독립성과 경계

구성요소는 상위 컨테이너 없이도 목적과 필요한 입력을 설명할 수 있어야 한다. 단순한 색상 Span이나 일회성 간격 Wrapper는 독립 구성요소로 등록하지 않는다. 구조·상태·검수 책임이 반복될 때 등록 후보가 된다.

# 5. Anatomy와 Slot

## 5.1 Anatomy 명세

명세에는 Root, Header, Body, Metadata, Action, Source 등 실제로 존재하는 부분과 그 순서를 기록한다. 시각적 재배치가 있더라도 DOM과 보조기술의 읽기 순서는 의미 순서를 유지한다.

## 5.2 필수와 선택 Slot

필수 Slot은 값 유형, 허용 길이 또는 범위, 누락 시 실패 처리를 함께 정의한다. 선택 Slot은 값이 없을 때 빈 Wrapper·구분선·공백을 남기지 않는다. 의미 없는 Placeholder로 누락을 감추지 않는다.

## 5.3 Slot 계약 예시

| Slot | 필요성 | 계약 |
|---|---|---|
| title | Required | 구성요소 목적을 식별하는 텍스트 또는 연결된 제목 |
| body | Required | 핵심 정보를 읽기 순서대로 보존 |
| metadata | Optional | 값이 있을 때만 Label과 함께 표시 |
| action | Optional | 목적·대상·상태가 명확한 Link 또는 Button |
| source | Conditional | 사실 주장에 근거가 필요할 때 출처 정책에 따라 표시 |

# 6. Variant와 State

## 6.1 Variant 원칙

Variant는 같은 목적과 핵심 Slot을 유지해야 한다. Compact, Featured, With Media처럼 차이를 의미 이름으로 기록하고 단순 색상 이름만으로 구분하지 않는다. 핵심 구조가 달라지면 별도 구성요소인지 검토한다.

## 6.2 State 목록

지원하는 Default, Hover, Focus, Active, Visited, Disabled, Loading, Empty, Error, Success 상태를 필요한 범위에서 명시한다. 존재하지 않는 State를 관성적으로 추가하지 않고, 지원 State는 텍스트·아이콘·ARIA 등 색상 외 단서로 구분한다.

## 6.3 상태 전이

상태가 바뀔 때 원인, 결과, 복구 행동과 사용자에게 전달할 메시지를 정의한다. Loading이 무기한 지속되거나 Error가 핵심 입력을 잃게 하지 않는다. 정적 게시 구성요소는 동적 State를 강제로 갖지 않는다.

# 7. 데이터·Cardinality·빈 상태

## 7.1 데이터 연결

각 Slot은 승인 Content Schema의 Field 또는 생성 근거와 연결한다. 같은 의미의 데이터를 여러 Slot에 중복 저장하지 않는다. Markdown, HTML, DOCX로 변환할 때도 값의 의미와 출처 연결을 유지한다.

## 7.2 Cardinality

반복 구성요소는 최소·대표·최대 Fixture를 갖는다. 개수는 실제 데이터에 따라 유동적이며, 특정 날짜의 Editor's Insight 7개 같은 관찰값을 전역 고정 수로 사용하지 않는다. Project MASTER가 최소나 최대를 정하면 그 근거와 Overflow 처리를 함께 기록한다.

## 7.3 Empty와 Partial

데이터가 없으면 구성요소를 생략할지, 명시적 Empty State를 표시할지 계약으로 정한다. 일부 Slot만 누락된 Partial 상태에서는 핵심 목적이 유지될 때만 렌더하며, 필수 Slot 누락은 생성·Release 실패로 처리한다.

# 8. 조합과 중첩

## 8.1 허용 조합

상위 구성요소는 허용하는 하위 구성요소 유형, 순서와 반복 범위를 명시한다. Section 안의 Card List처럼 자연스러운 조합은 허용하지만, 구성요소가 자신의 복제본을 제한 없이 중첩하거나 Landmark를 잘못 포함하지 않는다.

## 8.2 의존성 최소화

하위 구성요소는 우연한 부모 Class, DOM 깊이 또는 형제 순서에 의존하지 않는다. 필요한 Context는 명시적 Variant, State, Attribute 또는 승인 Token으로 전달한다.

## 8.3 중복 의미 금지

같은 제목·출처·행동을 부모와 자식에서 중복 노출하지 않는다. 시각적 반복이 필요한 경우 보조기술 중복 읽기와 링크 목적 혼동을 검수한다.

# 9. 의미 구조와 접근성

## 9.1 의미 HTML

구성요소의 Root와 Slot은 DSG-001의 Landmark, Sectioning, Heading, List, Table, Figure와 Link·Button 의미를 따른다. `div`와 시각 Class만으로 의미를 대신하지 않는다.

## 9.2 이름과 관계

Control과 Landmark는 보이는 Label 또는 연결된 접근 가능한 이름을 가진다. 제목과 본문, 표와 Caption, 이미지와 대체 설명, Error와 입력의 관계를 구조적으로 연결한다.

## 9.3 키보드와 Focus

상호작용 구성요소는 키보드로 접근·실행·이탈할 수 있어야 하며 보이는 Focus를 유지한다. 시각적 순서와 Focus 순서가 모순되지 않고, 비활성 상태는 의미와 동작을 함께 차단한다.

# 10. 반응형과 Overflow

## 10.1 모바일 우선 계약

기본 흐름은 좁은 화면에서 한 열 읽기와 자연스러운 세로 확장을 보장한다. 넓은 화면 Variant는 최소 폭과 데이터 조건을 근거로 추가하며 핵심 정보 순서를 바꾸지 않는다.

## 10.2 가변 콘텐츠

짧은·긴 제목, 다국어, 긴 URL, 코드, 표, 최소·대표·최대 반복 수를 Fixture로 검증한다. 고정 높이, 임의 Line Clamp나 숨김으로 핵심 내용을 잘라내지 않는다.

## 10.3 Overflow 소유권

구성요소는 자신이 만든 표·코드·미디어의 Overflow 경계를 책임진다. 페이지 전체 수평 스크롤을 기본 해결책으로 사용하지 않고, CSS 구현은 DSG-003의 Root Scope와 사용 가능 폭 계약을 따른다.

# 11. 콘텐츠·출처·행동 패턴

## 11.1 제목과 본문

제목은 구성요소 목적을 식별하고 본문은 결론·근거·행동이 구분되게 구성한다. 실제 문체와 필드 내용은 Content Schema와 작성 원칙이 소유하며 Component Library는 위치와 필수성만 정한다.

## 11.2 출처와 링크

출처 구성요소는 최소한 출처명과 접근 가능한 링크 목적을 보존한다. 표현이 인라인 또는 목록으로 달라도 출처 정책과 링크 검증을 통과해야 한다. 링크처럼 보이는 텍스트를 비동작 요소로 만들지 않는다.

## 11.3 행동 요소

이동은 Link, 현재 Context의 작업은 Button을 사용한다. Action Label은 결과를 설명하고 아이콘만 사용할 경우 접근 가능한 이름을 제공한다. 위험하거나 되돌리기 어려운 행동은 해당 운영 기준의 확인·복구 규칙을 따른다.

# 12. CSS·브랜드·이미지 경계

## 12.1 CSS 경계

DSG-004는 필요한 구조·상태 Hook과 Token 역할을 명세하지만 Selector, Specificity, 실제 값과 변경 절차는 DSG-003이 소유한다. Inline Style이나 과도한 구조 선택자로 계약을 구현하지 않는다.

## 12.2 브랜드 경계

색상·로고·서체·모서리·그림자 같은 실제 Brand 값은 DSG-007과 Project MASTER가 정한다. Component Library는 의미 대비, Focus 가시성, 상태 구분 등 검증 가능한 요구만 전달한다.

## 12.3 이미지 경계

구성요소는 이미지 Slot의 목적, 비율 Context, Caption·Alt 필요성을 명시할 수 있다. 이미지 생성·선정·안전·저작권은 DSG-005, 썸네일 전용 배치는 DSG-006이 담당한다.

# 13. 등록·버전·폐기

## 13.1 Registry 항목

등록에는 Component ID, 이름, 목적, Owner, Version, Status, Anatomy, Slot, Variant, State, Cardinality, 의존 문서, Fixture와 QA Evidence를 포함한다. 미등록 실험 요소는 Production 공통 구성요소로 선언하지 않는다.

## 13.2 변경 등급

문구 교정이나 비의미 메타데이터는 PATCH, 호환 가능한 Slot·Variant 추가는 MINOR, 필수 Slot·의미·DOM·행동 계약 파괴는 MAJOR 후보로 본다. 실제 버전 결정은 COR-007 VERSION POLICY를 따른다.

## 13.3 Deprecation

폐기 구성요소는 대체 대상, 전환 기한, 영향 프로젝트와 제거 조건을 기록하고 ID를 재사용하지 않는다. 소비 프로젝트가 남아 있는 동안 계약과 최소 회귀 Fixture를 유지한다.

# 14. 변경 영향과 회귀

## 14.1 영향 표면

변경 전 Component, Slot, Variant, State, Schema Field, CSS Hook, Brand Token, 지원 폭, 산출물 형식과 게시 채널을 식별한다. 이름 검색만으로 동적 조합과 데이터 의존성을 누락하지 않는다.

## 14.2 대표 Fixture

최소·대표·최대 데이터, 빈·부분·오류 상태, 360px·390px·Desktop 또는 MASTER 지정 폭, 키보드와 보조기술 경로를 검수한다. 변경된 구성요소와 이를 포함하는 상위 조합을 함께 확인한다.

## 14.3 비교와 복구

승인 이전 Render와 구조 Evidence를 기준으로 의도된 차이와 비의도 차이를 분리한다. 회귀가 발생하면 승인본을 조용히 덮어쓰지 않고 후보 버전에서 수정하거나 승인된 Rollback 경로를 따른다.

# 15. 검증과 품질 Gate

## 15.1 계약 검수

- Component ID, 목적, Owner, Version과 Status
- Required·Optional Slot, Variant, State와 Cardinality
- Schema Field, CSS Hook, Token 역할과 책임 문서 연결
- 허용 중첩, 금지 조합, Empty·Partial·Error 처리
- 접근 가능한 이름, 관계, 키보드와 Focus 계약

## 15.2 시각·구조 검수

- 360px·390px·Desktop 또는 MASTER 지정 폭의 전체 화면
- 최소·대표·최대 반복 수와 긴 제목·URL·코드·표
- 잘림·겹침·수평 넘침·고정 높이·빈 Wrapper·순서 왜곡
- Default·Focus·Disabled·Loading·Empty·Error 등 지원 상태
- 실제 게시 또는 Sanitization 결과와 로컬 결과의 차이

## 15.3 Gate 판정

Critical 또는 Major 계약 결함이 하나라도 열려 있으면 PASS·LOCK·Release를 선언하지 않는다. REVIEW 문서는 사용자 검토와 대표 구현 회귀 적용 전 APPROVED 또는 LOCKED로 표시하지 않는다.

# 16. 변경·승인·LOCK 수명주기

1. 적용 Project·Delivery·지원 폭과 Content Schema를 식별한다.
2. Anatomy·Slot·Variant·State·Cardinality·경계를 후보로 작성한다.
3. Markdown·DOCX·PDF와 QA·해시 패키지를 REVIEW로 작성한다.
4. 사용자 검토와 수정 후 APPROVED로 전환한다.
5. 대표 HTML과 게시 경로에서 최소·대표·최대 Fixture 회귀를 실행한다.
6. PASS Evidence와 연결 버전·해시를 Registry에 기록한다.
7. 명시적 잠금 승인 후 LOCKED로 전환한다.

LOCKED 이후 계약을 변경할 때는 같은 파일을 조용히 덮어쓰지 않고 버전 후보와 History를 만든다.

# 17. 규칙 카탈로그

## 17.A 권한·식별

### CMP-001 - 상위 기준 우선

- **Priority:** Critical
- **Statement:** 구성요소는 사용자 요청, 승인 Schema·MASTER와 상위 안전·접근성 기준을 무효화하지 않는다.
- **Verification:** 연결 문서와 구현 계약의 충돌을 대조한다.
- **Exceptions:** 승인된 법률·안전·플랫폼 필수 제한.

### CMP-002 - 의미 기반 식별자

- **Priority:** High
- **Statement:** 구성요소 ID와 이름은 외형이 아니라 안정적인 목적을 나타낸다.
- **Verification:** Registry 이름과 Anatomy 목적을 비교한다.
- **Exceptions:** 기존 호환 ID의 표시 이름 보정.

### CMP-003 - 명시적 소유권

- **Priority:** Critical
- **Statement:** 각 구성요소는 Owner, Version, Status와 변경 승인 경로를 기록한다.
- **Verification:** Registry와 패키지 메타데이터를 확인한다.
- **Exceptions:** 폐기 전 미등록 Prototype.

### CMP-004 - 유형과 경계 명시

- **Priority:** High
- **Statement:** Landmark·Information·Editorial·Reference·Status·Control 중 역할과 Root 경계를 명시한다.
- **Verification:** DOM과 구성요소 명세를 대조한다.
- **Exceptions:** 두 역할을 결합하도록 승인된 Composite.

### CMP-005 - 특정 구현 종속 금지

- **Priority:** High
- **Statement:** 특정 Framework·CMS·브라우저·AI 도구를 공통 계약의 유일한 실행 조건으로 요구하지 않는다.
- **Verification:** 필수 도구와 Fallback 목록을 감사한다.
- **Exceptions:** Project MASTER가 선언한 제한 환경.

### CMP-006 - 참고 구현 비강제

- **Priority:** Critical
- **Statement:** 참고 Output의 개수·문구·색상·외형을 전역 구성요소 필수값으로 승격하지 않는다.
- **Verification:** MASTER와 현재 Schema의 실제 요구를 비교한다.
- **Exceptions:** 명시적으로 승인된 Project 고정값.

## 17.B Anatomy·Slot·Variant

### CMP-007 - Anatomy 완전성

- **Priority:** Critical
- **Statement:** Root와 구조 부분, 순서, 필수 관계를 검증 가능한 Anatomy로 기록한다.
- **Verification:** 명세와 DOM·산출물을 대조한다.
- **Exceptions:** 구조가 없는 순수 데이터 Token.

### CMP-008 - 필수 Slot 실패

- **Priority:** Critical
- **Statement:** Required Slot 누락을 임의 Placeholder로 감추지 않고 생성 또는 Release 실패로 처리한다.
- **Verification:** 필수값 누락 Fixture를 실행한다.
- **Exceptions:** 승인된 Empty State가 핵심 목적을 대체하는 경우.

### CMP-009 - 선택 Slot 잔여물 금지

- **Priority:** High
- **Statement:** Optional Slot이 비면 빈 Wrapper·구분선·불필요한 공백을 남기지 않는다.
- **Verification:** 선택값 제거 전후 Render와 DOM을 비교한다.
- **Exceptions:** Layout 안정성을 위한 접근 가능한 예약 영역.

### CMP-010 - 의미 Variant

- **Priority:** High
- **Statement:** Variant는 목적과 핵심 Slot을 유지하며 차이를 의미 이름과 조건으로 기록한다.
- **Verification:** Variant별 Anatomy와 Fixture를 비교한다.
- **Exceptions:** MAJOR 버전 후보로 분리된 구조 변경.

### CMP-011 - 지원 State 명시

- **Priority:** Critical
- **Statement:** 필요한 Default·Focus·Disabled·Loading·Empty·Error 등 State와 전이 조건을 명시한다.
- **Verification:** 지원 State Matrix와 실제 결과를 대조한다.
- **Exceptions:** 상태가 없는 정적 구성요소.

### CMP-012 - 색상 외 상태 단서

- **Priority:** Critical
- **Statement:** 상태와 중요도를 색상만으로 전달하지 않고 텍스트·아이콘·구조·ARIA 중 적합한 단서를 함께 제공한다.
- **Verification:** 무채색·고대비·보조기술 경로를 확인한다.
- **Exceptions:** 의미가 없는 장식 차이.

## 17.C 데이터·조합

### CMP-013 - Schema 연결

- **Priority:** Critical
- **Statement:** 각 데이터 Slot을 승인 Content Schema Field 또는 생성 근거와 연결한다.
- **Verification:** Slot Map과 입력·출력 Fixture를 대조한다.
- **Exceptions:** 정적 Label과 구조 보조문.

### CMP-014 - Cardinality 범위

- **Priority:** Critical
- **Statement:** 반복 구성요소는 최소·대표·최대 개수와 초과 처리를 정의한다.
- **Verification:** 세 범위 Fixture와 Overflow를 렌더한다.
- **Exceptions:** Schema가 명시적으로 단일 항목을 보장하는 경우.

### CMP-015 - 관찰 개수 고정 금지

- **Priority:** Critical
- **Statement:** 특정 날짜나 참고 Output의 항목 수를 공통 고정 수로 사용하지 않는다.
- **Verification:** 서로 다른 개수의 실제 또는 합성 Fixture를 비교한다.
- **Exceptions:** Project MASTER가 근거와 함께 고정한 구성요소.

### CMP-016 - Empty·Partial 계약

- **Priority:** High
- **Statement:** 데이터 없음과 일부 누락에서 생략·대체·실패 중 하나를 명시적으로 결정한다.
- **Verification:** Empty와 Partial Fixture를 실행한다.
- **Exceptions:** 없음.

### CMP-017 - 허용 중첩 제한

- **Priority:** Critical
- **Statement:** 부모는 허용 자식 유형·순서·반복 범위를 명시하고 무한 자기 중첩을 금지한다.
- **Verification:** Composition Matrix와 DOM 깊이를 검사한다.
- **Exceptions:** 깊이 상한이 있는 승인 Tree 구성요소.

### CMP-018 - 암묵적 Context 금지

- **Priority:** High
- **Statement:** 하위 구성요소가 우연한 부모 Class·DOM 깊이·형제 순서에 의존하지 않게 한다.
- **Verification:** 독립·다른 부모 Context에서 렌더한다.
- **Exceptions:** 의미 구조가 필수인 승인 List·Table 관계.

## 17.D 의미·접근성·반응형

### CMP-019 - 의미 구조 준수

- **Priority:** Critical
- **Statement:** 구성요소는 DSG-001의 Landmark·Heading·List·Table·Link·Button 의미를 따른다.
- **Verification:** DOM Outline과 접근성 Tree를 검사한다.
- **Exceptions:** 플랫폼이 의미 요소를 제거하는 경우의 검증된 대체 속성.

### CMP-020 - 접근 가능한 이름과 관계

- **Priority:** Critical
- **Statement:** Control·Landmark·Figure·Table·Error는 필요한 이름과 연결 관계를 가진다.
- **Verification:** Label·ARIA·Caption·오류 연결을 검사한다.
- **Exceptions:** 이름이 불필요한 장식 요소.

### CMP-021 - 키보드와 Focus

- **Priority:** Critical
- **Statement:** 상호작용 구성요소는 키보드 실행·이탈이 가능하고 보이는 Focus와 논리적 순서를 유지한다.
- **Verification:** 키보드만으로 전체 경로를 수행한다.
- **Exceptions:** 상호작용이 없는 정적 구성요소.

### CMP-022 - 모바일 우선 읽기

- **Priority:** Critical
- **Statement:** 기본 구성요소는 좁은 화면 한 열 읽기와 의미 있는 DOM 순서를 보장한다.
- **Verification:** 360px·390px와 Desktop 순서를 비교한다.
- **Exceptions:** 명시적 가로 탐색이 본질인 승인 구성요소.

### CMP-023 - 가변 콘텐츠 안전

- **Priority:** Critical
- **Statement:** 긴 제목·URL·다국어·코드·표와 최대 반복에서 핵심 내용을 자르거나 숨기지 않는다.
- **Verification:** 장문·다국어·최대 Fixture를 렌더한다.
- **Exceptions:** 접근 가능한 전체 보기 경로가 있는 승인 요약 UI.

### CMP-024 - 국소 Overflow

- **Priority:** High
- **Statement:** 표·코드·미디어 Overflow는 구성요소 내부에서 제어하고 페이지 전체 수평 넘침을 만들지 않는다.
- **Verification:** Root 폭과 수평 스크롤 범위를 확인한다.
- **Exceptions:** 플랫폼이 강제하는 고정 폭 Embed.

## 17.E Registry·변경·QA

### CMP-025 - Registry 완전성

- **Priority:** Critical
- **Statement:** 등록 구성요소는 ID·Owner·Version·Status·계약·Fixture·Evidence를 연결한다.
- **Verification:** Registry 필수 Field를 검사한다.
- **Exceptions:** Production에 사용하지 않는 명시적 Prototype.

### CMP-026 - 변경 등급 분류

- **Priority:** High
- **Statement:** 계약 변경을 PATCH·MINOR·MAJOR 영향으로 분류하고 호환성 근거를 기록한다.
- **Verification:** 변경 전후 Slot·DOM·State·소비 프로젝트를 비교한다.
- **Exceptions:** 해시에 영향을 주지 않는 외부 전달 메타데이터.

### CMP-027 - Deprecation 추적

- **Priority:** High
- **Statement:** 폐기 시 대체 대상·전환 기한·영향 범위·제거 조건을 기록하고 ID를 재사용하지 않는다.
- **Verification:** Registry와 소비 프로젝트 검색 결과를 대조한다.
- **Exceptions:** 배포되지 않은 Prototype ID.

### CMP-028 - 통합 회귀 재실행

- **Priority:** Critical
- **Statement:** Component 변경이 Schema·CSS·Brand·이미지·산출물·게시 결과에 영향을 주면 연결 Gate를 다시 실행한다.
- **Verification:** 연결 QA 결과와 변경 버전을 확인한다.
- **Exceptions:** 영향 없음이 구조적으로 입증된 주석 교정.

### CMP-029 - 열린 결함 Release 금지

- **Priority:** Critical
- **Statement:** 열린 Critical 또는 Major 구성요소 결함이 있으면 PASS·LOCK·Release를 선언하지 않는다.
- **Verification:** Defect Register와 Gate 판정을 대조한다.
- **Exceptions:** 없음.

### CMP-030 - 최종 해시 갱신

- **Priority:** Critical
- **Statement:** 계약·DOCX·PDF·QA·상태가 바뀌면 최종 패키지 해시를 다시 계산하고 검증한다.
- **Verification:** SHA 파일과 현재 산출물 해시를 비교한다.
- **Exceptions:** 해시 대상 밖 외부 전달 메타데이터.

# 18. AI용 압축 Component Library

## 18.1 압축 지침

다음 블록은 DSG-004가 APPROVED 또는 LOCKED된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 LOCKED이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-004 COMPONENT LIBRARY v2.0을 따른다.
1. 승인 Schema·Project MASTER가 실제 데이터와 구성요소 수를 결정하며 참고 Output의 개수·문구·외형을 전역 고정하지 않는다.
2. 각 구성요소는 의미 기반 ID·목적·Owner·Version·Status와 Root·Anatomy·Slot·Variant·State·Cardinality를 가진다.
3. Required Slot 누락은 실패시키고 Optional Slot 누락 시 빈 Wrapper·구분선·공백을 남기지 않으며 Empty·Partial 처리를 명시한다.
4. 부모·자식 유형·순서·반복 범위를 제한하고 우연한 DOM 깊이·부모 Class·형제 순서에 의존하지 않는다.
5. DSG-001 의미 구조를 따르고 접근 가능한 이름·관계·키보드·Focus·색상 외 상태 단서를 보장한다.
6. 모바일 한 열 읽기와 의미 순서를 기본으로 하며 긴 제목·URL·다국어·코드·표·최대 반복에서 핵심 내용을 자르지 않는다.
7. CSS 선언·값은 DSG-003, 실제 Brand 값은 DSG-007과 Project MASTER, 이미지·썸네일·게시는 각 전담 문서가 소유한다.
8. Registry에 계약·Fixture·Evidence를 연결하고 변경을 버전화하며 Deprecation ID를 재사용하지 않는다.
9. 최소·대표·최대·Empty·Partial·Error와 360px·390px·Desktop 또는 MASTER 폭에서 구성요소와 상위 조합을 회귀 검수한다.
10. Critical 또는 Major 결함이 열려 있으면 PASS·LOCK·Release하지 않고 변경 후 연결 Gate와 최종 해시를 갱신한다.
```

## 18.2 추출 조건

- DSG-004가 APPROVED 또는 LOCKED 상태다.
- 실제 Project MASTER·Schema·CSS·Brand 계약과 충돌하지 않는지 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| 구성요소의 Anatomy·Slot·Variant·State·Cardinality는? | DSG-004 COMPONENT LIBRARY |
| HTML Landmark·제목 계층·DOM 의미는? | DSG-001 HTML SYSTEM |
| DOCX 조판과 PDF 변환은? | DSG-002 DOCX SYSTEM |
| CSS Token·Scope·Cascade·변경 통제는? | DSG-003 CSS GOVERNANCE |
| 이미지 생성·선정·대체 설명은? | DSG-005 IMAGE SYSTEM |
| 썸네일 비율과 안전 영역은? | DSG-006 THUMBNAIL RULES |
| 실제 색상·로고·서체 조합은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 게시 채널 발행·수정·삭제는? | CNT-006 PUBLISHING SYSTEM |
| 자동 Build·Deploy·실패 복구는? | AUT 문서 |

## 19.2 알려진 제한

- 현재 기준은 정적 콘텐츠형 HTML과 외부 게시 채널 게시용 본문 조각에서 추출했다.
- 복잡한 Web App, 실시간 협업, Drag and Drop, 가상화 목록과 고급 Widget은 실제 적용 검증 전이다.
- 실제 Component Registry 파일 형식과 Brand Token 값은 후속 DSG 문서와 Project MASTER에서 확정한다.
- 게시 채널별 Sanitization과 지원 범위는 대상 Delivery마다 별도 검증이 필요하다.
- 이 문서는 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이며 운영 Runtime·Release 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | LOCKED PROJECT_REFERENCE_FIXTURE v1.0.1 BLOG_SUMMARY_HTML과 DSG-001~003 경계에서 구성요소 식별·Anatomy·Slot·Variant·State·Cardinality·조합·접근성·등록·회귀 규칙을 분리하고 사용자 승인·잠금 승인 완료 |
