# JCOS v2.0.0 - DSG-007 BRAND SYSTEM
## 프로젝트별 브랜드 식별·토큰·자산·채널 적용 기준

| Field | Value |
|---|---|
| Document ID | DSG-007 |
| Title | BRAND SYSTEM |
| Korean Title | 프로젝트별 브랜드 식별·토큰·자산·채널 적용 기준 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS 프로젝트의 이름·Logo·색·서체·형태·이미지 방향과 채널별 Brand 표현 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001~006 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / DOCX_FULL_REPORT·BLOG_SUMMARY_HTML |
| Depends On | COR-007 VERSION POLICY, FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 프로젝트별 실제 Brand 값과 승인 자산의 식별·적용·변경 계약을 분리해 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이다. 특정 디자인 도구·AI·플랫폼을 필수로 요구하지 않는다.

# 문서 목적

DSG-007은 JCOS 프로젝트가 채널과 산출물 형식이 달라도 같은 주체로 식별되도록 Brand Profile, 이름, Logo, 색, 서체, 형태 Token, 이미지 방향, 채널 Variant와 검수 Evidence를 관리한다.

이 문서는 공통 단일 색상이나 Logo를 모든 프로젝트에 강제하지 않는다. 실제 값은 프로젝트별 승인 Brand Profile과 Project MASTER에 기록하고, DSG-007은 그 값의 필드·우선순위·사용 조건·변경 Gate를 정의한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. Brand Profile과 Registry
5. 이름·명칭·Identity
6. Logo·Mark·Lockup
7. 색상 체계
8. Typography
9. 형태·간격·표면 표현
10. 이미지·일러스트 방향
11. 채널 Variant와 반응형 적용
12. 접근성·포용성·지역화
13. 구현 매핑과 Fallback
14. 자산 권리·출처·배포
15. 검증과 품질 Gate
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 Brand Rules
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- 프로젝트 공식 명칭, 약칭, Series·Product 관계와 표기 규칙
- Logo·Symbol·Wordmark·Lockup의 승인 원본, Variant, Clear Space와 최소 크기
- 색상·Typography·형태·간격·모서리·표면 효과의 프로젝트별 실제 Token
- 이미지·일러스트·아이콘에 전달할 Brand Art Direction
- HTML·DOCX·PDF·Image·Thumbnail과 채널별 Brand Variant 매핑
- 접근성·지역화·Fallback·Registry·버전·교체 회귀와 QA

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| HTML 의미 구조·접근성 Markup | DSG-001 HTML SYSTEM |
| DOCX 조판·페이지·PDF 변환 | DSG-002 DOCX SYSTEM |
| CSS 선언·Scope·Cascade·동결 | DSG-003 CSS GOVERNANCE |
| Component Anatomy·Slot·State | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·출처·권리·Alt | DSG-005 IMAGE SYSTEM |
| Thumbnail 비율·Safe Area·Crop·Overlay | DSG-006 THUMBNAIL RULES |
| 글의 논지·문체·사실·출처 | COR-002~004와 Project Content Schema |
| 게시 채널 발행·캐시·회수 | CNT-006 PUBLISHING SYSTEM |
| 자동 생성·배포·실패 복구 | AUT 문서 |

## 1.3 금지되는 확장

- JCOS 공통 영역에 한 프로젝트의 실제 색·Logo·서체를 전역 기본값으로 고정
- 특정 Design Tool, AI 생성기, Plugin 또는 플랫폼 계정을 필수 제작 경로로 요구
- Brand를 이유로 의미 구조·사실성·권리·접근성·사용자 승인 기준을 무효화
- 승인 Profile 없이 유행·취향·자동 추천값을 Brand 기준으로 승격

# 2. 계층과 권한

## 2.1 권한 순서

1. 법률·권리·안전·접근성 필수 제한
2. 사용자의 현재 명시적 요청과 승인
3. 승인 Content Schema·Project MASTER·Brand Profile
4. DSG-007 BRAND SYSTEM과 DSG-001~006 전달 계약
5. 실제 채널에서 검증한 Brand Fixture와 회귀 Evidence
6. 참고 구현과 과거 Output

