import factory
from .models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product  # ✅ Solo el modelo va en Meta

    name = factory.Faker('company')  # ✅ Esto va fuera de Meta
    price = factory.Faker('random_int', min=200, max=9000)  # ✅ También esto
