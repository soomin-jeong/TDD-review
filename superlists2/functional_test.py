# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        self.browser.implicitly_wait(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
            # She checks out the homepage
            self.browser.get(url='http://localhost:8000')

            # She notices he page title and header mention to-do lists

            # instead of the following code
            # assert 'To-do' in browser.title, 'Browser title was ' + browser.title
            self.assertIn('To-Do', self.browser.title, msg=self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            # Is invitied to enter a to-do item straight away
            input_box = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

            # Types "Buy peacock feathers" into a text box
            input_box.send_keys('Buy peacock feathers')
            # When hits enter, the page updates and now the page lists  "1: Buy peacock feathers"
            input_box.send_keys(Keys.ENTER)

            # There is still a text box inviting her to add another item.
            # Enters "Use peacock feathers to make a fly"
            self.browser.implicitly_wait(10)
            input_box = self.browser.find_element_by_id('id_new_item')
            input_box.send_keys('Use peacock feathers to make a fly')
            input_box.send_keys(Keys.ENTER)

            self.check_for_row_in_list_table('1: Buy peacock feathers')
            self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

            # The page updates again and now shows both items on her list

            # The site generates a unique URL for her (with explanatory text to the effect"

            # Visits the URL (with the to-do list)

            # Is Satisfied

            self.fail('Finish the test!')

    # finally:
        #     browser.close()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

