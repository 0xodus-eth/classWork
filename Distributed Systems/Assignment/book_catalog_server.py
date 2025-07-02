import Pyro4
import time
from typing import Dict, List, Optional

@Pyro4.expose
class BookCatalog:
    def __init__(self):
        # Sample book data
        self.books: Dict[str, Dict] = {
            "B001": {
                "title": "Python Programming",
                "author": "John Smith",
                "isbn": "978-1234567890",
                "available": True
            },
            "B002": {
                "title": "Distributed Systems",
                "author": "Jane Doe",
                "isbn": "978-0987654321",
                "available": True
            },
            "B003": {
                "title": "Database Management",
                "author": "Bob Wilson",
                "isbn": "978-1122334455",
                "available": True
            },
            "B004": {
                "title": "Web Development",
                "author": "Alice Johnson",
                "isbn": "978-5566778899",
                "available": False
            }
        }
    
    def list_all_books(self) -> List[Dict]:
        """List all books in the catalog"""
        time.sleep(0.5)  # Simulate database query delay
        books_list = []
        for book_id, book_info in self.books.items():
            book_copy = book_info.copy()
            book_copy['book_id'] = book_id
            books_list.append(book_copy)
        return books_list
    
    def search_books(self, query: str) -> List[Dict]:
        """Search books by title or author"""
        time.sleep(0.3)  # Simulate search delay
        results = []
        query_lower = query.lower()
        
        for book_id, book_info in self.books.items():
            if (query_lower in book_info['title'].lower() or 
                query_lower in book_info['author'].lower()):
                book_copy = book_info.copy()
                book_copy['book_id'] = book_id
                results.append(book_copy)
        
        return results
    
    def get_book(self, book_id: str) -> Optional[Dict]:
        """Get book details by ID"""
        if book_id in self.books:
            book_copy = self.books[book_id].copy()
            book_copy['book_id'] = book_id
            return book_copy
        return None
    
    def update_book_availability(self, book_id: str, available: bool) -> bool:
        """Update book availability status"""
        if book_id in self.books:
            self.books[book_id]['available'] = available
            return True
        return False

if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    try:
        ns = Pyro4.locateNS()
        uri = daemon.register(BookCatalog())
        ns.register("library.bookcatalog", uri)
        print(f"BookCatalog service ready. URI: {uri}")
    except:
        uri = daemon.register(BookCatalog())
        print(f"Name server not found. Direct URI: {uri}")
    
    daemon.requestLoop()