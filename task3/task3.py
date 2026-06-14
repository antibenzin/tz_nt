import json
import sys

def values(node, values_dict):
    if isinstance(node, dict):
        if 'id' in node and node['id'] in values_dict:
            node['value'] = values_dict[node['id']]
        
        for key, val in node.items():
            values(val, values_dict)
            
    elif isinstance(node, list):
        for item in node:
            values(item, values_dict)

values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]
   
with open(values_path, 'r', encoding='utf-8') as f:
        values_data = json.load(f)

values_dict = {}
items = values_data.get('values', []) if isinstance(values_data, dict) else values_data
    
for item in items:
    if isinstance(item, dict) and 'id' in item and 'value' in item:
        values_dict[item['id']] = item['value']

with open(tests_path, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)
    
values(tests_data, values_dict)

with open(report_path, 'w', encoding='utf-8') as f:
        
    json.dump(tests_data, f, indent=2, ensure_ascii=False)