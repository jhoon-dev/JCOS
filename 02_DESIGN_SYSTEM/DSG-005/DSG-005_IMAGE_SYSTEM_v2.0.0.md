# JCOS v2.0.0 - DSG-005 IMAGE SYSTEM

## 이미지 생성·선정·사용 기준

| Field | Value |
|---|---|
| Document ID | DSG-005 |
| Title | IMAGE SYSTEM |
| Korean Title | 이미지 생성·선정·사용 기준 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | JCOS 산출물에 포함되거나 연결되는 생성·원본·라이선스·공식 이미지와 파생본 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001~004 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / DOCX_FULL_REPORT·BLOG_SUMMARY_HTML |
| Depends On | COR-004 SOURCE POLICY, FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 이미지의 목적·출처·권리·생성·편집·형식·접근성·추적·검수 계약을 분리해 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이다. 특정 AI 서비스나 모델을 필수로 요구하지 않는다.

# 문서 목적

DSG-005는 이미지가 장식이 아니라 명확한 역할과 근거를 갖고, 생성 도구나 게시 채널이 달라도 권리·의미·품질·접근성을 잃지 않도록 공통 계약을 정의한다. 원본에서 파생본까지 출처와 변경을 연결하고 허위 증거, 오인 편집, 무단 사용과 접근성 누락을 방지한다.

이 문서는 실제 브랜드 색·로고·화풍, 썸네일 전용 비율·문자 안전 영역, 구성요소의 이미지 Slot 개수, 게시 채널 운영을 정하지 않는다. 각 값은 DSG-004·006·007, Project MASTER와 CNT-006이 소유한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. 이미지 역할과 유형
5. 출처와 Provenance
6. 권리·동의·개인정보
7. 선정·관련성·사실성
8. 생성 Brief와 도구 독립성
9. 편집·Crop·합성의 무결성
10. 해상도·형식·색 관리
11. 반응형 파생본과 Fallback
12. 대체 설명·Caption·접근성
13. Asset Registry·이름·버전
14. 변경 영향·교체·복구
15. 검증과 품질 Gate
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 Image System
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- 생성형 이미지, 직접 촬영·제작 이미지, 공식 제공 이미지, 라이선스 Stock, 사용자 제공 이미지
- Hero·본문 Figure·Diagram·Screenshot·증거 자료·Illustration·장식 이미지와 파생본
- 목적, 출처, 권리, 동의, 생성 기록, 편집 무결성, 파일 품질, 접근성, Registry와 QA
- 모바일·문서·웹 전달을 위한 원본 보존, Crop·Resize·Compression·Format 변환과 Fallback

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| 이미지 Slot의 구조·필수성·Cardinality | DSG-004 COMPONENT LIBRARY |
| HTML Figure·img·Caption 의미 구조 | DSG-001 HTML SYSTEM |
| DOCX 배치와 PDF 변환 | DSG-002 DOCX SYSTEM |
| CSS 크기·비율·Overflow 구현 | DSG-003 CSS GOVERNANCE |
| 썸네일 비율·안전 영역·텍스트 배치 | DSG-006 THUMBNAIL RULES |
| 실제 색상·로고·서체·화풍 | DSG-007 BRAND SYSTEM과 Project MASTER |
| 출처 인용·신뢰 등급·링크 정책 | COR-004 SOURCE POLICY |
| 게시 채널 발행·수정·삭제 | CNT-006 PUBLISHING SYSTEM |
| 생성·변환 자동화와 실패 복구 | AUT 문서 |

## 1.3 금지되는 확장

- 특정 AI 업체·모델·Stock 서비스·편집기를 유일한 실행 조건으로 지정
- 참고 Output의 이미지 수, 비율, 화풍 또는 위치를 전역 고정값으로 승격
- 사실을 증명하는 사진·Screenshot처럼 보이는 합성물을 실제 증거로 표시
- 권리·동의·출처를 확인할 수 없는 이미지를 장식 목적이라는 이유로 Production에 사용

# 2. 계층과 권한

## 2.1 권한 순서