## 2.2 채널 값과 전역 값

공통 Brand Profile은 의미 역할과 승인 자산을 정의하고, Channel Variant는 매체 제약에 맞는 표현을 기록한다. 채널별 값은 상속 근거와 차이를 명시하며 다른 프로젝트나 전역 규칙으로 자동 확장하지 않는다.

## 2.3 충돌 처리

Brand 표현이 가독성·접근성·권리·사실성·채널 필수 규격과 충돌하면 상위 제한을 우선한다. 충돌한 표현은 Fallback Variant로 교체하고 적용 범위와 Evidence를 기록한다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Brand Profile | 프로젝트의 Brand 역할·값·자산·Variant·검수 조건 묶음 |
| Brand Token | 색·서체·간격·모서리 등 의미 역할에 연결된 승인 값 |
| Identity Asset | Logo·Symbol·Wordmark·Lockup처럼 주체를 식별하는 승인 자산 |
| Wordmark | 프로젝트 이름을 고유한 문자 형태로 표현한 자산 |
| Symbol | 이름 없이도 식별에 사용하는 승인 기호 |
| Lockup | Wordmark·Symbol·Tagline 등을 승인된 관계로 결합한 구성 |
| Clear Space | 다른 요소가 침범하지 않아야 하는 Identity Asset 주변 영역 |
| Channel Variant | 매체·배경·크기·색상 모드에 맞춘 승인 표현 |
| Semantic Token | `primary`, `surface`, `text-muted`처럼 역할을 나타내는 이름 |
| Primitive Value | Hex·RGB·pt·px처럼 실제 구현에 전달되는 값 |
| Fallback | 기본 자산·서체·색 표현이 불가능할 때 쓰는 승인 대체 경로 |
| Brand Fixture | 실제 채널에서 비교 가능한 승인 기준 화면·문서·이미지 |

# 4. Brand Profile과 Registry

## 4.1 Profile 필드

Brand Profile에는 Project ID, Owner, Version, 상태, 적용일, 공식 이름·약칭, Identity Asset ID, Semantic Token, Typography Stack, 형태 Token, Channel Variant, Fallback, 금지 사용, 권리·출처, Fixture와 Evidence를 포함한다.

## 4.2 프로젝트 분리

각 Project는 독립 Brand Profile을 가진다. 공통 Token 이름을 재사용할 수 있지만 Primitive Value와 Identity Asset은 명시적 상속 또는 사용자 승인 없이 다른 Project에 복사하지 않는다.

## 4.3 Registry 추적

Registry는 Profile ID·Version·상태·Owner·경로·현재 해시·대체 Version·소비 산출물을 기록한다. 파일명이나 화면상 유사성만으로 현재 승인본을 판단하지 않는다.

# 5. 이름·명칭·Identity

## 5.1 공식 이름

공식 이름, 대소문자, 공백, 기호, 언어별 표기와 허용 약칭을 Profile에 기록한다. 제목 공간이 부족하다는 이유로 승인되지 않은 축약이나 철자를 만들지 않는다.

## 5.2 관계 표기

Project, Product, Series, Feature와 Publisher 관계를 구분한다. 상위 Brand와 하위 이름을 함께 표시할 때 우선순위·구분자·Lockup을 명시하고 소유 관계를 오인시키지 않는다.

## 5.3 일반 본문과 Identity 자산

Wordmark는 승인 자산이며 일반 본문의 검색 가능한 프로젝트 이름을 대체하지 않는다. 접근 가능한 이름과 문서 Metadata에는 텍스트 표기를 제공한다.

# 6. Logo·Mark·Lockup

## 6.1 승인 원본

Logo·Symbol·Wordmark·Lockup은 Asset ID·Version·권리·색상 Variant가 확인된 승인 원본만 사용한다. 캡처 이미지나 검색 결과에서 다시 추출한 자산을 기준본으로 사용하지 않는다.

