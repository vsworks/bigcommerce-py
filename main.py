from config import settings
from bigcommerce.api import BigCommerceApi

bc_api = BigCommerceApi(
    path=f"https://api.bigcommerce.com/stores/{settings.bc_store.hash}/v3/catalog",
    client_id=settings.bc_store.client_id,
    access_token=settings.bc_store.access_token,
)
print(bc_api.get("products", params={'sku': "KLN AGENT-M3"}))
