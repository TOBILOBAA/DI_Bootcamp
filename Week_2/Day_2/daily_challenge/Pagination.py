import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0 
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
    def go_to_page(self, page_num):
        if self.total_pages == 0:
            raise ValueError("no pages available.")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page out of range.")
        self.current_idx = page_num - 1 

    def first_page(self):
        if self.total_pages > 0:
            self.current_idx = 0
        return self
        
    def last_page (self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1 
        return self   

    def next_page(self):
        if self.total_pages == 0:
            return self 
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self
    
    def previous_page(self):
        if self.total_pages == 0:
            return self 
        if self.current_idx > 0:
            self.current_idx -= 1
        return self 
        
    def __str__(self):
        return "\n".join(str(x) for x in self.get_visible_items())

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

# These should raise ValueError:
try:
    p.go_to_page(10)
    print(p.current_idx + 1)  # won't reach here
except ValueError as e:
    print("ValueError:", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("ValueError:", e)

    

