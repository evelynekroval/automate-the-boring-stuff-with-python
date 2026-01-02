message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count: dict[str, int] = {} # mypy: ignore-errors; type: ignore

for character in message.lower():
    count.setdefault(character, 0)
    count[character] += 1

print(count)   