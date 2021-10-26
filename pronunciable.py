import re
import itertools


def get_all_combinations_possible_in_given_str(inp_string):
    all_possible_combinations = []
    for str_len in range(2, len(inp_string) + 1):
        all_possible_combinations.extend("".join(i) for i in itertools.permutations(inp_string, str_len))

    regex_pattern = re.compile("[^aeiouAEIOU]{0,2}[aeiouAEIOU]")
    ret_set = set()
    for possible_combination in all_possible_combinations:
        if regex_pattern.match(possible_combination):
            ret_set.add(possible_combination)
    return ret_set


if __name__ == '__main__':
    inp_word = input("Enter a word ? ")
    sub_strings = get_all_combinations_possible_in_given_str(inp_word)
    print("Output {}".format(' '.join(sub_strings)))
