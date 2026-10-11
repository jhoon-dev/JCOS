# JCOS Public Roadmap

| 항목 | 값 |
|---|---|
| Document ID | FND-005 |
| Version | 2.1.0 |
| Status | REVIEW |
| Owner | JCOS Maintainers |

## 기존 공통 문서 작성 범위

- Foundation 구조와 문서 식별 체계
- Core 운영·작성·조사·출처·품질·전달·버전·의사결정 원칙
- HTML·DOCX·CSS·구성요소·이미지·썸네일·브랜드 Design System
- 조사·작성·편집·사실 검증·검색·게시·수명주기 Content System
- 자동화 아키텍처·일정·프롬프트·복구·QA·Runbook
- Core Runtime Compact와 원문 Source Map

## 공개판 유지보수

1. 공통 문서의 상호 참조와 책임 경계를 검수합니다.
2. Markdown 기준본의 공개 범위와 민감정보 부재를 지속적으로 확인합니다.
3. 변경 시 문서 ID, 버전, 영향 범위와 검증 근거를 기록합니다.
4. 공개가 검증된 경우에만 DOCX·PDF를 별도 릴리스 자산으로 제공합니다.

## 공개 범위 밖

개별 프로젝트의 로드맵, 프로젝트 전용 MASTER·Runtime·QA·실행 결과와 내부 History는 이 공개 로드맵에서 관리하지 않습니다.

## 2026-10-02 공개판 정비

- 공개 파일 안내와 현재 상태 설명 정리
- Foundation ID·경로 연결과 SHA-256 등록부
- Quickstart, 문서 선택표와 가상 로컬 편집 예제
- 문서·Runtime·예제 입력 정적 검사와 실패 사례 테스트
- AUT-003 우선순위 명확화 REVIEW 후보
- FND-006 작업별 적용 수준 REVIEW 검토안

정적 검사 통과는 운영 검증 또는 승인 완료를 의미하지 않습니다.

## 다음 업데이트와 완료 기준

1. Foundation·Runtime 통합 검토: 실제 승인 근거와 상태를 연결하고 사용할 기준본 조합을 확정합니다.
2. 적용 수준 채택: CNT-002·AUT-003 영향과 버전 증가를 판단하고 후보·QA·승인·마이그레이션을 제공합니다.
3. Runtime 선택 구성: 승인 문서의 적용 범위에 따라 필요한 Compact만 선택하고 원문·해시·추출 위치를 검증합니다.
4. 운영 회귀 사례: 사용자 요청 충돌, 오래된 출처, 빈 입력, 게시 UNKNOWN·PARTIAL을 재현 가능한 테스트로 검증합니다.
5. 실제 채널 검증: 대표 Project Fixture에서 렌더링·게시·복구 결과를 확인한 뒤 통합 후보를 운영 기준으로 전환합니다.
