from typing import Generator


def numbers_generator(qnt: int) -> Generator[int, int, str]:
    # Generator[yield_type, send_type, return_type]
    result = 0
    while qnt >= 0:

        # yield result as sending
        value = yield result
        # new value for result to be obtained when receiving ("return")
        result = value * qnt
        # decrease counter
        qnt -= 1

    return "Completed"


qnt = 10
multiply_by = 100
random_numbers_generator = numbers_generator(qnt)

# start iteration with next
next(random_numbers_generator)

# now truly counting
n_list = []
while True:
    try:
        n_list.append(random_numbers_generator.send(multiply_by))
    except StopIteration as e:
        # display Completed
        print(e.value)
        break

print(n_list)

# prints from 1000 to 100 as string (decrease based on counting)
