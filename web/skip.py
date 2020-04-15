import unittest

class Skip(unittest.TestCase):

    # @unittest.skip("理由就是不想运行")
    def test_1(self):
        print('1')
    # @unittest.skipIf( 1 < 2,'这就是if的条件')
    def test_2(self):
        print('2')
    # @unittest.skipUnless(1 > 2,"除非的条件")
    def test_3(self):
        print('3')
    # @unittest.expectedFailure  # 如果用例执行失败，不计入失败的case中
    def test_4(self):
        print('4')
    def test_5(self):
        print('5')
#
# if __name__ == '__main__':
#     unittest.main()