1. 법률·안전·플랫폼 필수 제한과 당사자 동의
2. 사용자의 현재 명시적 요청
3. 승인 Content Schema와 Project MASTER
4. COR-004 SOURCE POLICY와 DSG-005 IMAGE SYSTEM
5. DSG-004 Component, DSG-007 Brand와 DSG-001~003 전달 형식
6. 실제 입력 Asset과 게시 채널의 검증된 제한
7. 참고 구현과 과거 Output

## 2.2 충돌 처리

상위 기준이 더 엄격하면 그 기준을 따른다. Project MASTER의 화풍·비율 지시도 권리, 동의, 개인정보, 사실성, 접근성 기준을 무효화하지 않는다. 충돌을 해소할 수 없으면 임의 생성이나 대체 없이 사용을 중단하고 기록한다.

## 2.3 참고 구현의 역할

PROJECT_REFERENCE_FIXTURE는 풀 리포트와 모바일 요약에서 이미지 사용 여부와 전달 차이를 검수한 참고 구현이다. 특정 날짜의 이미지 개수와 실제 소재는 관찰값이며 공통 필수값이 아니다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Source Asset | Crop·Resize·압축 전의 보존 원본 |
| Derivative | 전달 목적에 맞춰 원본에서 만든 파생 파일 |
| Provenance | 생성·획득·편집·전달의 출처와 변경 기록 |
| Rights Basis | 소유권·라이선스·허가·동의 등 사용 근거 |
| Generation Brief | 역할·사실 제약·금지 요소·구도·출력 조건을 담은 도구 독립 명세 |
| Prompt Record | 생성 도구에 실제 전달한 입력과 주요 설정 기록 |
| Focal Point | Crop 과정에서도 보존해야 하는 핵심 시각 대상 |
| Safe Crop | 핵심 의미와 필수 대상을 잃지 않는 허용 Crop 범위 |
| Alt Text | 이미지를 보지 못할 때 같은 기능·핵심 의미를 전달하는 대체 설명 |
| Decorative | 제거해도 정보·기능·정서적 의도가 손상되지 않는 이미지 |
| Asset Registry | Asset ID, 원본, 권리, 버전, 파생본과 사용처를 연결한 목록 |

# 4. 이미지 역할과 유형

## 4.1 역할 우선

이미지를 선택하거나 생성하기 전에 Hero, Evidence, Diagram, Explanation, Illustration, Identity, Decorative 중 역할을 선언한다. 같은 파일을 여러 역할에 쓰면 각 Context에서 목적·Caption·Alt와 Crop 적합성을 다시 검증한다.

## 4.2 정보 기여

이미지는 본문과 중복 장식이 아니라 이해, 근거, 탐색 또는 정서적 방향에 기여해야 한다. 정보 기여를 설명할 수 없으면 제거하거나 명시적 Decorative로 분류한다.

## 4.3 유형별 주의

| 유형 | 필수 검토 |
|---|---|
| Photo·Screenshot | 촬영·캡처 시점, 맥락, 조작 여부, 개인정보 |
| Diagram·Chart | 데이터 근거, Label, 범례, 텍스트 대안 |
| Generated Illustration | 생성 사실, 사실 주장과의 구분, 도구 기록 |
| Logo·Identity | 권리, 공식 원본, 변형 허용 범위 |
| Decorative | 빈 Alt 처리와 불필요한 다운로드 비용 |

# 5. 출처와 Provenance

## 5.1 Source Class

모든 Production 이미지는 Original, User-provided, Official/Primary, Licensed Stock, Generated 중 하나 이상의 Source Class를 기록한다. 다운로드 URL만 남기지 않고 제공자, 획득일, 원본 파일과 권리 근거를 연결한다.

## 5.2 생성 기록

생성 이미지에는 사용 가능한 범위에서 도구·모델·버전, 실행일, Prompt Record, 주요 설정, Seed 또는 작업 ID와 후편집 내역을 기록한다. 값이 제공되지 않으면 `unavailable`로 명시하고 임의 값을 만들지 않는다.

## 5.3 연결성

원본, 편집본, 전달 파생본과 실제 사용처는 같은 Asset ID 계보로 연결한다. 출처가 불명확해진 복사본을 새 원본으로 등록하지 않는다.

# 6. 권리·동의·개인정보

