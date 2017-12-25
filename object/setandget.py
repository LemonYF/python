#  访问限制  private私有变量和set get 方法


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):  #  定义set
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_score(self):  #  定义get
        return self.__score


stu1 = Student('yefan', 88)
stu1.print_score()
stu1.set_score(80)
stu1.print_score()
print(stu1.get_score())



