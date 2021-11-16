from collections import deque
import itertools


def main():
    with open("input.txt") as file:
        buffer_size = int(file.readline())
        buffer = deque(maxlen=buffer_size)

        for _ in range(buffer_size):
            buffer.append(int(file.readline()))

        while True:
            next_ = int(file.readline())
            if next_ == '':
                raise EOFError

            if next_ in [sum(combo) for combo in itertools.combinations(buffer, 2)]:
                buffer.append(next_)
            else:
                part_1 = next_
                print(f"{part_1 = }")
                break

    with open("input.txt") as file:
        _ = file.readline()
        input_ = [int(line) for line in file]

    for i in range(len(input_)):
        sum_ = input_[i]
        for j in range(i + 1, len(input_)):
            sum_ += input_[j]
            if sum_ == part_1:
                summands = input_[i:j + 1]
                print("part 2 =", min(summands) + max(summands))
                break
        else:
            continue
        break


if __name__ == '__main__':
    main()