## 6.1 사용 근거

License, 소유권, 서면 허가, 플랫폼 제공 조건 또는 사용자 명시적 제공 중 사용 근거와 허용 범위를 기록한다. 지역·기간·매체·수정·상업 사용·Attribution 제한이 있으면 Delivery 전에 확인한다.

## 6.2 사람과 민감 정보

식별 가능한 사람, 미성년자, 의료·금융·위치·문서 화면 등 민감 정보는 동의와 필요성을 우선 검토한다. 불필요한 얼굴·이름·계정·연락처·고유 식별자는 Crop, Mask 또는 대체 이미지로 제거한다.

## 6.3 금지와 중단

권리나 동의를 합리적으로 확인할 수 없거나 제한이 목적과 충돌하면 사용하지 않는다. 생성 가능하다는 사실을 실존 인물의 오인, 상표 위장 또는 권리 회피 근거로 삼지 않는다.

# 7. 선정·관련성·사실성

## 7.1 선정 기준

후보 이미지는 내용 관련성, 사실 적합성, 시각적 명료성, 모바일 판독성, 권리 안정성, 접근성 작성 가능성, 파일 품질 순으로 비교한다. 해상도만 높거나 자극적인 후보를 우선하지 않는다.

## 7.2 사실 주장

Evidence로 쓰는 이미지와 Screenshot은 실제 출처·시점·Context를 확인한다. 예시·재현·합성·생성 이미지는 실제 현장 사진이나 제품 화면처럼 오인되지 않도록 인접 설명에서 구분한다.

## 7.3 편향과 대표성

사람·지역·직업·문화·위험을 묘사할 때 고정관념이나 부당한 대표성을 검토한다. 민감한 주제에서 극적인 연출이 정확한 Context를 대체하지 않게 한다.

# 8. 생성 Brief와 도구 독립성

## 8.1 Brief 필드

Generation Brief에는 역할, 독자, 핵심 대상, 장면·구도, 사실 제약, 금지 요소, 전달 비율 Context, 필요한 여백, 텍스트 포함 여부, 접근성 메모와 검수 기준을 포함한다. 실제 Brand 값은 Project MASTER나 DSG-007에서 참조한다.

## 8.2 도구 독립 계약

Brief는 한 업체의 Prompt 문법이나 고유 Parameter 없이도 다른 생성기, Stock 검색, 직접 제작 또는 수작업 Diagram으로 실행 가능해야 한다. 도구별 Prompt는 파생 기록이며 공통 계약을 대체하지 않는다.

## 8.3 실패와 대안

생성기가 사실 제약, 권리, 안전, 텍스트 정확성 또는 재현성을 충족하지 못하면 재시도 횟수를 무한히 늘리지 않는다. 공식 이미지, 단순 Diagram, 텍스트 전용 구성 또는 이미지 생략 경로를 사용한다.

# 9. 편집·Crop·합성의 무결성

## 9.1 허용 편집

Resize, Compression, Color 보정, 배경 제거, Crop과 Annotation은 목적과 의미를 바꾸지 않는 범위에서 수행하고 주요 편집을 기록한다. 증거 이미지의 내용 삭제·추가·재배열은 원칙적으로 금지한다.

## 9.2 Crop

Focal Point, 필수 인물·물체·Label과 Context를 먼저 지정하고 Safe Crop을 검증한다. 모바일 Crop이 인물의 신체, 제품 정보, Diagram Label 또는 사실 맥락을 부당하게 잘라내지 않게 한다.

## 9.3 합성과 표시

합성·재현·생성 이미지가 사실성 판단에 영향을 주면 그 성격을 인접 Caption 또는 본문에서 알린다. 워터마크, 서명, 출처 표시와 권리 고지를 제거하거나 가리지 않는다.

# 10. 해상도·형식·색 관리

## 10.1 원본과 크기

Source Asset은 가능한 한 비파괴 원본으로 보존한다. Delivery 파생본은 실제 표시 크기와 기기 배율을 근거로 만들며 불필요한 초대형 파일이나 작은 파일의 인위적 확대를 피한다.

## 10.2 Format

