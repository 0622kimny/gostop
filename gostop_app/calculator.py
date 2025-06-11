ALL_CARDS = {
    '1gwang': {'name': '1광(일광)', 'type': 'gwang', 'pi_value': 1}, '1yeol': {'name': '1열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '1hongdan': {'name': '1띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '1pi1': {'name': '1피1', 'type': 'pi', 'pi_value': 1}, '1pi2': {'name': '1피2', 'type': 'pi', 'pi_value': 1},
    '2yeol': {'name': '2열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '2chongdan': {'name': '2띠(청단)', 'type': 'ddi', 'pi_value': 1}, '2pi1': {'name': '2피1', 'type': 'pi', 'pi_value': 1}, '2pi2': {'name': '2피2', 'type': 'pi', 'pi_value': 1},
    '3gwang': {'name': '3광(삼광)', 'type': 'gwang', 'pi_value': 1}, '3hongdan': {'name': '3띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '3pi1': {'name': '3피1', 'type': 'pi', 'pi_value': 1}, '3pi2': {'name': '3피2', 'type': 'pi', 'pi_value': 1},
    '4yeol': {'name': '4열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '4chodan': {'name': '4띠(초단)', 'type': 'ddi', 'pi_value': 1}, '4pi1': {'name': '4피1', 'type': 'pi', 'pi_value': 1}, '4pi2': {'name': '4피2', 'type': 'pi', 'pi_value': 1},
    '5yeol': {'name': '5열끗', 'type': 'yeol', 'pi_value': 1}, '5chodan': {'name': '5띠(초단)', 'type': 'ddi', 'pi_value': 1}, '5pi1': {'name': '5피1', 'type': 'pi', 'pi_value': 1}, '5pi2': {'name': '5피2', 'type': 'pi', 'pi_value': 1},
    '6yeol': {'name': '6열끗', 'type': 'yeol', 'pi_value': 1}, '6chongdan': {'name': '6띠(청단)', 'type': 'ddi', 'pi_value': 1}, '6pi1': {'name': '6피1', 'type': 'pi', 'pi_value': 1}, '6pi2': {'name': '6피2', 'type': 'pi', 'pi_value': 1},
    '7yeol': {'name': '7열끗', 'type': 'yeol', 'pi_value': 1}, '7chodan': {'name': '7띠(초단)', 'type': 'ddi', 'pi_value': 1}, '7pi1': {'name': '7피1', 'type': 'pi', 'pi_value': 1}, '7pi2': {'name': '7피2', 'type': 'pi', 'pi_value': 1},
    '8gwang': {'name': '8광(팔광)', 'type': 'gwang', 'pi_value': 1}, '8yeol': {'name': '8열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '8pi1': {'name': '8피1', 'type': 'pi', 'pi_value': 1}, '8pi2': {'name': '8피2', 'type': 'pi', 'pi_value': 1},
    '9yeol': {'name': '9열끗(국진)', 'type': 'yeol', 'pi_value': 2}, '9chongdan': {'name': '9띠(청단)', 'type': 'ddi', 'pi_value': 1}, '9pi1': {'name': '9피1', 'type': 'pi', 'pi_value': 1}, '9pi2': {'name': '9피2', 'type': 'pi', 'pi_value': 1},
    '10yeol': {'name': '10열끗', 'type': 'yeol', 'pi_value': 2}, '10hongdan': {'name': '10띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '10pi1': {'name': '10피1', 'type': 'pi', 'pi_value': 1}, '10pi2': {'name': '10피2', 'type': 'pi', 'pi_value': 1},
    '11gwang': {'name': '11광(똥광)', 'type': 'gwang', 'pi_value': 2}, '11ssangpi': {'name': '11쌍피', 'type': 'pi', 'pi_value': 2}, '11pi1': {'name': '11피1', 'type': 'pi', 'pi_value': 1}, '11pi2': {'name': '11피2', 'type': 'pi', 'pi_value': 1},
    '12gwang': {'name': '12광(비광)', 'type': 'gwang', 'pi_value': 1}, '12ddi': {'name': '12띠(비띠)', 'type': 'ddi', 'pi_value': 1}, '12yeol': {'name': '12열끗', 'type': 'yeol', 'pi_value': 2}, '12ssangpi': {'name': '12쌍피', 'type': 'pi', 'pi_value': 3},
}

def _calculate_base_score(cards):
    """한 플레이어의 카드 덱으로 기본 점수만 계산하는 내부 함수"""
    score = 0
    if not cards:
        return 0

    gwangs = [c for c in cards if ALL_CARDS[c]['type'] == 'gwang']
    yeols = [c for c in cards if ALL_CARDS[c]['type'] == 'yeol']
    ddis = [c for c in cards if ALL_CARDS[c]['type'] == 'ddi']
    pis_list = [c for c in cards if ALL_CARDS[c]['type'] == 'pi']

    # 광 점수
    if len(gwangs) == 5: score += 15
    elif len(gwangs) == 4: score += 4
    elif len(gwangs) == 3: score += 2 if '12gwang' in gwangs else 3

    # 고도리
    godori_cards = {'1yeol', '2yeol', '4yeol', '8yeol'}
    my_godori = {c for c in yeols if c in godori_cards}
    if len(my_godori) == 3:
        score += 5
        yeols = [y for y in yeols if y not in my_godori]

    # 단(띠 족보) 점수
    hongdan_set, chodan_set, chongdan_set = set(['1hongdan', '3hongdan', '10hongdan']), set(['4chodan', '5chodan', '7chodan']), set(['2chongdan', '6chongdan', '9chongdan'])
    collected_ddis = set(ddis)
    used_ddis = set()

    if hongdan_set.issubset(collected_ddis):
        score += 3
        used_ddis.update(hongdan_set)
    if chodan_set.issubset(collected_ddis):
        score += 3
        used_ddis.update(chodan_set)
    if chongdan_set.issubset(collected_ddis):
        score += 3
        used_ddis.update(chongdan_set)

    # 나머지 띠 점수 계산
    remaining_ddis = [d for d in ddis if d not in used_ddis]
    if len(remaining_ddis) >= 5:
        score += len(remaining_ddis) - 4

    # 열끗 점수
    if len(yeols) >= 5:
        score += len(yeols) - 4
        
    # 피 점수
    pi_value = sum(ALL_CARDS[p]['pi_value'] for p in pis_list)
    if pi_value >= 10:
        score += pi_value - 9

    return score


def determine_winner_and_calculate(all_players_data, previous_nagari_count):
    """모든 플레이어의 데이터를 받아 승자를 판별하고 최종 점수를 계산하는 메인 함수"""
    scores = {player['name']: _calculate_base_score(player['cards']) for player in all_players_data}
    
    potential_winners = {name: score for name, score in scores.items() if score >= 3}
    if not potential_winners:
        return {'is_nagari': True}
        
    winner_name = max(potential_winners, key=potential_winners.get)
    
    winner_data = next(p for p in all_players_data if p['name'] == winner_name)
    losers_data = [p for p in all_players_data if p['name'] != winner_name]
    
    base_score = scores[winner_name]
    breakdown = {'기본점수': base_score}
    
    # 뻑, 따닥 보너스 점수 계산
    bonus_points = 0
    bonus_map = {'first_ppeok': 1, 'first_ddadak': 1, 'second_ppeok': 2, 'third_ppeok': 4}
    winner_bonus = winner_data.get('bonus', 'none')
    if winner_bonus in bonus_map:
        bonus_points = bonus_map[winner_bonus]
        breakdown[f'보너스({winner_bonus})'] = f'+{bonus_points}점'

    # 고(Go) 점수 계산
    go_count = winner_data.get('go', 0)
    go_bonus, go_multiplier = 0, 1
    if go_count == 1: go_bonus = 1
    elif go_count == 2: go_bonus = 2
    elif go_count >= 3:
        go_bonus = go_count
        go_multiplier = 2 ** (go_count - 2)

    # 배율 적용 전 최종 점수
    final_score = base_score + go_bonus + bonus_points
    if go_count > 0: breakdown[f'{go_count}고'] = f'+{go_bonus}점'

    # 전체 배율 계산
    base_multiplier = go_multiplier
    
    # 멍따 배율
    winner_yeols = [c for c in winner_data['cards'] if ALL_CARDS[c]['type'] == 'yeol']
    godori_cards = {'1yeol', '2yeol', '4yeol', '8yeol'}
    my_godori_in_winner = {c for c in winner_yeols if c in godori_cards}
    if not len(my_godori_in_winner) == 3:
      if len(winner_yeols) >= 7:
          base_multiplier *= 2
          breakdown['멍따'] = 'x2'
    
    # 흔들기/폭탄 배율
    heundeulgi_count = winner_data.get('heundeulgi', 0)
    if heundeulgi_count > 0:
        heundeulgi_multiplier = 2 ** heundeulgi_count
        base_multiplier *= heundeulgi_multiplier
        breakdown[f'흔들기/폭탄({heundeulgi_count}회)'] = f'x{heundeulgi_multiplier}'

    # 이전 나가리 배율
    if previous_nagari_count > 0:
        nagari_multiplier = 2 ** previous_nagari_count
        base_multiplier *= nagari_multiplier
        breakdown[f'이전 나가리({previous_nagari_count}회)'] = f'x{nagari_multiplier}'

    # 최종 점수 분배
    player_deltas = {p['name']: 0 for p in all_players_data}
    gobak_player = next((p['name'] for p in losers_data if p.get('is_gobak_target')), None)
    if gobak_player:
        breakdown[f'{gobak_player} 고박'] = '적용'

    total_points_won = 0
    winner_gwangs = {c for c in winner_data['cards'] if ALL_CARDS[c]['type'] == 'gwang'}
    winner_pi_value = sum(ALL_CARDS[p]['pi_value'] for p in winner_data['cards'] if ALL_CARDS[p]['type'] == 'pi')

    for loser in losers_data:
        bak_multiplier = 1
        loser_breakdown = []
        
        loser_gwangs = {c for c in loser['cards'] if ALL_CARDS[c]['type'] == 'gwang'}
        if len(winner_gwangs) >= 3 and not loser_gwangs:
            bak_multiplier *= 2
            loser_breakdown.append('광박')

        loser_pi_value = sum(ALL_CARDS[p]['pi_value'] for p in loser['cards'] if ALL_CARDS[p]['type'] == 'pi')
        if winner_pi_value >= 10 and loser_pi_value <= 5:
            bak_multiplier *= 2
            loser_breakdown.append('피박')

        if loser_breakdown:
            breakdown[f'{loser["name"]}'] = " ".join(loser_breakdown)

        points_lost = final_score * base_multiplier * bak_multiplier
        
        # 고박인 경우, 고박 플레이어에게 모든 점수를 합산
        if gobak_player and gobak_player != loser['name']:
            player_deltas[gobak_player] -= points_lost
        else:
            player_deltas[loser['name']] -= points_lost
        
        total_points_won += points_lost

    player_deltas[winner_name] = total_points_won

    return {
        'is_nagari': False, 
        'winner_name': winner_name,
        'breakdown': breakdown, 
        'player_deltas': player_deltas 
    }