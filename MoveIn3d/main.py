def make_step(position, orientation, step):
    if step == 'F':
        # move ahead of you
        position[abs(orientation[0])-1] += 1 if orientation[0] > 0 else -1
    elif step == 'R':
        # turn right
        # front -> -left, left -> front
        orientation[0], orientation[2] = -orientation[2], orientation[0]
    elif step == 'L':
        # turn left
        # front -> left, left -> -front
        orientation[0], orientation[2] = orientation[2], -orientation[0]
    elif step == "U":
        # turn up so your front would be previous up
        # front -> up, up -> -front
        orientation[0], orientation[1] = orientation[1], -orientation[0]
    elif step == "D":
        # turn down so your front would be previous down
        # front -> -up, up -> front
        orientation[0], orientation[1] = -orientation[1], orientation[0]
    elif step == "<":
        # turn on your left side so your up would be previous left
        # up -> left, left -> -up
        orientation[1], orientation[2] = orientation[2], -orientation[1]
    elif step == ">":
        # turn on your right side so your up would be previous right
        # up -> -left, left -> up
        orientation[1], orientation[2] = -orientation[2], orientation[1]
    else:
        raise Exception(f"Unknown step '{step}'")


def run():
    lines = [x.strip() for x in open('test.txt', 'r').readlines()]
    for line in lines:
        print('---> start at [0,0,0] <---')
        steps = [x for x in line]
        position = [0, 0, 0]  # where you stand
        orientation = [1, 2, 3]  # [front-axis, up-axis, left-axis] where 1..x, 2..y, 3..z, -1..-x, -2..-y, -3..-z
        for step in steps:
            make_step(position, orientation, step)
            print(step, '->', position, orientation)

    print('Finished.')


if __name__ == '__main__':
    run()
