import unittest

from palindrome import algorithms

strings = ['cjlkpttezjbwcxevjrdggylnmwsyqimgbjdwggvjpgnwiirvztoxqnoiwnivnabamqkptwgfgintlptsbavhcphziikc', 
          '', 
          'yrjpurgpscwgpprwgnuyfptqedaxiqhlruvkllkvurlhqixadeqtpfyungwrppgwcspgrupjry', 
          'jmarkblerochxyywfbuazhkvgjhafttmrxjtdnllmcyjumaywqeutzcxpirz', 
          'tmnfligugeoeotezrznqiriyrqetrfsnsfgzbbzgfsnsfrteqryiriqnzrzetoeoegugilfnmt', 
          'hhiitcktucncxzeugwtjksrstojlgfssiqaptxuwpllmpriqrf', 
          'qyoflvimiwjieslqtbvzokfhzyphjgrippyvprofssforpvyppirgjhpyzhfkozvbtqlseijwimivlfoyq', 
          'aca', 
          'qekxaktmdykfbbtyoehxawbwrktncso', 
          'eyyfkvgwvavulddhcauwfrchu', 'a', 
          'bdnoiwflhhimagtwnpcwfxmrjcfucpwwxqsnkmysyktandiyjyoubogyocrkgcrhzloajyxfsngkfqnmicsyldbsmdp', 
          'twccmcjauujmpjjtgwcavpvnztddtznvpvacwgtjjpmjuuajcmccwt', 
          'kmqcxcaxwhwmfntctrmisqjsjjlmjckmputd', 
          'nochjsddlfrbmswkjqrubbbjvtbkojprmgavjbs', 
          'aaaaaaaaaaaaaaa', 
          'aikfmmfkia', 
          'wtohnkjxlcvsrkyeowno', 
          'aaaaccccaaaa', 
          'wdffztprqeplxhwyfwvabillsweaidjvvjdiaewsllibavwfywhxlpeqrptzffdw']

expected = [False, True, True, False, True, False, True, True, False, False, True, False, True, False, False, 
            True, True, False, True, True]

class AlgorithmsTests(unittest.TestCase):
    def test_two_pointers(self):
        for i in range(len(strings)):
            string = strings[i]
            answer = algorithms.two_pointers(string)
            self.assertEqual(answer, expected[i])

    def test_reverse_string(self):
        for i in range(len(strings)):
            string = strings[i]
            answer = algorithms.reverse_string(string)
            self.assertEqual(answer, expected[i])

    def test_recursive(self):
        for i in range(len(strings)):
            string = strings[i]
            answer = algorithms.recursive(string)
            self.assertEqual(answer, expected[i])

    def test_stack(self):
        for i in range(len(strings)):
            string = strings[i]
            answer = algorithms.stack(string)
            self.assertEqual(answer, expected[i])

if __name__ == "__main__":
    unittest.main()
