"""
3. Рефакторинг.
Дано: неоптимальный код.
Задание: оптимизировать следующий код.
def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    responses = []
    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        responses.append(new_response)
    return responses
"""

def responses_creator(item_ids):
    if item_ids is None:
        return None
    else:
        responses = []
        for item_id in item_ids:
            new_response = dict(item_id=item_id)
            responses.append(new_response)
    return responses

responses_creator(item_ids= 12)