사진은 효율적인 손실 압축 형식, 투명도·선명한 경계는 무손실 또는 Alpha 지원 형식, 단순 도형은 접근성과 플랫폼 지원을 확인한 Vector를 우선 검토한다. 최신 형식만 제공하지 않고 지원되지 않는 채널에는 검증된 Fallback을 둔다.

## 10.3 색과 Metadata

웹·문서 전달은 호환 가능한 색 공간을 사용하고 변환 전후 색상과 투명도를 확인한다. 위치·기기·작성자 등 불필요한 민감 Metadata는 제거하되 권리·Provenance 기록은 Registry에 보존한다.

# 11. 반응형 파생본과 Fallback

## 11.1 파생본 세트

필요한 표시 폭, 밀도, 비율과 채널을 근거로 파생본을 만든다. 단순 파일명 차이가 아니라 원본 Asset ID, 변환 규칙, Pixel 크기, Format, 해시와 Intended Use를 기록한다.

## 11.2 Art Direction

좁은 화면용 별도 Crop은 같은 의미와 핵심 대상을 보존해야 한다. 썸네일 전용 텍스트·안전 영역은 DSG-006에서 결정하며 일반 본문 이미지 규칙으로 대신하지 않는다.

## 11.3 Fallback과 실패

이미지 로드 실패, Format 미지원, 느린 연결 또는 문서 변환 시에도 핵심 내용이 사라지지 않게 Alt, Caption, Text Summary 또는 기본 파생본을 제공한다. 깨진 URL이나 빈 Frame을 성공으로 처리하지 않는다.

# 12. 대체 설명·Caption·접근성

## 12.1 Alt 결정

Alt는 파일 외형 목록이 아니라 현재 Context에서 이미지가 수행하는 기능과 핵심 의미를 전달한다. 인접 본문과 같은 문장을 반복하지 않고, Link나 Control 이미지면 시각 묘사보다 동작 목적을 우선한다.

## 12.2 Caption과 상세 대안

출처·시점·합성 여부·해석에 필요한 Context는 Caption이나 인접 본문에 둔다. Chart, 복잡한 Diagram, 정보가 많은 Screenshot은 짧은 Alt 외에 데이터 표, 단계 설명 또는 Long Description을 제공한다.

## 12.3 Decorative

정말 Decorative인 이미지는 보조기술에서 제외되도록 Delivery 형식에 맞게 빈 Alt 또는 동등 처리를 한다. 의미 있는 이미지를 문서 분량이나 작성 편의를 이유로 Decorative로 표시하지 않는다.

# 13. Asset Registry·이름·버전

## 13.1 필수 항목

Registry는 Asset ID, 역할, Source Class, Owner, 상태, 원본 경로·해시, Rights Basis, 획득·생성일, 생성 기록, 편집 이력, 파생본, Alt·Caption, 사용처, 교체·폐기 정보를 연결한다.

## 13.2 이름과 버전

파일명은 안정적 Asset ID, 의미 있는 Slug, Variant 또는 크기, Version과 확장자를 일관되게 표현한다. `final-final2`나 날짜 없는 `image1`을 사용하지 않으며 같은 파일명으로 다른 바이트를 조용히 덮어쓰지 않는다.

## 13.3 중복과 보존

해시와 시각 비교로 동일·유사 Asset을 식별하되 Crop·권리·Alt 차이를 근거 없이 합치지 않는다. 승인 원본과 사용 중 파생본은 소비 문서가 전환되고 복구 가능성이 확인될 때까지 보존한다.

# 14. 변경 영향·교체·복구

## 14.1 영향 표면

이미지 교체 전 Component Slot, HTML, DOCX, PDF, CSS, Thumbnail, Brand, Alt·Caption, Source, 캐시와 게시 URL을 확인한다. 같은 Asset ID를 참조하는 다른 프로젝트와 과거 게시물을 함께 검색한다.

## 14.2 교체와 폐기

교체 이유, 이전·신규 ID, 권리·의미 차이, 영향 Delivery, 전환일과 복구 경로를 기록한다. 권리 철회나 개인정보 문제는 우선순위와 제거 범위를 명시하고 파생본·캐시까지 추적한다.

## 14.3 회귀

