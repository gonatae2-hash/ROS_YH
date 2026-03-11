# 🏷️ URDF 중요 태그 완벽 정리

> 로봇 모델링에 사용되는 URDF 태그 상세 설명
> ROS1 (noetic) / Ubuntu 기준

---

## 📌 전체 태그 구조

```
<robot>
    ├── <link>
    │     ├── <visual>
    │     │     ├── <geometry> (box/cylinder/sphere/mesh)
    │     │     ├── <origin>
    │     │     └── <material>
    │     ├── <collision>
    │     │     ├── <geometry>
    │     │     └── <origin>
    │     └── <inertial>
    │           ├── <mass>
    │           ├── <origin>
    │           └── <inertia>
    ├── <joint>
    │     ├── <parent>
    │     ├── <child>
    │     ├── <origin>
    │     ├── <axis>
    │     ├── <limit>
    │     └── <dynamics>
    └── <gazebo>
```

---

## 1. 🤖 `<robot>` - 최상위 태그

```xml
<?xml version="1.0"?>
<robot name="my_robot">   <!-- 모든 태그를 감싸는 최상위 태그 -->
    ...
</robot>
```

| 속성 | 설명 |
|------|------|
| `name` | 로봇 이름 (필수) |

> ✅ URDF 파일에서 **단 하나만** 존재
> ✅ 모든 link, joint 태그는 반드시 이 안에 있어야 함

---

## 2. 🔗 `<link>` - 로봇 부품 정의

```xml
<link name="base_link">
    <visual/>      <!-- 눈에 보이는 모양 -->
    <collision/>   <!-- 충돌 판정 영역 -->
    <inertial/>    <!-- 질량/관성 -->
</link>
```

| 속성 | 설명 |
|------|------|
| `name` | 링크 이름 (필수, 고유해야 함) |

> ✅ 로봇의 **각 부품**을 나타냄 (몸통, 팔, 바퀴 등)
> ✅ 반드시 **하나의 root link** 가 있어야 함 (보통 base_link)
> ⚠️ root link(base_link)에 inertial 있으면 KDL 경고 발생

---

## 3. 👁️ `<visual>` - 눈에 보이는 모양

```xml
<visual>
    <geometry>
        <cylinder length="0.4" radius="0.04"/>
    </geometry>
    <origin xyz="0 0 0.09" rpy="0 0 0"/>
    <material name="red">
        <color rgba="1 0 0 1"/>
    </material>
</visual>
```

> ✅ **RViz에서 보이는 모양과 색상** 정의
> ✅ 물리 계산에는 전혀 영향 없음
> ✅ 게임으로 치면 **캐릭터 스킨**

---

## 4. 💥 `<collision>` - 충돌 판정 영역

```xml
<collision>
    <geometry>
        <cylinder length="0.42" radius="0.06"/>  <!-- visual보다 살짝 크게 -->
    </geometry>
    <origin xyz="0 0 0.09" rpy="0 0 0"/>
</collision>
```

> ✅ **Gazebo에서 충돌 계산**에 사용
> ✅ 게임으로 치면 **히트박스**
> ✅ visual과 모양이 달라도 됨
> 💡 visual보다 **조금 크게** 설정하는 것이 관례

---

## 5. ⚖️ `<inertial>` - 질량과 관성

```xml
<inertial>
    <mass value="1.0"/>              <!-- 질량 (kg) -->
    <origin xyz="0 0 0"              <!-- 무게중심 위치 -->
            rpy="0 0 0"/>
    <inertia ixx="1.0" ixy="0.0" ixz="0.0"
             iyy="1.0" iyz="0.0" izz="1.0"/>
</inertial>
```

| 태그 | 속성 | 설명 |
|------|------|------|
| `<mass>` | `value` | 질량 (kg) |
| `<origin>` | `xyz`, `rpy` | 무게중심 위치/회전 |
| `<inertia>` | `ixx~izz` | 관성 텐서 6개 값 |

### 관성 텐서 이해하기
```
ixx = X축 회전에 대한 저항
iyy = Y축 회전에 대한 저항
izz = Z축 회전에 대한 저항
ixy, ixz, iyz = 축간 교차 관성 (보통 0)
```

> ✅ **Gazebo 물리 시뮬레이션**에서만 사용
> ✅ RViz에서는 영향 없음
> ⚠️ Gazebo 사용 시 반드시 있어야 함
> ⚠️ `<inertia>` 태그 없으면 에러 발생

