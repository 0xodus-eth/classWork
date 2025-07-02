import Pyro4
import time
from typing import Dict, List
from datetime import datetime, timedelta

class BookAlreadyIssuedException(Exception):
    """Custom exception for already issued books"""
    pass

class BookNotIssuedException(Exception):
    """Custom exception for books not currently issued"""
    pass

class InvalidMemberException(Exception):
    """Custom exception for invalid member IDs"""
    pass

class InvalidBookException(Exception):
    """Custom exception for invalid book IDs"""
    pass

@Pyro4.expose
class IssueService:
    def __init__(self):
        self.issued_books: Dict[str, Dict] = {
            "B004": {
                "member_id": "M001",
                "issue_date": "2024-06-01",
                "due_date": "2024-06-15"
            }
        }
        
        # Connect to other services
        try:
            self.book_catalog = Pyro4.Proxy("PYRONAME:library.bookcatalog")
            self.member_manager = Pyro4.Proxy("PYRONAME:library.membermanager")
        except:
            print("Warning: Could not connect to other services")
            self.book_catalog = None
            self.member_manager = None
    
    def issue_book(self, book_id: str, member_id: str) -> Dict:
        """Issue a book to a member"""
        time.sleep(1)  # Simulate processing delay
        
        # Validate member
        if self.member_manager and not self.member_manager.member_exists(member_id):
            raise InvalidMemberException(f"Member {member_id} does not exist")
        
        # Validate book
        if self.book_catalog:
            book = self.book_catalog.get_book(book_id)
            if not book:
                raise InvalidBookException(f"Book {book_id} does not exist")
            
            if not book['available']:
                raise BookAlreadyIssuedException(f"Book {book_id} is already issued")
        
        # Check if book is already in issued list
        if book_id in self.issued_books:
            raise BookAlreadyIssuedException(f"Book {book_id} is already issued")
        
        # Issue the book
        issue_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        
        self.issued_books[book_id] = {
            "member_id": member_id,
            "issue_date": issue_date,
            "due_date": due_date
        }
        
        # Update book availability
        if self.book_catalog:
            self.book_catalog.update_book_availability(book_id, False)
        
        print(f"Book {book_id} issued to member {member_id}")
        return {
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": issue_date,
            "due_date": due_date,
            "status": "issued"
        }
    
    def return_book(self, book_id: str) -> Dict:
        """Return a book"""
        time.sleep(0.5)  # Simulate processing delay
        
        if book_id not in self.issued_books:
            raise BookNotIssuedException(f"Book {book_id} is not currently issued")
        
        # Get issue details
        issue_info = self.issued_books[book_id]
        return_date = datetime.now().strftime("%Y-%m-%d")
        
        # Remove from issued books
        del self.issued_books[book_id]
        
        # Update book availability
        if self.book_catalog:
            self.book_catalog.update_book_availability(book_id, True)
        
        print(f"Book {book_id} returned by member {issue_info['member_id']}")
        return {
            "book_id": book_id,
            "member_id": issue_info['member_id'],
            "issue_date": issue_info['issue_date'],
            "return_date": return_date,
            "status": "returned"
        }
    
    def list_issued_books(self) -> List[Dict]:
        """List all currently issued books"""
        issued_list = []
        for book_id, issue_info in self.issued_books.items():
            issue_copy = issue_info.copy()
            issue_copy['book_id'] = book_id
            issued_list.append(issue_copy)
        return issued_list
    
    def get_member_books(self, member_id: str) -> List[str]:
        """Get all books issued to a specific member"""
        return [book_id for book_id, info in self.issued_books.items() 
                if info['member_id'] == member_id]

if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    try:
        ns = Pyro4.locateNS()
        uri = daemon.register(IssueService())
        ns.register("library.issueservice", uri)
        print(f"IssueService ready. URI: {uri}")
    except:
        uri = daemon.register(IssueService())
        print(f"Name server not found. Direct URI: {uri}")
    
    daemon.requestLoop()