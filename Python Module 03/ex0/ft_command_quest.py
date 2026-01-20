import sys


def command_quest() -> None:
    print("=== Command Quest ===")

    total_args = len(sys.argv)
    program_name = sys.argv[0]

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    print(f"Program name: {program_name}")
    arg_count = total_args - 1
    print(f"Arguments received: {arg_count}")

    i = 1
    while i < total_args:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest()
