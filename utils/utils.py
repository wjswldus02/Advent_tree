import random


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


def generate_point_inside_triangle(triangle_vertices):
    # 삼각형의 꼭지점 좌표
    a, b, c = triangle_vertices
    
    # 삼각형 내부의 점 생성
    while True:
        x = random.uniform(min(a[0], b[0], c[0]), max(a[0], b[0], c[0]))
        y = random.uniform(min(a[1], b[1], c[1]), max(a[1], b[1], c[1]))
        
        if is_point_inside_triangle((x, y), a, b, c):
            return x, y

# 삼각형의 세 꼭지점 좌표
triangle_vertices = [(0, 0), (10, 100), (20, 0)]

# 삼각형 내부의 랜덤 점 생성
random_point_inside_triangle = generate_point_inside_triangle(triangle_vertices)

print(f"삼각형 내부의 랜덤 점: {random_point_inside_triangle}")
