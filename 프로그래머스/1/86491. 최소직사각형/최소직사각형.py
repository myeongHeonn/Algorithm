def solution(sizes):
    for size in sizes:
        size.sort()

    w = max(size[0] for size in sizes)
    h = max(size[1] for size in sizes)

    return w * h