## 6.2 비율과 변형

Identity Asset은 종횡비·내부 간격·획·문자 관계를 유지한다. 늘이기, 기울이기, 임의 Crop, 재조합, 효과 추가, 윤곽선 변경을 금지하며 허용 변형은 별도 Variant로 승인한다.

## 6.3 Clear Space와 최소 크기

Clear Space와 최소 표시 크기는 채널별 Profile에서 검증한다. 공간이 부족하면 Logo를 찌그러뜨리지 않고 승인 축약 Mark, 단색 Variant, 텍스트 이름 또는 생략 경로를 사용한다.

## 6.4 배경과 Lockup

밝은 배경·어두운 배경·단색·인쇄용 Variant를 구분한다. Contrast가 부족하거나 배경이 복잡하면 승인 보호 영역 또는 대체 Variant를 사용하며 임의 색 반전은 하지 않는다.

# 7. 색상 체계

## 7.1 의미 역할 우선

색은 Hex 값만 나열하지 않고 `brand-primary`, `accent`, `surface`, `text`, `border`, `success`, `warning`, `critical` 같은 의미 역할과 사용 조건을 기록한다.

## 7.2 접근 가능한 조합

본문·제목·링크·버튼·상태·표·이미지 Overlay 조합은 실제 크기와 배경에서 대비를 검증한다. Brand 색 자체가 대비를 충족하지 않으면 승인된 접근성 Variant를 사용한다.

## 7.3 색상 단독 신호 금지

Series, 상태, 위험, 선택 여부를 색만으로 전달하지 않는다. 텍스트·아이콘·형태·Pattern 중 하나 이상을 함께 제공하고 무채색 Preview에서도 의미를 확인한다.

## 7.4 색상 모드와 출력

Light·Dark·고대비·인쇄·저품질 Preview의 Token 매핑을 분리한다. 자동 반전이나 색 공간 변환 결과를 승인값으로 간주하지 않고 실제 출력 Fixture로 검수한다.

# 8. Typography

## 8.1 서체 Stack과 권리

Primary·Fallback·CJK·Monospace 서체와 사용 권리를 기록한다. 특정 앱에만 설치된 서체를 유일한 경로로 요구하지 않으며 대체 시 줄바꿈·문자 폭·누락 글리프를 검수한다.

## 8.2 계층과 가독성

Display, Heading, Body, Caption, Data, Code 역할별 크기·굵기·행간·자간 범위를 정의한다. Brand 개성을 위해 본문 가독성이나 접근 가능한 최소 크기를 훼손하지 않는다.

## 8.3 문자 안전

한글·영문·숫자·기호·고유명사·URL·코드가 필요한 글리프를 지원하는지 확인한다. 검색·복사·번역이 필요한 정보는 Raster 문자나 Logo 자산에만 의존하지 않는다.

# 9. 형태·간격·표면 표현

## 9.1 Shape Token

모서리, 선, 간격, 그림자, 표면, 강조 방식은 의미 Token으로 기록한다. Component Anatomy나 Layout 구조를 Brand 장식 값으로 재정의하지 않는다.

## 9.2 절제와 일관성

같은 역할의 Component는 같은 Token 조합을 사용한다. 장식 효과가 정보 계층·Focus·상태·표 경계를 약화하면 제거하거나 접근성 Variant로 교체한다.

# 10. 이미지·일러스트 방향

## 10.1 Art Direction

Brand Profile은 허용 분위기, 색 경향, 구도, 질감, 일러스트·사진 역할과 금지 표현을 Brief 수준으로 제공한다. 생성·선정·권리·사실성은 DSG-005를 따른다.

## 10.2 Identity와 이미지 분리

생성 이미지 속 임의 Logo·문자·상표를 공식 Identity Asset으로 간주하지 않는다. Brand Asset은 승인 원본을 별도 합성하고 Asset Version과 배치 근거를 기록한다.

## 10.3 Thumbnail 전달

