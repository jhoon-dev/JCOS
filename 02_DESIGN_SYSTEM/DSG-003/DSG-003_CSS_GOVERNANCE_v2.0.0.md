# JCOS v2.0.0 - DSG-003 CSS GOVERNANCE

## CSS 동결·변경 관리

| Field | Value |
|---|---|
| Document ID | DSG-003 |
| Title | CSS GOVERNANCE |
| Korean Title | CSS 동결·변경 관리 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS HTML에 연결되거나 포함되는 CSS와 승인 Style Token |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001 v2.0.0 APPROVED, DSG-002 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / BLOG_SUMMARY_HTML |
| Depends On | FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 잠금된 참조 프로젝트 HTML에서 실제 검증된 CSS 범위 격리·토큰·반응형·변경 검수 원칙만 분리해 사용자 승인과 명시적 잠금 승인을 받은 `LOCKED` 기준본이다. 프로젝트별 색상·로고·구성요소 외형을 공통 필수값으로 추가하지 않는다.

# 문서 목적

DSG-003은 JCOS HTML의 CSS가 프로젝트와 게시 환경이 달라도 승인 범위 밖을 침범하지 않고, 예측 가능한 Cascade와 반응형 동작을 유지하며, 변경의 영향과 회귀 결과를 추적할 수 있도록 공통 거버넌스를 정의한다.

CSS의 실제 색상·간격·모서리 값은 Brand System과 Project MASTER가 정하고, 구성요소의 필수 상태와 구조는 Component Library가 정한다. DSG-003은 그 값을 선언·적용·동결·변경·검수하는 방법과 안전 하한선만 제공한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. CSS 산출물과 연결 방식
5. Token 소유권과 선언
6. Root Scope와 선택자
7. Cascade·Specificity·Override
8. Layout과 반응형
9. Typography·색상·상태
10. Overflow와 가변 콘텐츠
11. 외부 자산과 Fallback
12. 플랫폼 호환성과 Sanitization
13. 동결·버전·변경 등급
14. 변경 영향과 회귀
15. 검증과 품질 게이트
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 CSS Governance
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- 독립 HTML 문서와 게시용 HTML 조각에 포함되거나 연결되는 CSS
- Custom Property와 승인 Token의 선언·참조·Fallback
- Root Scope, 선택자, Cascade, Specificity와 예외 Override
- 모바일 우선 Layout, Breakpoint, Overflow와 가변 콘텐츠 대응
- 스타일 동결, 변경 등급, 영향 분석, 회귀 검수와 해시 추적

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| HTML 의미 구조·제목 계층·DOM 순서 | DSG-001 HTML SYSTEM |
| 재사용 카드·상자·표의 구조와 상태 계약 | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·대체 설명 | DSG-005 IMAGE SYSTEM |
| 썸네일 비율·안전 영역·텍스트 배치 | DSG-006 THUMBNAIL RULES |
| 프로젝트별 색상·로고·서체 조합 | DSG-007 BRAND SYSTEM과 Project MASTER |
| 콘텐츠 필드·반복 수·문장 | 승인 Content Schema와 Project MASTER |
| 게시·수정·삭제·채널 운영 | CNT-006 PUBLISHING SYSTEM |
| 자동 배포·실패 복구·Schedule | AUT 문서 |

## 1.3 금지되는 확장

- 참조 프로젝트의 파란색·둥근 카드·특정 Breakpoint를 모든 프로젝트에 강제
- 특정 CSS Framework, 전처리기, 브라우저 또는 AI 도구를 유일한 구현 방식으로 지정
- 페이지 수나 고정 카드 수를 맞추기 위해 CSS로 콘텐츠를 숨기거나 잘라냄
- CSS 변경만으로 HTML 구조·콘텐츠 Schema·브랜드 정책을 우회

# 2. 계층과 권한

## 2.1 권한 순서

CSS 구현은 다음 순서로 해석한다.

1. 안전·법률·접근성·플랫폼 필수 제한
2. 사용자의 현재 명시적 요청
3. 승인 Content Schema와 Project MASTER
4. DSG-007 Brand System과 DSG-004 Component Library
5. DSG-003 CSS GOVERNANCE
6. DSG-001 HTML SYSTEM
7. 실행 시점 입력과 게시 환경의 검증된 제한
8. 참고 CSS와 과거 Output

## 2.2 상위 기준 우선