원본 및 파생 해시, 모바일 Crop, Alt·Caption, 문서 변환, 게시 결과를 다시 검수한다. 승인본을 덮어쓰기보다 새 Version으로 교체하고 필요한 경우 검증된 이전 Version으로 Rollback한다.

# 15. 검증과 품질 Gate

## 15.1 권리·사실 Gate

- Source Class, 제공자, 원본, Rights Basis와 사용 범위
- 사람·미성년자·민감 정보·상표·워터마크와 동의
- 실제·예시·재현·합성·생성 여부와 표시의 정확성
- 주장, 날짜, 제품 UI, Diagram 데이터와 본문 Context 일치

## 15.2 시각·기술 Gate

- Focal Point와 Safe Crop, 모바일·Desktop·DOCX·PDF 결과
- 실제 표시 크기, 기기 배율, Format, 색 공간, Alpha와 파일 크기
- 깨짐·늘어남·왜곡·과도한 압축·잘림·불필요한 Metadata
- Alt, Caption, Long Description, Decorative 처리와 로드 실패 Fallback

## 15.3 판정

권리·동의·사실성·개인정보·핵심 접근성의 Critical 결함이 하나라도 열려 있으면 사용·PASS·LOCK·Release를 선언하지 않는다. 도구가 자동 생성한 결과도 사람이 목적과 Context에 맞게 검수한다.

# 16. 변경·승인·LOCK 수명주기

1. 이미지 역할, 사용처, 독자와 Content 근거를 식별한다.
2. Source 후보 또는 Generation Brief와 권리·사실 제약을 작성한다.
3. 원본, Prompt Record, 편집, 파생본과 접근성 정보를 Registry에 연결한다.
4. 권리·사실·시각·기술 Gate를 실행하고 REVIEW Evidence를 남긴다.
5. 사용자 검토와 수정 후 기준 문서를 APPROVED로 전환한다.
6. 대표 HTML·DOCX·PDF·게시 경로에서 회귀를 실행한다.
7. 명시적 잠금 승인 후 LOCKED로 전환한다.

LOCKED 이후 규칙이나 Asset을 변경할 때는 승인본을 조용히 덮어쓰지 않고 Version 후보와 History를 만든다.

# 17. 규칙 카탈로그

## 17.A 권한·목적·출처

### IMG-001 - 상위 기준 우선
- **Priority:** Critical
- **Statement:** 이미지는 법률·안전·동의, 사용자 요청과 승인 MASTER를 무효화하지 않는다.
- **Verification:** Rights·요청·MASTER와 사용처를 대조한다.
- **Exceptions:** 더 엄격한 플랫폼 필수 제한.

### IMG-002 - 역할 선행
- **Priority:** High
- **Statement:** 선택·생성 전에 이미지 역할과 정보 기여를 명시한다.
- **Verification:** Brief와 Component Slot을 확인한다.
- **Exceptions:** 검증된 Decorative Asset.

### IMG-003 - 관찰값 고정 금지
- **Priority:** Critical
- **Statement:** 참고 Output의 이미지 수·비율·위치·화풍을 전역 고정하지 않는다.
- **Verification:** 현재 Schema·MASTER와 비교한다.
- **Exceptions:** Project MASTER의 근거 있는 고정값.

### IMG-004 - Source Class 기록
- **Priority:** Critical
- **Statement:** 모든 Production 이미지는 Source Class, 제공자, 획득·생성일과 원본을 기록한다.
- **Verification:** Registry 필수 Field를 검사한다.
- **Exceptions:** 없음.

### IMG-005 - Provenance 연결
- **Priority:** Critical
- **Statement:** 원본·편집본·파생본·사용처를 하나의 추적 가능한 계보로 연결한다.
- **Verification:** Asset ID와 해시 Chain을 대조한다.
- **Exceptions:** 외부 채널이 만든 비보존 Preview.

### IMG-006 - 특정 도구 종속 금지
- **Priority:** High
- **Statement:** 특정 AI·Stock·편집 도구를 유일한 실행 조건으로 요구하지 않는다.
- **Verification:** Brief와 Fallback 경로를 검사한다.
- **Exceptions:** Project MASTER가 선언한 제한 환경.