DSG-007은 실제 Brand 값과 허용 Variant를 제공하고, 비율·Safe Area·Crop·Overlay·최소 Preview 검수는 DSG-006 Profile을 따른다.

# 11. 채널 Variant와 반응형 적용

## 11.1 Channel Matrix

HTML, DOCX, PDF, Image, Thumbnail과 게시 채널별 지원 Token·Identity Variant·배경·크기·Fallback을 Matrix로 기록한다. 모든 채널에 같은 Primitive Value를 강제하지 않는다.

## 11.2 축소와 반응형

작은 화면·축소 Preview·좁은 문서 폭에서는 장식보다 이름·핵심 식별·가독성을 우선한다. 축약·재배치·생략은 승인 Variant이며 Desktop을 단순 축소한 결과로 결정하지 않는다.

## 11.3 Context 분리

Marketing, Editorial, Product UI, Internal Document 등 Context별 허용 표현을 구분한다. 한 Context의 캠페인 표현을 장기 Brand 기준이나 다른 채널 기본값으로 자동 승격하지 않는다.

# 12. 접근성·포용성·지역화

## 12.1 접근 가능한 이름

Logo·Symbol·장식 이미지에는 Context에 맞는 접근 가능한 이름 또는 장식 제외 처리를 제공한다. 시각 Brand가 Heading·Label·Link 목적을 대신하지 않는다.

## 12.2 포용적 표현

색·형태·이미지·명칭이 차별적 고정관념이나 오인을 강화하지 않는지 검토한다. 법률·안전·권리 또는 사용자 요구와 충돌하면 Brand 선호보다 상위 제한을 따른다.

## 12.3 지역화

언어별 이름·문장 길이·서체·방향·날짜·숫자 차이를 Profile Variant로 관리한다. 번역된 Wordmark나 임의 음역을 만들지 않으며 승인 텍스트 이름을 Fallback으로 제공한다.

# 13. 구현 매핑과 Fallback

## 13.1 형식별 전달

Brand Profile의 의미 Token을 CSS Custom Property, DOCX Style, PDF 색·서체, 이미지 Asset과 Thumbnail Profile에 매핑한다. 구현 문법은 각 전담 문서를 따르고 DSG-007은 값과 관계를 소유한다.

## 13.2 Fallback 순서

기본 자산이나 값이 불가능하면 승인 대체 Variant, System Fallback, 중립 표현 순서로 적용한다. Fallback이 의미·상태·소유 관계를 바꾸면 사용하지 않고 열린 결함으로 기록한다.

## 13.3 도구 독립성

Brand 계약은 개방형 값·파일·필드·해시로 전달 가능해야 한다. 특정 AI·Design Tool·Plugin의 내부 스타일 이름이나 비공개 Preset만으로 승인 근거를 남기지 않는다.

# 14. 자산 권리·출처·배포

## 14.1 Provenance

Identity Asset과 서체는 출처, 권리 근거, 허용 범위, 수정 가능 여부, 만료·교체 조건과 해시를 기록한다. 권리 불명 자산은 유사해 보여도 배포하지 않는다.

## 14.2 원본과 파생본

편집 가능한 승인 원본과 채널 파생본을 구분한다. 파생본에는 Source Asset ID·Profile Version·변환 조건을 연결하고 반복 손실 변환을 피한다.

## 14.3 외부 공유

외부 전달 Package에는 필요한 자산과 사용 조건만 포함한다. 내부 원본·라이선스 문서·개인정보를 무조건 복제하지 않으며 수신자가 현재 승인 Version을 확인할 수 있게 한다.

# 15. 검증과 품질 Gate

## 15.1 구성 Gate

- Project ID·Brand Profile ID·Version·상태·Owner
- 공식 이름·약칭·Identity Asset·Semantic Token·Typography Stack
- Channel Variant·Fallback·금지 사용·권리·Fixture·Evidence
- 소비 문서·Component·Image·Thumbnail·게시 채널 연결

## 15.2 실제 출력 Gate

