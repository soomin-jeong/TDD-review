import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_test: str) -> None:
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"New to-do item did not appear in table. Contents were:\n{table.text}"
        )

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(url='http://127.0.0.1:8000/')

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
        time.sleep(1)

        # TODO: When she hits enter, the page updates, and now the page lists "1: Buy peacock feathers" as an item in a to-do list"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # TODO: There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
        #  (Edith is very methodical)
        # TODO: The page updates again, and now shows both items on her list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        self.fail('Finish the test!')


        # TODO: Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL
        #  for her -- there is some explanatory text to that effect.

        # TODO: She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings='ignore')