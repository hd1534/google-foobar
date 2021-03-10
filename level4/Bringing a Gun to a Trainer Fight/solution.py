import math

X = 0; Y = 1
YOU = 0; TRAINER = 1


def mirrorMap(target, dimensions, distance):
    " returns target's coordinates in the mirrored map "

    mirrored = [[], []]  # [ X[], Y[] ]

    for i in range(-(distance // dimensions[X]) - 1, (distance // dimensions[X] + 2)):
        mirrored[X].append(getMirror(i, target[X], dimensions[X]))
        
    for i in range(-(distance // dimensions[Y]) - 1, (distance // dimensions[Y] + 2)):
        mirrored[Y].append(getMirror(i, target[Y], dimensions[Y]))

    return mirrored


def getMirror(mirror, coordinates, dimensions):
    " returns coordinates that in the mirror "

    result = coordinates
    mirror_rotation = [2*(dimensions - coordinates), 2*coordinates]
    
    if mirror < 0:
        for i in range(mirror, 0):
            result -= mirror_rotation[i % 2]  # when even -> 2*(dimensions - coordinates)
    else:
        for i in range(mirror):
            result += mirror_rotation[i % 2]  # when even -> 2*(dimensions - coordinates)
     
        #  same as
        # for i in range(1, mirror + 1):
        #     result += mirror_rotation[(i+1) % 2]
    
    return result


def solution(dimensions, your_position, trainer_position, distance):
    " returns number of directions hit the elite trainer "

    mirrored = [
            mirrorMap(your_position, dimensions, distance),    # YOU
            mirrorMap(trainer_position, dimensions, distance)  # TRAINER
        ]
    result = set()
    angles = {}
    
    # mapping YOU
    for x in mirrored[YOU][X]:
        for y in mirrored[YOU][Y]:
            beam = math.atan2((your_position[Y] - y), (your_position[X] - x))
            l = math.sqrt((your_position[X] - x)**2 + (your_position[Y] - y)**2)
            if [x, y] != your_position and l <= distance:
                if(beam not in angles or l < angles[beam]):
                    angles[beam] = l

    # mapping TRAINER
    for x in mirrored[TRAINER][X]:
        for y in mirrored[TRAINER][Y]:
            beam = math.atan2((your_position[Y] - y), (your_position[X] - x))
            l = math.sqrt((your_position[X] - x)**2 + (your_position[Y] - y)**2)
            if [x, y] != your_position and l <= distance:
                if(beam not in angles or l < angles[beam]):
                    angles[beam] = l
                    result.add(beam)

    return len(result)


if __name__ == "__main__":
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
