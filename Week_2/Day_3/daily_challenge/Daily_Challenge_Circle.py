import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        """
        items: list (optional). Defaults to empty list.
        page_size: int (optional). Defaults to 10. Must be > 0.
        """
        if items is None:
            items = []
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer")

        self.items = list(items)                # keep a copy as list
        self.page_size = page_size
        self.current_idx = 0                    # 0-based page index

        # total_pages is at least 1 (so page 1 shows [] when items empty)
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    def get_visible_items(self):
        """
        Return the list of items visible on the current page.
        """
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # ---------- navigation ----------
    def go_to_page(self, page_num):
        """
        Go to a specific page using 1-based indexing.
        Raises ValueError if page_num is out of range.
        """
        if not isinstance(page_num, int):
            raise ValueError("page number must be an integer")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"page_num must be between 1 and {self.total_pages}")
        self.current_idx = page_num - 1
        return self  # (optional) allow chaining here too

    def first_page(self):
        self.current_idx = 0
        return self   # allow method chaining

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self   # allow method chaining

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self   # allow method chaining

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self   # allow method chaining

    # ---------- bonus ----------
    def __str__(self):
        """
        Show the items on the current page, one per line.
        """
        return "\n".join(str(x) for x in self.get_visible_items())


# --------------------------
# Test cases from the brief
# --------------------------
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())
    # ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())
    # ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())
    # ['y', 'z']

    # This should raise ValueError (page 10 doesn't exist: total_pages = ceil(26/4)=7)
    try:
        p.go_to_page(10)
        print(p.current_idx + 1)
    except ValueError as e:
        print("ValueError:", e)

    # This should raise ValueError (page numbers start at 1)
    try:
        p.go_to_page(0)
    except ValueError as e:
        print("ValueError:", e)

    # Bonus demo: __str__
    print("\nCurrent page as text:")
    print(str(p))