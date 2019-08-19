# -*- coding:utf-8 -*-

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    def setUp(self, timeout=3):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        time.sleep(2)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def input_a_new_item(self, browser, item_string):
        input_box = browser.find_element_by_id('id_new_item')
        input_box.send_keys(item_string)
        input_box.send_keys(Keys.ENTER)
        time.sleep(5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # She checks out the homepage
        self.browser.get(self.live_server_url)

        # She notices he page title and header mention to-do lists

        # instead of the following code
        # assert 'To-do' in browser.title, 'Browser title was ' + browser.title
        self.assertIn('To-Do', self.browser.title, msg=self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Is invitied to enter a to-do item straight away
        self.input_a_new_item(self.browser, 'Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item.
        # Enters "Use peacock feathers to make a fly"
        self.input_a_new_item(self.browser, 'Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.browser.quit()

        # new user signed in
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text

        ## can the new browser access previous user's contents?
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        self.input_a_new_item(self.browser, 'Buy Milk')
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertEqual(edith_list_url, francis_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        self.fail('Finish the test!')


