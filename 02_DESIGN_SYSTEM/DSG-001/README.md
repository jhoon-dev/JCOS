# JCOS v2.0 - DSG-001

## 문서

- Document ID: `DSG-001`
- Title: `HTML SYSTEM`
- Korean Title: `HTML 구조 원칙`
- Version: `2.0.0`
- Status: `LOCKED`

## 포함 파일

- `DSG-001_HTML_SYSTEM_v2.0.0.md` - 규범적 검토 원본
- `DSG-001_HTML_SYSTEM_v2.0.0.docx` - 사람 검토·편집용 문서
- `DSG-001_HTML_SYSTEM_v2.0.0.pdf` - 고정 레이아웃 검토본
- `QA_REPORT.md` - 범위·내용·형식·렌더링 검수 결과
- `SHA256SUMS.txt` - 자신을 제외한 패키지 파일의 SHA-256

## 문서 범위

이 문서는 JCOS HTML의 의미 구조, 모바일 우선 흐름, Overflow 안전성, 구성요소 구조 계약, 링크·접근성, 의존성 경계와 공통 QA를 정의한다.

참조 프로젝트 전용 콘텐츠·카드 수·색상과 외부 게시 채널 게시 절차를 공통 규칙으로 승격하지 않는다. CSS 토큰, Component 세부 명세, 브랜드, Publishing과 Automation은 후속 전담 문서에 남긴다.

## 기준 근거

- Core 8종 v2.0.0 `LOCKED`
- `PROJECT_REFERENCE_FIXTURE` v1.0.1 `LOCKED`
- `BLOG_SUMMARY_HTML`의 Article Scope, 모바일 단일 열, 긴 문자열·표 Overflow 보호와 외부 의존성 0건 QA
- `INTERNAL-REGRESSION-FIXTURE` HTML Delivery PASS

## 현재 상태

DSG-001 v2.0.0은 사용자 승인과 명시적 잠금 승인을 받은 Phase 3 Design System의 첫 `LOCKED` 기준본이다. 변경 전 REVIEW·APPROVED 패키지는 History에 원형 보존했다. 운영 Runtime 반영은 후속 통합·검증 Gate에서 별도로 결정한다.
