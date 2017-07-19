import unittest
from operations import CountNumberOfElements

class DomBuilderMock():
    lastSuscribeCall = None
    def subscribe(self, *args):
        self.lastSuscribeCall = args

class CountNumberOfElementsTest(unittest.TestCase):
    def setUp(self):
        self.instance = CountNumberOfElements()

    def test_resultIsCorrect(self):
        testDom = [('body', None), ('div', 0), ('p', 1), ('p', 1)] 
        self.instance.attachTo(testDom)

        self.assertEqual(4, self.instance.getResults())

        testDom = [] 
        self.instance.attachTo(testDom)

        self.assertEqual(0, self.instance.getResults())

        testDom = [('body', None)] 
        self.instance.attachTo(testDom)

        self.assertEqual(1, self.instance.getResults())
        
if __name__ == "__main__":
    unittest.main()
