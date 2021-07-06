import sys
class Human:    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __eq__(self, object):
        return self.name == object.name
    def __add__(self, object):
        if isinstance(object, Human):
            return self.age + object.age
        else:
            return self.age + object
    def __str__(self):
        return self.sex

if __name__ == "__main__":
    a = sys.stdin.readline().split()
    A = Human(a[0], int(a[1]), a[2])
    a = sys.stdin.readline().split()
    B = Human(a[0], int(a[1]), a[2])
    a = sys.stdin.readline().split()
    C = Human(a[0], int(a[1]), a[2])

    if A == B and B == C:
        print("같은 이름")
    else:
        print("다른 이름")
    print("나이의 합 :", A+(B+C))
    print("{}의 성별 : {}".format(A.name, A))
    print("{}의 성별 : {}".format(B.name, B))
    print("{}의 성별 : {}".format(C.name, C))