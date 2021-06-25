from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.test import TestCase
from django.contrib import auth
from accounts.models import Token

User = auth.get_user_model()


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

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()
        List.create_new(first_item_text='new item text', owner=user)
        new_list = List.objects.first()
        self.assertEqual(new_list.owner, user)


class NewListTest(TestCase):
    ITEM_TEXT = 'A new list item'

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'text': self.ITEM_TEXT})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, self.ITEM_TEXT)

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'text': self.ITEM_TEXT})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')


class UserModelTest(TestCase):
    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email='edith@example.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user)  # should not raise


class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

    def test_create_new_creates_list_and_first_item(self):
        List.create_new(first_item_text='new item text')
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'new item text')
        new_list = List.objects.first()
        self.assertEqual(new_item.list, new_list)

    def test_lists_can_have_owners(self):
        List(owner=User())  # should not raise

    def test_list_owner_is_optional(self):
        List().full_clean()  # should not raise

    def test_create_returns_new_list_object(self):
        returned = List.create_new(first_item_text='new item text')
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)

    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='first item')
        Item.objects.create(list=list_, text='second item')
        self.assertEqual(list_.name, 'first item')



