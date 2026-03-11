# 🤖 ROS 로봇 모델링 패키지 정리

## 1. ✍️ 모델 작성 패키지

| 패키지 | 역할 |
|--------|------|
| `urdf` | 로봇 모델 파일 형식 (XML) |
| `xacro` | URDF를 편하게 작성하는 매크로 도구 |

## 2. ⚙️ 모델 처리 패키지

| 패키지 | 역할 |
|--------|------|
| `robot_state_publisher` | 관절값 + URDF → TF 계산 발행 |
| `joint_state_publisher` | 관절값 자동 발행 (테스트용) |
| `joint_state_publisher_gui` | 슬라이더 GUI로 관절 조작 |
| `kdl_parser` | URDF → KDL 트리 변환 |

## 3. 👁️ 시각화 패키지

| 패키지 | 역할 |
|--------|------|
| `rviz` | 3D 시각화 |
| `gazebo_ros` | 물리 시뮬레이션 |

## 4. 🔍 검증 도구

| 도구 | 역할 |
|------|------|
| `check_urdf` | URDF 문법 검증 |
| `urdf_to_graphiz` | URDF 구조 그래프로 시각화 |
| `liburdfdom-tools` | check_urdf 포함 패키지 |

## 전체 흐름

xacro로 모델 작성 → check_urdf 검증 → joint_state_publisher → robot_state_publisher → RViz/Gazebo