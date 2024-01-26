#!/usr/bin/python3

def one_dic(list_of_dics):
    keys = list_of_dics[0].keys()
    final_dict = {key:[] for key in keys}
    for dic_ in list_of_dics:
        for key, value in dic_.items():
            final_dict[key].append(value)
    return final_dict
list1 = [{'id': 1610612737,
  'full_name': 'Atlanta Hawks',
  'abbreviation': 'ATL',
  'nickname': 'Hawks',
  'city': 'Atlanta',
  'state': 'Atlanta',
  'year_founded': 1949},
 {'id': 1610612738,
  'full_name': 'Boston Celtics',
  'abbreviation': 'BOS',
  'nickname': 'Celtics',
  'city': 'Boston',
  'state': 'Massachusetts',
  'year_founded': 1946},
 {'id': 1610612739,
  'full_name': 'Cleveland Cavaliers',
  'abbreviation': 'CLE',
  'nickname': 'Cavaliers',
  'city': 'Cleveland',
  'state': 'Ohio',
  'year_founded': 1970}]

print( one_dic(list1))