## 17.B 권리·동의·안전

### IMG-007 - Rights Basis 확인
- **Priority:** Critical
- **Statement:** 매체·지역·기간·수정·상업 사용 범위를 포함한 사용 근거를 확인한다.
- **Verification:** License 또는 허가 Evidence를 검토한다.
- **Exceptions:** 법적으로 검증된 공용 자산.

### IMG-008 - Attribution 보존
- **Priority:** Critical
- **Statement:** 필요한 Attribution·워터마크·권리 고지를 제거하거나 가리지 않는다.
- **Verification:** 원본 조건과 최종 Delivery를 비교한다.
- **Exceptions:** 권리자가 서면으로 면제한 경우.

### IMG-009 - 사람과 동의
- **Priority:** Critical
- **Statement:** 식별 가능한 사람과 미성년자 사용은 필요성·동의·오인 위험을 검토한다.
- **Verification:** Consent와 사용 Context를 확인한다.
- **Exceptions:** 적법한 보도·공적 기록의 승인 사용.

### IMG-010 - 개인정보 최소화
- **Priority:** Critical
- **Statement:** 화면·문서·사진의 불필요한 개인·위치·계정 정보를 제거한다.
- **Verification:** 확대 원본과 Metadata를 검사한다.
- **Exceptions:** 정보 자체가 승인된 보도 대상인 경우.

### IMG-011 - 실존 대상 오인 금지
- **Priority:** Critical
- **Statement:** 생성·합성 이미지로 실존 인물·기관·제품의 행동이나 보증을 허위 암시하지 않는다.
- **Verification:** 대상, Caption과 공개 Context를 검토한다.
- **Exceptions:** 명확히 표시된 승인 풍자·가상 예시.

### IMG-012 - 권리 불명 사용 중단
- **Priority:** Critical
- **Statement:** 권리·동의·출처를 합리적으로 확인할 수 없으면 사용하지 않는다.
- **Verification:** 미확인 Asset 차단 목록을 확인한다.
- **Exceptions:** 없음.

## 17.C 생성·편집·사실성

### IMG-013 - 도구 독립 Brief
- **Priority:** High
- **Statement:** Generation Brief는 역할·사실 제약·금지 요소·구도·출력 조건을 도구 독립적으로 기록한다.
- **Verification:** 다른 제작 경로로 실행 가능한지 검토한다.
- **Exceptions:** 도구별 Prompt Record.

### IMG-014 - 생성 실행 기록
- **Priority:** High
- **Statement:** 가능한 도구·모델·버전·Prompt·설정·Seed·작업 ID와 실행일을 기록한다.
- **Verification:** Registry와 생성 기록을 대조한다.
- **Exceptions:** 제공되지 않는 값은 unavailable로 표시.

### IMG-015 - 생성 사실 구분
- **Priority:** Critical
- **Statement:** 생성·합성·재현 이미지가 실제 증거로 오인되면 인접 설명으로 성격을 밝힌다.
- **Verification:** 이미지와 Caption·본문을 함께 검토한다.
- **Exceptions:** 오인 가능성이 없는 명백한 추상 장식.

### IMG-016 - 증거 조작 금지
- **Priority:** Critical
- **Statement:** Photo·Screenshot·Chart의 의미를 바꾸는 삭제·추가·재배열을 증거 편집으로 사용하지 않는다.
- **Verification:** 원본과 편집본 Pixel·Context를 비교한다.
- **Exceptions:** 명시된 개인정보 Mask와 비의미 Crop.

### IMG-017 - Safe Crop 보존
- **Priority:** Critical
- **Statement:** Crop은 Focal Point, 핵심 대상·Label과 사실 Context를 보존한다.
- **Verification:** 모든 파생 비율을 원본과 비교한다.
- **Exceptions:** 별도 의미로 승인된 새 Asset Version.

### IMG-018 - 편향 검토
- **Priority:** High
- **Statement:** 사람·문화·직업·위험 묘사에서 고정관념과 부당한 대표성을 검토한다.
- **Verification:** 후보 세트와 본문 Context를 함께 검토한다.
- **Exceptions:** 근거 있는 역사·보도 Context.

