def find_board_size(n, w, h):
    '''Пошук найменшої сторои квадратної дошки щоб розмісти n листків розміром w * h'''
    left, right= min(w, h), max(w, h) * n

    while left < right:
        mid = (right + left) // 2
        if (mid // w) * (mid // h) >= n:
            right = mid
        else:
            left = mid + 1
    return left
