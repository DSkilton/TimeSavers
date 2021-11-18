def anagram_solution(s1, s2):
    s2_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(s2_list) and not found:
            if s1[pos1] == s2_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

            if found:
                s2_list[pos2] = None
            else:
                still_ok = False

            pos1 = pos1 + 1

        return still_ok

print(anagram_solution("cake", "kace"))

def anagram_solution2(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()
    s2_list.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if s1_list[pos] == s2_list[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagram_solution2("cake", "kace"))