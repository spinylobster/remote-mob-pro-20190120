class VersionNumber:
    def __init__(self, value: int):
        if (not isinstance(value, int)):
            raise ValueError("入力できる値は整数型の数値であること")
        if (value < 0):
            raise ValueError("数値は０以上であること")

        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class SemVer:
    def __init__(self, major: VersionNumber, minor: VersionNumber, patch: VersionNumber):
        if (not isinstance(major, VersionNumber)):
            raise ValueError("入力できる値は整数型の数値であること")
        if (not isinstance(minor, VersionNumber)):
            raise ValueError("入力できる値は整数型の数値であること")
        if (not isinstance(patch, VersionNumber)):
            raise ValueError("入力できる値は整数型の数値であること")

        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return ('%s.%s.%s' % (self.major, self.minor, self.patch))

    def __eq__(self, other):
        return self.major == other.major \
            and self.minor == other.minor \
            and self.patch == other.patch

    @classmethod
    def generate(cls, major: int, minor: int, patch: int):
        return SemVer(VersionNumber(major), VersionNumber(minor), VersionNumber(patch))
