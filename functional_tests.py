import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        assert 'To-Do' in self.browser.title, "Browser title was " + self.browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # TODO: She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # TODO: She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # TODO: When she hits enter, the page updates, and now the page lists "1: Buy peacock feathers" as an item in a to-do list"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # TODO: There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        #  (Edith is very methodical)
        # TODO: The page updates again, and now shows both items on her list
        self.fail('Finish the test!')

        # TODO: Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL
        #  for her -- there is some explanatory text to that effect.

        # TODO: She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings='ignore')