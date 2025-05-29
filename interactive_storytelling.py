import random

# 게임 상태 초기화
state = {
    "fuel": 100,
    "items": [],
    "visited_planets": [],
    "ai_name": input("🤖 동행할 AI의 이름을 정해주세요: "),
    "spaceship": {"name": "스타십", "fuel": 80, "speed": 5},
    "score": 0,
    "level": 1,
    "lives": 3,
    "base_fuel": 100,
    "mission_success": False,
    "blackhole_attempts": 0,
    "blackhole_traps": 0,
    "turn_count": 0,
    "current_location": "earth"
}

planet_list = ['mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'mercury', 'venus']
obstacles = random.sample(planet_list, k=2)

planet_effects = {
    'mars': {'success_bonus': 10, 'item': "방진복"},
    'jupiter': {'failure_penalty': 30, 'description': "폭풍으로 실패 시 연료 손실 증가"},
    'saturn': {'success_bonus': 20, 'item': "얼음 코어"},
    'uranus': {'fuel_boost_on_success': 30, 'description': "자기장 에너지 수집으로 연료 추가 보상"},
    'neptune': {'score_multiplier': 2, 'description': "깊은 바다 미션으로 점수 두 배"},
    'mercury': {'item': "열 차단막", 'failure_penalty': 20},
    'venus': {'item': "방사능 해독제", 'score_bonus': 5}
}

planet_distances = {
    ('earth', 'mars'): 2,
    ('earth', 'jupiter'): 5,
    ('earth', 'saturn'): 6,
    ('earth', 'uranus'): 8,
    ('earth', 'neptune'): 10,
    ('earth', 'mercury'): 3,
    ('earth', 'venus'): 1
}

travel_random_items = [
    {"name": "속도 업그레이드", "effect": lambda: increase_speed()},
    {"name": "연료 급속 충전기", "effect": lambda: quick_refuel()},
    {"name": "라이프 캡슐", "effect": lambda: gain_life()}
]

planet_missions = {
    'earth': "지구는 탐사의 출발지이자 도착지입니다.",
    'mars': "화성의 붉은 먼지를 채집하세요.",
    'jupiter': "목성의 폭풍을 피하며 대기 샘플을 수집하세요.",
    'saturn': "토성 고리에서 얼음 조각을 수거하세요.",
    'uranus': "천왕성의 극한 자기장을 분석하세요.",
    'neptune': "해왕성의 깊은 바다 데이터를 수집하세요.",
    'mercury': "수성의 열기를 견디며 암석 샘플을 확보하세요.",
    'venus': "금성의 두꺼운 대기 속에서 구조를 탐사하세요."
}

def increase_speed():
    state['spaceship']['speed'] = min(5, state['spaceship']['speed'] + 1)
    print("🚀 속도 업그레이드 획득! 현재 속도:", state['spaceship']['speed'])

def quick_refuel():
    bonus = random.randint(20, 40)
    state['fuel'] += bonus
    print(f"⚡ 연료 급속 충전기 사용! 연료 +{bonus}, 현재 연료: {state['fuel']}")

def gain_life():
    if random.random() < 0.25:
        state['lives'] += 1
        print("❤️ 라이프 캡슐 획득! 현재 라이프:", state['lives'])

def calculate_fuel_cost(from_planet, to_planet, speed):
    return max(1, planet_distances.get((from_planet, to_planet), 4) * (6 - speed))

def space_station():
    print("\n🛰️ 우주정거장에 도착했습니다. 연료를 보급합니다!")
    state['fuel'] = state['base_fuel']
    print(f"⛽ 연료가 {state['fuel']}으로 충전되었습니다.")

def blackhole_escape():
    print("\n🌀 블랙홀에 빨려들어갔습니다! 탈출하려면 주사위 두 개가 같은 눈을 보여야 합니다.")
    for _ in range(3):
        input("▶ 주사위를 던지려면 Enter를 누르세요.")
        die1, die2 = random.randint(1, 6), random.randint(1, 6)
        print(f"🎲 결과: {die1}, {die2}")
        if die1 == die2:
            print("✅ 탈출 성공!")
            state['blackhole_attempts'] = 0
            return True
    state['blackhole_attempts'] += 1
    state['blackhole_traps'] += 1
    if state['blackhole_traps'] >= 2:
        state['lives'] -= 1
        print("💀 블랙홀에 2회 갇혀 라이프 감소! 지구로 귀환합니다.")
        state['visited_planets'] = []
        state['fuel'] = state['base_fuel']
        state['current_location'] = 'earth'
    return False

def choose_planet():
    available = [p for p in planet_list if p not in state['visited_planets'] and p not in obstacles]
    if not available:
        state['mission_success'] = True
        return None
    print("\n🌌 방문 가능한 행성:")
    for i, p in enumerate(available):
        print(f"{i+1}. {p} {'🚫 운석 있음' if p in obstacles else ''}")
    while True:
        try:
            choice = int(input("방문할 행성 번호를 선택하세요: ")) - 1
            if 0 <= choice < len(available):
                return available[choice]
        except ValueError:
            pass
        print("❗ 유효한 숫자를 입력하세요.")

def visit_planet(planet):
    if planet in state['visited_planets']:
        print(f"🔁 {planet}은(는) 이미 방문했습니다.")
        return
    fuel_cost = calculate_fuel_cost(state['current_location'], planet, state['spaceship']['speed'])
    state['fuel'] -= fuel_cost
    state['current_location'] = planet
    print(f"🚀 {planet}로 이동. 연료 {fuel_cost} 소모 → 남은 연료: {state['fuel']}")
    if random.random() < 0.3:
        item = random.choice(travel_random_items)
        print(f"🎉 이동 중 아이템 발견: {item['name']}")
        item['effect']()
    if state['fuel'] <= 0:
        print("💣 연료 부족! 우주정거장으로 이동합니다.")
        space_station()
        return
    print(f"🪐 {planet.upper()} 미션: {planet_missions.get(planet)}")
    state['turn_count'] += 1
    chance = random.randint(1, 10)
    if chance <= (7 - state['spaceship']['speed']):
        print("✅ 미션 성공!")
        state['visited_planets'].append(planet)
        bonus = planet_effects.get(planet, {}).get('success_bonus', 10)
        multiplier = planet_effects.get(planet, {}).get('score_multiplier', 1)
        fuel_bonus = planet_effects.get(planet, {}).get('fuel_boost_on_success', random.randint(10, 20))
        score_gain = bonus * multiplier
        state['score'] += score_gain
        state['fuel'] += fuel_bonus
        print(f"⭐ 점수 +{score_gain}, ⛽ 연료 +{fuel_bonus}")
        item = planet_effects.get(planet, {}).get('item')
        if item:
            state['items'].append(item)
            print(f"🎁 아이템 획득: {item}")
    else:
        print("❌ 미션 실패!")
        penalty = planet_effects.get(planet, {}).get('failure_penalty', random.randint(10, 25))
        state['fuel'] -= penalty
        print(f"🔋 연료 {penalty} 손실 → 남은 연료: {state['fuel']}")
        if state['fuel'] <= 0:
            print("💥 연료 소진! 지구로 귀환 및 라이프 감소")
            state['lives'] -= 1
            state['visited_planets'] = []
            state['fuel'] = state['base_fuel']
            state['current_location'] = 'earth'

# 메인 게임 루프
print("🌍 2092년, 인류는 태양계를 탐사할 인공지능 동반자를 탑재한 우주선을 출발시킵니다.")
while not state['mission_success'] and state['lives'] > 0:
    planet = choose_planet()
    if planet:
        visit_planet(planet)
    else:
        break

print("\n🚀 탐사 종료!")
print(f"🧮 점수: {state['score']}  📦 아이템: {state['items']}  ⏱️ 턴 수: {state['turn_count']}")
if state['score'] >= 100:
    print("🌟 당신은 전설의 탐사자입니다!")
elif len(state['items']) >= 5:
    print("🏅 다양한 특수 장비를 수집했습니다. 귀국 후 기술 연구에 큰 기여를 합니다.")
else:
    print("✅ 임무 완료. 지구에서의 삶으로 복귀합니다.")
