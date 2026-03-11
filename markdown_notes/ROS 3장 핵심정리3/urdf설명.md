# 📄 URDF 완벽 정리

> Unified Robot Description Format
> 로봇의 생김새, 관절, 물리 특성을 XML로 표현하는 파일

---

## 1. 기본 구조

```xml
<?xml version="1.0"?>
<robot name="my_robot">    <!-- 로봇 이름 -->

    <link name="..."/>     <!-- 부품 정의 -->
    <joint name="..."/>    <!-- 연결 정의 -->

</robot>
```

> ✅ 모든 URDF는 `<robot>` 태그로 시작
> ✅ **link** 와 **joint** 의 조합으로 로봇을 표현

---

## 2. Link (링크) - 로봇의 부품

> 로봇을 이루는 각각의 부품 (팔, 다리, 몸통 등)

```xml
<link name="base_link">

    <!-- 👁️ 눈에 보이는 모양 (RViz) -->
    <visual>
        <geometry>
            <cylinder length="0.1" radius="0.2"/>
        </geometry>
        <origin xyz="0 0 0" rpy="0 0 0"/>
        <material name="yellow">
            <color rgba="1 1 0 1"/>
        </material>
    </visual>

    <!-- 💥 충돌 판정 영역 (Gazebo) -->
    <collision>
        <geometry>
            <cylinder length="0.12" radius="0.2"/>  <!-- 살짝 크게 -->
        </geometry>
        <origin xyz="0 0 0" rpy="0 0 0"/>
    </collision>

    <!-- ⚖️ 질량/관성 (Gazebo 물리 계산) -->
    <inertial>
        <mass value="1.0"/>
        <inertia ixx="1.0" ixy="0.0" ixz="0.0"
                 iyy="1.0" iyz="0.0" izz="1.0"/>
    </inertial>

</link>
```

### visual / collision / inertial 비교

| 태그 | 역할 | 사용처 |
|------|------|--------|
| `visual` | 눈에 보이는 모양/색상 | RViz |
| `collision` | 충돌 판정 히트박스 | Gazebo |
| `inertial` | 질량/관성 물리 계산 | Gazebo |

---

## 3. geometry - 모양 종류

```xml
<!-- 박스 -->
<box size="0.1 0.2 0.3"/>              <!-- 가로 세로 높이 (m) -->

<!-- 원기둥 -->
<cylinder length="0.4" radius="0.04"/> <!-- 길이 반지름 (m) -->

<!-- 구 -->
<sphere radius="0.05"/>                <!-- 반지름 (m) -->

<!-- 3D 메시 파일 -->
<mesh filename="package://my_pkg/meshes/robot.stl"/>
```

---

## 4. Joint (조인트) - 링크 사이 연결

> 링크와 링크를 어떻게 연결하고 움직이는지 정의

```xml
<joint name="pan_joint" type="revolute">
    <parent link="base_link"/>       <!-- 부모 링크 -->
    <child link="pan_link"/>         <!-- 자식 링크 -->
    <origin xyz="0 0 0.1"            <!-- 부모 기준 위치 (m) -->
            rpy="0 0 0"/>            <!-- 부모 기준 회전 (rad) -->
    <axis xyz="0 0 1"/>              <!-- 회전 축 -->
    <limit lower="-3.14"             <!-- 최소 각도 (rad) -->
           upper="3.14"              <!-- 최대 각도 (rad) -->
           effort="300"              <!-- 최대 힘 (N) -->
           velocity="0.1"/>          <!-- 최대 속도 (rad/s) -->
    <dynamics damping="50"           <!-- 감쇠 -->
              friction="1"/>         <!-- 마찰 -->
</joint>
```

### 조인트 타입 6가지

| 타입 | 움직임 | 제한 | 사용 예 |
|------|--------|------|---------|
| `revolute` | 회전 | 있음 | 로봇 팔, pan/tilt |
| `continuous` | 무한 회전 | 없음 | 바퀴, 프로펠러 |
| `prismatic` | 직선 이동 | 있음 | 그리퍼, 리프트 |
| `fixed` | 고정 | 없음 | 카메라 고정 |
| `floating` | 6자유도 | 없음 | 드론 |
| `planar` | 평면 이동 | 없음 | 평면 로봇 |

---

## 5. origin - 위치와 회전

```xml
<origin xyz="0.1 0.2 0.3"    <!-- X Y Z 위치 (미터) -->
        rpy="0 1.57 0"/>      <!-- Roll Pitch Yaw 회전 (라디안) -->
```

### xyz 이해하기
```
xyz="0.1  0.2  0.3"
      ↑    ↑    ↑
      X    Y    Z
    앞뒤  좌우  상하
```

### rpy 이해하기
```
rpy="0   1.57   0"
      ↑    ↑    ↑
    Roll Pitch  Yaw
    좌우  상하  회전

1.57 rad = 90도
3.14 rad = 180도
```

---

## 6. material - 색상

```xml
<material name="red">
    <color rgba="1 0 0 1"/>   <!-- R G B 투명도 -->
</material>
```

### 색상 치트시트
```
빨간색:  rgba="1 0 0 1"
초록색:  rgba="0 1 0 1"
파란색:  rgba="0 0 1 1"
노란색:  rgba="1 1 0 1"
흰색:    rgba="1 1 1 1"
검정:    rgba="0 0 0 1"
회색:    rgba="0.5 0.5 0.5 1"
```

---

## 7. 로봇 구조 예시 (pan_tilt)

```
base_link (노란 원판)
    │
    │ pan_joint (Z축 회전 - 좌우)
    │
pan_link (파란 원기둥 - 수직)
    │
    │ tilt_joint (Y축 회전 - 상하)
    │
tilt_link (빨간 원기둥 - 수평)
```

---

## 8. URDF 작성 후 확인 명령어

```bash
# 문법 검증
check_urdf robot.urdf

# 구조 그래프로 보기
urdf_to_graphiz robot.urdf
evince robot.pdf
```

---

## 9. URDF vs xacro

| 항목 | URDF | xacro |
|------|------|-------|
| 변수 사용 | ❌ | ✅ |
| 수식 사용 | ❌ | ✅ |
| 매크로(함수) | ❌ | ✅ |
| 파일 include | ❌ | ✅ |
| 가독성 | 낮음 | 높음 |

> 💡 실무에서는 거의 xacro로 작성하고
> catkin_make 로 URDF로 자동 변환해서 사용해요!

---

## 10. 자주 나오는 에러

| 에러 | 원인 | 해결 |
|------|------|------|
| `material undefined` | material 미정의 | URDF 상단에 정의 추가 |
| `Geometry tag contains no child` | geometry 비어있음 | box/cylinder/sphere 추가 |
| `root link has inertia` | base_link에 inertial | dummy_link 추가 |
| `Inertial must have inertia` | inertia 태그 누락 | `<inertia>` 추가 |

---

## 11. dummy_link 추가 (KDL 경고 해결)

```xml
<!-- base_link 위에 추가 -->
<link name="dummy_link"/>

<joint name="dummy_joint" type="fixed">
    <parent link="dummy_link"/>
    <child link="base_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
</joint>
```

---

*정리일: 2026-03-09 | ROS1 (noetic) / Ubuntu 기준*
