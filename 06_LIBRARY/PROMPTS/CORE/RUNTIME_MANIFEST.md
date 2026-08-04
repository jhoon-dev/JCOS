# JCOS Core Runtime Manifest v2.0.0

## Runtime

| Field | Value |
|---|---|
| Runtime File | `JCOS_CORE_COMPACT_v2.0.0.md` |
| Runtime Status | `REVIEW` |
| Runtime Type | `DERIVED` |
| Generated | `2026-07-30` |
| Source Scope | `COR-001~COR-008 v2.0.0 LOCKED` |
| Runtime SHA-256 | `fd914eba05844005f270de3919a302d9d47c194ea68f4650e856e2d6b7e22166` |
| Authority | 상세 LOCKED Core가 우선하며 Runtime은 비규범적 실행 표현 |

## Source Map

| Document | Source File | Source Section | Source SHA-256 |
|---|---|---|---|
| COR-001 | `01_CORE/COR-001/COR-001_CORE_INSTRUCTIONS_v2.0.0.md` | `20.1 AI용 압축 Core Instructions` | `95b29dd5fb9f849577102a81c4982982672d6b2dfcfee00728172b10ae1e3741` |
| COR-002 | `01_CORE/COR-002/COR-002_WRITING_PRINCIPLES_v2.0.0.md` | `17.1 AI용 압축 Writing Instructions` | `cb09edd9d3c19e589dfa12af696559993474ac09a2798a96cf6e7d4fcc82d35d` |
| COR-003 | `01_CORE/COR-003/COR-003_RESEARCH_PRINCIPLES_v2.0.0.md` | `17.1 AI용 압축 Research Instructions` | `da0be5d2b34ce45dbc2d652ec45c238a08390dc6cd8baf0c73947fbea79e9b7c` |
| COR-004 | `01_CORE/COR-004/COR-004_SOURCE_POLICY_v2.0.0.md` | `17.1 AI용 압축 Source Instructions` | `d158a145cb7aef318149aa0e978a9af5d217ee1ece2dac405377ca553fbcdd1b` |
| COR-005 | `01_CORE/COR-005/COR-005_QUALITY_GATE_v2.0.0.md` | `17.1 AI용 압축 Quality Gate Instructions` | `8c19c131a3c389b74b6ae15b0b4fa4ef94d5364ab7e2c74302778dd37e0b164e` |
| COR-006 | `01_CORE/COR-006/COR-006_FILE_DELIVERY_v2.0.0.md` | `17.1 AI용 압축 File Delivery Instructions` | `2117a9e60d6ccfc4126abe97f6ca44ed53d2de1f3da610b9524687c545ceaf77` |
| COR-007 | `01_CORE/COR-007/COR-007_VERSION_POLICY_v2.0.0.md` | `17.1 AI용 압축 Version Instructions` | `dea229f05d80aa7e9a972d416903be143f6622ee8089bb64b96bbd97bee98b65` |
| COR-008 | `01_CORE/COR-008/COR-008_DECISION_RULES_v2.0.0.md` | `17.1 AI용 압축 Decision Instructions` | `7c8dc81eb0f8d0711435aa86877e6047109742d1caaea6af7f9b0d3cb41fc5b1` |

## Build Contract

1. Source Map의 정확한 섹션에서 압축 블록을 추출한다.
2. COR-001부터 COR-008 순서로 배치한다.
3. 원문 블록의 문장, 번호와 순서를 변경하지 않는다.
4. Runtime 메타데이터와 사용 원칙은 파생본의 권한·범위만 설명하며 새 규칙을 추가하지 않는다.
5. 원본 해시가 달라지면 Runtime을 사용 중지하고 영향 분석, 재생성과 QA를 수행한다.
6. Project Runtime은 승인된 Project Module이 준비된 뒤 별도 Manifest로 생성한다.
