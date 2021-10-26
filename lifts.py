import random


def find_closest_lift():
    lifts_on_floors = [int(i.replace('D', '').replace('U', '')) for i in initial_lift_positions]
    closest_list_on_floor = min(lifts_on_floors,
                                key=lambda i: abs(i - int(user_on_floor.replace('D', '').replace('U', ''))))
    return lifts_on_floors.index(closest_list_on_floor) + 1


if __name__ == '__main__':
    no_of_floors = 20
    lift_directions = ['U', 'D']
    no_of_lifts = 5
    initial_lift_positions = ["{}{}".format(random.randint(0, no_of_floors), random.choice(lift_directions)) for i in
                              range(0, no_of_lifts)]
    print(initial_lift_positions)
    user_on_floor = input("Enter a request? ")
    print("Lift #{} will be coming up to receive you.".format({find_closest_lift()}))
