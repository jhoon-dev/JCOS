# JCOS v2.0.0 - DSG-001 HTML SYSTEM

## HTML 구조 원칙

| Field | Value |
|---|---|
| Document ID | DSG-001 |
| Title | HTML SYSTEM |
| Korean Title | HTML 구조 원칙 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS가 생성·관리하는 HTML 문서와 게시용 HTML 조각 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / BLOG_SUMMARY_HTML |
| Depends On | FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 참조 프로젝트의 잠금된 HTML에서 실제 검증된 공통 구조 원칙만 분리해 사용자 승인과 명시적 잠금 승인을 받은 `LOCKED` 기준본이다. 프로젝트별 콘텐츠, 브랜드 토큰, 게시 절차와 자동화 규칙을 추가하지 않는다.

## 문서 목적

DSG-001은 JCOS HTML 산출물이 채널과 프로젝트가 달라도 의미 구조, 모바일 안전성, 접근성, 이식성과 검수 가능성을 일관되게 유지하도록 공통 구조 계약을 정의한다.

이 문서는 특정 프로젝트의 HTML MASTER를 대체하지 않는다. 프로젝트별 정보 계층과 시각 표현은 승인된 Content Schema와 MASTER가 결정하며, DSG-001은 HTML로 투영할 때 지켜야 할 공통 경계와 검증 기준만 제공한다.

## 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. HTML 산출물 유형
5. 문서 루트와 의미 구조
6. 정보 계층과 제목
7. 모바일 우선 구조
8. 구성요소 구조 계약
9. 표·코드·긴 콘텐츠
10. 링크·출처·탐색
11. 접근성
12. CSS·스크립트·외부 의존성 경계
13. 데이터·가변 반복·플레이스홀더
14. 검증과 품질 게이트
15. 변경·승인·LOCK 수명주기
16. 규칙 카탈로그
17. AI용 압축 HTML System
18. 책임 경계와 알려진 제한
19. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- 완결된 HTML 문서와 게시 플랫폼에 삽입하는 HTML 본문 조각
- 의미 구조, 제목 계층, 탐색, 링크, 표, 코드와 반복 구성요소의 마크업
- 모바일 폭, 긴 문자열, 수평 넘침과 반응형 구조의 최소 안전 조건
- 프로젝트 MASTER를 HTML로 투영할 때 필요한 공통 검수 기준
- 정적 HTML의 이식성, 접근성, 외부 의존성 기록과 실패 처리

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| 색상·간격·선·그림자 토큰의 동결과 변경 | DSG-003 CSS GOVERNANCE |
| 카드·Hero·Timeline 등 승인 구성요소의 세부 명세 | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·대체 텍스트 세부 정책 | DSG-005 IMAGE SYSTEM |
| 프로젝트별 색상·로고·브랜드 표현 | DSG-007 BRAND SYSTEM과 Project MASTER |
| 원고 조사·작성·편집·사실 검증 | CNT-001~004 |
| SEO 제목·메타·태그 전략 | CNT-005 SEO SYSTEM |
| 채널 게시·수정·삭제 절차 | CNT-006 PUBLISHING SYSTEM |
| 예약·재시도·실패 복구 구현 | AUT-002·004·006 |

## 1.3 금지되는 확장

- HTML 구조 문서에서 프로젝트 콘텐츠 필드나 Item 수를 새로 정의
- 참조 프로젝트의 Hero·카드·색상 체계를 모든 프로젝트의 시각 표준으로 강제
- 특정 블로그, 브라우저, AI 서비스 또는 편집기를 유일한 실행 환경으로 요구
- 일일 Output의 우연한 구조를 승인된 MASTER보다 우선
- 게시·예약·API 구현을 HTML 구조 규칙에 혼합

# 2. 계층과 권한

## 2.1 권한 순서

HTML 산출물은 다음 순서로 해석한다.

1. 안전·법률·게시 플랫폼 필수 제한
2. 사용자의 현재 명시적 요청
3. 승인된 Project Content Schema와 MASTER
4. DSG-001 HTML SYSTEM
5. DSG-003 CSS GOVERNANCE와 DSG-004 COMPONENT LIBRARY
6. Execution과 날짜별 입력
7. 참고 HTML과 과거 Output

## 2.2 MASTER 우선

DSG-001은 공통 구조의 하한선이다. 승인 MASTER가 더 구체적인 구조를 정의하면 그 구조를 따르되, 의미 손실·접근성 저하·모바일 넘침 또는 검증 불가능 상태를 허용하지 않는다.

## 2.3 참조 구현의 역할

`PROJECT_REFERENCE_FIXTURE` v1.0.1의 `BLOG_SUMMARY_HTML`은 다음 항목을 실제로 검증한 참조 구현이다.

