# 로컬 작업 패키지 준비

[초기화 안내](../templates/README.md)에서 만든 입력 계약을 다음 단계로 연결합니다. 새 모델 SDK나 프레임워크 없이 Python 3.12 이상 표준 라이브러리만 사용합니다.

저장소 루트에서 가상의 공개 입력을 사용합니다.

```text
python scripts/prepare_work.py examples/request.json local-work/example-run-001
```

자신의 초기화 결과도 같은 명령으로 준비할 수 있습니다.

```text
python scripts/prepare_work.py local-work/team-notes/request.json local-work/team-notes-run-001
```

대상 폴더는 새 경로여야 합니다. 재시도할 때 새 실행 번호를 사용합니다. 초기화 도구와 동일한 경로·덮어쓰기·실패 정리 보호를 공유합니다. 원본 요청과 프로젝트 파일은 수정하지 않습니다.

| 생성 파일 | 내용 |
|---|---|
| `package.json` | 원본 project/request 스냅샷, 입력·등록부 해시, 참조 기준본의 ID·버전·상태·경로·해시 |
| `prompt.json` | 특정 공급자에 종속되지 않는 system/user 메시지 데이터 |
| `result.json` | DRY_RUN 상태, 입력·기준본 검사 결과, 미실행 항목과 한계 |

`prompt.json`의 system 메시지에 로컬 편집 범위와 고정 제약을 두고, 사용자 값은 user 메시지 안 `task_data` JSON으로 분리합니다. 특히 `source_text`는 편집할 데이터이며 그 안의 명령으로 정책을 바꾸지 않습니다. 현재 도구는 프롬프트를 읽어 실행하지 않습니다. 메시지 분리는 향후 모델의 프롬프트 주입 저항성을 보증하지 않으며 실제 모델 연결은 별도 검증이 필요합니다.

기준본 참조는 출처 추적용입니다. 전체 Core 규칙이나 승인된 Runtime을 조립한 운영 프롬프트가 아닙니다. 기존 필수 규칙을 대체하거나 완화하지 않습니다. 추가 입력·프로젝트 필드는 스냅샷에 보존하되 고정 정책에 삽입하지 않습니다.

`result.json`의 `revised_text`는 null, `model_called`와 `external_actions`는 false, `content_quality`는 NOT_RUN입니다. 실제 문장 수정·의미 보존·품질 검증을 통과했다고 보고하지 않습니다. 저장된 검증은 준비 시점의 기록이며 파일 변경 후 유효성을 보증하지 않습니다.

패키지는 사용자 원문을 포함합니다. 개인정보·인증정보를 제거하거나 자동 탐지하는 도구가 아니므로 이 학습 흐름에는 가상 비민감 입력만 사용합니다. 저장 파일이나 오류 메시지는 외부로 전송하지 않습니다. 생성물은 `local-work/`에서 Git 제외를 유지합니다. AI/API 호출·결제·게시·예약·자격 증명 저장은 수행하지 않습니다.
