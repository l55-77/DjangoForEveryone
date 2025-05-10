from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """测试 1 + 1 是否等于 2"""
        self.assertEqual(1 + 1, 2)