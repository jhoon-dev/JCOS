# JCOS v2.0.0 - DSG-006 THUMBNAIL RULES

## 채널별 썸네일 구성·안전 영역 기준

| Field | Value |
|---|---|
| Document ID | DSG-006 |
| Title | THUMBNAIL RULES |
| Korean Title | 채널별 썸네일 구성·안전 영역 기준 |
| Version | 2.0.0 |
| Status | LOCKED |
| Owner | JCOS Maintainers |
| Category | DESIGN SYSTEM |
| Applies To | 목록·검색·공유·게시 미리보기에 사용하는 Cover·Thumbnail·Preview 이미지와 파생본 |
| Priority | HIGH |
| Created | 2026-08-02 |
| Last Updated | 2026-08-02 |
| Inherits | JCOS Core v2.0.0 LOCKED, DSG-001~004 v2.0.0 APPROVED, DSG-005 v2.0.0 APPROVED |
| Reference Implementation | PROJECT_REFERENCE_FIXTURE v1.0.1 LOCKED / DOCX_FULL_REPORT·BLOG_SUMMARY_HTML |
| Depends On | COR-004 SOURCE POLICY, FND-002 ARCHITECTURE, FND-003 DOCUMENT REGISTER, FND-005 ROADMAP |

> 상태 알림: 이 문서는 썸네일의 역할·Profile·비율·안전 영역·Crop·텍스트·채널 파생·검수 계약을 분리해 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이다. 특정 AI 생성기나 편집기를 필수로 요구하지 않는다.

# 문서 목적

DSG-006은 같은 콘텐츠가 목록, 검색, 공유 카드와 게시 화면에서 서로 다른 Crop과 Overlay를 거치더라도 핵심 의미와 브랜드 식별성을 잃지 않도록 썸네일 계약을 정의한다. 전역 단일 비율 대신 실제 Channel·Slot 요구를 Thumbnail Profile로 기록하고, 안전 영역·Focal Point·텍스트·파일·접근성·회귀 조건을 검증 가능하게 만든다.

이 문서는 이미지 생성·출처·권리, 실제 색·로고·서체 값, 게시 운영이나 Component Cardinality를 다시 정의하지 않는다. 각 값은 DSG-005·007, Project MASTER, CNT-006과 DSG-004가 소유한다.

# 목차

1. 적용 범위와 비범위
2. 계층과 권한
3. 핵심 용어
4. 썸네일 역할과 Profile
5. Canvas·비율·크기
6. 안전 영역과 Crop
7. 구성·Focal Point·시각 계층
8. 텍스트 Overlay와 가독성
9. 브랜드·대비·식별성
10. 이미지 출처·사실성·권리 경계
11. 채널 파생본과 반응형 Preview
12. 파일 형식·품질·성능
13. 접근성·Metadata·Fallback
14. Registry·버전·교체
15. 검증과 품질 Gate
16. 변경·승인·LOCK 수명주기
17. 규칙 카탈로그
18. AI용 압축 Thumbnail Rules
19. 책임 경계와 알려진 제한
20. 변경 이력

# 1. 적용 범위와 비범위

## 1.1 적용 범위

- 게시 목록, 검색 결과, 관련 글, 소셜 공유, 메신저 Preview, Cover와 대표 이미지
- Channel·Slot별 Thumbnail Profile, Canvas 비율·Pixel 크기·Safe Area·Crop·Focal Point
- 텍스트 Overlay, Logo·Badge·Label 배치 역할과 모바일 축소 가독성
- 원본 연결, 파생본 이름·해시·파일 품질·Fallback·Registry와 회귀 QA

## 1.2 비범위

| 항목 | 전담 기준 |
|---|---|
| 원본 이미지 생성·선정·출처·권리·Alt | DSG-005 IMAGE SYSTEM |
| Thumbnail Slot·필수성·Cardinality | DSG-004 COMPONENT LIBRARY |
| HTML img·picture·Metadata 의미 구조 | DSG-001 HTML SYSTEM |
| DOCX Cover 배치와 PDF 변환 | DSG-002 DOCX SYSTEM |
| CSS object-fit·aspect-ratio·Overflow 구현 | DSG-003 CSS GOVERNANCE |
| 실제 색상·로고·서체·화풍 | DSG-007 BRAND SYSTEM과 Project MASTER |
| 제목·요약 문구의 내용 | Content Schema와 작성 기준 |
| 게시 채널 발행·수정·캐시 제거 | CNT-006 PUBLISHING SYSTEM |
| 자동 생성·Resize·배포·실패 복구 | AUT 문서 |

