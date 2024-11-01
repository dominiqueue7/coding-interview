from rest_framework import viewsets
from api.models.category import Category
from api.serializers.category import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = Category.objects.all()

        if company_id:
            queryset = queryset.filter(company_id=company_id)

        return queryset