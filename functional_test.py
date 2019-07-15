# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
            # She checks out the homepage
            self.browser.get(url='http://localhost:8000')

            # She notices he page title and header mention to-do lists

            # instead of the following code
            # assert 'To-do' in browser.title, 'Browser title was ' + browser.title

            self.assertIn('To-Do', self.browser.title)
            self.fail('Finish the test!')

            # Is invitied to enter a to-do item straight away

            # Types "Buy peacock feathers" into a text box

            # When hits enter, the page updates and now the page lists  "1: Buy peacock feathers"

            # There is still a text box inviting her to add another item.
            # Enters "Use peacock feathers to make a fly"

            # The page updates again and now shows both items on her list

            # The site generates a unique URL for her (with explanatory text to the effect"

            # Visits the URL (with the to-do list)

            # Is Satisfied

        # finally:
        #     browser.close()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