- 하나의 범위가 지정된 Article 루트
- Hero, 내부 목차, 의미 Section, 반복 카드, 표 Wrapper, 코드 블록과 Source 목록
- 720px 이하 단일 열 전환
- 긴 문자열 줄바꿈과 표의 수평 스크롤 보호
- 외부 Script·Stylesheet·Image 의존성 없는 게시용 본문 조각

이 구현의 프로젝트 전용 클래스명, 색상, 섹션 수와 카드 수는 공통 규칙이 아니다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| HTML Document | `html`, `head`, `body`를 포함해 독립 실행 가능한 문서 |
| HTML Fragment | 게시 플랫폼의 본문 영역에 삽입하는 범위 지정 HTML 조각 |
| Root Scope | 산출물의 CSS·ID·탐색 범위를 한정하는 최상위 고유 요소 |
| Semantic Region | `article`, `main`, `section`, `nav`, `header`, `footer`처럼 역할이 명확한 영역 |
| Component Instance | 같은 의미·구조 계약을 따라 실제 데이터만 달라지는 반복 요소 |
| Overflow Safety | 좁은 화면이나 긴 값에서도 내용이 잘리거나 화면 폭을 강제로 넓히지 않는 상태 |
| External Dependency | 외부 URL·API·글꼴·스크립트·스타일·이미지·권한에 의존하는 요소 |
| Progressive Enhancement | 핵심 내용을 기본 HTML로 제공하고 추가 기능 실패 시에도 읽을 수 있게 하는 방식 |
| Placeholder | 실제 값으로 치환하기 위한 명시적 입력 표식 |

# 4. HTML 산출물 유형

## 4.1 독립 문서

독립 문서는 유효한 문서 선언, 언어, 문자 인코딩, viewport와 제목을 가진다. 문서 단독 저장·재개봉·브라우저 표시가 가능해야 한다.

## 4.2 게시용 본문 조각

본문 조각은 대상 플랫폼이 문서 Shell을 제공한다는 전제에서 하나의 고유 Root Scope 아래 콘텐츠와 필요한 범위 지정 스타일을 포함한다. 전역 `body`, 무범위 태그 선택자와 다른 게시물에 영향을 주는 규칙을 사용하지 않는다.

## 4.3 Delivery Variant 명시

같은 논리 Output이 독립 문서와 게시용 요약 조각으로 나뉠 수 있다. 각 Variant는 정보량, 허용 태그, Style 포함 방식과 누락 가능한 필드를 Manifest 또는 MASTER에 명시한다. Variant 차이를 새 사실이나 새 해석을 추가하는 권한으로 사용하지 않는다.

# 5. 문서 루트와 의미 구조

## 5.1 단일 콘텐츠 루트

하나의 산출물은 주 콘텐츠를 감싸는 단일 Root Scope를 가진다. Root ID는 문서나 Output을 식별할 수 있어야 하며 같은 페이지에서 중복되지 않아야 한다.

## 5.2 의미 요소 우선

- 독립적인 글은 `article`, 페이지의 유일한 본문은 `main`을 우선한다.
- 제목이 있는 주제 묶음은 `section`으로 구성한다.
- 내부 목차는 `nav`와 목적을 설명하는 접근성 Label을 사용한다.
- 단순 배치 목적으로 의미 요소를 남용하지 않는다.
- 일반 컨테이너는 의미 요소로 표현하기 어려운 레이아웃 그룹에만 사용한다.

## 5.3 DOM 순서

DOM 순서는 CSS가 없거나 보조 기술로 읽어도 정보의 이해 순서와 일치해야 한다. 시각적 Grid 순서를 만들기 위해 핵심 문장을 DOM 뒤쪽으로 보내지 않는다.

## 5.4 구획 독립성

각 Section은 제목과 내용의 관계가 명확해야 한다. 카드·표·코드 블록은 어느 제목에 속하는지 DOM과 시각 구조 모두에서 식별할 수 있어야 한다.

# 6. 정보 계층과 제목

## 6.1 단일 주제 제목

하나의 독립 HTML 산출물은 주제 `h1`을 하나만 사용한다. 게시 플랫폼이 별도 페이지 제목을 제공하더라도 본문 조각의 Master 계약이 `h1`을 요구하면 중복 노출 여부를 대상 환경에서 검수한다.

## 6.2 제목 단계

- 제목 단계는 문서 구조를 나타내며 글자 크기만을 위한 선택이 아니다.
- `h1` 다음의 주요 구획은 `h2`, 그 하위는 `h3`을 사용한다.
- 시각적 크기를 이유로 단계를 건너뛰지 않는다.
- 반복 카드의 제목은 상위 Section 제목 아래 동일한 단계로 유지한다.

## 6.3 독자용 정보만 노출

QA 상태, Binding 해시, 내부 검수 추적과 템플릿 운영 메모는 독자용 본문에 넣지 않는다. 사용자에게 필요한 불확실성·한계·출처는 읽기 쉬운 콘텐츠로 표현한다.

# 7. 모바일 우선 구조

## 7.1 기본 흐름

