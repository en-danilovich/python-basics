def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalpha()]
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # 01: palindrom
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (".,!", True),
        ("a", True),
        ("ab", False),
        ("Aa", True),
        ("No 'x' in Nixon", True),
    ]
    for text, expected in cases:
        assert is_palindrome(text) is expected, f"expected: {expected}, got: {text}"

    # 02:

    print("OK")
