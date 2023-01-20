from typing import List, Dict

def combine_dict_on_key(
    _array: List[Dict], 
    __array: List[Dict], 
    property: str
) -> List[Dict]:
    """Merges two arrays of dictionaries on a specified key"""
    _array.extend(
        list(
            map(
                lambda x, y: 
                    y if x.get(property) != y.get(property) 
                    else x.update(y), _array, __array
            )
        )
    )
    return _array

x = [
  { "id": 1, "name": 'John' },
  { "id": 2, "name": 'Maria' }
];
y = [
  { "id": 1, "age": 28 },
  { "id": 3, "age": 26 },
  { "age": 3}
];


print(combine_dict_on_key(x, y, 'id')) # [{'id': 1, 'name': 'John', 'age': 28}, {'id': 2, 'name': 'Maria'}, {'id': 3, 'age': 26}]