기본 HTML은 한 열의 자연스러운 문서 흐름으로 읽을 수 있어야 한다. 다열 Grid와 복잡한 배치는 충분한 폭에서만 추가한다.

## 7.2 전환 조건

Breakpoint 값은 Project MASTER가 정한다. 공통 기준은 카드·제목·표·탐색이 겹치거나 지나치게 좁아지기 전에 단일 열 또는 스크롤 안전 구조로 전환하는 것이다.

## 7.3 긴 문자열

URL, 영문 제품명, 해시, 코드와 붙어 있는 숫자는 화면 밖으로 밀려나지 않아야 한다. 일반 텍스트에는 의미를 보존하는 줄바꿈을 적용하고, URL·해시처럼 분리 가능한 값은 `overflow-wrap:anywhere`와 동등한 보호를 제공한다.

## 7.4 터치와 탐색

링크와 버튼이 인접할 때 오작동 없이 선택할 수 있는 간격을 확보한다. 내부 목차와 긴 문서는 모바일에서 과도한 탐색 부담을 만들지 않도록 항목을 읽기 순서대로 제공한다.

## 7.5 검수 폭

Project MASTER가 별도 폭을 정하지 않으면 최소 360px, 대표 390px와 데스크톱 폭에서 핵심 구조를 확인한다. 특정 기기 이름보다 실제 Viewport 폭을 QA 기록에 남긴다.

# 8. 구성요소 구조 계약

## 8.1 공통 원칙

구성요소는 시각 상자가 아니라 의미 단위다. 같은 역할의 반복 요소는 같은 DOM 골격, 제목 단계, 데이터 순서와 상태 표현을 사용한다.

## 8.2 Hero

Hero는 문서 식별, 주 제목, 날짜 또는 핵심 Lead처럼 시작에 필요한 정보만 포함한다. 장식 때문에 본문 시작을 과도하게 밀어내거나 제목 왼쪽을 잘라서는 안 된다.

## 8.3 Summary·Role Card

카드는 독립된 요약이나 비교 단위에 사용한다. 일반 문단을 모두 카드로 감싸지 않으며, 카드 수는 실제 데이터 Cardinality를 따른다. 좁은 화면에서는 한 열로 전환하고 DOM 읽기 순서를 유지한다.

## 8.4 Highlight·Note

강조 상자는 판단, 경고, 핵심 요약처럼 일반 본문과 구분할 이유가 있을 때만 사용한다. 색상만으로 의미를 전달하지 않고 Label이나 문장으로 역할을 표시한다.

## 8.5 Timeline·Action

시간 순서나 실행 순서가 실제 의미일 때 목록 구조를 사용한다. 단순 장식 숫자나 날짜를 위해 순서 의미를 만들지 않는다.

## 8.6 Source List

출처는 읽을 수 있는 Publisher·Title·Locator 관계를 유지한다. 독자용 목록은 과도한 표보다 단순한 인라인 목록을 우선하며, 프로젝트 MASTER가 정의한 회색 보조 계층을 사용할 수 있다.

# 9. 표·코드·긴 콘텐츠

## 9.1 표 사용 조건

표는 여러 행이 같은 열 의미를 공유해 비교·조회가 쉬워질 때만 사용한다. 일반 설명, 한 문장짜리 상태와 카드형 콘텐츠를 표로 포장하지 않는다.

## 9.2 표 구조

- 열 머리는 `th`로 표시하고 필요한 경우 `scope`를 지정한다.
- 논리적 머리행과 본문을 구분한다.
- 셀 병합은 모바일 읽기와 보조 기술 해석을 복잡하게 만들면 사용하지 않는다.
- 표 앞뒤의 제목·설명·출처 관계를 유지한다.

## 9.3 모바일 표

표는 내용을 임의 삭제하거나 글자를 읽기 어려운 크기로 축소하지 않는다. 필요한 최소 폭이 Viewport보다 넓으면 범위가 지정된 Wrapper 안에서 수평 스크롤을 제공하고 페이지 전체의 수평 넘침은 막는다.

## 9.4 코드와 프롬프트

코드·명령·프롬프트는 `pre`와 `code`의 의미를 유지한다. 공백과 줄바꿈을 보존하고 구성요소 내부에서만 스크롤되도록 하며, 긴 코드가 전체 페이지 폭을 넓히지 않게 한다.

# 10. 링크·출처·탐색

## 10.1 링크 목적

링크 텍스트는 단독으로 읽어도 이동 목적을 이해할 수 있어야 한다. `여기`, `클릭`만으로 목적을 표시하지 않는다.

## 10.2 외부 링크

새 창을 사용하는 외부 링크는 대상 환경과 사용자 경험상 필요할 때만 적용한다. `target="_blank"`를 사용하면 `rel="noopener"` 또는 동등한 보호를 함께 사용한다.

## 10.3 내부 목차

