from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_lsit_and_retrieve_it_later(self):

        assert 'To-Do' in self.browser.title, "Browser title was " + self.browser.title

        # TODO: She is invited to enter a to-do item straight away

        # TODO: She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)

        # TODO: When she hits enter, the page updates, and now the page lists "1: Buy peacock feathers" as an item in a to-do list"

        # TODO: There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        #  (Edith is very methodical)

        # TODO: The page updates again, and now shows both items on her list

        # TODO: Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL
        #  for her -- there is some explanatory text to that effect.

        # TODO: She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings='ignore')