---

## 6. 📦 `<geometry>` - 모양 정의

```xml
<!-- 박스 (직육면체) -->
<geometry>
    <box size="0.1 0.2 0.3"/>
    <!--       ↑   ↑   ↑
              X   Y   Z (미터) -->
</geometry>

<!-- 원기둥 -->
<geometry>
    <cylinder length="0.4" radius="0.04"/>
    <!--        ↑              ↑
               높이           반지름 (미터) -->
</geometry>

<!-- 구 -->
<geometry>
    <sphere radius="0.05"/>
    <!--      ↑
             반지름 (미터) -->
</geometry>

<!-- 3D 메시 파일 -->
<geometry>
    <mesh filename="package://my_pkg/meshes/robot.stl"
          scale="1 1 1"/>   <!-- 크기 배율 -->
</geometry>
```

| 모양 | 태그 | 속성 |
|------|------|------|
| 직육면체 | `<box>` | `size="x y z"` |
| 원기둥 | `<cylinder>` | `length`, `radius` |
| 구 | `<sphere>` | `radius` |
| 3D 파일 | `<mesh>` | `filename`, `scale` |

---

## 7. 📍 `<origin>` - 위치와 회전

```xml
<origin xyz="0.1 0.2 0.3"   <!-- X Y Z 위치 (미터) -->
        rpy="0 1.57 0"/>     <!-- Roll Pitch Yaw 회전 (라디안) -->
```

### xyz - 위치
```
xyz="0.1  0.2  0.3"
      ↑    ↑    ↑
      X    Y    Z
    앞뒤  좌우  상하  (미터 단위)
```

### rpy - 회전
```
rpy="0    1.57   0"
      ↑     ↑    ↑
    Roll  Pitch  Yaw  (라디안 단위)

예: rpy="0 1.57 0" → Y축으로 90도 회전 → 원기둥 눕히기
```

### 라디안 변환표
| 라디안 | 도 |
|--------|-----|
| 0 | 0° |
| 0.785 | 45° |
| 1.571 | 90° |
| 3.141 | 180° |
| 6.283 | 360° |

---

## 8. 🎨 `<material>` - 색상 정의

```xml
<!-- link 안에서 직접 정의 -->
<material name="red">
    <color rgba="1 0 0 1"/>
</material>

<!-- 전역으로 먼저 정의 후 재사용 -->
<material name="blue">
    <color rgba="0 0 1 1"/>
</material>
...
<material name="blue"/>   <!-- 이름만 써서 재사용 -->
```

### rgba 색상 치트시트
```
rgba = "R    G    B    투명도"
        ↑    ↑    ↑      ↑
      빨강 초록 파랑   1=불투명
                       0=투명

빨간색:  rgba="1 0 0 1"
초록색:  rgba="0 1 0 1"
파란색:  rgba="0 0 1 1"
노란색:  rgba="1 1 0 1"
흰색:    rgba="1 1 1 1"
검정:    rgba="0 0 0 1"
회색:    rgba="0.5 0.5 0.5 1"
주황색:  rgba="1 0.5 0 1"
```

---

## 9. 🔄 `<joint>` - 링크 연결 및 움직임

```xml
<joint name="pan_joint" type="revolute">
    <parent link="base_link"/>    <!-- 부모 링크 -->
    <child link="pan_link"/>      <!-- 자식 링크 -->
    <origin xyz="0 0 0.1"         <!-- 부모 기준 위치 -->
            rpy="0 0 0"/>
    <axis xyz="0 0 1"/>           <!-- 회전/이동 축 -->
    <limit lower="-3.14"          <!-- 최소값 (rad 또는 m) -->
           upper="3.14"           <!-- 최대값 -->
           effort="300"           <!-- 최대 힘 (N) -->
           velocity="0.1"/>       <!-- 최대 속도 (rad/s) -->
    <dynamics damping="50"        <!-- 감쇠 계수 -->
              friction="1"/>      <!-- 마찰 계수 -->
</joint>
```

### 조인트 타입 6가지

| 타입 | 움직임 | limit 필요 | 사용 예 |
|------|--------|-----------|---------|
| `revolute` | 제한 회전 | ✅ | 로봇 팔, pan/tilt |
| `continuous` | 무한 회전 | ❌ | 바퀴, 프로펠러 |
| `prismatic` | 직선 이동 | ✅ | 그리퍼, 리프트 |
| `fixed` | 고정 | ❌ | 카메라 고정 |
| `floating` | 6자유도 | ❌ | 드론 |
| `planar` | 평면 이동 | ❌ | 평면 로봇 |

