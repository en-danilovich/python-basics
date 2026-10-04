# Time: O(n), Space: O(n) - list of letters plus its reversed copy
def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalpha()]
    return cleaned == cleaned[::-1]

# Time: O(n), Space: O(k) - dict of counts, k = number of distinct chars
def is_anagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    counts: dict[str, int] = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True

# Time: O(n) - two passes, Space: O(k) - dict of counts
def first_unique_char(s: str | None) -> int:
    if not s:
        return -1
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

# Time: O(n), Space: O(n) - split() builds a list of words
def count_words(s: str | None) -> int:
    return len(s.split()) if s else 0

# Time: O(n), Space: O(n) - list of words plus the result string
def reverse_words(s: str | None) -> str:
    return ' '.join(reversed(s.split())) if s else ""

# Time: O(n), Space: O(k) - dict of unique chars (plus the result string)
def remove_duplicates(s: str | None) -> str:
    return ''.join(dict.fromkeys(s)) if s else ""

# Time: O(n) - single pass, Space: O(k) - dict of counts
def most_frequent_char(s: str | None) -> str | None:
    if not s:
        return None
    counts: dict[str, int] = {}
    best_char, best_count = None, 0
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
        if counts[ch] > best_count:
            best_char, best_count = ch, counts[ch]
    return best_char

# Time: O(n), Space: O(k) - set of chars with an odd count
def is_palindrome_permutation(s: str | None) -> bool:
    if not s:
        return True
    odd = set()
    for ch in s:
        if ch in odd:
            odd.remove(ch)
        else:
            odd.add(ch)
    return len(odd) <= 1

# Time: O(n + m), Space: O(n + m) - a stack for each string
def backspace_compare(a: str | None, b: str | None) -> bool:
    def build(s: str) -> str:
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return build(a or "") == build(b or "")

# Time: O(n), Space: O(n) - list of parts plus the compressed string
def compress(s: str | None) -> str:
    if not s:
        return ""
    parts = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            parts.append(f"{s[i - 1]}{count}")
            count = 1
    parts.append(f"{s[-1]}{count}")
    compressed = ''.join(parts)
    return compressed if len(compressed) < len(s) else s

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

    # 02: anagram
    cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "a", False),
        ("aab", "abb", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    for a, b, expected in cases:
        assert is_anagram(a, b) is expected, f"expected: {expected}, got: {text}"

    # 03: first unique char
    cases = [
        ("leetcode", 0),
        ("aabb", -1),
        ("loveleetcode", 2),
        ("abcabcd", 6),
        ("a", 0),
        ("aa", -1),
        ("", -1),
        (None, -1),
    ]
    for text, expected in cases:
        assert first_unique_char(text) == expected, f"expected: {expected}, got: {first_unique_char(text)} for {text!r}"

    # 04: count words
    cases = [
        ("  Hello world  ", 2),
        ("one", 1),
        ("a  b   c", 3),
        ("   leading", 1),
        ("trailing   ", 1),
        ("   ", 0),
        ("", 0),
        (None, 0),
    ]
    for text, expected in cases:
        assert count_words(text) == expected, f"expected: {expected}, got: {count_words(text)} for {text!r}"

    # 05: reverse words
    cases = [
        ("  the sky is blue  ", "blue is sky the"),
        ("hello world", "world hello"),
        ("a  b", "b a"),
        ("a", "a"),
        ("   ", ""),
        ("", ""),
        (None, ""),
    ]
    for text, expected in cases:
        assert reverse_words(text) == expected, f"expected: {expected!r}, got: {reverse_words(text)!r} for {text!r}"

    # 06: remove duplicates
    cases = [
        ("banana", "ban"),
        ("abcabc", "abc"),
        ("abc", "abc"),
        ("aaaa", "a"),
        ("aAa", "aA"),
        ("a", "a"),
        ("", ""),
        (None, ""),
    ]
    for text, expected in cases:
        assert remove_duplicates(text) == expected, f"expected: {expected!r}, got: {remove_duplicates(text)!r} for {text!r}"

    # 07: most frequent char (ties may return any of the tied chars)
    cases = [
        ("abcccccddee", {'c'}),
        ("abcabca", {'a'}),
        ("aabb", {'a', 'b'}),
        ("abc", {'a', 'b', 'c'}),
        ("a", {'a'}),
        ("", {None}),
        (None, {None}),
    ]
    for text, allowed in cases:
        assert most_frequent_char(text) in allowed, f"expected one of: {allowed}, got: {most_frequent_char(text)!r} for {text!r}"

    # 08: palindrome permutation
    cases = [
        ("civic", True),
        ("ivicc", True),
        ("hello", False),
        ("aabb", True),
        ("aab", True),
        ("abc", False),
        ("ab", False),
        ("Aa", False),
        ("a", True),
        ("", True),
        (None, True),
    ]
    for text, expected in cases:
        assert is_palindrome_permutation(text) is expected, f"expected: {expected}, got: {text!r}"

    # 09: backspace compare
    cases = [
        ("ab#c", "ad#c", True),
        ("a#c", "b", False),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#b", "b", True),
        ("abc", "ab#c", False),
        ("#", "", True),
        ("a", "a", True),
        ("", "", True),
        (None, "", True),
        (None, "a", False),
    ]
    for a, b, expected in cases:
        assert backspace_compare(a, b) is expected, f"expected: {expected}, got: {a!r}, {b!r}"

    # 10: string compression
    cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abc", "abc"),
        ("aa", "aa"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("aaaaaaaaaaaa", "a12"),
        ("a", "a"),
        ("", ""),
        (None, ""),
    ]
    for text, expected in cases:
        assert compress(text) == expected, f"expected: {expected!r}, got: {compress(text)!r} for {text!r}"

    print("OK")
