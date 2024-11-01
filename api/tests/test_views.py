from builtins import len
from rest_framework.test import APITestCase
from rest_framework import status
from api.models.category import Category
from api.models.company import Company
from django.urls import reverse


class CategoryViewTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name="test company")
        self.category = Category.objects.create(
            company=self.company,
            name="test category"
        )
        self.list_url = reverse('category-list')
        self.detail_url = reverse('category-detail', kwargs={'pk': self.category.id})

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(f"{self.list_url}?company_id={self.company.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "test category")

    def test_create(self):
        data = {
            'company': self.company.id,
            'name': "new category"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

        # 중복 이름 테스트
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        data = {
            'company': self.company.id,
            'name': "modified category"
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "modified category")

        patch_data = {'name': "patched category"}
        response = self.client.patch(self.detail_url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "patched category")

    def test_destroy(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