Project MASTER가 승인 Token 값과 Breakpoint를 구체적으로 정하면 그 값을 따른다. 단, 전역 오염·접근성 저하·콘텐츠 은폐·검증 불가 상태는 승인된 예외와 근거 없이 허용하지 않는다.

## 2.3 참고 구현의 역할

`PROJECT_REFERENCE_FIXTURE` v1.0.1은 고유 Root ID, `box-sizing`, Custom Property, 모바일 단일 열, 긴 문자열과 표 Overflow, 채널 CSS 충돌 방어를 실제 검수한 참고 구현이다. 그 색상·Class 이름·카드 수는 공통 규칙이 아니다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Root Scope | CSS 영향 범위를 특정 산출물의 최상위 요소 아래로 제한하는 고유 선택자 |
| Style Token | 색상·간격·글꼴·크기·모서리 등 반복 값을 의미 이름으로 참조하는 변수 |
| Cascade Contract | 선언 순서·상속·Specificity·Origin이 충돌할 때 적용 값을 예측할 수 있는 규칙 |
| Specificity Budget | Override 난립을 막기 위해 선택자 복잡도에 두는 상한 |
| Frozen CSS | 사용자 승인과 회귀 검수를 통과해 동일 버전에서 임의 변경할 수 없는 CSS |
| Semantic Change | Token 의미, Layout, 상태 또는 접근성 동작을 바꾸는 변경 |
| Cosmetic Change | 의미·구조·동작을 바꾸지 않는 제한적 시각 조정 |
| Regression Surface | CSS 변경으로 영향을 받을 수 있어 다시 확인해야 하는 화면·상태·폭의 집합 |
| Platform Sanitization | 게시 채널이 Style·속성·선택자를 제거하거나 재작성하는 현상 |

# 4. CSS 산출물과 연결 방식

## 4.1 산출물 유형

CSS는 독립 Stylesheet, 독립 문서의 `<style>` 블록, 게시용 본문 조각에 포함된 Scoped Style 중 하나로 식별한다. 유형과 연결 경로를 MASTER 또는 Delivery 기록에 남긴다.

## 4.2 단일 기준 원본

같은 Delivery에 중복된 CSS 원본을 병행 운영하지 않는다. 생성 원본과 게시용 삽입본이 다르면 생성 관계·버전·해시와 허용된 변환을 연결한다.

## 4.3 배치 순서

Reset·Base·Token·Layout·Component·Utility·승인 Override의 적용 순서를 명시한다. 순서에 의존하는 규칙은 파일 병합이나 게시 Sanitization 뒤에도 같은 결과가 나는지 확인한다.

# 5. Token 소유권과 선언

## 5.1 의미 이름

Token은 `primary-blue` 같은 일회성 외형보다 `color-accent`, `space-section`, `radius-card`처럼 역할을 드러내는 이름을 우선한다. 프로젝트 Prefix와 Root Scope를 사용해 다른 문서의 변수와 충돌하지 않게 한다.

## 5.2 소유권 분리

DSG-003은 Token의 선언·변경·검증 방식을 정한다. 실제 브랜드 값은 DSG-007과 Project MASTER, 구성요소별 매핑은 DSG-004가 소유한다.

## 5.3 Fallback과 미정 값

필수 Token은 검증 가능한 Fallback을 갖거나 누락 시 생성·Release를 실패시킨다. 미정 값을 임의 색상·간격으로 채우거나 미치환 Placeholder를 출하하지 않는다.

## 5.4 중복과 Drift

같은 의미의 값이 여러 위치에 직접 반복되면 Token 후보로 통합한다. 다만 의미가 다른 우연히 같은 값까지 하나로 묶어 독립 변경을 막지 않는다.

# 6. Root Scope와 선택자

## 6.1 고유 Root Scope

게시용 조각의 모든 규칙은 고유 ID 또는 충돌 가능성이 낮은 Root Class 아래로 제한한다. `body`, `html`, `p`, `h1`, `.card` 같은 전역·범용 선택자를 Root 밖에서 사용하지 않는다.

## 6.2 Class 중심 선택자

재사용 Style은 Class를 우선하고 DOM 깊이나 우연한 Tag 순서에 과도하게 의존하지 않는다. 구조 선택자는 DSG-001과 DSG-004가 보장하는 계약 범위에서만 사용한다.

## 6.3 이름 공간