## 17.D 형식·반응형·접근성

### IMG-019 - 비파괴 원본 보존
- **Priority:** Critical
- **Statement:** Source Asset을 비파괴 보존하고 Delivery 변환은 파생본으로 만든다.
- **Verification:** 원본 해시와 파생 관계를 확인한다.
- **Exceptions:** 권리 조건상 원본 보존이 금지된 경우.

### IMG-020 - 표시 크기 적합성
- **Priority:** High
- **Statement:** 표시 폭과 기기 배율에 충분한 해상도를 제공하되 불필요한 초대형 전송을 피한다.
- **Verification:** 실제 Render 크기와 Pixel 크기를 비교한다.
- **Exceptions:** 사용자 확대가 핵심인 원본 보기.

### IMG-021 - Format Fallback
- **Priority:** Critical
- **Statement:** 형식 선택은 품질·투명도·지원 범위를 따르고 미지원 채널에 Fallback을 둔다.
- **Verification:** 지원 Matrix와 실제 Delivery를 검사한다.
- **Exceptions:** 단일 폐쇄 환경의 승인 형식.

### IMG-022 - 반응형 의미 보존
- **Priority:** Critical
- **Statement:** 모바일·Desktop 파생본은 같은 핵심 의미와 대상을 보존한다.
- **Verification:** 지원 폭별 전체 화면을 비교한다.
- **Exceptions:** 역할이 다른 별도 Asset으로 등록한 경우.

### IMG-023 - Context 기반 Alt
- **Priority:** Critical
- **Statement:** 의미 있는 이미지는 현재 Context의 기능·핵심 의미를 전달하는 Alt를 가진다.
- **Verification:** 이미지를 숨긴 읽기 경로를 검토한다.
- **Exceptions:** 동등 정보가 바로 인접하고 중복 Alt가 해로운 경우.

### IMG-024 - 복잡 이미지 상세 대안
- **Priority:** Critical
- **Statement:** Chart·Diagram·정보 Screenshot은 필요 시 표·상세 설명 등 동등 대안을 제공한다.
- **Verification:** 데이터와 관계가 텍스트 경로에서 복원되는지 확인한다.
- **Exceptions:** 본문이 이미 완전한 동등 대안인 경우.

## 17.E Registry·변경·QA

### IMG-025 - Registry 완전성
- **Priority:** Critical
- **Statement:** Asset ID, 원본·권리·상태·버전·파생본·접근성·사용처·Evidence를 연결한다.
- **Verification:** Registry 필수 Field를 검사한다.
- **Exceptions:** Production에 쓰지 않는 명시적 Prototype.

### IMG-026 - 안정적 이름과 버전
- **Priority:** High
- **Statement:** 파일명은 안정적 ID·의미·Variant·Version을 사용하고 다른 바이트를 조용히 덮어쓰지 않는다.
- **Verification:** 파일명, 버전과 해시 이력을 비교한다.
- **Exceptions:** 외부 플랫폼이 만든 캐시명.

### IMG-027 - 중복·폐기 추적
- **Priority:** High
- **Statement:** 중복과 폐기는 권리·Crop·Alt 차이, 대체 대상·사용처·복구 조건을 기록한다.
- **Verification:** 유사 Asset과 소비 문서를 대조한다.
- **Exceptions:** 배포되지 않은 임시 Preview.

### IMG-028 - 교체 영향 회귀
- **Priority:** Critical
- **Statement:** 교체 시 HTML·DOCX·PDF·CSS·Thumbnail·Alt·Source·게시·캐시 Gate를 다시 실행한다.
- **Verification:** 연결 QA와 변경 버전을 확인한다.
- **Exceptions:** 영향 없음이 입증된 Registry 주석 교정.

### IMG-029 - 열린 Critical 사용 금지
- **Priority:** Critical
- **Statement:** 권리·동의·사실성·개인정보·접근성 Critical 결함이 열려 있으면 사용·PASS·LOCK·Release하지 않는다.
- **Verification:** Defect Register와 Gate 판정을 대조한다.
- **Exceptions:** 없음.

