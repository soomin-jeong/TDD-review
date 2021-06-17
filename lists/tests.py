from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'The second list item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'The second list item')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='Itemey 1', list=correct_list)
        Item.objects.create(text='Itemey 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='Other Itemey 1', list=other_list)
        Item.objects.create(text='Other Itemey 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')

        self.assertContains(response, 'Itemey 1')
        self.assertContains(response, 'Itemey 2')
        self.assertNotContains(response, 'Other Itemey 1')
        self.assertNotContains(response, 'Other Itemey 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)


class NewListTest(TestCase):
    ITEM_TEXT = 'A new list item'

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': self.ITEM_TEXT})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, self.ITEM_TEXT)

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': self.ITEM_TEXT})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')


class NewItemTest(TestCase):
    ITEM_TEXT = 'A new item for an existing list'

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': self.ITEM_TEXT}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, self.ITEM_TEXT)
        self.assertEqual(new_item.list, correct_list)

        lists = List.objects.count()
        self.assertEqual(lists, 2)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={'item_text': self.ITEM_TEXT}
        )

        self.assertRedirects(response, f'/lists/{correct_list.id}/')