Class·Custom Property·Animation 이름은 프로젝트 또는 구성요소 Prefix를 사용한다. 외부 플랫폼·플러그인의 흔한 이름과 충돌할 수 있는 단독 이름을 피한다.

# 7. Cascade·Specificity·Override

## 7.1 예측 가능한 Specificity

선택자는 필요한 최소 수준으로 유지한다. ID 반복, 깊은 후손 연결, 불필요한 Tag 결합으로 Specificity를 높이지 않는다.

## 7.2 `!important` 예외

`!important`는 게시 플랫폼의 검증된 상위 스타일을 Scoped 범위 안에서 방어해야 할 때만 허용한다. 사용 이유·적용 범위·제거 조건을 MASTER 또는 QA에 기록한다.

## 7.3 Inline Style

반복 Style은 Class와 Token으로 관리한다. 채널이 `<style>`을 제거하거나 데이터 기반 단일 값이 필요한 경우에만 승인된 Inline Style을 사용하며, 동일 규칙의 이중 원본을 만들지 않는다.

## 7.4 Reset 경계

Reset과 `box-sizing`은 Root 내부 요소에만 적용한다. 플랫폼 전체 Form·관리 UI·본문 바깥 요소의 기본 동작을 바꾸지 않는다.

# 8. Layout과 반응형

## 8.1 모바일 우선 흐름

기본 CSS는 좁은 화면의 한 열 읽기 흐름을 보장하고, 넓은 화면 확장은 최소 폭 조건에서 추가한다. 핵심 정보의 DOM 순서와 시각 순서가 모순되지 않는다.

## 8.2 Breakpoint 근거

Breakpoint는 특정 기기 이름이 아니라 콘텐츠가 깨지는 실제 폭과 Project MASTER 근거로 정한다. 필요하지 않은 다수의 미세 Breakpoint를 만들지 않는다.

## 8.3 사용 가능 폭

Grid·Flex·표·코드·이미지는 Root의 사용 가능 폭을 넘지 않는다. 고정 폭은 승인된 최소·최대 조건과 함께 사용하고 기본 흐름은 유연한 단위를 우선한다.

## 8.4 순서와 숨김

CSS `order`, 시각적 재배치, `display:none`은 의미 순서와 핵심 정보 접근을 훼손하지 않는다. Desktop과 Mobile 사이에서 콘텐츠를 중복 생성해 관리 Drift를 만들지 않는다.

# 9. Typography·색상·상태

## 9.1 글꼴 Stack

글꼴 Stack은 Project MASTER가 승인한 서체와 시스템 Fallback 순서를 명시한다. 외부 글꼴 실패 시 누락 글리프·가독성 붕괴·과도한 Layout Shift가 없어야 한다.

## 9.2 상대 단위와 확대

본문·제목·간격은 사용자 확대와 Root Context를 존중하는 단위를 우선한다. 고정 높이나 작은 절대 글자 크기로 텍스트를 자르지 않는다.

## 9.3 색상과 대비

색상 값의 소유권은 Brand와 MASTER에 있지만, 텍스트·링크·상태는 승인된 대비 기준을 충족해야 한다. 색상만으로 선택·위험·성공을 구분하지 않는다.

## 9.4 Focus와 Motion

보이는 Focus를 제거하지 않는다. Motion이 있으면 핵심 이해에 필수적이지 않아야 하며, 환경과 MASTER가 요구하면 `prefers-reduced-motion` 대체를 제공한다.

# 10. Overflow와 가변 콘텐츠

## 10.1 긴 문자열

URL·코드·영문 식별자·긴 제목이 Root 폭을 밀어내지 않도록 의미를 보존하는 줄바꿈 또는 요소 내부 스크롤을 적용한다. 전체 페이지의 수평 스크롤을 해결책으로 사용하지 않는다.

## 10.2 표와 코드

넓은 표와 코드는 명시된 Wrapper 안에서만 가로 스크롤을 허용한다. Wrapper 밖 본문과 페이지 가구는 고정 폭을 넘지 않는다.

## 10.3 가변 반복

Item·Insight·Action·Source 수가 변해도 Grid와 간격이 자연스럽게 재배치되어야 한다. `nth-child`로 특정 개수에만 맞춘 필수 Layout을 만들지 않는다.

## 10.4 내용 높이

