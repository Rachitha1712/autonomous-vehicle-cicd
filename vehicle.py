def vehicle_decision(distance):

    if distance < 10:
        return "STOPPED"

    elif distance < 30:
        return "SLOW DOWN"

    else:
        return "MOVE FORWARD"


if __name__ == "__main__":

    distance = int(input("Enter obstacle distance: "))

    print(vehicle_decision(distance))