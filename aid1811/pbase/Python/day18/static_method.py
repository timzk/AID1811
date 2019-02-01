#静态方法@staticmethod
class A:
    @staticmethod
    def myadd(a,b):
        return a+b

print(A.myadd(100,200))  #打印300
print(A.myadd("ABC","123"))  #打印ABC123