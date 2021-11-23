from dataclasses import dataclass


@dataclass
class Instruction:
    """Stores a single instruction for the handheld console."""
    operation: str
    argument: int

    def get(self):
        """Returns the instruction as a tuple."""
        return self.operation, self.argument


class Computer:
    """Creates a computer object that runs the handheld's boot code."""
    def __init__(self):
        self.accumulator = 0
        self.program_counter = 0
        self.program = []
        self.instruction_register = None
        self.halt = False

    def print_state(self):
        """Prints the current computer state."""
        print(f"{self.program_counter = }\n{self.accumulator = }")

    def load_program(self, program):
        """Loads a program into the computer"""
        self.program = program
        print("Program loaded.")

    def fetch(self):
        """Fetches the next instruction pointed to by program_counter."""
        try:
            if not self.halt:
                self.instruction_register = self.program[self.program_counter]
        except IndexError:
            self.instruction_register = Instruction('hlt', -1)

    def execute(self):
        """Executes the instruction in the instruction register."""
        try:
            opcode, argument = self.instruction_register.get()

            if opcode == 'acc':
                self.accumulator += argument
                self.program_counter += 1
            elif opcode == 'jmp':
                self.program_counter += argument
            elif opcode == 'nop':
                self.program_counter += 1
            elif opcode == 'hlt':
                self.halt = True
                print("Program halted.")
            else:
                raise ValueError
        except ValueError:
            print("Invalid opcode")
            raise

    def run_program(self, step=False):
        """Runs the program starting from the current state.
        Can set step to True to execute a single instruction
        """
        while not self.halt:
            self.fetch()
            self.execute()
            if step:
                # self.print_state()  # debug
                return

        print("Final State:")
        self.print_state()

    def reset(self):
        "Resets the computer to the initial state."
        self.accumulator = 0
        self.program_counter = 0
        self.halt = False


def parse_input():
    """Reads the input and parses into a program/list of Instructions."""
    with open('input.txt') as file:
        program = [Instruction(operation, int(argument)) for operation, argument in
                   (line.strip().split(' ') for line in file)]

    # print(f"{program = }")  # debug
    return program


def run(computer):
    """Runs the program on the passed computer and prints the answers to the puzzle."""
    repetitions = set()

    while True:
        computer.run_program(step=True)

        if computer.halt:
            print("\nHalt final accumulator value:", computer.accumulator)
            break
        if computer.program_counter in repetitions:
            print("\nRepetition Final accumulator value:", computer.accumulator)
            break
        else:
            repetitions.add(computer.program_counter)

        # input()

    return computer


def main():
    computer = Computer()

    program = parse_input()
    computer.load_program(program)

    computer = run(computer)
    computer.reset()

    for index, instruction in enumerate(program):
        if instruction.operation == 'jmp':
            computer.program[index].operation = 'nop'

            computer = run(computer)
            if computer.halt:
                break

            computer.reset()
            computer.program[index].operation = 'jmp'

        elif instruction.operation == 'nop':
            computer.program[index].operation = 'jmp'

            computer = run(computer)
            if computer.halt:
                break

            computer.reset()
            computer.program[index].operation = 'nop'


if __name__ == '__main__':
    main()
