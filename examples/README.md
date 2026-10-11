# 가상 로컬 편집 예제

이 폴더는 공개 학습용 자료입니다. 실제 고객·프로젝트·실행 결과나 비공개 MASTER를 포함하지 않습니다. 등록부의 프로젝트 전용 자산 제외 정책과 별개로 허용된 범용 예제입니다.

| 파일 | 역할 |
|---|---|
| [project.json](project.json) | 가상 프로젝트의 목적·범위·기준본 참조 |
| [request.json](request.json) | 로컬 문장 수정 요청과 최소 결과 계약 |
| [EXPECTED_RESULTS.md](EXPECTED_RESULTS.md) | 정상 결과, 실패, 부분 성공, 미확인 처리 |

프로젝트 이름은 `Example Local Editing`이며 게시 채널·계정·일정·외부 도구를 사용하지 않습니다. 프로필 값 SIMPLE은 검토안의 분류 예시입니다. 전체 CNT 또는 AUT 준수를 주장하지 않습니다.

```text
python scripts/validate_example.py examples/request.json
```

검사는 입력·원문 참조·부작용 제한과 기준본 해시를 확인합니다. 수정문을 생성하거나 사용자 대신 게시하지 않습니다. 요청값을 실제 운영에 복사하기 전 목적·출처·권한·필수 계약을 구체화해야 합니다.
