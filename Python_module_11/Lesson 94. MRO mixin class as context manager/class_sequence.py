class X:
    def __init__(self, letter='X'):
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class A(X):
    def __init__(self, letter='A'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class B(X):
    def __init__(self, letter='B'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class C(X):
    def __init__(self, letter='C'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class D(X):
    def __init__(self, letter='D'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class E(A, B):
    def __init__(self, letter='E'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class F(B, C):
    def __init__(self, letter='F'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class G(B, C, D):
    def __init__(self, letter='G'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class H(C, D):
    def __init__(self, letter='H'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class J(E, F):
    def __init__(self, letter='J'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class K(F, G, H):
    def __init__(self, letter='K'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')


class Z(J, K):
    def __init__(self, letter='Z'):
        super().__init__(letter)
        self.letter = letter

    def introduce(self):
        print(f'Hello, I am {self.letter}!')