내부 목차의 모든 Fragment 링크는 실제 고유 ID와 연결되어야 한다. 중복 ID, 빈 Target과 끊어진 링크를 허용하지 않는다.

## 10.4 출처 Locator

실제 Locator를 확인할 수 없으면 추정 URL을 만들지 않는다. 미확인 Locator는 프로젝트 Source Policy에 따라 상태를 기록하고 게시용 활성 링크로 가장하지 않는다.

# 11. 접근성

## 11.1 언어와 문자

독립 문서는 주 언어와 UTF-8을 명시한다. 본문 조각은 대상 플랫폼의 문서 언어를 상속하되, 다른 언어 구절이 읽기에 중요한 경우 해당 범위를 표시할 수 있다.

## 11.2 키보드와 Focus

상호작용 요소는 키보드로 접근 가능해야 하며 보이는 Focus를 제거하지 않는다. 클릭 가능한 `div`보다 목적에 맞는 링크나 버튼 요소를 사용한다.

## 11.3 색상과 상태

상태, 위험, 성공과 구분을 색상 하나에만 의존하지 않는다. 텍스트 Label, 아이콘 설명 또는 구조 차이를 함께 제공한다.

## 11.4 이미지 대체

정보성 이미지는 목적을 설명하는 대체 텍스트를 가져야 한다. 장식 이미지는 보조 기술에서 불필요하게 반복되지 않도록 처리한다. 세부 정책은 DSG-005를 따른다.

## 11.5 확대와 재배치

텍스트 확대와 좁은 화면 재배치에서 핵심 내용이 잘리거나 겹치지 않아야 한다. 고정 높이는 콘텐츠 길이가 변하는 카드·제목·본문에 사용하지 않는다.

# 12. CSS·스크립트·외부 의존성 경계

## 12.1 CSS 범위

게시용 조각의 CSS는 고유 Root Scope 아래로 제한한다. 전역 Tag, 범용 Class와 대상 플랫폼의 관리자 UI에 영향을 주는 선택자를 사용하지 않는다. 구체적인 토큰과 변경 절차는 DSG-003에서 정의한다.

## 12.2 Inline Style과 `!important`

일반 HTML 문서에서는 재사용 가능한 Class를 우선한다. 게시 플랫폼의 기존 CSS가 강하게 개입하는 경우에만 범위가 지정된 선택자에서 Inline Style 또는 `!important`를 예외로 허용하고 MASTER와 QA에 이유를 남긴다.

## 12.3 스크립트

핵심 콘텐츠는 JavaScript 없이도 읽을 수 있어야 한다. Script가 필요한 상호작용은 기능, 권한, 실패 시 대체 경로와 외부 의존성을 명시하며 대상 플랫폼이 허용하지 않으면 제거한다.

## 12.4 외부 자산

외부 글꼴, 스타일, Script, 이미지와 Embed는 가용성·개인정보·보안·성능 영향을 기록한다. 외부 자산 실패가 본문 가독성이나 핵심 정보 접근을 차단하면 Release할 수 없다.

## 12.5 글꼴 Stack

웹 글꼴은 하나의 설치 환경을 전제하지 않고 읽을 수 있는 Fallback Stack을 가진다. 참조 프로젝트 참조 구현은 System UI, Segoe UI, Noto Sans KR, Malgun Gothic 계열을 사용했지만 프로젝트별 Stack은 MASTER가 승인한다.

# 13. 데이터·가변 반복·플레이스홀더

## 13.1 Schema 기반 투영

HTML 요소는 승인된 Content Schema의 실제 필드에서 생성한다. HTML 편의를 이유로 새로운 사실 필드, 추정 값이나 내부 상태를 독자용 콘텐츠에 추가하지 않는다.

## 13.2 가변 Cardinality

Item, Summary, Insight, Action, Timeline과 Source 수는 실제 적격 데이터에 따라 반복·병합·삭제한다. MASTER의 예시 슬롯 수를 고정 요구사항으로 해석하지 않는다.

## 13.3 미사용 요소 제거

값이 없는 선택 구성요소는 빈 카드, 빈 제목, 빈 행이나 숨겨진 Placeholder로 남기지 않고 구조 전체를 제거한다. 제거 후 제목 단계와 인접 간격을 다시 검수한다.

## 13.4 Placeholder 실패

`[[...]]`, `{{...}}`, `TBD`, `TODO` 등 미치환 표식이 최종 독자용 HTML에 남으면 Delivery FAIL이다. 값을 확인할 수 없으면 추정하지 않고 실행을 중지하거나 허용된 누락 처리로 전환한다.

## 13.5 안전한 문자열 처리

데이터를 HTML에 삽입할 때 Markup과 Text의 경계를 구분한다. 신뢰하지 않은 값은 실행 가능한 HTML로 해석하지 않고 이스케이프하거나 승인된 Sanitization 절차를 사용한다.

# 14. 검증과 품질 게이트

## 14.1 구조 QA

