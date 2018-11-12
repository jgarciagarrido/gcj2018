
def calculate_damage(program):
    beam_strength = 1
    damage = 0
    for instruction in program:
        if instruction == "C":
            beam_strength *= 2
        if instruction == "S":
            damage += beam_strength
    return damage


def hack(program):
    for i in xrange(len(program)-2, -1, -1):
        if program[i:i+2] == "CS":
            return program[:i] + "SC" + program[i+2:]
    return program


def min_hacks(damage, program):
    hacks = 0
    current_damage = calculate_damage(program)
    while current_damage > damage:
        hacked_program = hack(program)
        hacked_damage = calculate_damage(hacked_program)
        hacks += 1
        if hacked_damage == current_damage:
            return "IMPOSSIBLE"
        current_damage = hacked_damage
        program = hacked_program
    return hacks


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        line = raw_input().split(" ")
        total_damage_allowed = int(line[0])
        program = line[1]
        print "Case #{}: {}".format(
            i,
            min_hacks(total_damage_allowed, program))