## 1.3 금지되는 확장

- 한 플랫폼의 현재 권장 비율이나 Pixel 값을 JCOS 전역 영구값으로 고정
- 참고 Output의 이미지 수, 소재, 문구, 배치와 장식 외형을 공통 필수값으로 승격
- 특정 AI 생성기·Design Tool·Plugin을 유일한 제작 경로로 요구
- 작은 Preview에서 읽히지 않는 본문, 출처, 표 또는 핵심 설명을 썸네일에 축약 수록

# 2. 계층과 권한

## 2.1 권한 순서

1. 법률·안전·플랫폼 필수 제한과 이미지 권리
2. 사용자의 현재 명시적 요청
3. 승인 Content Schema·Project MASTER·Channel Profile
4. DSG-006 THUMBNAIL RULES와 DSG-005 IMAGE SYSTEM
5. DSG-004 Component, DSG-007 Brand와 DSG-001~003 전달 형식
6. 실제 게시 채널에서 검증한 Slot·Crop·Preview 동작
7. 참고 구현과 과거 Output

## 2.2 채널 값의 권한

비율, 최소 Pixel, 파일 용량과 Overlay 제한은 Channel·Slot별 검증 Evidence와 적용일을 가진 Profile에서 정한다. 플랫폼 안내와 실제 Render가 다르면 실제 결과를 기록하고 더 안전한 범위를 적용하되 전역 규칙으로 확대하지 않는다.

## 2.3 충돌 처리

Brand 표현과 작은 화면 가독성이 충돌하면 핵심 제목·대상 식별과 접근성을 우선한다. 권리·사실성·안전 기준과 충돌하면 썸네일 사용을 중단하거나 텍스트 전용 Fallback을 사용한다.

# 3. 핵심 용어

| 용어 | 정의 |
|---|---|
| Thumbnail Profile | Channel·Slot별 목적, 비율, 크기, Crop, Overlay와 QA 조건 묶음 |
| Canvas | 최종 썸네일 파일의 전체 Pixel 영역 |
| Aspect Ratio | Canvas 너비와 높이의 비 관계 |
| Safe Area | 자동 Crop·UI Overlay 후에도 핵심 정보를 보존해야 하는 내부 영역 |
| Exclusion Zone | Logo·얼굴·제목 등 다른 요소가 침범하지 않아야 하는 영역 |
| Focal Point | 축소·Crop 후에도 가장 먼저 식별해야 하는 대상 |
| Text Overlay | Canvas 안에 Raster 또는 Vector로 합성된 제목·Label·Badge |
| Preview Fixture | 실제 Channel·Slot·기기에서 표시 결과를 검증하는 샘플 |
| Master Thumbnail | 여러 Profile 파생본의 근거가 되는 편집 가능한 승인 원본 |
| Derivative | Profile에 맞춰 Master Thumbnail에서 만든 최종 파일 |

# 4. 썸네일 역할과 Profile

## 4.1 역할 선언

썸네일은 콘텐츠 식별, 주제 예고, Series 식별, 행동 유도 중 주 역할 하나와 필요한 보조 역할을 기록한다. 실제 본문을 대체하거나 사실을 과장하는 역할을 부여하지 않는다.

## 4.2 Profile 필드

Profile에는 Channel, Slot, 목적, 적용일, Canvas 비율·Pixel 범위, Safe Area, 허용 Crop, Focal Point, Overlay 허용량, Logo·Badge 역할, 파일 제한, Fallback과 Preview Fixture를 포함한다.

## 4.3 관찰값과 승인값

특정 날짜의 썸네일 모습은 참고 Fixture이며 규칙이 아니다. Platform 안내나 실제 Slot 변화가 확인되면 Profile Version을 갱신하고 영향 채널을 다시 검수한다.

# 5. Canvas·비율·크기

## 5.1 비율 결정

비율은 Channel·Slot에서 실제로 보이는 영역과 자동 Crop 동작을 근거로 정한다. 하나의 Master Canvas로 여러 극단적 비율을 억지로 해결하지 않고 의미 보존이 어려우면 별도 Art Direction 파생본을 만든다.

## 5.2 Pixel 크기