카드·강조 상자·제목은 내용에 따라 확장한다. 시각적 높이 통일을 위해 본문을 자르거나 숨기는 고정 높이·강제 Line Clamp를 기본값으로 사용하지 않는다.

# 11. 외부 자산과 Fallback

## 11.1 외부 의존성 등록

외부 글꼴·Stylesheet·Icon·Script가 CSS 표현에 필요하면 URL, 목적, 버전·가용성·보안·개인정보 영향과 실패 대체를 기록한다.

## 11.2 핵심 가독성 보존

외부 자산이 실패해도 제목·본문·링크·표·출처는 읽을 수 있어야 한다. 장식 효과 실패가 핵심 정보 접근 실패로 이어지지 않게 한다.

## 11.3 미사용 규칙 제거

승인 산출물에 사용되지 않는 Framework 전체, 중복 Reset, 오래된 Component Style을 관성적으로 포함하지 않는다. 제거 시 동적 상태와 조건부 Class 사용 여부를 먼저 확인한다.

# 12. 플랫폼 호환성과 Sanitization

## 12.1 지원 범위

지원하는 브라우저·게시 채널·최소 화면 폭과 미검증 범위를 MASTER 또는 QA에 기록한다. 특정 엔진에서만 우연히 동작하는 비표준 선언을 필수 경로로 삼지 않는다.

## 12.2 Progressive Enhancement

최신 CSS 기능은 지원 환경에서 표현을 향상하는 데 사용할 수 있다. 핵심 읽기·탐색·상태 이해는 지원되지 않을 때도 합리적인 Fallback을 가져야 한다.

## 12.3 Sanitization 후 검수

게시 채널이 `<style>`, Custom Property, 선택자 또는 속성을 제거·재작성할 수 있으면 실제 게시 또는 동일 Sanitization 경로의 결과를 다시 검사한다. 로컬 Preview만으로 게시 PASS를 선언하지 않는다.

# 13. 동결·버전·변경 등급

## 13.1 동결 단위

CSS를 LOCK할 때 원본 경로·버전·상태·해시·연결 MASTER와 지원 화면을 함께 기록한다. 파일 일부만 동결하면 추출 범위와 결합 순서를 명시한다.

## 13.2 변경 등급

변경은 `PATCH`, `MINOR`, `MAJOR` 영향으로 분류한다. 오탈자·동등 표현 교정은 PATCH, 새 Token·상태·Breakpoint 추가는 MINOR, 기존 계약·Scope·시각 의미 파괴는 MAJOR 후보로 본다.

## 13.3 승인 없는 변경 금지

LOCKED CSS는 사용자 승인 없이 값·순서·선택자·주석을 변경하지 않는다. 긴급 수정도 별도 후보본과 회귀 증거를 만든 뒤 승인 경로를 따른다.

## 13.4 생성물과 원본 연결

Minify·병합·Inline 변환본은 규범적 원본을 대체하지 않는다. 생성 도구·입력 해시·출력 해시와 변환 옵션을 기록해 다시 만들 수 있어야 한다.

# 14. 변경 영향과 회귀

## 14.1 영향 표면 식별

변경 전 영향받는 Token, 선택자, Component, 상태, Breakpoint, Delivery와 게시 채널을 식별한다. Class 이름 검색만으로 동적·상속·Custom Property 영향을 놓치지 않는다.

## 14.2 대표 폭과 상태

최소 360px, 대표 390px, Desktop 또는 MASTER 지정 폭을 확인한다. Hover·Focus·Active·Visited·Disabled·긴 콘텐츠·빈 선택 요소 등 실제 지원 상태도 필요한 범위에서 검수한다.

## 14.3 비교 기준

승인 이전 화면 또는 MASTER Render를 기준으로 변경 전후를 비교한다. 의도된 차이와 비의도 차이를 분리하고, 기준 파일과 최종 파일의 정확한 버전·해시를 남긴다.

## 14.4 연결 문서 재검수

CSS 변경이 HTML 구조·Component 계약·Brand Token·게시 결과에 영향을 주면 해당 전담 기준의 Gate도 다시 실행한다. CSS 자체 Syntax PASS만으로 통합 PASS를 선언하지 않는다.

# 15. 검증과 품질 게이트

## 15.1 구조 검수

- CSS Syntax와 중괄호·주석·미디어 쿼리 닫힘
- Root Scope 밖 전역 선택자와 이름 충돌
- 미정 Token, 미치환 Placeholder, 사용되지 않는 필수 변수
- 중복 선언·죽은 Override·과도한 Specificity·무근거 `!important`
- 외부 자산과 Fallback, 원본·생성물 해시 연결