- [ ] 산출물 유형이 독립 문서 또는 본문 조각으로 명시됐다.
- [ ] 단일 Root Scope와 고유 ID를 확인했다.
- [ ] `h1`과 하위 제목 단계가 논리적으로 연결된다.
- [ ] DOM 순서가 CSS 없이도 읽기 순서와 일치한다.
- [ ] 반복 요소가 같은 구조 계약을 따른다.

## 14.2 내용·데이터 QA

- [ ] 승인 Schema와 MASTER의 필드만 투영했다.
- [ ] 실제 Cardinality만큼 요소를 반복하고 미사용 슬롯을 제거했다.
- [ ] 미치환 Placeholder와 빈 필수 요소가 없다.
- [ ] 내부 QA·Binding 메타데이터가 독자용 본문에 노출되지 않는다.
- [ ] Source Label과 Locator가 실제 Source Record에 연결된다.

## 14.3 모바일·렌더 QA

- [ ] 최소 360px, 대표 390px와 데스크톱 폭에서 전체 화면을 검사했다.
- [ ] 제목·카드·표·코드·URL의 잘림과 겹침이 없다.
- [ ] 다열 요소가 좁은 화면에서 안전하게 재배치된다.
- [ ] 넓은 표와 코드는 구성요소 내부에서만 스크롤된다.
- [ ] 페이지 전체에 의도하지 않은 수평 스크롤이 없다.

## 14.4 링크·접근성 QA

- [ ] 중복 ID와 끊어진 내부 링크가 없다.
- [ ] 외부 링크의 목적과 새 창 보호 속성이 적절하다.
- [ ] 제목, 목록, 표, 링크와 버튼이 의미 요소로 표현된다.
- [ ] 키보드 Focus와 색상 외 상태 단서가 유지된다.
- [ ] 독립 문서는 언어, UTF-8과 viewport를 명시한다.

## 14.5 의존성·보존 QA

- [ ] 외부 Script·Style·Font·Image·Embed를 목록화했다.
- [ ] 외부 의존성 실패 시 핵심 콘텐츠를 읽을 수 있다.
- [ ] 기존 사용자 파일과 승인 MASTER를 덮어쓰지 않았다.
- [ ] 최종 파일 해시와 검수 대상을 연결했다.

## 14.6 판정

Critical 또는 Major 결함이 하나라도 열려 있으면 PASS나 운영 Release를 선언하지 않는다. `APPROVED` 문서는 실제 프로젝트 회귀 적용과 명시적 잠금 승인 전까지 `LOCKED`로 표시하지 않는다.

# 15. 변경·승인·LOCK 수명주기

1. 잠금된 실제 HTML에서 공통 후보 원칙을 추출한다.
2. Project 전용 시각·콘텐츠 규칙을 제거하고 책임 문서에 남긴다.
3. Markdown·DOCX·PDF와 QA·해시 패키지를 `REVIEW`로 작성한다.
4. 사용자 검토와 수정 후 `APPROVED`로 전환한다.
5. 참조 프로젝트 HTML에 회귀 적용해 구조·모바일·접근성·이식성을 검증한다.
6. 다른 프로젝트 또는 두 번째 HTML 유형에서 재사용 가능성을 확인한다.
7. 명시적 잠금 승인 후 `LOCKED`로 전환한다.

의미 구조, 적용 범위, 필수 QA 또는 책임 경계가 바뀌면 버전을 증가시킨다. 승인된 기존 버전은 History에 보존하며 파일을 조용히 덮어쓰지 않는다.

# 16. 규칙 카탈로그

## 16.A 권한과 범위

### HTML-001 - Project MASTER 우선
- **Priority:** Critical
- **Statement:** 프로젝트별 정보 계층과 시각 구조는 승인된 Content Schema와 MASTER를 우선한다.
- **Verification:** 적용 Project의 Binding과 HTML 구조를 대조한다.
- **Exceptions:** 안전·법률·플랫폼 필수 제한 또는 사용자의 명시적 변경 승인.

### HTML-002 - 단일 책임
- **Priority:** High
- **Statement:** HTML SYSTEM은 공통 구조 계약만 정의하고 콘텐츠·브랜드·게시·자동화 규칙을 새로 만들지 않는다.
- **Verification:** 규칙별 전담 문서와 중복 여부를 확인한다.
- **Exceptions:** 책임 경계를 설명하기 위한 참조.

### HTML-003 - 산출물 유형 명시
- **Priority:** High
- **Statement:** 독립 문서와 게시용 본문 조각 중 어떤 형식인지 명시하고 각 형식의 필수 Shell을 구분한다.
- **Verification:** README·MASTER·실제 파일을 대조한다.
- **Exceptions:** 없음.

## 16.B 의미 구조

### HTML-004 - 단일 Root Scope
- **Priority:** Critical
- **Statement:** 하나의 HTML 산출물은 주 콘텐츠와 스타일 범위를 한정하는 고유 Root Scope를 가져야 한다.
- **Verification:** Root 수, ID 고유성과 선택자 범위를 검사한다.
- **Exceptions:** 독립 문서의 전역 Shell 규칙.