Pixel 크기는 표시 크기, 기기 배율, 플랫폼 재압축과 파일 제한을 함께 고려한다. 작은 원본을 인위적으로 확대하지 않고, 필요 이상의 초대형 파일을 기본 전달하지 않는다.

## 5.3 방향과 회전

가로·세로·정방형은 Profile의 명시적 Variant다. EXIF 회전에 의존하지 않고 최종 Pixel 방향을 확정하며, 회전 또는 Mirror가 텍스트·Logo·사실 Context를 바꾸지 않는지 확인한다.

# 6. 안전 영역과 Crop

## 6.1 Safe Area

Safe Area는 단순 중앙 Percentage가 아니라 실제 자동 Crop, 모서리 Mask, 재생 아이콘, 시간 Label, Channel UI Overlay를 반영한다. 제목, 얼굴, Logo와 핵심 Focal Point는 해당 Profile의 안전 영역 안에 둔다.

## 6.2 Crop 허용 범위

Crop은 핵심 대상·제품 정보·Diagram Label과 사실 Context를 보존해야 한다. 얼굴·신체·상표·문자 또는 대상 간 관계를 부자연스럽게 자르지 않고, Crop마다 DSG-005 Asset 계보를 유지한다.

## 6.3 Exclusion Zone

Logo, 제목, Badge, Focal Point의 최소 이격과 상호 침범 금지 영역을 Profile에 기록한다. 플랫폼 UI가 차지하는 영역은 콘텐츠 배치에 사용하지 않는다.

# 7. 구성·Focal Point·시각 계층

## 7.1 단일 핵심

작은 크기에서 첫 시선 대상이 하나로 식별되도록 구성한다. 여러 사진, 긴 Chart, 작은 Icon을 밀집시켜 본문 페이지를 축소한 것처럼 만들지 않는다.

## 7.2 계층

Focal Point, 제목, Series·Category, Brand 식별자, 보조 Badge 순으로 중요도를 정한다. 모든 요소를 같은 크기·대비로 강조하지 않고, 보조 정보는 제거해도 주제 식별이 유지되어야 한다.

## 7.3 배경과 분리

텍스트와 핵심 대상은 복잡한 배경에서 충분히 분리한다. 필요하면 승인된 Overlay·Gradient·Mask를 사용하되 이미지 사실 의미나 Brand 규칙을 왜곡하지 않는다.

# 8. 텍스트 Overlay와 가독성

## 8.1 텍스트 최소화

Overlay는 짧은 제목, Series, Category 또는 상태 Label처럼 썸네일에서 필요한 정보만 사용한다. 본문 요약, 출처 목록, 여러 문장, URL과 표를 넣지 않는다.

## 8.2 축소 가독성

문자 크기, 줄 수, 행간, 자간과 대비는 Profile의 최소 Preview 크기에서 확인한다. 임의 Line Clamp로 핵심 단어를 자르지 않고, 긴 제목은 승인된 축약 또는 텍스트 없는 Variant를 사용한다.

## 8.3 문자 안전

문자는 Safe Area와 Exclusion Zone 안에 두며 가장자리, 얼굴, Logo, 플랫폼 UI와 겹치지 않는다. Raster 합성 전 오탈자·날짜·숫자·고유명사를 검수하고 생성 이미지 속 가짜 문자를 그대로 사용하지 않는다.

# 9. 브랜드·대비·식별성

## 9.1 Brand 역할

DSG-006은 Brand Token 역할과 배치 조건만 요구한다. 실제 색, Logo Variant, 서체, 모서리와 화풍은 DSG-007과 Project MASTER의 승인값을 사용한다.

## 9.2 대비

텍스트·Logo·Badge는 배경과 충분히 구분되고 색상만으로 Series·상태를 전달하지 않는다. 밝고 어두운 후보 배경, 축소, 저품질 Preview와 무채색 경로에서 식별성을 검수한다.

## 9.3 Logo 사용

Logo는 승인 원본·Clear Space·최소 크기·배경 Variant를 따른다. 공간이 부족하면 Logo를 변형하거나 찌그러뜨리지 않고 Profile이 허용한 축약 Mark 또는 생략 Variant를 사용한다.

# 10. 이미지 출처·사실성·권리 경계

## 10.1 DSG-005 상속

