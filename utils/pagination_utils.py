class PaginationParams:
    def __init__(self, size: int = 10, page: int = 1):
        self.size = size
        self.page = page


def from_response_to_page(page: PaginationParams, items) -> dict:
    return {
        "total": len(items),
        "size": page.size,
        "items": items[(page.page - 1) * page.size : page.page * page.size],
        "page": page.page,
    }
