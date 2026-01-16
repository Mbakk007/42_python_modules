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

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest()
