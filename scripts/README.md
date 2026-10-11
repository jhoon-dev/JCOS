# 공개 패키지 검사

Python 3.12 이상, 표준 라이브러리만 사용합니다.

`prepare_work.py`는 검증된 요청을 [로컬 작업 패키지와 dry-run 기록](../examples/DRY_RUN.md)으로 준비합니다. 사용자 입력과 고정 정책을 분리하고 기준본 참조를 기록합니다. `local_files.py`는 두 생성 명령의 새 폴더 쓰기와 실패 정리를 공유합니다.

```text
python scripts/validate_docs.py
python scripts/validate_example.py examples/request.json
python -m unittest discover -s tests -v
```

`validate_docs.py`는 등록 문서 존재, 메타데이터·버전·상태·해시, 의존 ID, 활성 기준본별 규칙 ID 고유성, 로컬 Markdown 링크, Core Runtime의 원문·순서를 검사합니다. 같은 규칙 ID가 과거 기준본과 검토 후보에 존재하는 것은 버전 이력이며 활성 기준본 중복으로 보지 않습니다.

`validate_example.py`는 범용 로컬 편집 예제의 필수 입력·프로젝트 범위·부작용 금지·기준본 해시를 검사합니다. 실제 AI 실행·게시·예약을 수행하지 않습니다.

`init_project.py`는 [공통 템플릿](../templates/README.md)에 사용자 설정을 넣고 기존 검사기로 검증한 뒤 새 폴더에 프로젝트·요청 JSON을 생성합니다. 기존 폴더를 덮어쓰지 않습니다. 게시·예약·AI 호출 없이 로컬 입력 계약만 준비합니다. 쓰기 실패 시 이번 호출이 생성한 파일과 대상 폴더를 정리합니다. 정리 자체가 실패하면 경로를 오류로 알립니다. 새로 만든 상위 폴더는 남을 수 있습니다.

외부 URL 접근성, Markdown 앵커, 내용의 사실성, 규칙 사이 의미 충돌, 승인 근거, 기밀정보 전수 탐지와 실제 프로젝트 QA는 검사 범위 밖입니다. SHA-256은 바이트 무결성을 확인하며 승인 증거를 대신하지 않습니다.

문서를 변경하면 [등록부](../00_FOUNDATION/DOCUMENT_REGISTER.md)의 정책에 따라 새 버전·상태를 확인하고 해당 등록 항목을 갱신합니다. 검사 실패를 없애기 위해 승인본 해시만 무조건 갱신하지 않습니다. Core 변경은 Runtime 재생성·Manifest·검증을 함께 수행합니다.

`.gitattributes`는 체크아웃 줄바꿈을 고정합니다. 기존 Content·Automation v2.0.0은 현재 바이트를 유지하는 CRLF, 나머지 문서는 LF를 사용합니다. Git을 거치지 않은 도구가 줄바꿈을 바꾸면 해시 검사가 실패하므로 편집기의 줄바꿈 설정도 확인합니다.
