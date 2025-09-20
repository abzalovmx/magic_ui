import os
# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_is('Sale')