Master Thumbnail과 모든 시각 Asset은 DSG-005의 Source Class, Rights Basis, 동의, 생성 기록, 편집 무결성과 해시 계보를 통과해야 한다. 썸네일 용도라는 이유로 권리 검수를 생략하지 않는다.

## 10.2 사실성

자극적인 Crop·합성·Label로 본문이 말하지 않는 결과, 인물 발언, 제품 기능 또는 사건 현장을 암시하지 않는다. 생성·재현 이미지가 증거로 오인되면 본문과 Metadata의 표시 경로를 마련한다.

## 10.3 민감 소재

미성년자, 사고, 의료, 범죄, 재난과 개인 식별 정보는 노출 필요성과 낙인·충격 위험을 검토한다. 클릭 유도를 위해 민감 장면을 확대하거나 Context 없이 사용하지 않는다.

# 11. 채널 파생본과 반응형 Preview

## 11.1 파생 전략

동일 Master에서 Resize만 할지, Crop을 바꿀지, 구성을 새로 만드는 Art Direction이 필요한지 Profile별로 결정한다. 별도 구성이면 같은 Content ID 아래 독립 Asset Version으로 추적한다.

## 11.2 실제 Preview

파일 자체만 검수하지 않고 실제 목록·검색·공유 카드·메신저·모바일·Desktop Preview에서 확인한다. 플랫폼 재압축, 모서리 Mask, 제목 중복, UI Overlay와 Dark Mode 영향을 포함한다.

## 11.3 캐시와 전파

교체 후 오래된 Preview 캐시가 남을 수 있음을 기록하고 CNT-006의 갱신·무효화 절차와 연결한다. URL Query 변경을 유일한 복구 방식으로 고정하지 않고 채널별 검증 경로를 둔다.

# 12. 파일 형식·품질·성능

## 12.1 Format과 Alpha

사진, 평면 그래픽, 투명 배경의 특성과 Channel 지원 범위에 맞는 Format을 선택한다. Alpha가 검정·흰색 배경에서 깨지지 않는지 확인하고 미지원 형식에는 Fallback을 제공한다.

## 12.2 압축 품질

축소 Preview에서 경계, 작은 문자, 얼굴, Gradient와 Logo가 뭉개지거나 Ringing이 생기지 않는 범위로 압축한다. 원본 품질과 전달 용량을 함께 기록하며 같은 파일을 반복 손실 압축하지 않는다.

## 12.3 파일 안전

확장자·MIME·실제 Encoding을 일치시키고 EXIF 방향을 확정한다. 불필요한 위치·기기 Metadata는 제거하되 Rights·Provenance 정보는 Registry에 보존한다.

# 13. 접근성·Metadata·Fallback

## 13.1 대체 경로

썸네일 안의 핵심 주제와 Overlay 텍스트는 접근 가능한 제목·Alt·Label 또는 인접 본문에서 동등하게 제공한다. 이미지 속 문자만으로 콘텐츠 제목이나 상태를 전달하지 않는다.

## 13.2 공유 Metadata

Open Graph 등 공유 Metadata는 정확한 제목, 설명, 이미지 URL, 크기·Format 정보를 현재 Content Version과 연결한다. 썸네일 교체 후 Metadata와 실제 응답을 다시 확인한다.

## 13.3 Fallback

이미지 누락·로드 실패·차단·Crop 실패 시 기본 Brand Placeholder, 텍스트 전용 카드 또는 승인된 원본 Crop을 사용한다. 깨진 Frame, 빈 Alt와 무관한 과거 썸네일을 성공으로 처리하지 않는다.

# 14. Registry·버전·교체

## 14.1 Profile Registry

Registry는 Profile ID, Channel·Slot, Owner, Version, 상태, 적용일, Canvas, Safe Area, Overlay, 파일 제한, Fixture와 Evidence를 기록한다. 검증되지 않은 추정값은 Production Profile로 선언하지 않는다.

## 14.2 Asset 연결

Thumbnail ID를 Content ID, Master Thumbnail, DSG-005 Source Asset, Profile Version, 파생본 경로·크기·해시, Alt·Metadata와 사용 URL에 연결한다.

## 14.3 교체와 폐기

교체 이유, 이전·신규 ID, 영향 Channel, 캐시, Metadata, 전환일과 Rollback 경로를 기록한다. 다른 Content에 재사용 중인 Asset을 검색 없이 삭제하거나 같은 ID로 다른 바이트를 덮어쓰지 않는다.

