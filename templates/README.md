# 사용자별 로컬 편집 계약

생성한 입력의 다음 단계는 [로컬 작업 패키지 준비](../examples/DRY_RUN.md)입니다. 외부 실행 없이 모델 독립적 메시지 입력과 dry-run 검사 기록을 만듭니다.

`local-editing`은 입력값이 비어 있는 공통 템플릿입니다. [가상 예제](../examples/README.md)는 완성된 학습 입력이며, 사용자 설정은 초기화 도구가 생성한 별도 폴더의 `project.json`과 `request.json`에서 관리합니다. 공통 기준본은 복사하지 않고 ID로 참조합니다.

Python 3.12 이상에서 저장소 루트 기준으로 실행합니다. 한 줄 명령이므로 PowerShell과 일반 셸에서 사용할 수 있습니다.

```text
python scripts/init_project.py local-work/team-notes --project-id team-notes --name "Team Notes" --purpose "Clarify an internal reminder" --audience "New teammates" --language en --source-text "Please send feedback after reviewing."
python scripts/validate_example.py local-work/team-notes/request.json
```

목적·독자·언어·입력문·이름을 자신의 작업에 맞게 지정합니다. `--project-id`는 영문 소문자·숫자·하이픈으로 구성하고 영문자로 시작합니다. 경로에 공백이 있으면 따옴표로 감쌉니다. 대상 폴더가 이미 있으면 덮어쓰지 않고 실패합니다. `local-work/`는 Git에서 제외되며, 다른 경로에 만들 경우 해당 프로젝트에서 별도로 제외 정책을 설정합니다. 입력문을 명령에 넣으면 셸 기록에 남을 수 있으므로 이 시작 예제에는 비민감 문장만 사용합니다.

생성 후 실행할 요청의 목적·독자·언어·입력문은 `request.json`에서 수정하고 다시 검증합니다. 프로젝트 정체성과 공통 기준본 참조는 `project.json`에서 관리합니다. 기준본의 상태와 해시는 이 JCOS 체크아웃의 공개 등록부로 확인하므로 검증할 때 같은 기준본 버전을 유지해야 합니다. 폴더를 저장소 밖으로 옮겨도 검사 명령에 요청 파일의 경로를 지정할 수 있습니다.

확장 지점은 프로젝트의 `baseline_refs`, 요청의 `output_contract`와 별도 프로젝트 규칙입니다. 현재 도구는 SIMPLE 로컬 내부 초안만 지원합니다. `master`는 null, 외부 부작용·새 사실 추가·MASTER 변경은 false로 유지합니다. 게시·계정·예약·HTML/DOCX MASTER 등은 별도의 실행 계약과 검증이 필요한 후속 범위입니다. 템플릿은 승인 MASTER나 운영 승인본이 아니며, 생성된 파일도 입력 계약이지 AI 산출물이 아닙니다.

출력은 명시한 새 로컬 폴더에만 생성합니다. 상대·절대 경로를 지원하지만 `..`, 드라이브 상대 경로, UNC·장치 네임스페이스와 심볼릭 링크·Windows junction을 통과하는 경로는 거부합니다. 외부 폴더를 지정하면 그 폴더에 쓰므로 경로를 확인합니다. 쓰기 오류 시 이번 호출이 생성한 파일과 대상 폴더만 정리하며, 정리 실패는 오류로 알립니다. 새 상위 폴더는 남을 수 있습니다. 다른 프로세스가 실행 중 경로를 변경하는 경쟁 상황까지 방어하는 파일시스템 격리 도구는 아닙니다.

사용자 문자열은 JSON 문자열로 저장하며 Markdown·셸 명령으로 렌더링하거나 실행하지 않습니다. 셸은 도구 실행 전에 인자를 해석하므로 특수 문자가 있는 실제 입력은 생성 후 JSON 편집기로 수정하는 편이 안전합니다.
