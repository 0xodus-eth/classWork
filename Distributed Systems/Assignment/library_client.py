import Pyro4
import time
import threading
from concurrent.futures import ThreadPoolExecutor

class LibraryClient:
    def __init__(self):
        try:
            self.book_catalog = Pyro4.Proxy("PYRONAME:library.bookcatalog")
            self.member_manager = Pyro4.Proxy("PYRONAME:library.membermanager")
            self.issue_service = Pyro4.Proxy("PYRONAME:library.issueservice")
            print("Connected to all library services!")
        except Exception as e:
            print(f"Error connecting to services: {e}")
            return
    
    def display_menu(self):
        print("\n" + "="*50)
        print("DISTRIBUTED LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. List all books")
        print("2. Search books")
        print("3. List all members")
        print("4. Register new member (Async)")
        print("5. Issue book")
        print("6. Return book")
        print("7. List issued books")
        print("8. Get member's issued books")
        print("9. Exit")
        print("-"*50)
    
    def list_books(self):
        print("\n📚 Fetching all books...")
        try:
            books = self.book_catalog.list_all_books()
            print(f"\n{'ID':<6} {'Title':<20} {'Author':<15} {'Available':<10}")
            print("-"*60)
            for book in books:
                status = "✅ Yes" if book['available'] else "❌ No"
                print(f"{book['book_id']:<6} {book['title']:<20} {book['author']:<15} {status:<10}")
        except Exception as e:
            print(f"Error fetching books: {e}")
    
    def search_books(self):
        query = input("\n🔍 Enter search term (title or author): ")
        try:
            books = self.book_catalog.search_books(query)
            if books:
                print(f"\n{'ID':<6} {'Title':<20} {'Author':<15} {'Available':<10}")
                print("-"*60)
                for book in books:
                    status = "✅ Yes" if book['available'] else "❌ No"
                    print(f"{book['book_id']:<6} {book['title']:<20} {book['author']:<15} {status:<10}")
            else:
                print("No books found matching your search.")
        except Exception as e:
            print(f"Error searching books: {e}")
    
    def list_members(self):
        print("\n👥 Fetching all members...")
        try:
            members = self.member_manager.list_all_members()
            print(f"\n{'ID':<6} {'Name':<20} {'Email':<25} {'Registration':<12}")
            print("-"*70)
            for member in members:
                print(f"{member['member_id']:<6} {member['name']:<20} {member['email']:<25} {member['registration_date']:<12}")
        except Exception as e:
            print(f"Error fetching members: {e}")
    
    def register_member_async(self):
        print("\n👤 Register New Member (Asynchronous)")
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        phone = input("Enter member phone: ")
        
        print("\n🔄 Starting asynchronous member registration...")
        
        # Method 1: Using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.member_manager.register_member, name, email, phone)
            
            # Do other work while waiting
            print("⏳ Registration in progress...")
            for i in range(5):
                print(f"   Working... {i+1}/5")
                time.sleep(0.4)
            
            try:
                member_id = future.result(timeout=10)
                print(f"✅ Member registered successfully! ID: {member_id}")
            except Exception as e:
                print(f"❌ Registration failed: {e}")
    
    def issue_book(self):
        print("\n📖 Issue Book")
        book_id = input("Enter book ID: ").upper()
        member_id = input("Enter member ID: ").upper()
        
        try:
            result = self.issue_service.issue_book(book_id, member_id)
            print(f"✅ Book issued successfully!")
            print(f"   Book ID: {result['book_id']}")
            print(f"   Member ID: {result['member_id']}")
            print(f"   Issue Date: {result['issue_date']}")
            print(f"   Due Date: {result['due_date']}")
        except Exception as e:
            print(f"❌ Failed to issue book: {e}")
    
    def return_book(self):
        print("\n📚 Return Book")
        book_id = input("Enter book ID to return: ").upper()
        
        try:
            result = self.issue_service.return_book(book_id)
            print(f"✅ Book returned successfully!")
            print(f"   Book ID: {result['book_id']}")
            print(f"   Member ID: {result['member_id']}")
            print(f"   Return Date: {result['return_date']}")
        except Exception as e:
            print(f"❌ Failed to return book: {e}")
    
    def list_issued_books(self):
        print("\n📋 Currently Issued Books")
        try:
            issued = self.issue_service.list_issued_books()
            if issued:
                print(f"\n{'Book ID':<8} {'Member ID':<10} {'Issue Date':<12} {'Due Date':<12}")
                print("-"*50)
                for issue in issued:
                    print(f"{issue['book_id']:<8} {issue['member_id']:<10} {issue['issue_date']:<12} {issue['due_date']:<12}")
            else:
                print("No books are currently issued.")
        except Exception as e:
            print(f"Error fetching issued books: {e}")
    
    def get_member_books(self):
        print("\n📚 Member's Issued Books")
        member_id = input("Enter member ID: ").upper()
        
        try:
            books = self.issue_service.get_member_books(member_id)
            if books:
                print(f"Books issued to {member_id}: {', '.join(books)}")
            else:
                print(f"No books currently issued to {member_id}")
        except Exception as e:
            print(f"Error fetching member books: {e}")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ")
            
            if choice == '1':
                self.list_books()
            elif choice == '2':
                self.search_books()
            elif choice == '3':
                self.list_members()
            elif choice == '4':
                self.register_member_async()
            elif choice == '5':
                self.issue_book()
            elif choice == '6':
                self.return_book()
            elif choice == '7':
                self.list_issued_books()
            elif choice == '8':
                self.get_member_books()
            elif choice == '9':
                print("👋 Thank you for using the Library Management System!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    client = LibraryClient()
    client.run()