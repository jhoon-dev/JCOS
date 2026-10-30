# Contributing to JCOS

JCOS의 공통 원칙을 더 명확하고 재사용 가능하게 만드는 제안을 환영합니다.

## 제안 원칙

- 특정 프로젝트의 이름, 운영 데이터, 고객 정보 또는 비공개 자산을 포함하지 않습니다.
- 기존 규칙의 책임 범위와 충돌 여부를 먼저 확인합니다.
- 규칙 변경에는 변경 이유, 영향 범위와 검증 방법을 함께 적습니다.
- 큰 변경은 구현 전에 Issue에서 목적과 범위를 먼저 논의합니다.

## Pull Request

1. 변경 범위를 하나의 주제로 제한합니다.
2. 관련 문서 ID와 버전을 명시합니다.
3. 링크, 문서 경로와 상호 참조가 유효한지 확인합니다.
4. 개인정보, API 키, 토큰, 로컬 경로와 임시 파일이 없는지 확인합니다.

## 공개 패키지 검사와 버전

Python 3.12 이상에서 다음을 실행하고 결과를 PR에 적습니다.

```text
python scripts/validate_docs.py
python scripts/validate_example.py examples/request.json
python -m unittest discover -s tests -v
```

LOCKED 파일을 덮어쓰지 않고 변경 성격에 맞는 새 버전과 상태를 사용합니다. [등록부](00_FOUNDATION/DOCUMENT_REGISTER.md)의 경로·메타데이터·해시·의존성을 함께 갱신합니다. 후보는 자동 활성화하지 않습니다. Core 변경 시 Runtime Source Map, 원문 추출 블록과 Runtime 해시도 함께 검토합니다.

정적 검사 PASS를 승인 또는 실제 프로젝트 QA로 표시하지 않습니다. 공개 학습 예제는 가상 데이터만 사용하고 실제 프로젝트·계정·실행 결과를 넣지 않습니다.

개별 프로젝트 모듈과 프로젝트 전용 산출물은 이 공개 저장소의 기여 범위에 포함하지 않습니다.