### IMG-030 - 최종 해시 갱신
- **Priority:** Critical
- **Statement:** 원본·파생본·계약·QA·상태가 바뀌면 관련 최종 해시를 다시 계산하고 검증한다.
- **Verification:** Registry·SHA 파일과 현재 파일을 비교한다.
- **Exceptions:** 해시 대상 밖 전달 메타데이터.

# 18. AI용 압축 Image System

## 18.1 압축 지침

다음 블록은 DSG-005가 APPROVED 또는 LOCKED된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 LOCKED이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-005 IMAGE SYSTEM v2.0을 따른다.
1. 이미지 역할과 정보 기여를 먼저 정하고 참고 Output의 개수·비율·위치·화풍을 전역 고정하지 않는다.
2. Original·User-provided·Official·Licensed·Generated Source Class와 원본·제공자·권리·날짜를 기록한다.
3. 원본·편집본·파생본·사용처를 Asset ID와 해시로 연결하고 다른 바이트를 같은 Version으로 덮어쓰지 않는다.
4. 권리·동의·개인정보·워터마크를 확인하며 불명확하거나 목적과 충돌하면 사용을 중단한다.
5. 생성 Brief는 도구 독립적으로 작성하고 가능한 도구·모델·Prompt·설정·Seed·후편집을 기록하되 제공되지 않는 값은 만들지 않는다.
6. 생성·합성·재현이 실제 증거로 오인되면 성격을 표시하고 증거 이미지의 의미를 바꾸는 편집을 금지한다.
7. 원본을 비파괴 보존하고 Focal Point·Label·Context를 지키는 Crop, 적정 해상도·Format·색·Fallback을 검증한다.
8. 모바일·Desktop·DOCX·PDF 파생본은 같은 의미를 보존하고 Alt·Caption·복잡 이미지 상세 대안을 제공한다.
9. Registry에 역할·권리·버전·파생본·사용처·Evidence를 연결하고 교체 시 모든 연결 Delivery를 회귀 검수한다.
10. 권리·동의·사실성·개인정보·접근성 Critical 결함이 열려 있으면 사용·PASS·LOCK·Release하지 않는다.
```

## 18.2 추출 조건

- DSG-005가 APPROVED 또는 LOCKED 상태다.
- Project MASTER·Brand·Component·Source·Delivery 계약과 충돌하지 않는지 대표 Asset으로 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| 이미지 역할·출처·권리·생성·편집·Alt·파생본은? | DSG-005 IMAGE SYSTEM |
| 이미지 Slot·구조·Cardinality는? | DSG-004 COMPONENT LIBRARY |
| HTML Figure·img·Caption 의미는? | DSG-001 HTML SYSTEM |
| DOCX 배치와 PDF 변환은? | DSG-002 DOCX SYSTEM |
| CSS 크기·비율·Overflow는? | DSG-003 CSS GOVERNANCE |
| 썸네일 비율·문자 안전 영역은? | DSG-006 THUMBNAIL RULES |
| 실제 Brand 색·로고·서체·화풍은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 출처 인용과 신뢰 등급은? | COR-004 SOURCE POLICY |
| 게시 발행·수정·삭제는? | CNT-006 PUBLISHING SYSTEM |
| 자동 생성·변환·실패 복구는? | AUT 문서 |

## 19.2 알려진 제한

- 현재 기준은 정적 리포트, 모바일 블로그 본문, DOCX와 PDF 전달을 중심으로 추출했다.
- 의료 영상, 법정 증거, 생체 식별, 고정밀 과학·지도·원격탐사 이미지는 분야별 전문 검증이 추가로 필요하다.
- 생성 도구별 안전 설정과 License 조건은 변할 수 있으므로 실제 실행 시점의 공식 조건을 별도 확인해야 한다.
- 실제 Brand 화풍과 썸네일 안전 영역은 DSG-006·007 및 Project MASTER 승인 전 확정되지 않는다.
- 이 문서는 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이며 운영 Runtime·Release 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | DSG-001~004와 COR-004 경계에서 이미지 역할·출처·권리·생성·편집·형식·접근성·Registry·회귀 규칙을 특정 AI 도구 비종속 계약으로 분리하고 사용자 승인·잠금 승인 완료 |