### HTML-005 - 의미 요소 우선
- **Priority:** High
- **Statement:** 문서·구획·탐색·목록·표·링크·버튼은 역할에 맞는 의미 요소로 표현한다.
- **Verification:** DOM 역할과 보이는 역할을 비교한다.
- **Exceptions:** 의미 요소로 표현하기 어려운 순수 레이아웃 Wrapper.

### HTML-006 - DOM 읽기 순서
- **Priority:** Critical
- **Statement:** DOM 순서는 CSS와 Script가 없어도 이해 가능한 읽기 순서와 일치해야 한다.
- **Verification:** Style을 제거한 텍스트 순서를 확인한다.
- **Exceptions:** 없음.

### HTML-007 - 제목 단계 연속성
- **Priority:** High
- **Statement:** 주 제목과 하위 제목은 의미 단계에 따라 연결하고 시각 크기를 위해 단계를 건너뛰지 않는다.
- **Verification:** `h1`~`h6` 순서와 Section 관계를 검사한다.
- **Exceptions:** 외부 플랫폼이 접근 가능한 페이지 제목을 별도로 제공하는 경우 기록.

## 16.C 모바일과 Overflow

### HTML-008 - 모바일 우선 기본 흐름
- **Priority:** Critical
- **Statement:** 기본 콘텐츠는 한 열의 자연스러운 흐름으로 읽을 수 있고 넓은 화면에서만 다열 배치를 추가한다.
- **Verification:** 360px에서 콘텐츠 순서와 폭을 확인한다.
- **Exceptions:** 승인 MASTER가 다른 최소 Viewport를 명시한 전용 화면.

### HTML-009 - 다열 안전 전환
- **Priority:** High
- **Statement:** 다열 카드와 Grid는 내용이 지나치게 좁아지기 전에 한 열 또는 안전한 대체 구조로 전환한다.
- **Verification:** Breakpoint 전후 렌더를 비교한다.
- **Exceptions:** 의미상 고정 비교가 필요하고 내부 스크롤을 제공하는 경우.

### HTML-010 - 긴 문자열 보호
- **Priority:** Critical
- **Statement:** URL·영문명·해시·코드는 페이지 폭을 강제로 넓히거나 잘려서는 안 된다.
- **Verification:** 긴 제목·URL·코드 경계값을 렌더링한다.
- **Exceptions:** 의미 보존을 위해 구성요소 내부 수평 스크롤이 필요한 코드·표.

### HTML-011 - 전체 페이지 수평 넘침 금지
- **Priority:** Critical
- **Statement:** 표·코드 등 넓은 요소의 넘침은 해당 Wrapper 안에서 처리하고 전체 페이지에 의도하지 않은 수평 스크롤을 만들지 않는다.
- **Verification:** Viewport와 Document 폭을 비교한다.
- **Exceptions:** 승인된 캔버스형 전용 화면.

## 16.D 구성요소와 데이터

### HTML-012 - 구조 계약 일치
- **Priority:** High
- **Statement:** 같은 역할의 반복 구성요소는 동일한 DOM 골격, 데이터 순서와 제목 단계를 사용한다.
- **Verification:** 반복 Instance의 구조를 비교한다.
- **Exceptions:** Schema가 다른 Variant를 명시한 경우.

### HTML-013 - 실제 Cardinality
- **Priority:** Critical
- **Statement:** 반복 요소 수는 실제 적격 데이터에 따라 결정하고 MASTER의 예시 슬롯 수를 고정값으로 사용하지 않는다.
- **Verification:** Schema Record 수와 DOM Instance 수를 비교한다.
- **Exceptions:** 승인 Schema가 정확한 고정 수를 요구하는 경우.

### HTML-014 - 빈 구성요소 제거
- **Priority:** High
- **Statement:** 값이 없는 선택 요소는 빈 카드·제목·행으로 남기지 않고 구성요소 전체를 제거한다.
- **Verification:** 빈 요소와 보이는 Placeholder를 검색한다.
- **Exceptions:** 사용자 입력용 Form의 의도된 빈 Field.

### HTML-015 - 미치환 Placeholder 금지
- **Priority:** Critical
- **Statement:** 최종 독자용 HTML에 템플릿 Placeholder, TODO 또는 추정 대체값을 남기지 않는다.
- **Verification:** 표식 Pattern과 빈 필수 필드를 검사한다.
- **Exceptions:** 명시적으로 전달하는 REVIEW 템플릿 자체.

### HTML-016 - 안전한 문자열 삽입
- **Priority:** Critical
- **Statement:** 신뢰하지 않은 데이터는 실행 가능한 Markup으로 해석하지 않고 Text로 처리하거나 승인된 Sanitization을 적용한다.
- **Verification:** 태그·속성·URL 주입 경계값을 검사한다.
- **Exceptions:** 검수된 승인 HTML Fragment를 의도적으로 삽입하는 Field.

