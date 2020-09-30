# zhou

cat = """
/\___/\\
(=^o^=)
(") (")__/
"""

def solution():
    n = int(input())
    cat1 = "/\___/\\    " * n + "\n"
    cat2 = "(=^o^=)    " * n + "\n"
    cat3 = '(") (")__/ ' * n
    print(cat1+cat2+cat3)


if __name__ == "__main__":
    solution()
