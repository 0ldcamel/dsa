def find_segments(data):
    data += "@"
    n = len(data) - 1
    segments_dict = {}
    segment_list = []
    i = 0
    start = 0
    while i < n:
        if data[i] == data[i + 1]:
            i += 1
        else:
            segment_list.append((i + 1 - start, data[i]))
            i += 1
            start = i
    return segment_list

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]