from math import sqrt, gcd


class Field:

    def __init__(self, dimensions, you, trainer, distance):
        self.dimensions = dimensions
        self.you = you
        self.trainer = trainer
        self.distance = distance

    def shot(self, dx, dy):
        X = 0; Y = 1
        x, y = self.you
        x += dx; y += dy
        count = 1

        while sqrt((dx * dx + dy * dy) * count * count) <= self.distance:
            while x < 0 or x > self.dimensions[X]:
                if x > self.dimensions[X]:
                    x = 2 * self.dimensions[X] - x
                    dx *= -1
                if x < 0:
                    x *= -1; dx *= -1
            while y < 0 or y > self.dimensions[Y]:
                if y > self.dimensions[Y]:
                    y = 2 * self.dimensions[Y] - y
                    dy *= -1
                if y < 0:
                    y *= -1; dy *= -1

            if x == self.you[X] and y == self.you[Y]:
                return False
            if x == self.trainer[X] and y == self.trainer[Y]:
                return True

            count += 1
            x += dx; y += dy

        return False


def solution(dimensions, your_position, trainer_position, distance):
    #Your code here

    field = Field(dimensions, your_position, trainer_position, float(distance))

    result = field.shot(1, 0) + field.shot(-1, 0) + field.shot(0, 1) \
        + field.shot(0, -1) + field.shot(1, 1) + field.shot(-1, 1) \
        + field.shot(1, -1) + field.shot(-1, -1)

    for i in range(1, distance):
        for j in range(1, distance):
            if gcd(i, j) == 1:
                if sqrt(i * i + j * j) > distance:
                    break
                result += field.shot(i, j) + field.shot(-i, j) \
                     + field.shot(i, -j) + field.shot(-i ,-j)

    return result


if __name__ == "__main__":
    print(solution([3,2], [1,1], [2,1], 4))
    print(solution([300,275], [150,150], [185,100], 500))
