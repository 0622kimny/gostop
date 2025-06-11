from django.shortcuts import render
from .calculator import determine_winner_and_calculate, ALL_CARDS
import json

def setup_view(request):
    if request.method == 'POST':
        player_names = request.POST.getlist('player_names')
        bet_per_point = request.POST.get('bet_per_point', 100)
        previous_nagari_count = request.POST.get('previous_nagari_count', 0)
        
        categorized_cards = {
            'gwangs': [], 'ddis': [], 'yeols': [], 'pis': [], 'ssang_pis': []
        }
        for key, card in ALL_CARDS.items():
            card_data = (key, card)
            if card['type'] == 'gwang':
                categorized_cards['gwangs'].append(card_data)
            elif card['type'] == 'ddi':
                categorized_cards['ddis'].append(card_data)
            elif card['type'] == 'yeol':
                categorized_cards['yeols'].append(card_data)
            elif card['type'] == 'pi':
                if card['pi_value'] >= 2:
                    categorized_cards['ssang_pis'].append(card_data)
                else:
                    categorized_cards['pis'].append(card_data)

        context = {
            'player_names': player_names,
            'bet_per_point': bet_per_point,
            'previous_nagari_count': previous_nagari_count,
            'categorized_cards': categorized_cards,
        }
        return render(request, 'calculator_form.html', context)
    
    return render(request, 'setup.html')

def calculate_view(request):
    if request.method != 'POST':
        return render(request, 'setup.html')

    form_data = request.POST
    player_names_str = form_data.get('player_names', '')
    player_names = player_names_str.split(',') if player_names_str else []
    bet_per_point = int(form_data.get('bet_per_point', 100))
    previous_nagari_count = int(form_data.get('previous_nagari_count', 0))

    all_players_data = []
    for name in player_names:
        player_data = {
            'name': name,
            'cards': form_data.getlist(f'cards_{name}'),
            'go': int(form_data.get(f'go_{name}', 0)),
            'heundeulgi': int(form_data.get(f'heundeulgi_{name}', 0)),
            'is_gobak_target': form_data.get(f'is_gobak_target_{name}') == 'on',
            'bonus': form_data.get(f'bonus_{name}', 'none'),
            'is_5yeol_ssangpi': form_data.get(f'is_5yeol_ssangpi_{name}') == 'on',
        }
        all_players_data.append(player_data)
    
    result = determine_winner_and_calculate(all_players_data, previous_nagari_count)
    
    if not result.get('is_nagari'):
        for name, delta in result['player_deltas'].items():
            money_change = delta * bet_per_point
            result['player_deltas'][name] = money_change
            
    context = {
        'round_result': result,
    }
    return render(request, 'result.html', context)