# 15. 검증과 품질 Gate

## 15.1 구성 Gate

- 역할·Content ID·Profile ID·Channel·Slot과 Focal Point
- Canvas 비율·Pixel·Safe Area·Exclusion Zone·자동 Crop
- 제목·Logo·Badge 계층, 최소 Preview의 문자·대상 식별성
- 민감 소재, 사실성, Rights Basis와 생성·편집 기록

## 15.2 전달 Gate

- 원본·파생 해시, Format·MIME·Alpha·색·압축·파일 용량
- 목록·검색·공유·메신저·모바일·Desktop 실제 Preview
- UI Overlay·Mask·재압축·Dark Mode·캐시·Metadata·Fallback
- 접근 가능한 제목·Alt·Label과 이미지 속 문자 동등 대안

## 15.3 판정

권리·사실성·핵심 대상 잘림·제목 판독 불가·잘못된 Content 연결·접근성 Critical 결함이 하나라도 열려 있으면 사용·PASS·LOCK·Release를 선언하지 않는다. 자동 점수나 생성 도구 Preview만으로 최종 판정하지 않는다.

# 16. 변경·승인·LOCK 수명주기

1. Content, Channel, Slot과 썸네일 역할을 식별한다.
2. Profile과 Master Thumbnail 후보, Focal Point와 Safe Area를 정한다.
3. 텍스트·Brand 역할·DSG-005 Asset·파생 조건을 연결한다.
4. 최소 Preview와 실제 채널 Fixture에서 구성·전달 Gate를 실행한다.
5. Markdown·DOCX·PDF·QA·해시 패키지를 REVIEW로 작성한다.
6. 사용자 검토와 수정 후 기준 문서를 APPROVED로 전환한다.
7. 대표 채널 회귀와 명시적 잠금 승인 후 LOCKED로 전환한다.

LOCKED 이후 Profile이나 규칙을 변경할 때는 승인본을 조용히 덮어쓰지 않고 Version 후보와 History를 만든다.

# 17. 규칙 카탈로그

## 17.A 권한·Profile·Canvas

### THM-001 - 상위 기준 우선
- **Priority:** Critical
- **Statement:** 썸네일은 법률·안전·권리, 사용자 요청과 승인 MASTER·Channel 제한을 무효화하지 않는다.
- **Verification:** 적용 Profile과 상위 계약을 대조한다.
- **Exceptions:** 더 엄격한 플랫폼 필수 제한.

### THM-002 - 역할 선행
- **Priority:** High
- **Statement:** 제작 전에 Content, Channel, Slot과 썸네일의 주 역할을 기록한다.
- **Verification:** Brief·Profile·사용처를 확인한다.
- **Exceptions:** 승인된 기본 Placeholder.

### THM-003 - Profile 기반 값
- **Priority:** Critical
- **Statement:** 비율·Pixel·Safe Area·Overlay 제한은 버전화된 Channel·Slot Profile에서 가져온다.
- **Verification:** Profile ID와 적용일을 확인한다.
- **Exceptions:** REVIEW Fixture의 명시적 실험값.

### THM-004 - 전역 비율 고정 금지
- **Priority:** Critical
- **Statement:** 한 채널의 비율·Pixel 값을 JCOS 전역 영구값으로 사용하지 않는다.
- **Verification:** Profile 간 값과 근거를 비교한다.
- **Exceptions:** 모든 대상 Slot이 동일함을 검증한 Project 범위.

### THM-005 - 특정 도구 종속 금지
- **Priority:** High
- **Statement:** 특정 AI 생성기·편집기·Plugin을 유일한 제작 조건으로 요구하지 않는다.
- **Verification:** Brief와 대체 제작 경로를 검사한다.
- **Exceptions:** Project MASTER가 선언한 제한 환경.

### THM-006 - Pixel 적합성
- **Priority:** High
- **Statement:** 표시 크기·기기 배율·재압축에 충분한 Pixel을 제공하되 불필요한 초대형 파일을 피한다.
- **Verification:** Canvas와 실제 Render 크기를 비교한다.
- **Exceptions:** 사용자 확대용 원본 보기.

## 17.B Safe Area·Crop·구성

### THM-007 - 실제 Safe Area
- **Priority:** Critical
- **Statement:** Safe Area는 자동 Crop·Mask·UI Overlay를 반영하고 핵심 요소를 내부에 보존한다.
- **Verification:** 실제 Channel Preview를 비교한다.
- **Exceptions:** Crop이 없는 검증된 Slot.