---

## 10. 🔩 `<axis>` - 회전/이동 축

```xml
<axis xyz="0 0 1"/>   <!-- Z축 기준 회전 (좌우) -->
<axis xyz="0 1 0"/>   <!-- Y축 기준 회전 (상하) -->
<axis xyz="1 0 0"/>   <!-- X축 기준 회전 (앞뒤) -->
```

```
xyz="1 0 0" → X축  (앞뒤 방향)
xyz="0 1 0" → Y축  (좌우 방향)
xyz="0 0 1" → Z축  (상하 방향)
```

---

## 11. 🚧 `<limit>` - 관절 제한값

```xml
<limit lower="-3.14"    <!-- 최소 각도/거리 (rad 또는 m) -->
       upper="3.14"     <!-- 최대 각도/거리 -->
       effort="300"     <!-- 최대 힘/토크 (N 또는 Nm) -->
       velocity="0.1"/> <!-- 최대 속도 (rad/s 또는 m/s) -->
```

> ✅ `revolute`, `prismatic` 타입에서 **필수**
> ✅ `continuous` 타입은 lower/upper 불필요

---

## 12. 🌊 `<dynamics>` - 물리 특성

```xml
<dynamics damping="50"    <!-- 감쇠: 움직임을 서서히 멈추게 하는 힘 -->
          friction="1"/>  <!-- 마찰: 정지 상태 유지하는 힘 -->
```

| 속성 | 설명 | 높을수록 |
|------|------|---------|
| `damping` | 감쇠 계수 | 빨리 멈춤 |
| `friction` | 마찰 계수 | 움직이기 어려움 |

> ✅ Gazebo 물리 시뮬레이션에서 사용
> ✅ 없어도 되지만 있으면 더 현실적인 동작

---

## 13. 🌍 `<gazebo>` - Gazebo 전용 설정

```xml
<!-- 링크 색상 설정 -->
<gazebo reference="base_link">
    <material>Gazebo/Blue</material>
</gazebo>

<!-- 물리 특성 설정 -->
<gazebo reference="base_link">
    <mu1>0.2</mu1>        <!-- 마찰계수1 -->
    <mu2>0.2</mu2>        <!-- 마찰계수2 -->
    <kp>1000000.0</kp>    <!-- 강성 -->
    <kd>1.0</kd>          <!-- 감쇠 -->
</gazebo>

<!-- 레이저 센서 추가 -->
<gazebo reference="laser_link">
    <sensor type="ray" name="laser">
        <plugin name="laser_plugin"
                filename="libgazebo_ros_laser.so">
            <topicName>/scan</topicName>
            <frameName>laser_link</frameName>
        </plugin>
    </sensor>
</gazebo>
```

### Gazebo 색상 종류
```
Gazebo/Red      Gazebo/Green    Gazebo/Blue
Gazebo/Yellow   Gazebo/White    Gazebo/Black
Gazebo/Grey     Gazebo/Orange   Gazebo/Purple
```

> ✅ `reference` 안의 이름이 link name과 **정확히 일치**해야 함
> ✅ RViz의 material과 **별개**로 설정해야 함

---

## ⭐ 핵심 요약

| 태그 | 역할 | 필수 여부 |
|------|------|----------|
| `<robot>` | 최상위 태그 | ✅ 필수 |
| `<link>` | 부품 정의 | ✅ 필수 |
| `<joint>` | 연결 정의 | ✅ 필수 |
| `<visual>` | 모양/색상 | ✅ 권장 |
| `<collision>` | 충돌 영역 | Gazebo 사용 시 필수 |
| `<inertial>` | 질량/관성 | Gazebo 사용 시 필수 |
| `<geometry>` | 실제 모양 | ✅ 필수 |
| `<origin>` | 위치/회전 | 선택 (없으면 원점) |
| `<material>` | 색상 | 선택 |
| `<axis>` | 회전/이동 축 | revolute/prismatic 필수 |
| `<limit>` | 관절 제한 | revolute/prismatic 필수 |
| `<dynamics>` | 물리 특성 | 선택 |
| `<gazebo>` | Gazebo 전용 | Gazebo 사용 시 |

---

*정리일: 2026-03-09 | ROS1 (noetic) / Ubuntu 기준*
