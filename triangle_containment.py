"""
https://projecteuler.net/problem=102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt, a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""


def sign(p0, p1, p2):
    return (p0[0] - p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p0[1] - p2[1])


def contains_origin(triangle):
    """
    Does a triangle contain origin?
    :param triangle: (a,b,c)
    :return: True iff it contains origin
    """
    a, b, c = triangle
    o = (0, 0)
    sign1 = sign(o, a, b) < 0
    sign2 = sign(o, b, c) < 0
    sign3 = sign(o, c, a) < 0
    return sign1 == sign2 == sign3


def solution():
    """
    Solve the problem
    :return: number of triangles containing origin
    """
    triangles_data = open('resources\p102_triangles.txt', 'r').readlines()
    triangles = 0

    for row in triangles_data:
        r = map(lambda x: int(x), row.split(','))
        a, b, c = r[:2], r[2:4], r[4:]
        if contains_origin((a, b, c)):
            triangles += 1

    return triangles

import cProfile

cProfile.run('solution()', sort='cumtime')