### THM-008 - Exclusion Zone
- **Priority:** High
- **Statement:** 제목·Logo·Badge·Focal Point와 플랫폼 UI 사이의 침범 금지 영역을 정의한다.
- **Verification:** Overlay Map과 최종 Preview를 검사한다.
- **Exceptions:** 단일 요소 Text-only Thumbnail.

### THM-009 - Focal Point 보존
- **Priority:** Critical
- **Statement:** 모든 Profile 파생본에서 핵심 대상과 사실 Context를 보존한다.
- **Verification:** Master와 파생 Crop을 대조한다.
- **Exceptions:** 별도 역할의 독립 Asset Version.

### THM-010 - 부자연스러운 Crop 금지
- **Priority:** Critical
- **Statement:** 얼굴·신체·상표·문자·Diagram Label과 대상 관계를 오해하게 자르지 않는다.
- **Verification:** 지원 비율별 전체 Crop을 확인한다.
- **Exceptions:** 의미에 영향 없는 배경 Crop.

### THM-011 - 단일 시선 핵심
- **Priority:** High
- **Statement:** 최소 Preview에서 첫 시선 대상 하나와 보조 계층을 식별 가능하게 한다.
- **Verification:** 축소·Blur·5초 식별 Fixture를 확인한다.
- **Exceptions:** 승인된 비교형 두 대상 구성.

### THM-012 - 밀집 구성 금지
- **Priority:** High
- **Statement:** 본문 페이지·표·여러 이미지를 축소 복제해 작은 요소를 밀집시키지 않는다.
- **Verification:** 최소 Preview에서 요소 수와 판독성을 확인한다.
- **Exceptions:** 읽기보다 패턴 인지가 목적인 승인 Collage.

## 17.C 텍스트·Brand·사실성

### THM-013 - Overlay 최소화
- **Priority:** High
- **Statement:** 텍스트는 짧은 제목·Series·Category·상태 Label 등 필요한 정보로 제한한다.
- **Verification:** Overlay 문자열과 Content Schema를 대조한다.
- **Exceptions:** Text-only Fallback.

### THM-014 - 최소 Preview 판독
- **Priority:** Critical
- **Statement:** 문자 크기·줄 수·행간·대비를 Profile 최소 Preview에서 검증한다.
- **Verification:** 실제 Pixel 크기로 렌더한다.
- **Exceptions:** 텍스트 없는 승인 Variant.

### THM-015 - 문자 정확성
- **Priority:** Critical
- **Statement:** 제목·날짜·숫자·고유명사를 검수하고 생성 이미지 속 가짜 문자를 사용하지 않는다.
- **Verification:** 원문 Field와 Raster 결과를 비교한다.
- **Exceptions:** 의미 없는 추상 문자 Texture.

### THM-016 - Brand 계약 준수
- **Priority:** Critical
- **Statement:** 색·Logo·서체·화풍은 DSG-007과 Project MASTER의 승인값을 사용한다.
- **Verification:** Brand Token·Asset Version을 확인한다.
- **Exceptions:** DSG-007 승인 전 명시적 무브랜드 Prototype.

### THM-017 - 색상 외 식별
- **Priority:** Critical
- **Statement:** Series·Category·상태를 색상만으로 구분하지 않고 텍스트·형태·구조 단서를 제공한다.
- **Verification:** 무채색·고대비 Preview를 확인한다.
- **Exceptions:** 의미가 없는 장식 색 변화.

### THM-018 - 과장·오인 금지
- **Priority:** Critical
- **Statement:** Crop·합성·Label로 본문에 없는 결과·발언·기능·사건을 암시하지 않는다.
- **Verification:** Thumbnail 주장과 본문 근거를 대조한다.
- **Exceptions:** 명확히 표시된 승인 풍자·가상 예시.

## 17.D 채널·파일·접근성

### THM-019 - Art Direction 분기
- **Priority:** High
- **Statement:** 의미 보존이 어려운 극단 비율은 Resize 대신 별도 구성 파생본으로 관리한다.
- **Verification:** Profile별 Crop 손실을 비교한다.
- **Exceptions:** 동일 Crop으로 의미가 보존되는 경우.