## 15.2 시각 검수

- 360px·390px·Desktop 또는 MASTER 지정 폭의 전체 화면
- 잘림·겹침·수평 넘침·고정 높이·긴 문자열·표·코드
- 제목 계층·본문 리듬·카드 간격·Focus·색상 외 상태 단서
- 가변 Item·Source·Action 수와 빈 선택 요소 제거 후 흐름
- 실제 게시 또는 Sanitization 결과와 로컬 결과의 차이

## 15.3 Gate 판정

Critical 또는 Major 결함이 하나라도 열려 있으면 PASS·LOCK·Release를 선언하지 않는다. REVIEW 문서는 사용자 검토와 실제 프로젝트 회귀 적용 전까지 APPROVED 또는 LOCKED로 표시하지 않는다.

# 16. 변경·승인·LOCK 수명주기

1. 적용 Project·Delivery·지원 폭과 기준 MASTER를 식별한다.
2. Token·Scope·선택자·Cascade·Fallback·변경 경계를 초안으로 작성한다.
3. Markdown·DOCX·PDF와 QA·해시 패키지를 `REVIEW`로 작성한다.
4. 사용자 검토와 수정 후 `APPROVED`로 전환한다.
5. 실제 HTML과 게시 경로에서 대표 폭·상태·가변 콘텐츠 회귀를 실행한다.
6. PASS Evidence와 연결 버전·해시를 기록한다.
7. 명시적 잠금 승인 후 `LOCKED`로 전환한다.

LOCKED 이후 Semantic Change는 같은 파일을 조용히 덮어쓰지 않고 새 버전 후보와 History를 만든다.

# 17. 규칙 카탈로그

## 17.A 계층·산출물

### CSS-001 - 상위 기준 우선
- **Priority:** Critical
- **Statement:** CSS는 사용자 요청, 승인 Schema·MASTER·Brand·Component 계약을 무효화하지 않는다.
- **Verification:** 연결 문서와 구현의 충돌을 대조한다.
- **Exceptions:** 안전·법률·접근성·플랫폼 필수 제한.

### CSS-002 - 명시적 산출물 유형
- **Priority:** High
- **Statement:** 독립 Stylesheet·문서 Style·게시 조각 Scoped Style 중 유형과 연결 경로를 기록한다.
- **Verification:** Delivery Manifest 또는 MASTER 참조를 확인한다.
- **Exceptions:** 단일 파일 내부의 검토용 Prototype.

### CSS-003 - 단일 규범 원본
- **Priority:** Critical
- **Statement:** 같은 Delivery의 CSS 규범 원본을 하나로 유지하고 파생본은 생성 관계와 해시를 연결한다.
- **Verification:** 원본·삽입본·Minify 본의 경로와 해시를 대조한다.
- **Exceptions:** 승인된 다중 테마 Variant.

### CSS-004 - 적용 순서 명시
- **Priority:** High
- **Statement:** Base·Token·Layout·Component·Utility·Override 순서를 예측 가능하게 유지한다.
- **Verification:** 병합 전후 Cascade 결과를 비교한다.
- **Exceptions:** 외부 플랫폼의 고정 Style 삽입 순서.

### CSS-005 - 특정 구현 종속 금지
- **Priority:** High
- **Statement:** 특정 Framework·전처리기·AI·브라우저를 공통 규칙의 유일한 실행 조건으로 요구하지 않는다.
- **Verification:** 규칙 문구와 필수 도구 목록을 감사한다.
- **Exceptions:** Project MASTER가 선언한 제한 환경.

### CSS-006 - 콘텐츠 은폐 금지
- **Priority:** Critical
- **Statement:** 페이지·카드 수나 외형을 맞추기 위해 CSS로 핵심 콘텐츠를 자르거나 숨기지 않는다.
- **Verification:** 고정 높이·Overflow·Line Clamp·Display 규칙을 검사한다.
- **Exceptions:** 접근 가능한 대체 경로가 있는 승인 접기 UI.

## 17.B Token·Scope·Cascade

### CSS-007 - 의미 Token
- **Priority:** High
- **Statement:** 반복 값은 역할 기반 Token으로 선언하고 프로젝트 Prefix와 소유권을 명시한다.
- **Verification:** 직접 값 반복과 Token 이름을 비교한다.
- **Exceptions:** 의미 없는 단일 계산 보정값.

