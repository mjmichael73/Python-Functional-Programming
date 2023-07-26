from itertools import combinations

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pairs = combinations(num_list, 2)

filtered_pairs = filter(lambda x: all(num >= 5 for num in x), pairs)

filtered_pairs_list = list(filtered_pairs)

sum_pairs = filter(lambda x: sum(x) >= 15, filtered_pairs_list)

sum_pairs_list = list(sum_pairs)

print(sum_pairs_list)