### THM-020 - 실제 채널 Preview
- **Priority:** Critical
- **Statement:** 파일만 보지 않고 목록·검색·공유·메신저·모바일·Desktop 실제 결과를 검수한다.
- **Verification:** Preview Fixture Evidence를 확인한다.
- **Exceptions:** 배포 전 명시적 구조 Prototype.

### THM-021 - Format Fallback
- **Priority:** Critical
- **Statement:** Format·Alpha·MIME를 채널 지원에 맞추고 미지원 환경에 Fallback을 둔다.
- **Verification:** 지원 Matrix와 실제 응답을 검사한다.
- **Exceptions:** 단일 폐쇄 환경의 승인 형식.

### THM-022 - 손실 누적 금지
- **Priority:** High
- **Statement:** 반복 손실 압축을 피하고 Master에서 각 전달 파생본을 생성한다.
- **Verification:** 생성 계보와 압축 Artifact를 확인한다.
- **Exceptions:** 외부 플랫폼의 통제 불가 재압축.

### THM-023 - 접근 가능한 동등 경로
- **Priority:** Critical
- **Statement:** 주제와 Overlay 텍스트를 제목·Alt·Label 또는 인접 본문에서 동등하게 제공한다.
- **Verification:** 이미지를 숨긴 읽기 경로를 검토한다.
- **Exceptions:** 완전한 인접 중복 정보.

### THM-024 - Metadata 일치
- **Priority:** Critical
- **Statement:** 공유 제목·설명·이미지 URL·크기·Format을 현재 Content·Thumbnail Version과 일치시킨다.
- **Verification:** 실제 공유 응답과 Registry를 비교한다.
- **Exceptions:** Metadata를 지원하지 않는 채널.

## 17.E Registry·변경·QA

### THM-025 - Profile Registry 완전성
- **Priority:** Critical
- **Statement:** Profile ID·Channel·Slot·Version·Canvas·Safe Area·Overlay·Fixture·Evidence를 기록한다.
- **Verification:** 필수 Field를 검사한다.
- **Exceptions:** Production에 쓰지 않는 명시적 Prototype.

### THM-026 - Asset 연결 완전성
- **Priority:** Critical
- **Statement:** Thumbnail을 Content·Master·Source Asset·Profile·파생본·Alt·Metadata·URL과 연결한다.
- **Verification:** Registry 관계와 해시를 대조한다.
- **Exceptions:** 없음.

### THM-027 - 조용한 덮어쓰기 금지
- **Priority:** Critical
- **Statement:** 같은 ID·Version으로 다른 Thumbnail 바이트를 조용히 덮어쓰지 않는다.
- **Verification:** 파일 해시와 Version 이력을 확인한다.
- **Exceptions:** 해시에 영향 없는 외부 표시명.

### THM-028 - 교체·캐시 회귀
- **Priority:** Critical
- **Statement:** 교체 시 Channel Preview·Metadata·URL·캐시·Fallback과 소비 Content를 다시 검수한다.
- **Verification:** 전환 Evidence와 이전·신규 ID를 확인한다.
- **Exceptions:** 영향 없음이 입증된 Registry 주석 교정.

### THM-029 - 열린 Critical 사용 금지
- **Priority:** Critical
- **Statement:** 권리·오인·핵심 잘림·판독·Content 연결·접근성 Critical 결함이 열려 있으면 사용·PASS·LOCK·Release하지 않는다.
- **Verification:** Defect Register와 Gate 판정을 대조한다.
- **Exceptions:** 없음.

### THM-030 - 최종 해시 갱신
- **Priority:** Critical
- **Statement:** Profile·Master·파생본·계약·QA·상태가 바뀌면 관련 최종 해시를 다시 계산하고 검증한다.
- **Verification:** Registry·SHA 파일과 현재 파일을 비교한다.
- **Exceptions:** 해시 대상 밖 전달 메타데이터.

# 18. AI용 압축 Thumbnail Rules

## 18.1 압축 지침

다음 블록은 DSG-006이 APPROVED 또는 LOCKED된 뒤 Core·Project Runtime에 연결할 후보 압축본이다. 현재 상태는 LOCKED이며 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

