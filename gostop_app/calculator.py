ALL_CARDS = {
    '1gwang': {'name': '1광', 'type': 'gwang', 'pi_value': 1}, '1yeol': {'name': '1열끗', 'type': 'yeol', 'pi_value': 1}, '1hongdan': {'name': '1띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '1pi1': {'name': '1피', 'type': 'pi', 'pi_value': 1}, '1pi2': {'name': '1피', 'type': 'pi', 'pi_value': 1},
    '2yeol': {'name': '2열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '2chongdan': {'name': '2띠(청단)', 'type': 'ddi', 'pi_value': 1}, '2pi1': {'name': '2피', 'type': 'pi', 'pi_value': 1}, '2pi2': {'name': '2피', 'type': 'pi', 'pi_value': 1},
    '3gwang': {'name': '3광', 'type': 'gwang', 'pi_value': 1}, '3hongdan': {'name': '3띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '3pi1': {'name': '3피', 'type': 'pi', 'pi_value': 1}, '3pi2': {'name': '3피', 'type': 'pi', 'pi_value': 1},
    '4yeol': {'name': '4열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '4chodan': {'name': '4띠(초단)', 'type': 'ddi', 'pi_value': 1}, '4pi1': {'name': '4피', 'type': 'pi', 'pi_value': 1}, '4pi2': {'name': '4피', 'type': 'pi', 'pi_value': 1},
    '5yeol': {'name': '5월 열끗', 'type': 'yeol', 'pi_value': 1}, '5chodan': {'name': '5띠(초단)', 'type': 'ddi', 'pi_value': 1}, '5pi1': {'name': '5피', 'type': 'pi', 'pi_value': 1}, '5pi2': {'name': '5피', 'type': 'pi', 'pi_value': 1},
    '6yeol': {'name': '6열끗', 'type': 'yeol', 'pi_value': 1}, '6chongdan': {'name': '6띠(청단)', 'type': 'ddi', 'pi_value': 1}, '6pi1': {'name': '6피', 'type': 'pi', 'pi_value': 1}, '6pi2': {'name': '6피', 'type': 'pi', 'pi_value': 1},
    '7yeol': {'name': '7열끗', 'type': 'yeol', 'pi_value': 1}, '7chodan': {'name': '7띠(초단)', 'type': 'ddi', 'pi_value': 1}, '7pi1': {'name': '7피', 'type': 'pi', 'pi_value': 1}, '7pi2': {'name': '7피', 'type': 'pi', 'pi_value': 1},
    '8gwang': {'name': '8광', 'type': 'gwang', 'pi_value': 1}, '8yeol': {'name': '8열끗(고도리)', 'type': 'yeol', 'pi_value': 1}, '8pi1': {'name': '8피', 'type': 'pi', 'pi_value': 1}, '8pi2': {'name': '8피', 'type': 'pi', 'pi_value': 1},
    '9yeol': {'name': '9열끗(국진)', 'type': 'yeol', 'pi_value': 2}, '9chongdan': {'name': '9띠(청단)', 'type': 'ddi', 'pi_value': 1}, '9pi1': {'name': '9피', 'type': 'pi', 'pi_value': 1}, '9pi2': {'name': '9피', 'type': 'pi', 'pi_value': 1},
    '10yeol': {'name': '10열끗', 'type': 'yeol', 'pi_value': 2}, '10hongdan': {'name': '10띠(홍단)', 'type': 'ddi', 'pi_value': 1}, '10pi1': {'name': '10피', 'type': 'pi', 'pi_value': 1}, '10pi2': {'name': '10피', 'type': 'pi', 'pi_value': 1},
    '11gwang': {'name': '11광(똥광)', 'type': 'gwang', 'pi_value': 2}, '11ssangpi': {'name': '11쌍피', 'type': 'pi', 'pi_value': 2}, '11pi1': {'name': '11피', 'type': 'pi', 'pi_value': 1}, '11pi2': {'name': '11피', 'type': 'pi', 'pi_value': 1},
    '12gwang': {'name': '12광(비광)', 'type': 'gwang', 'pi_value': 1}, '12ddi': {'name': '12띠(비띠)', 'type': 'ddi', 'pi_value': 1}, '12yeol': {'name': '12열끗', 'type': 'yeol', 'pi_value': 2}, '12ssangpi': {'name': '12쌍피', 'type': 'pi', 'pi_value': 3},
}

def _calculate_base_score(cards, is_5yeol_ssangpi):
    score = 0
    breakdown = {}
    if not cards:
        return 0, {}

    # 5월 열끗을 쌍피로 사용할 경우, 카드 목록에서 임시로 변경
    pi_points_from_5yeol = 0
    if '5yeol' in cards and is_5yeol_ssangpi:
        cards = [c for c in cards if c != '5yeol']
        pi_points_from_5yeol = 2 # 쌍피(2)로 취급

    gwangs = [c for c in cards if ALL_CARDS[c]['type'] == 'gwang']
    yeols = [c for c in cards if ALL_CARDS[c]['type'] == 'yeol']
    ddis = [c for c in cards if ALL_CARDS[c]['type'] == 'ddi']
    pis_list = [c for c in cards if ALL_CARDS[c]['type'] == 'pi']

    # 광 점수
    if len(gwangs) == 5: score, breakdown['오광'] = 15, 15
    elif len(gwangs) == 4: score, breakdown['사광'] = 4, 4
    elif len(gwangs) == 3:
        if '12gwang' in gwangs: score, breakdown['비삼광'] = 2, 2
        else: score, breakdown['삼광'] = 3, 3

    # 고도리 (5점)
    godori_cards = {'2yeol', '4yeol', '8yeol'}
    my_godori = {c for c in yeols if c in godori_cards}
    if len(my_godori) == 3:
        score += 5
        breakdown['고도리'] = 5
        yeols = [y for y in yeols if y not in my_godori]

    # 단(띠 족보) 점수 (각 3점)
    hongdan_set, chodan_set, chongdan_set = set(['1hongdan', '3hongdan', '10hongdan']), set(['4chodan', '5chodan', '7chodan']), set(['2chongdan', '6chongdan', '9chongdan'])
    collected_ddis_set = set(ddis)
    used_ddis = set()

    if hongdan_set.issubset(collected_ddis_set):
        score += 3
        breakdown['홍단'] = 3
        used_ddis.update(hongdan_set)
    if chodan_set.issubset(collected_ddis_set):
        score += 3
        breakdown['초단'] = 3
        used_ddis.update(chodan_set)
    if chongdan_set.issubset(collected_ddis_set):
        score += 3
        breakdown['청단'] = 3
        used_ddis.update(chongdan_set)

    # 나머지 띠 점수 (5장부터 1점, 1장 추가마다 +1점)
    remaining_ddis_count = len([d for d in ddis if d not in used_ddis])
    if remaining_ddis_count >= 5:
        ddi_score = remaining_ddis_count - 4
        score += ddi_score
        breakdown['띠'] = ddi_score

    # 열끗 점수 (5장부터 1점, 1장 추가마다 +1점)
    if len(yeols) >= 5:
        yeol_score = len(yeols) - 4
        score += yeol_score
        breakdown['열끗'] = yeol_score
        
    # 피 점수 (10장부터 1점, 1장 추가마다 +1점)
    pi_value = sum(ALL_CARDS[p]['pi_value'] for p in pis_list) + pi_points_from_5yeol
    if pi_value >= 10:
        pi_score = pi_value - 9
        score += pi_score
        breakdown['피'] = pi_score

    return score, breakdown


def determine_winner_and_calculate(all_players_data, previous_nagari_count):
    scores = {}
    breakdowns = {}
    for player in all_players_data:
        is_5yeol_ssangpi = player.get('is_5yeol_ssangpi', False)
        s, b = _calculate_base_score(list(player['cards']), is_5yeol_ssangpi) # list()로 복사본 전달
        scores[player['name']] = s
        breakdowns[player['name']] = b
        
    potential_winners = {name: score for name, score in scores.items() if score >= 3}
    if not potential_winners:
        return {'is_nagari': True}
        
    winner_name = max(potential_winners, key=potential_winners.get)
    
    winner_data = next(p for p in all_players_data if p['name'] == winner_name)
    losers_data = [p for p in all_players_data if p['name'] != winner_name]
    
    base_score = scores[winner_name]
    breakdown = breakdowns[winner_name]
    if not breakdown: # 점수는 있으나 breakdown이 없는 경우 (예: 피 10장)
        breakdown['기본점수'] = base_score

    bonus_points = 0
    bonus_map = {'first_ppeok': 1, 'first_ddadak': 1, 'second_ppeok': 2, 'third_ppeok': 4}
    winner_bonus = winner_data.get('bonus', 'none')
    if winner_bonus in bonus_map:
        bonus_points = bonus_map[winner_bonus]
        breakdown[f'보너스({winner_bonus})'] = f'+{bonus_points}점'

    go_count = winner_data.get('go', 0)
    go_bonus, go_multiplier = 0, 1
    if go_count == 1: go_bonus = 1
    elif go_count == 2: go_bonus = 2
    elif go_count >= 3:
        go_bonus = go_count
        go_multiplier = 2 ** (go_count - 2)

    final_score = base_score + go_bonus + bonus_points
    if go_count > 0: breakdown[f'{go_count}고'] = f'+{go_bonus}점'

    base_multiplier = go_multiplier
    
    winner_yeols_cards = [c for c in winner_data['cards'] if ALL_CARDS[c]['type'] == 'yeol']
    if '5yeol' in winner_data['cards'] and winner_data.get('is_5yeol_ssangpi'):
        pass # 5월 열끗을 쌍피로 썼으면 멍따 계산에 포함 안함
    else:
        godori_cards = {'2yeol', '4yeol', '8yeol'}
        my_godori_in_winner = {c for c in winner_yeols_cards if c in godori_cards}
        if not len(my_godori_in_winner) == 3 and len(winner_yeols_cards) >= 7:
            base_multiplier *= 2
            breakdown['멍따'] = 'x2'
    
    heundeulgi_count = winner_data.get('heundeulgi', 0)
    if heundeulgi_count > 0:
        base_multiplier *= (2 ** heundeulgi_count)
        breakdown[f'흔들기/폭탄({heundeulgi_count}회)'] = f'x{2 ** heundeulgi_count}'

    if previous_nagari_count > 0:
        base_multiplier *= (2 ** previous_nagari_count)
        breakdown[f'이전 나가리({previous_nagari_count}회)'] = f'x{2 ** previous_nagari_count}'

    player_deltas = {p['name']: 0 for p in all_players_data}
    gobak_player = next((p['name'] for p in losers_data if p.get('is_gobak_target')), None)
    if gobak_player:
        breakdown[f'{gobak_player} 고박'] = '적용'

    total_points_won = 0
    
    # 박 계산을 위한 승자 패 정보
    winner_gwangs = {c for c in winner_data['cards'] if ALL_CARDS[c]['type'] == 'gwang'}
    winner_is_5yeol_ssangpi = winner_data.get('is_5yeol_ssangpi', False)
    winner_pi_value = sum(ALL_CARDS[p]['pi_value'] for p in winner_data['cards'] if ALL_CARDS[p]['type'] == 'pi')
    if '5yeol' in winner_data['cards'] and winner_is_5yeol_ssangpi:
        winner_pi_value += 2

    for loser in losers_data:
        bak_multiplier = 1
        
        # 광박
        loser_gwangs = {c for c in loser['cards'] if ALL_CARDS[c]['type'] == 'gwang'}
        if len(winner_gwangs) >= 3 and not loser_gwangs:
            bak_multiplier *= 2
            breakdown[f'{loser["name"]}-광박'] = "적용"

        # 피박
        loser_is_5yeol_ssangpi = loser.get('is_5yeol_ssangpi', False)
        loser_pi_value = sum(ALL_CARDS[p]['pi_value'] for p in loser['cards'] if ALL_CARDS[p]['type'] == 'pi')
        if '5yeol' in loser['cards'] and loser_is_5yeol_ssangpi:
            loser_pi_value += 2
        if winner_pi_value >= 10 and loser_pi_value <= 5:
            bak_multiplier *= 2
            breakdown[f'{loser["name"]}-피박'] = "적용"
        
        # 멍박
        if '멍따' in breakdown:
            loser_yeols_cards = [c for c in loser['cards'] if ALL_CARDS[c]['type'] == 'yeol']
            if '5yeol' in loser['cards'] and loser_is_5yeol_ssangpi:
                 loser_yeols_cards = [c for c in loser_yeols_cards if c != '5yeol']
            if not loser_yeols_cards:
                bak_multiplier *= 2
                breakdown[f'{loser["name"]}-멍박'] = "적용"

        points_lost = final_score * base_multiplier * bak_multiplier
        
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