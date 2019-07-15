# -*- coding:utf-8 -*-

from selenium import webdriver

browser = webdriver.Firefox()

try:
    # She checks out the homepage
    browser.get(url='http://localhost:8000')

    # She notices he page title and header mention to-do lists
    assert 'To-do' in browser.title, 'Browser title was ' + browser.title

    # Is invitied to enter a to-do item straight away

    # Types "Buy peacock feathers" into a text box

    # When hits enter, the page updates and now the page lists  "1: Buy peacock feathers"

    # There is still a text box inviting her to add another item.
    # Enters "Use peacock feathers to make a fly"

    # The page updates again and now shows both items on her list

    # The site generates a unique URL for her (with explanatory text to the effect"

    # Visits the URL (with the to-do list)

    # Is Satisfied

finally:
    browser.close()
