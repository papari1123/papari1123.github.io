from collections import defaultdict, deque


def get_time(in_frames):
    h = in_frames // 3600
    m = (in_frames % 3600) // 60
    s = in_frames % 60
    return f'{h:02}:{m:02}:{s:02}'


def get_frames(in_time):
    h, m, s = map(int, in_time.split(':'))
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    startframe = defaultdict(int)
    endframe = defaultdict(int)

    for log in logs:
        s, e = log.split('-')
        sf = get_frames(s)
        ef = get_frames(e)
        startframe[sf] += 1
        endframe[ef] += 1

    time_sum = 0
    add = 0
    max_sum = 0
    answer = 0
    frame_stack = deque()
    ad_frame = get_frames(adv_time)

    for frame in range(get_frames(play_time) + 1):
        frame_stack.append(add)
        time_sum += add
        add += startframe[frame]
        add -= endframe[frame]

        if max_sum < time_sum:
            max_sum = time_sum
            answer = frame - ad_frame

        if frame >= ad_frame:
            time_sum -= frame_stack.popleft()

    return get_time(answer) if answer > 0 else '00:00:00'