### CSS-008 - 필수 Token 완결성
- **Priority:** Critical
- **Statement:** 필수 Token은 승인 값 또는 안전한 Fallback을 가지며 미치환 값을 남기지 않는다.
- **Verification:** `var()` 참조·Fallback·Placeholder를 검사한다.
- **Exceptions:** Release되지 않는 명시적 Prototype.

### CSS-009 - Root Scope 격리
- **Priority:** Critical
- **Statement:** 게시용 CSS의 모든 규칙은 고유 Root Scope 아래에 있어 외부 페이지를 변경하지 않는다.
- **Verification:** Root 밖 선택자와 실제 게시 페이지 영향 범위를 검사한다.
- **Exceptions:** 독립 전체 문서의 승인된 `html`·`body` Base.

### CSS-010 - 이름 공간 충돌 방지
- **Priority:** High
- **Statement:** Class·Custom Property·Animation 이름에 프로젝트 또는 구성요소 Prefix를 사용한다.
- **Verification:** 범용 단독 이름과 외부 Style 충돌을 검색한다.
- **Exceptions:** 표준 상태 속성과 승인 Utility Namespace.

### CSS-011 - Specificity 예산
- **Priority:** High
- **Statement:** 선택자는 필요한 최소 Specificity를 사용하고 깊은 후손·ID 반복·Tag 결합을 누적하지 않는다.
- **Verification:** 선택자 깊이와 Override 연쇄를 검사한다.
- **Exceptions:** 격리된 외부 Widget 방어 규칙.

### CSS-012 - Override 근거
- **Priority:** Critical
- **Statement:** `!important`와 Inline Style은 검증된 채널 충돌 등 승인 예외에만 사용하고 이유·범위·제거 조건을 기록한다.
- **Verification:** 모든 `!important`와 Style 속성을 근거 기록과 대조한다.
- **Exceptions:** 없음.

## 17.C Layout·시각·접근성

### CSS-013 - 모바일 우선 기본 흐름
- **Priority:** Critical
- **Statement:** 기본 CSS는 좁은 화면 한 열 읽기를 보장하고 넓은 화면 확장은 조건부로 추가한다.
- **Verification:** 360px와 Desktop의 DOM·시각 순서를 비교한다.
- **Exceptions:** 승인된 고정 폭 전문 도면.

### CSS-014 - 근거 있는 Breakpoint
- **Priority:** High
- **Statement:** Breakpoint는 콘텐츠가 깨지는 실제 폭 또는 MASTER 근거로 정의한다.
- **Verification:** 각 Media Query의 목적과 전후 Layout을 확인한다.
- **Exceptions:** 플랫폼이 강제하는 고정 Embed 폭.

### CSS-015 - 사용 가능 폭 준수
- **Priority:** Critical
- **Statement:** Grid·Flex·표·코드·이미지는 Root의 사용 가능 폭을 넘지 않는다.
- **Verification:** 대표 폭에서 요소 경계와 수평 스크롤 범위를 확인한다.
- **Exceptions:** 명시적 Wrapper 내부의 표·코드 스크롤.

### CSS-016 - 가변 Cardinality 안전
- **Priority:** Critical
- **Statement:** 반복 Item 수가 변해도 Layout과 간격이 자연스럽고 특정 `nth-child` 개수에 종속되지 않는다.
- **Verification:** 최소·대표·최대 데이터 Fixture를 렌더한다.
- **Exceptions:** Schema가 고정 수를 강제한 승인 구성요소.

### CSS-017 - 확대와 내용 높이
- **Priority:** Critical
- **Statement:** 텍스트 확대와 긴 내용에서 상자가 확장되며 고정 높이로 본문을 자르지 않는다.
- **Verification:** 확대·장문·다국어 Fixture에서 잘림을 검사한다.
- **Exceptions:** 접근 가능한 대체가 있는 승인 미리보기.

### CSS-018 - 상태 접근성
- **Priority:** Critical
- **Statement:** Focus를 보존하고 색상만으로 상태를 전달하지 않으며 필요한 경우 Reduced Motion 대체를 제공한다.
- **Verification:** 키보드 Focus·대비·상태 Label·Motion 환경을 확인한다.
- **Exceptions:** 의미 없는 장식 Animation.