- HTML·DOCX·PDF·Image·Thumbnail 대표 Fixture
- Light·Dark·인쇄·축소·모바일·고대비·지역화 Variant
- Logo 비율·Clear Space·최소 크기·배경 적합성
- 색 대비·색상 비의존·서체 Fallback·누락 글리프

## 15.3 판정

권리·식별·접근성·잘못된 승인 상태 Critical 결함이 하나라도 열려 있으면 사용·PASS·LOCK·Release를 선언하지 않는다. 자동 유사도나 생성 도구 Preview만으로 Brand 일치를 최종 판정하지 않는다.

# 16. 변경·승인·LOCK 수명주기

1. Project와 Brand 역할, Owner, 소비 채널을 식별한다.
2. 이름·Identity Asset·Semantic Token·Typography·Channel Variant를 작성한다.
3. DSG-001~006과 Project MASTER의 경계를 연결한다.
4. 대표 Fixture로 접근성·식별·권리·형식 Gate를 실행한다.
5. Markdown·DOCX·PDF·QA·해시 패키지를 REVIEW로 작성한다.
6. 사용자 검토와 수정 후 기준 문서를 APPROVED로 전환한다.
7. 실제 Project Brand Profile과 대표 채널 회귀 적용을 검증한다.
8. 명시적 잠금 승인 후 LOCKED로 전환한다.

LOCKED 이후 Profile·Token·Identity Asset을 변경할 때는 승인본을 조용히 덮어쓰지 않고 Version 후보와 History를 만든다.

# 17. 규칙 카탈로그

## 17.A 권한·Profile·Token

### BRD-001 - 프로젝트 범위
- **Priority:** Critical
- **Statement:** Brand 값은 Project Brand Profile 범위에서만 유효하며 JCOS 전역이나 다른 Project로 자동 확장하지 않는다.
- **Verification:** Project ID·Profile ID·적용 범위를 대조한다.
- **Exceptions:** 사용자가 승인한 공통 상속 Profile.

### BRD-002 - 승인 원본 우선
- **Priority:** Critical
- **Statement:** 이름·Token·Identity Asset은 현재 승인 Registry Version만 사용한다.
- **Verification:** Registry 상태·경로·해시를 확인한다.
- **Exceptions:** REVIEW로 표시된 명시적 Prototype.

### BRD-003 - 의미 Token 우선
- **Priority:** High
- **Statement:** 실제 값을 역할 기반 Semantic Token에 연결하고 Primitive Value만 단독 공유하지 않는다.
- **Verification:** Token 이름·역할·값·소비처를 검사한다.
- **Exceptions:** 단일 값 교환용 진단 Fixture.

### BRD-004 - 상위 제한 우선
- **Priority:** Critical
- **Statement:** Brand 표현은 법률·권리·안전·접근성·사용자 승인을 무효화하지 않는다.
- **Verification:** 충돌 기록과 Fallback 적용을 확인한다.
- **Exceptions:** 없음.

## 17.B 이름·Logo·Lockup

### BRD-005 - 공식 이름 정확성
- **Priority:** Critical
- **Statement:** 공식 이름·약칭·대소문자·기호는 Profile 승인값과 일치한다.
- **Verification:** 제목·Metadata·접근 가능한 이름을 대조한다.
- **Exceptions:** 승인된 지역화 표기.

### BRD-006 - Identity Asset 출처
- **Priority:** Critical
- **Statement:** Logo·Symbol·Wordmark·Lockup은 Asset ID·권리·해시가 확인된 승인 원본을 사용한다.
- **Verification:** Asset Registry와 파일 해시를 확인한다.
- **Exceptions:** 명시적 무브랜드 Prototype.

### BRD-007 - 비율·구성 보존
- **Priority:** Critical
- **Statement:** Identity Asset의 비율·획·간격·요소 관계를 임의로 변형하지 않는다.
- **Verification:** 승인 원본 Overlay 비교를 수행한다.
- **Exceptions:** 별도 승인 Variant.

