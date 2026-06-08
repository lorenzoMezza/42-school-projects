import math


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "

    while True:
        raw_coordinates = input(prompt)

        try:
            x_text, y_text, z_text = raw_coordinates.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_text.strip())
            y = float(y_text.strip())
            z = float(z_text.strip())
        except ValueError as error:
            bad_parameter = str(error).split("'")[1]
            print(f"Error on parameter '{bad_parameter}': {error}")
            continue

        return (x, y, z)


def distance_between(
    first: tuple[float, float, float],
    second: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    first_pos = get_player_pos()

    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, "
        f"Y={first_pos[1]}, Z={first_pos[2]}"
    )

    center = (0.0, 0.0, 0.0)

    distance_to_center = round(
        distance_between(first_pos, center),
        4
    )

    print(f"Distance to center: {distance_to_center}")

    print("Get a second set of coordinates")

    second_pos = get_player_pos()

    distance = round(
        distance_between(first_pos, second_pos),
        4
    )

    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance}"
    )


if __name__ == "__main__":
    main()