## 17.D 의존성·변경·회귀

### CSS-019 - 외부 자산 Fallback
- **Priority:** Critical
- **Statement:** 외부 글꼴·Style·Icon 실패에도 핵심 콘텐츠의 읽기와 탐색이 유지된다.
- **Verification:** 외부 요청을 차단한 상태로 렌더한다.
- **Exceptions:** 외부 서비스 자체가 핵심인 승인 Embed.

### CSS-020 - Progressive Enhancement
- **Priority:** High
- **Statement:** 최신 CSS 기능은 향상에 사용하고 미지원 환경에서도 핵심 구조와 정보가 유지되게 한다.
- **Verification:** 지원 범위와 Fallback 선언을 대조한다.
- **Exceptions:** 제한 브라우저가 명시된 내부 도구.

### CSS-021 - Sanitization 재검수
- **Priority:** Critical
- **Statement:** 게시 채널이 Style을 제거·재작성하면 실제 결과 또는 동일 경로를 다시 검수한다.
- **Verification:** 로컬·Sanitized·게시 결과를 비교한다.
- **Exceptions:** Sanitization이 없는 독립 정적 파일.

### CSS-022 - 동결 단위 추적
- **Priority:** Critical
- **Statement:** LOCK 대상의 경로·버전·상태·해시·연결 MASTER·지원 화면을 함께 기록한다.
- **Verification:** Register·Manifest·SHA 파일을 대조한다.
- **Exceptions:** 없음.

### CSS-023 - 변경 등급 분류
- **Priority:** High
- **Statement:** CSS 변경을 PATCH·MINOR·MAJOR 영향으로 분류하고 승인·회귀 범위를 연결한다.
- **Verification:** 변경 기록과 실제 선택자·Token 영향을 비교한다.
- **Exceptions:** 해시에 영향을 주지 않는 외부 전달 메타데이터.

### CSS-024 - LOCKED 무단 변경 금지
- **Priority:** Critical
- **Statement:** LOCKED CSS는 사용자 승인 없이 값·순서·선택자·주석을 변경하지 않는다.
- **Verification:** 승인본 해시와 현재 파일을 비교한다.
- **Exceptions:** 별도 후보본으로 수행하는 긴급 수정.

## 17.E QA·수명주기

### CSS-025 - 영향 표면 식별
- **Priority:** Critical
- **Statement:** 변경 전 Token·선택자·Component·상태·Breakpoint·Delivery·채널의 영향 표면을 기록한다.
- **Verification:** 검색 결과와 상속·동적 Class·Custom Property 관계를 대조한다.
- **Exceptions:** 독립된 미사용 Prototype.

### CSS-026 - 대표 폭 전수 검수
- **Priority:** Critical
- **Statement:** 최소 360px·대표 390px·Desktop 또는 MASTER 지정 폭에서 전체 화면을 검수한다.
- **Verification:** 폭별 Render Evidence와 수평 Overflow를 확인한다.
- **Exceptions:** MASTER가 다른 명시적 지원 폭을 정한 경우.

### CSS-027 - 상태·가변 데이터 회귀
- **Priority:** High
- **Statement:** 지원 상태와 최소·대표·최대 Cardinality에서 잘림·겹침·간격·순서를 검수한다.
- **Verification:** Fixture와 화면 증거를 대조한다.
- **Exceptions:** 상태 또는 반복이 없는 정적 구성요소.

### CSS-028 - 통합 Gate 재실행
- **Priority:** Critical
- **Statement:** CSS 변경이 HTML·Component·Brand·게시 결과에 영향을 주면 해당 전담 Gate도 다시 실행한다.
- **Verification:** 연결 QA 결과와 변경 버전을 확인한다.
- **Exceptions:** 영향 없음이 구조적으로 입증된 주석 교정.

### CSS-029 - 열린 결함 Release 금지
- **Priority:** Critical
- **Statement:** 열린 Critical 또는 Major CSS 결함이 있으면 PASS·LOCK·Release를 선언하지 않는다.
- **Verification:** Defect Register와 Gate 판정을 대조한다.
- **Exceptions:** 없음.

### CSS-030 - 변경 후 해시 갱신
- **Priority:** Critical
- **Statement:** CSS·MASTER·생성 옵션·게시 경로가 바뀌면 최종 파일과 해시를 다시 검증한다.
- **Verification:** QA 대상 해시와 최종 패키지 해시를 비교한다.
- **Exceptions:** 해시에 영향을 주지 않는 외부 전달 메타데이터.