## 16.E 표·코드·링크

### HTML-017 - 표의 실제 비교성
- **Priority:** Medium
- **Statement:** 표는 반복 행이 같은 열 의미를 공유하는 비교·조회 데이터에만 사용한다.
- **Verification:** 행·열 관계와 대체 표현을 검토한다.
- **Exceptions:** 대상 플랫폼이 Form이나 데이터 Grid를 요구하는 경우.

### HTML-018 - 표 머리 구조
- **Priority:** High
- **Statement:** 표의 열·행 머리와 본문 관계를 의미 Markup으로 표현한다.
- **Verification:** `table`, `thead`, `tbody`, `th`와 Scope를 검사한다.
- **Exceptions:** 한 행의 단순 Key-Value 표는 더 적절한 구조로 대체 가능.

### HTML-019 - 코드 의미와 Overflow
- **Priority:** High
- **Statement:** 코드·명령·프롬프트는 `pre`·`code`의 공백 보존과 내부 Overflow 안전성을 유지한다.
- **Verification:** 긴 코드와 줄바꿈 렌더를 검사한다.
- **Exceptions:** 한 단어 수준의 Inline Code.

### HTML-020 - 설명 가능한 링크
- **Priority:** High
- **Statement:** 링크 텍스트는 단독으로 읽어도 목적을 이해할 수 있어야 한다.
- **Verification:** 링크 Text와 Target을 대조한다.
- **Exceptions:** 문맥상 목적이 바로 앞 Label로 명확한 짧은 반복 목록.

### HTML-021 - 내부 링크 무결성
- **Priority:** Critical
- **Statement:** 내부 목차의 모든 Target은 실제 고유 ID와 일치해야 한다.
- **Verification:** 중복 ID, 빈 Target과 끊어진 Fragment를 검사한다.
- **Exceptions:** 없음.

### HTML-022 - 외부 링크 보호
- **Priority:** High
- **Statement:** 새 창 외부 링크는 목적이 있어야 하며 Opener 격리 등 필요한 보호를 적용한다.
- **Verification:** `target`과 `rel` 조합을 검사한다.
- **Exceptions:** 대상 플랫폼이 속성을 안전하게 재작성하는 경우 결과 DOM을 확인한다.

## 16.F 접근성과 의존성

### HTML-023 - 색상 외 의미 단서
- **Priority:** Critical
- **Statement:** 상태·위험·성공·구분을 색상 하나만으로 전달하지 않는다.
- **Verification:** 색상을 제거한 상태 의미를 확인한다.
- **Exceptions:** 없음.

### HTML-024 - 키보드 접근
- **Priority:** Critical
- **Statement:** 상호작용 요소는 의미 요소와 키보드 Focus를 유지해야 한다.
- **Verification:** Tab 순서와 Focus 표시를 검사한다.
- **Exceptions:** 상호작용이 없는 정적 문서.

### HTML-025 - 고정 높이 금지
- **Priority:** High
- **Statement:** 내용 길이가 변하는 제목·카드·본문에 잘림을 유발하는 고정 높이를 사용하지 않는다.
- **Verification:** 최대 길이 샘플과 텍스트 확대를 검사한다.
- **Exceptions:** 계산된 높이와 Overflow 대체가 있는 승인된 미디어 Frame.

### HTML-026 - CSS 범위 격리
- **Priority:** Critical
- **Statement:** 게시용 조각의 CSS는 고유 Root Scope 밖의 페이지와 관리자 UI에 영향을 주지 않아야 한다.
- **Verification:** 선택자 Prefix와 삽입 전후 페이지를 비교한다.
- **Exceptions:** 독립 문서 Shell의 의도된 전역 Style.

### HTML-027 - 핵심 콘텐츠 Script 비의존
- **Priority:** Critical
- **Statement:** 핵심 내용은 JavaScript 실패나 차단 상태에서도 읽을 수 있어야 한다.
- **Verification:** Script를 비활성화해 본문과 탐색을 확인한다.
- **Exceptions:** 상호작용 자체가 산출물의 핵심이며 대체 설명을 제공하는 승인 App.

### HTML-028 - 외부 의존성 기록
- **Priority:** High
- **Statement:** 외부 Font·Style·Script·Image·Embed의 역할, 위치, 실패 영향과 대체 경로를 기록한다.
- **Verification:** 네트워크 요청과 Manifest를 비교한다.
- **Exceptions:** 외부 의존성이 0건이면 0건으로 기록한다.

## 16.G 검수와 변경

### HTML-029 - 대표 Viewport 전수 검수
- **Priority:** Critical
- **Statement:** 최종 HTML은 승인된 대표 Viewport에서 전체 화면을 검사하고 잘림·겹침·수평 넘침·끊어진 탐색을 확인한다.
- **Verification:** Viewport별 렌더와 QA 기록을 연결한다.
- **Exceptions:** 렌더 환경이 없으면 정적 검사 결과와 미검증 범위를 명시하고 Release하지 않는다.