### BRD-008 - Clear Space·최소 크기
- **Priority:** High
- **Statement:** 채널별 Clear Space와 최소 크기를 충족하지 못하면 승인 Fallback을 사용한다.
- **Verification:** 실제 Pixel·인쇄 크기와 주변 요소를 측정한다.
- **Exceptions:** 접근 가능한 텍스트 이름 대체.

### BRD-009 - 배경 Variant
- **Priority:** High
- **Statement:** 밝음·어두움·단색·인쇄 배경에 승인된 Identity Variant를 사용한다.
- **Verification:** Contrast와 배경 Fixture를 확인한다.
- **Exceptions:** Profile이 허용한 보호 영역.

### BRD-010 - 관계 오인 금지
- **Priority:** Critical
- **Statement:** Project·Product·Series·Publisher의 Lockup이 소유·보증 관계를 오인시키지 않는다.
- **Verification:** 명칭 계층과 Lockup Registry를 대조한다.
- **Exceptions:** 법적·계약상 승인 공동 Brand.

## 17.C 색상·Typography

### BRD-011 - 색 역할 매핑
- **Priority:** High
- **Statement:** 모든 Brand 색은 의미 역할·배경·상태·허용 조합과 함께 기록한다.
- **Verification:** Color Token Matrix를 검사한다.
- **Exceptions:** 원본 Artwork의 비 UI 색.

### BRD-012 - 대비 충족
- **Priority:** Critical
- **Statement:** 텍스트·링크·상태·Control·Overlay는 실제 크기와 배경에서 접근 가능한 대비를 충족한다.
- **Verification:** 대표 Fixture의 대비 Evidence를 확인한다.
- **Exceptions:** 읽을 필요가 없는 장식 요소.

### BRD-013 - 색상 단독 신호 금지
- **Priority:** Critical
- **Statement:** 상태·Series·선택·위험을 색만으로 전달하지 않는다.
- **Verification:** 무채색 Preview와 보조 Label·Icon·형태를 확인한다.
- **Exceptions:** 없음.

### BRD-014 - 서체 Stack·권리
- **Priority:** Critical
- **Statement:** Primary·Fallback·CJK·Monospace 서체와 사용 권리를 Profile에 기록한다.
- **Verification:** 설치 부재·대체 Render·라이선스를 확인한다.
- **Exceptions:** System Font만 사용하는 명시적 Profile.

### BRD-015 - 문자 가독성
- **Priority:** Critical
- **Statement:** Brand Typography는 본문 최소 크기·행간·글리프·검색 가능성을 훼손하지 않는다.
- **Verification:** 한글·영문·숫자·기호와 축소 Preview를 검사한다.
- **Exceptions:** 읽을 필요가 없는 장식 Letterform.

### BRD-016 - Raster 문자 의존 금지
- **Priority:** High
- **Statement:** 검색·복사·번역이 필요한 정보는 Logo나 이미지 속 문자만으로 제공하지 않는다.
- **Verification:** 실제 텍스트·Accessible Name 경로를 확인한다.
- **Exceptions:** 승인 Wordmark와 병행된 텍스트 이름.

## 17.D 형태·이미지·Thumbnail

### BRD-017 - 형태 Token 일관성
- **Priority:** High
- **Statement:** 모서리·선·간격·그림자·표면 효과를 역할 기반 Token으로 일관되게 적용한다.
- **Verification:** 동일 역할 Component의 Token 매핑을 비교한다.
- **Exceptions:** 상태를 명시한 승인 Variant.

### BRD-018 - 구조 책임 분리
- **Priority:** Critical
- **Statement:** Brand 장식 값으로 HTML 의미 구조·DOCX 조판·Component Anatomy를 재정의하지 않는다.
- **Verification:** DSG-001~004 계약과 대조한다.
- **Exceptions:** 사용자 승인 구조 변경 절차.

### BRD-019 - Art Direction 경계
- **Priority:** High
- **Statement:** Brand Profile은 이미지 방향과 금지 표현을 제공하고 생성·권리·사실성 판단은 DSG-005에 맡긴다.
- **Verification:** Generation Brief와 Asset Registry를 대조한다.
- **Exceptions:** 없음.

