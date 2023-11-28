import math
import os
import random

from datetime import datetime


def is_point_inside_triangle(p, a, b, c):
    # sign 함수 정의: 세 점으로 만들어지는 부등식의 부호를 판별
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    # 각 삼각형 변과 주어진 점 사이의 부등식 계산
    d1 = sign(p, a, b)
    d2 = sign(p, b, c)
    d3 = sign(p, c, a)

    # 부등식의 부호를 통해 삼각형 내부 여부 판별
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    # 부등식 결과를 통해 점이 삼각형 내부에 있는지 여부 반환
    return not (has_neg and has_pos)


def generate_point_inside_triangle_with_distance(count, d, existing_points):
    # 삼각형의 꼭지점 좌표
    a, b, c = select_next_item(count)

    cnt = 0
    i = 1
    # while d > 0.04:
    while d > 150:
        # 무작위로 삼각형 내부의 점 생성
        x = random.uniform(min(a[0], b[0], c[0]), max(a[0], b[0], c[0]))
        y = random.uniform(min(a[1], b[1], c[1]), max(a[1], b[1], c[1]))

        new_point = (x, y)

        # 생성된 점이 기존 점들과의 거리가 d 이상이며, 삼각형 내부에 있는지 확인
        if not is_point_inside_triangle(new_point, a, b, c):
            continue

        if all(
            math.dist(new_point, (float(a) for a in existing_point)) >= d for existing_point in existing_points
        ) and is_point_inside_triangle(new_point, a, b, c):
            print(cnt, i, "=============================================")
            return (str(p) for p in new_point)

        # 적절한 점을 찾지 못한 경우, d를 반으로 줄임
        d *= i
        if cnt % 1000 == 0:
            i += 1
        cnt += 1
        d /= i
    print(cnt, i, "here!")

    current_date = datetime.now()
    if count % 2 == 0:
        if (datetime(2023, 12, 3) <= current_date <= datetime(2023, 12, 9)) or (
            datetime(2023, 12, 17) <= current_date <= datetime(2023, 12, 23)
        ):
            return (str(p) for p in (random.randint(130, 725), random.randint(465, 950)))
        elif datetime(2023, 12, 24) <= current_date <= datetime(2023, 12, 30):
            return (str(p) for p in (random.randint(2500, 2900), random.randint(1700, 2100)))
        else:
            return (str(p) for p in (random.randint(220, 740), random.randint(370, 1375)))
    else:
        if (datetime(2023, 12, 3) <= current_date <= datetime(2023, 12, 9)) or (
            datetime(2023, 12, 17) <= current_date <= datetime(2023, 12, 23)
        ):
            return (str(p) for p in (random.randint(2280, 2850), random.randint(465, 950)))
        elif datetime(2023, 12, 24) <= current_date <= datetime(2023, 12, 30):
            return (str(p) for p in (random.randint(200, 600), random.randint(1700, 2100)))
        else:
            return (str(p) for p in (random.randint(2290, 2800), random.randint(370, 1375)))
    # return (0.9, 0.9)


# tree_1 = [
#     [(2500, 243), (1373, 2500), (3650, 2500)],
#     [(1373, 2500), (2340, 4398), (3650, 2500)],
#     [(1373, 2500), (2340, 4398), (789, 3818)],
#     [(2340, 4398), (4292, 3897), (3650, 2500)],
# ]

# tree_2 = [
#     [(2547, 288), (1780, 2320), (3325, 2320)],
#     [(2573, 4124), (1780, 2320), (3325, 2320)],
#     [(2573, 4124), (3760, 4000), (3325, 2320)],
#     [(2573, 4124), (1360, 4045), (1780, 2320)],
# ]

# tree_3 = [
#     [(2445, 243), (1250, 2260), (3660, 2260)],
#     [(2500, 4120), (1250, 2260), (3660, 2260)],
#     [(2500, 4120), (450, 3500), (1250, 2260)],
#     [(2500, 4120), (4610, 3500), (3660, 2260)],
# ]
tree_1 = [
    [(1435, 530), (600, 2545), (2585, 2545)],
]

