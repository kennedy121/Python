def solution(ratings):
    # Dicionário para armazenar as somas e contagens de avaliações para cada prato
    rating_sum = {}
    rating_count = {}
    
    # Iterar por cada avaliação
    for dish_id, rating in ratings:
        # Atualizar a soma e contagem das avaliações para cada prato
        if dish_id in rating_sum:
            rating_sum[dish_id] += rating
            rating_count[dish_id] += 1
        else:
            rating_sum[dish_id] = rating
            rating_count[dish_id] = 1

    # Calcular a média e encontrar o prato com a maior média
    best_dish = None
    best_avg = -1

    for dish_id in rating_sum:
        avg_rating = rating_sum[dish_id] / rating_count[dish_id]
        # Comparar médias e resolver empates pelo menor ID
        if avg_rating > best_avg or (avg_rating == best_avg and dish_id < best_dish):
            best_avg = avg_rating
            best_dish = dish_id

    return best_dish

n = 4
ratings = [(123, 4), (123, 3), (123, 5), (234, 2), (234, 3), (234, 4), (345, 5), (345, 4), (345, 3)]
print((n, ratings))  # Saída: 123


