def plusOne(self, digits: List[int]) -> List[int]:
    return str(int("".join(list(map(str, digits)))) + 1) 