### BRD-020 - Identity 합성 분리
- **Priority:** Critical
- **Statement:** 생성 이미지 속 임의 Logo·문자를 공식 Identity Asset으로 사용하지 않는다.
- **Verification:** 원본 Asset Layer와 최종 합성물을 대조한다.
- **Exceptions:** 승인된 비공식 예시임을 명시한 교육 Fixture.

### BRD-021 - Thumbnail 경계
- **Priority:** High
- **Statement:** Brand 값은 DSG-006 Profile의 Safe Area·Crop·Overlay·Preview 제한 안에서 적용한다.
- **Verification:** Brand Token과 Thumbnail Fixture를 함께 검사한다.
- **Exceptions:** 검증된 Text-only Variant.

## 17.E 채널·접근성·이식성

### BRD-022 - Channel Matrix
- **Priority:** Critical
- **Statement:** HTML·DOCX·PDF·Image·Thumbnail별 지원 Variant와 Fallback을 기록한다.
- **Verification:** Channel Matrix 필수 Field를 검사한다.
- **Exceptions:** 사용하지 않는 채널은 명시적 N/A.

### BRD-023 - 축소·반응형 식별
- **Priority:** Critical
- **Statement:** 작은 화면과 축소 Preview에서도 이름·핵심 식별·가독성을 보존한다.
- **Verification:** 모바일·최소 Preview Fixture를 확인한다.
- **Exceptions:** 승인된 Symbol-only Variant.

### BRD-024 - 지역화 안전
- **Priority:** High
- **Statement:** 언어별 이름·서체·문장 길이·방향을 승인 Variant로 관리한다.
- **Verification:** Locale Fixture와 Fallback 글리프를 확인한다.
- **Exceptions:** 원문 고유명사 고정 표기.

### BRD-025 - 도구 비종속
- **Priority:** Critical
- **Statement:** Brand 기준을 특정 AI·Design Tool·Plugin의 비공개 Preset에만 저장하지 않는다.
- **Verification:** 개방형 값·Asset·Metadata·해시로 재현한다.
- **Exceptions:** 임시 실험은 REVIEW와 재현 불가를 명시.

## 17.F Registry·변경·QA

### BRD-026 - Brand Registry 완전성
- **Priority:** Critical
- **Statement:** Profile·Token·Asset·Variant·Owner·Version·상태·소비처·Evidence를 Registry에 기록한다.
- **Verification:** 필수 Field 누락을 검사한다.
- **Exceptions:** Production에 쓰지 않는 명시적 Prototype.

### BRD-027 - 권리·출처 추적
- **Priority:** Critical
- **Statement:** Identity Asset과 서체의 출처·권리·수정·배포 조건과 해시를 보존한다.
- **Verification:** Provenance와 License Record를 확인한다.
- **Exceptions:** 권리 제한이 없는 자체 생성 자산도 생성 Evidence를 기록.

### BRD-028 - 조용한 덮어쓰기 금지
- **Priority:** Critical
- **Statement:** 승인 Profile·Token·Asset을 같은 ID·Version으로 조용히 덮어쓰지 않는다.
- **Verification:** Version·History·해시 변경을 대조한다.
- **Exceptions:** 해시에 영향 없는 Metadata 교정은 기록 후 처리.

### BRD-029 - 대표 회귀 Gate
- **Priority:** Critical
- **Statement:** Brand 변경은 대표 채널·모드·크기·지역화 Fixture에서 회귀 검수한다.
- **Verification:** Regression Matrix와 열린 결함을 확인한다.
- **Exceptions:** 영향 없음이 증명된 문서 오탈자.

### BRD-030 - 상태·해시 최종 갱신
- **Priority:** Critical
- **Statement:** 내용·자산·Version·상태가 바뀌면 문서·Registry·Package 해시를 다시 계산하고 승인 상태를 검증한다.
- **Verification:** 현재 파일과 SHA 목록을 비교한다.
- **Exceptions:** 해시 대상 밖의 임시 Render.

