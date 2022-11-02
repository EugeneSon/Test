class Singleton:
    """
    하나의 싱글톤 인스턴스를 생성
    이미 생성된 인스턴스가 있다면 재사용
    """

    def __new__(self):
        print('new')
        if not hasattr(self, 'instance'):
            self.instance = super(Singleton, self).__new__(self)
        return self.instance

    def __init__(self):
        print('init')


if __name__ == '__main__':
    s = Singleton()
    print("객체 생성", s)
    s1 = Singleton()
    print("객체 생성", s1)