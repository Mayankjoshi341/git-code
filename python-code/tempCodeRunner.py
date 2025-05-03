
dis = steps_per_day = {
    1: 1000,
    2: 1100,
    3: 1200,
    4: 1300,
    5: 1400,
    6: 1500,
    7: 1600,
    8: 1700,
    9: 1800,
    10: 1900,
    11: 2000,
    12: 2100,
    13: 2200,
    14: 2300,
    15: 2400,
    16: 2500,
    17: 2600,
    18: 2700,
    19: 2800,
    20: 2900,
    21: 3000,
    22: 3100,
    23: 3200,
    24: 3300,
    25: 3400,
    26: 3500,
    27: 3600,
    28: 3700,
    29: 3800,
    30: 3900
}

def main ():
    total_steps = 0
    for day, steps in dis.items():
        total_steps += steps
    average_steps = total_steps / len(dis)
    print(f"Total steps: {total_steps}")
    print(f"Average steps: {average_steps}")
    reward = 0
    for steps in steps_per_day.values():
        if steps > 1000:
            reward += 1
        else :
            return
    print(f"Total reward: {reward}")


main()