```text
JCOS DSG-006 THUMBNAIL RULES v2.0을 따른다.
1. Content·Channel·Slot·역할을 먼저 정하고 참고 Output이나 한 플랫폼의 비율·Pixel·개수를 전역 고정하지 않는다.
2. 비율·Canvas·Safe Area·Overlay·파일 제한은 적용일과 Evidence가 있는 버전화된 Thumbnail Profile에서 가져온다.
3. 자동 Crop·Mask·UI Overlay를 반영해 Focal Point·제목·Logo를 Safe Area 안에 두고 Exclusion Zone을 지킨다.
4. 작은 Preview에서 첫 시선 대상 하나와 보조 계층을 유지하며 본문·표·여러 이미지를 축소 밀집하지 않는다.
5. Overlay는 짧고 정확하게 쓰며 최소 Preview에서 문자·대상·대비를 확인하고 생성 이미지 속 가짜 문자를 사용하지 않는다.
6. 실제 Brand 값은 DSG-007·Project MASTER, 이미지 출처·권리·생성은 DSG-005를 따르고 과장·오인 Crop·합성을 금지한다.
7. 의미 보존이 어려운 비율은 별도 Art Direction 파생본으로 만들고 Master·Source·Profile·해시 계보를 유지한다.
8. Format·Alpha·MIME·압축·Fallback을 검증하고 제목·Alt·Label·공유 Metadata에 동등 정보를 제공한다.
9. 파일이 아니라 실제 목록·검색·공유·메신저·모바일·Desktop Preview와 캐시·Metadata를 회귀 검수한다.
10. 권리·오인·핵심 잘림·판독·연결·접근성 Critical 결함이 열려 있으면 사용·PASS·LOCK·Release하지 않는다.
```

## 18.2 추출 조건

- DSG-006이 APPROVED 또는 LOCKED 상태다.
- 실제 Project MASTER·Brand·Image·Channel Profile과 충돌하지 않는지 대표 Thumbnail로 회귀 검증했다.
- Runtime Manifest가 정확한 버전·상태·경로·해시와 추출 Section을 기록한다.
- 압축본에 없는 판단과 충돌은 상세 승인본이 우선한다.

# 19. 책임 경계와 알려진 제한

## 19.1 책임 경계

| 질문 | 담당 기준 |
|---|---|
| Channel·Slot별 비율·Safe Area·Crop·Overlay·Preview는? | DSG-006 THUMBNAIL RULES |
| 원본 이미지 생성·선정·권리·Alt·파생 계보는? | DSG-005 IMAGE SYSTEM |
| Thumbnail Slot·구조·Cardinality는? | DSG-004 COMPONENT LIBRARY |
| HTML img·picture·공유 Metadata 의미는? | DSG-001 HTML SYSTEM |
| DOCX Cover 배치와 PDF 변환은? | DSG-002 DOCX SYSTEM |
| CSS aspect-ratio·object-fit·Overflow는? | DSG-003 CSS GOVERNANCE |
| 실제 Brand 색·Logo·서체·화풍은? | DSG-007 BRAND SYSTEM과 Project MASTER |
| 제목·요약 문구 내용은? | Content Schema와 작성 기준 |
| 게시·공유 캐시 갱신은? | CNT-006 PUBLISHING SYSTEM |
| 자동 Resize·배포·실패 복구는? | AUT 문서 |

## 19.2 알려진 제한

- 현재 기준은 정적 리포트, 블로그 목록·본문 대표 이미지와 일반 공유 Preview를 중심으로 추출했다.
- 플랫폼별 비율·Pixel·파일 제한은 변경될 수 있으므로 실제 실행 시점의 공식 안내와 Preview를 다시 확인해야 한다.
- Video 자동 Thumbnail, Animated Image, 360도·3D Preview, Live Commerce와 광고 입찰용 Creative는 실제 적용 검증 전이다.
- 실제 Brand Token과 Logo Variant는 DSG-007 및 Project MASTER 승인 전 확정되지 않는다.
- 이 문서는 사용자 승인과 명시적 잠금 승인을 받은 LOCKED 기준본이며 운영 Runtime·Release 반영은 후속 통합·검증 Gate에서 별도로 결정한다.

# 20. 변경 이력

| Version | Date | Status | Description |
|---|---|---|---|
| 2.0.0 | 2026-08-02 | LOCKED | DSG-001~005와 DSG-007·Publishing 경계에서 Channel Profile·비율·Safe Area·Crop·Overlay·파생·Preview·Registry·회귀 규칙을 특정 도구 비종속 계약으로 분리하고 사용자 승인·잠금 승인 완료 |
