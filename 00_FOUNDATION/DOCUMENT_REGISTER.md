# JCOS Public Document Register

## 공개 문서군

| Prefix | 영역 | 공개 상태 |
|---|---|---|
| COR | Core 공통 원칙 | 포함 |
| DSG | Design System | 포함 |
| CNT | Content System | 포함 |
| AUT | Automation System | 포함 |
| PRJ | 개별 Project Module | 제외 |

## 현재 공개 패키지

- `COR-001`~`COR-008`
- `DSG-001`~`DSG-007`
- `CNT-001`~`CNT-007`
- `AUT-001`~`AUT-006`
- `06_LIBRARY/PROMPTS/CORE/JCOS_CORE_COMPACT_v2.0.0.md`
- `06_LIBRARY/PROMPTS/CORE/RUNTIME_MANIFEST.md`

## 등록 원칙

1. 문서 ID는 하나의 책임 영역에만 연결합니다.
2. 같은 ID와 Version의 승인 문서를 조용히 덮어쓰지 않습니다.
3. 파생 Runtime은 원문 문서, 섹션, Version과 해시를 Manifest에 기록합니다.
4. 공개 등록부에는 개별 프로젝트명, 전용 경로, 실행 결과와 내부 승인 기록을 넣지 않습니다.
5. 공개판에서 제외된 문서를 참조해야 하는 경우 구체적인 이름 대신 `Project Module` 또는 `Project Fixture` 역할만 표시합니다.