# 18. AI용 압축 Brand Rules

## 18.1 압축 지침

다음 블록은 DSG-007이 APPROVED 또는 LOCKED된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 LOCKED이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-007 BRAND SYSTEM v2.0.0을 따른다.
1. Brand 값은 Project Brand Profile 범위에서만 사용하고 다른 Project나 JCOS 전역으로 자동 확장하지 않는다.
2. 이름·Logo·Symbol·Wordmark·Lockup은 승인 Registry의 현재 Version·권리·해시를 확인한다.
3. Identity Asset의 비율·구성·Clear Space·최소 크기를 지키고 배경에 맞는 승인 Variant를 사용한다.
4. 실제 값은 역할 기반 Semantic Token에 연결하며 색만으로 상태·Series·선택·위험을 전달하지 않는다.
5. Typography Stack·권리·Fallback·글리프·최소 크기를 검증하고 검색 가능한 정보를 Raster 문자에만 두지 않는다.
6. 형태 Token은 Component 구조를 바꾸지 않으며 이미지 생성·권리·사실성은 DSG-005에 맡긴다.
7. Brand 값은 DSG-006 Thumbnail Profile의 Safe Area·Crop·Overlay·Preview 제한 안에서 적용한다.
8. HTML·DOCX·PDF·Image·Thumbnail별 Channel Variant와 Light·Dark·인쇄·모바일·지역화 Fallback을 기록한다.
9. 특정 AI·Design Tool·Plugin의 비공개 Preset에만 의존하지 않고 값·Asset·Metadata·해시로 재현한다.
10. Profile·Token·Asset·Version·권리·소비처·Evidence를 Registry에 남기고 변경 시 대표 회귀와 최종 해시를 갱신한다.
```

## 18.2 추출 조건

- DSG-007이 APPROVED 또는 LOCKED 상태다.
- 실제 Project Brand Profile과 대표 채널 Fixture가 충돌하지 않는지 확인했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| 프로젝트 실제 이름·색·Logo·서체·형태 값은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| HTML 의미 구조와 접근성 Markup은? | DSG-001 HTML SYSTEM |
| DOCX 조판과 PDF 변환은? | DSG-002 DOCX SYSTEM |
| CSS Token 선언·Scope·변경은? | DSG-003 CSS GOVERNANCE |
| Component 구조·State·Variant는? | DSG-004 COMPONENT LIBRARY |
| 이미지 생성·선정·권리·Alt는? | DSG-005 IMAGE SYSTEM |
| Thumbnail 비율·Safe Area·Crop은? | DSG-006 THUMBNAIL RULES |
| 글의 논지·문체·사실·출처는? | COR-002~004와 Project Content Schema |
| 게시·캐시·회수는? | CNT-006 PUBLISHING SYSTEM |
| 자동 생성·배포·실패 복구는? | AUT 문서 |

## 19.2 알려진 제한

- 이 문서는 Brand Profile의 필드와 관리 원칙을 정의하며 모든 프로젝트에 동일한 실제 색·Logo·서체를 지정하지 않는다.
- 현재 기준 Fixture는 참조 프로젝트 MASTER의 DOCX·PDF·HTML이며 다른 Project에는 별도 승인 Profile이 필요하다.
- 실제 상표 등록·법률 의견·서체 재배포 권한은 해당 권리 문서와 전문가 검토가 우선한다.
- 새로운 캠페인·Motion·3D·음향 Identity는 Project 요구와 사용자 승인 전 JCOS v2.0 범위에 추가하지 않는다.
- 이 문서는 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이며 운영 Runtime·Release 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | DSG-001~006과 Content·Publishing 경계에서 프로젝트별 이름·Identity Asset·색·서체·형태·채널 Variant·접근성·Registry·회귀 규칙을 특정 도구 비종속 계약으로 분리하고 사용자 승인·잠금 승인 완료 |
