# TODO: List solution (not efficient)
# def sum_pairs(ints, s):
#     output = []
#     my_index = 0
#     for outer in ints[::-1]:
#         my_index += 1
#         for inner in ints[::-1][my_index:]:
#             if outer + inner == s:
#                 output = [inner, outer]
#     return output if output else None

# TODO: Generator solution (not efficient enough)
# def sum_pairs(ints, s):
#     output = [None, None]
#     for indx1 in range(len(ints)-1, 0, -1):
#         if output[1] == ints[indx1]:
#             continue
#         for indx2 in range(indx1-1, -1, -1):
#             if output[0] == ints[indx2]:
#                 continue
#             if ints[indx1] + ints[indx2] == s:
#                 output = [ints[indx2], ints[indx1]]
#     return output if output != [None, None] else None

# TODO: Generator solution with list comprehension (not efficient enough)
# def sum_pairs(ints, s):
#     output = [[ints[indx2], ints[indx1]] for indx1 in range(len(ints)-1, 0, -1) for indx2 in range(indx1-1, -1, -1) if ints[indx1] + ints[indx2] == s]
#     return output[-1] if output else None


# TODO: Best practise
def sum_pairs(ints, s):
    my_set = set()
    for i in ints:
        if i in my_set:
            return [s - i, i]
        my_set.add(s - i)


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
