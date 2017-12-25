class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


class stu():
    pass


stu.name = 'yefan'

print(stu.name)


#  创建实例的时候，把一些我们认为必须绑定的属性强制填写进去,通过定义一个特殊的__init__方法

class stu1(object):

    def __init__(self, name, score):  # self参数表示实例本身
        self.name = name
        self.score = score


yefan = stu1('yefan1', 88)
print(yefan.name)
print(yefan.score)

