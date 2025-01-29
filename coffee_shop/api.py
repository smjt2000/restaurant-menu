from ninja import NinjaAPI, Schema, FilterSchema, Field, Query
from shop.models import  MenuItem
from typing import Optional, List

api = NinjaAPI()

class CategorySchema(Schema):
    id: int
    title: str
    status: bool
    description: str


class MenuItemSchema(Schema):
    id: int
    title: str
    thumbnail: str
    persian_digit_price: str
    description: str
    status: bool
    categories: CategorySchema


class MenuItemFilterByCatSchema(FilterSchema):
    search: Optional[str] = Field(None, q=['categories__id'])


class MenuItemFilterSchema(FilterSchema):
    fltr: Optional[str] = None


class MenuItemGetBySlugSchema(FilterSchema):
    id: Optional[int] = None


@api.get('/item', response=MenuItemSchema)
def item_detail(request, filters: MenuItemGetBySlugSchema = Query(...)):
    items = MenuItem.objects.active()
    if filters.id:
        return items.get(id=filters.id)

@api.get('/filter', response=List[MenuItemSchema])
def menu_items(request, filters: MenuItemFilterSchema = Query(...)):
    items = MenuItem.objects.active()
    match filters.fltr:
        case '-price':
            return items.order_by('-price')
        case '+price':
            return items.order_by('price')
        case '_all':
            return items
    return items

@api.get('/category', response=List[MenuItemSchema])
def category_items(request, filters:MenuItemFilterByCatSchema = Query(...)):
    items = MenuItem.objects.all().select_related('categories')
    if filters.search != '_all':
        items = filters.filter(items)
    return items



# from ninja import Form, File
# from ninja.files import UploadedFile

# class Error(Schema):
#     message: str

# class HelloSchema(Schema):
#     name: str = "world"

# class UserSchema(Schema):
#     username: str
#     is_authenticated: bool
#     email: str
#     first_name: str = None

# class CategoryFilter(FilterSchema):
#     search : Optional[str] = Field(None, q=['title__icontains', 'slug__icontains'])
#     # title: Optional[str] = None

# @api.get('/cats', response = list[CategoryIn])
# def cat(request, filters: CategoryFilter = Query(...)):
#     cats = Category.objects.all()
#     cats = filters.filter(cats)
#     return list(cats)

# class CategoryIn(Schema):
#     title: str
#     slug: str
#     description: str

# @api.post('/add/cat')
# def create_category(request, payload: CategoryIn):
#     cat = Category.objects.create(**payload.dict())
#     return {"id": cat.id}

# @api.post('/add/cat2')
# def add_cat(request, cat: Form[CategoryIn]):
#     return cat

# @api.get('/me', response={200: UserSchema, 403: Error})
# def me(request):
#     if not request.user.is_authenticated:
#         return 403, {"message": "please sign-in first"}
#     return request.user

# @api.post('/hello')
# def hello(request, data: HelloSchema):
#     return f"Hello {data.name}!"

# @api.get('/add')
# def add(request, a:int, b:int):
#     return f"{a} + {b} = {a+b}"

# @api.get('/add/{a}and{b}')
# def add_url(request, a:int, b:int):
#     return f"{a} + {b} = {a+b}"