### HTML-030 - 해시 기반 재검수
- **Priority:** Critical
- **Statement:** HTML 또는 연결된 MASTER·CSS가 변경되면 기존 PASS를 재사용하지 않고 변경된 정확한 파일을 재검수한다.
- **Verification:** QA 대상 해시와 최종 파일 해시를 비교한다.
- **Exceptions:** 해시에 영향을 주지 않는 외부 전달 메타데이터.

# 17. AI용 압축 HTML System

## 17.1 압축 지침

다음 블록은 DSG-001이 `APPROVED` 또는 `LOCKED`된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 `LOCKED`이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-001 HTML SYSTEM v2.0을 따른다.
1. 승인된 Content Schema와 Project MASTER가 HTML의 정보 계층과 시각 구조를 결정하며 HTML SYSTEM은 공통 구조 하한선만 제공한다.
2. 산출물 유형을 독립 문서 또는 게시용 본문 조각으로 명시하고 하나의 고유 Root Scope에서 의미 요소와 DOM 읽기 순서를 유지한다.
3. h1과 하위 제목 단계를 의미에 따라 연결하고 QA·Binding·템플릿 운영 메타데이터는 독자용 본문에 노출하지 않는다.
4. 기본 흐름은 모바일 한 열로 읽을 수 있어야 하며 카드·Grid는 좁은 화면에서 재배치하고 긴 문자열·표·코드는 전체 페이지 폭을 넘기지 않는다.
5. 반복 구성요소는 같은 구조 계약을 사용하되 수는 실제 Schema Cardinality를 따르고 빈 선택 요소와 미치환 Placeholder는 제거한다.
6. 표는 실제 비교 데이터에만 사용하고 머리 구조를 표시하며, 넓은 표와 코드는 범위 지정 Wrapper 안에서만 스크롤되게 한다.
7. 링크 목적, 내부 ID 무결성, 새 창 보호, 키보드 Focus와 색상 외 상태 단서를 확인한다.
8. 게시용 CSS는 Root Scope 밖에 영향을 주지 않고 핵심 콘텐츠는 Script나 단일 외부 자산 실패에도 읽을 수 있어야 한다.
9. 최종 HTML은 최소 360px·대표 390px·데스크톱 또는 MASTER 지정 폭에서 전체 화면을 검사하고 잘림·겹침·수평 넘침·끊어진 탐색을 기록한다.
10. HTML이나 연결 MASTER·CSS가 바뀌면 정확한 최종 파일과 해시를 다시 검수하며 Critical 또는 Major 결함이 열려 있으면 Release하지 않는다.
```

## 17.2 추출 조건

- DSG-001이 `APPROVED` 또는 `LOCKED` 상태다.
- 실제 Project MASTER와 충돌하지 않는지 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 섹션을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 18. 책임 경계와 알려진 제한

## 18.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| HTML의 의미 구조와 모바일 안전 하한선은? | DSG-001 HTML SYSTEM |
| DOCX 문서 디자인은? | DSG-002 DOCX SYSTEM |
| CSS 토큰·선택자·변경 동결은? | DSG-003 CSS GOVERNANCE |
| 승인 UI 구성요소의 세부 구조는? | DSG-004 COMPONENT LIBRARY |
| 이미지와 대체 텍스트 세부 규칙은? | DSG-005 IMAGE SYSTEM |
| 썸네일 비율과 안전 영역은? | DSG-006 THUMBNAIL RULES |
| 프로젝트별 브랜드 표현은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 게시 채널의 발행 절차는? | CNT-006 PUBLISHING SYSTEM |
| 예약·재시도·실패 복구는? | AUT-002·004·006 |

## 18.2 알려진 제한

- 현재 기준은 정적 콘텐츠형 HTML과 게시용 본문 조각에서 추출했다.
- 복잡한 Web App, Form, 실시간 데이터와 인증 흐름은 실제 적용 검증 전이다.
- Breakpoint·색상·간격·Component 이름은 Project MASTER와 후속 DSG 문서에서 확정한다.
- 외부 게시 채널의 실제 게시 후 Sanitization·Style 충돌은 CNT-006과 AUT Runbook 단계에서 검증한다.
- 이 문서는 사용자 승인을 받은 `APPROVED` 기준본이지만 실제 프로젝트 회귀 적용과 명시적 잠금 승인 전에는 `LOCKED` 또는 운영 Release로 자동 전환하지 않는다.

# 19. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | LOCKED `PROJECT_REFERENCE_FIXTURE` v1.0.1의 BLOG_SUMMARY_HTML에서 의미 구조·모바일 안전·범위 격리·가변 반복·접근성·검수 원칙을 분리하고 사용자 승인·잠금 승인 완료 |
