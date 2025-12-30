def collatz_function(n: int | None = None) -> list[int]:
    if n is None:
        while True:
            try:
                n = int(input("Enter a positive integer: "))
                break
            except ValueError:
                continue
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    res = collatz_function()
    print(res)

while __name__ =="__main__":
    main()
    