# 18. AI용 압축 CSS Governance

## 18.1 압축 지침

다음 블록은 DSG-003이 `APPROVED` 또는 `LOCKED`된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 `LOCKED`이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-003 CSS GOVERNANCE v2.0을 따른다.
1. 승인 Schema·Project MASTER·Brand·Component가 의미와 실제 값을 결정하며 CSS Governance는 선언·적용·동결·변경·검수 하한선만 제공한다.
2. CSS 산출물 유형과 단일 규범 원본을 식별하고 파생·병합·Minify·Inline 본은 버전·경로·입출력 해시로 연결한다.
3. 반복 값은 소유권이 명확한 의미 Token으로 관리하고 필수 Token의 미정 값과 Placeholder를 출하하지 않는다.
4. 게시용 규칙은 고유 Root Scope 아래로 격리하고 Class·변수·Animation에 이름 공간을 적용해 외부 페이지를 변경하지 않는다.
5. 선택자 Specificity를 최소화하고 `!important`와 Inline Style은 검증된 채널 충돌의 승인 예외로만 사용한다.
6. 기본 Layout은 모바일 한 열에서 읽히며 Breakpoint는 실제 콘텐츠 파손 근거로 정하고 표·코드·이미지의 Overflow를 요소 내부에서 제어한다.
7. 긴 제목·다국어·텍스트 확대·가변 Item 수에서 상자가 확장되고 고정 높이·숨김·Line Clamp로 핵심 내용을 자르지 않는다.
8. Focus·대비·색상 외 상태 단서와 외부 자산 실패 Fallback을 유지하고 최신 CSS 기능은 Progressive Enhancement로 사용한다.
9. CSS 변경 전 영향 Token·Component·상태·폭·Delivery·게시 채널을 식별하고 360px·390px·Desktop 또는 MASTER 지정 폭과 실제 Sanitization 결과를 재검수한다.
10. LOCKED CSS를 승인 없이 변경하지 않으며 변경 후 연결 Gate와 해시를 갱신하고 Critical 또는 Major 결함이 열려 있으면 Release하지 않는다.
```

## 18.2 추출 조건

- DSG-003이 `APPROVED` 또는 `LOCKED` 상태다.
- 실제 Project MASTER·Brand·Component 계약과 충돌하지 않는지 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| CSS Token·Scope·Cascade·동결·변경·회귀는? | DSG-003 CSS GOVERNANCE |
| HTML 의미 구조와 모바일 DOM 안전은? | DSG-001 HTML SYSTEM |
| DOCX 조판과 PDF 변환은? | DSG-002 DOCX SYSTEM |
| 재사용 UI 구성요소의 구조·상태·Variant는? | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·대체 설명은? | DSG-005 IMAGE SYSTEM |
| 썸네일 비율과 안전 영역은? | DSG-006 THUMBNAIL RULES |
| 프로젝트 색상·로고·서체 조합은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 게시 채널의 발행·수정·삭제는? | CNT-006 PUBLISHING SYSTEM |
| 자동 빌드·배포·실패 복구는? | AUT 문서 |

## 19.2 알려진 제한

- 현재 기준은 정적 콘텐츠형 HTML과 외부 게시 채널 게시용 본문 조각에서 추출했다.
- 복잡한 Web App, Shadow DOM, CSS-in-JS, 사용자 테마 전환과 대규모 Design Token 배포는 실제 적용 검증 전이다.
- 실제 Token 값·Component Variant·Brand 자산은 후속 DSG 문서와 Project MASTER에서 확정한다.
- 브라우저·게시 채널별 Sanitization과 지원 범위는 대상 Delivery마다 별도 검증이 필요하다.
- 이 문서는 사용자 승인을 받은 `APPROVED` 기준본이지만 실제 HTML·게시 경로 회귀 적용과 명시적 잠금 승인 전에는 `LOCKED` 또는 운영 Release로 자동 전환하지 않는다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | LOCKED `PROJECT_REFERENCE_FIXTURE` v1.0.1 BLOG_SUMMARY_HTML와 DSG-001 경계에서 Root Scope·Token·Cascade·반응형·동결·변경 영향·회귀 검수 원칙을 분리하고 사용자 승인·잠금 승인 완료 |