tree_2 = [
    [(1500, 245), (800, 1900), (2240, 1900)],  # 3개
    [(1050, 1005), (1500, 2465), (2240, 1900)],  # 2개
    [(1500, 245), (800, 1900), (2240, 1900)],  # 3개
    [(1180, 2540), (800, 1900), (2240, 1900)],  # 1개
    [(1500, 245), (800, 1900), (2240, 1900)],  # 3개
    [(1050, 1005), (1500, 2465), (2240, 1900)],  # 2개
]

tree_3 = [
    [(1500, 440), (900, 1500), (2020, 1500)],
    [(1500, 2500), (900, 1500), (2020, 1500)],
    [(1500, 2500), (900, 1500), (520, 2500)],
    [(1500, 2500), (2475, 2500), (2020, 1500)],
]

tree_4 = [
    [(1500, 225), (440, 2800), (2475, 2800)],
]

tree_5 = [
    [(1500, 145), (823, 1500), (2190, 1500)],
    [(823, 1500), (1404, 2638), (2190, 1500)],
    [(823, 1500), (1404, 2638), (473, 2290)],
    [(1404, 2638), (2575, 2338), (2190, 1500)],
]


def select_next_item(count):
    # 현재 날짜 구하기
    current_date = datetime.now()
    trees = [tree_1, tree_2, tree_3, tree_4, tree_5]

    # 주차 계산
    if datetime(2023, 12, 3) <= current_date <= datetime(2023, 12, 9):
        return trees[0][(count - 1) % len(trees[0])]
    elif datetime(2023, 12, 10) <= current_date <= datetime(2023, 12, 16):
        return trees[1][(count - 1) % len(trees[1])]
    elif datetime(2023, 12, 17) <= current_date <= datetime(2023, 12, 23):
        return trees[2][(count - 1) % len(trees[2])]
    elif datetime(2023, 12, 24) <= current_date <= datetime(2023, 12, 30):
        return trees[3][(count - 1) % len(trees[3])]
    else:
        return trees[4][(count - 1) % len(trees[4])]


# tree_1 = [
#     [(0.5, 0.0486), (0.2746, 0.5), (0.73, 0.5)],
#     [(0.2746, 0.5), (0.468, 0.8796), (0.73, 0.5)],
#     [(0.2746, 0.5), (0.468, 0.8796), (0.1578, 0.7636)],
#     [(0.468, 0.8796), (0.8584, 0.7794), (0.73, 0.5)],
# ]
# tree_2 = [
#     [(0.5094, 0.0576), (0.356, 0.464), (0.665, 0.464)],
#     [(0.5146, 0.8248), (0.356, 0.464), (0.665, 0.464)],
#     [(0.5146, 0.8248), (0.752, 0.8), (0.665, 0.464)],
#     [(0.5146, 0.8248), (0.272, 0.809), (0.356, 0.464)],
# ]
# tree_3 = [
#     [(0.489, 0.0486), (0.25, 0.452), (0.732, 0.452)],
#     [(0.5, 0.824), (0.25, 0.452), (0.732, 0.452)],
#     [(0.5, 0.824), (0.09, 0.7), (0.25, 0.452)],
#     [(0.5, 0.824), (0.922, 0.7), (0.732, 0.452)],
# ]


# def test():
#     e_l = list()
#     for i in range(1, 10000):
#         # p = generate_point_inside_triangle_with_distance(i, 0.3, e_l)
#         p = generate_point_inside_triangle_with_distance(i, 1500, e_l)
#         # print(p)
#         if p == (0.9, 0.9):
#             print(i)
#             if i > 115:
#                 print(e_l)
#             break
#         else:
#             e_l.append(p)


# test()
# for _ in range(100):
#     test()


def load_profanity_list():
    with open(f"{os.getcwd()}/utils/korean-bad-words.md", "r", encoding="utf-8") as file:
        profanity_list = [line.strip() for line in file]
    return list(dict.fromkeys(profanity_list))
