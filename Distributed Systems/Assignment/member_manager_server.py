import Pyro4
import time
from typing import Dict, List, Optional

@Pyro4.expose
class MemberManager:
    def __init__(self):
        self.members: Dict[str, Dict] = {
            "M001": {
                "name": "Alice Brown",
                "email": "alice@email.com",
                "phone": "123-456-7890",
                "registration_date": "2024-01-15"
            },
            "M002": {
                "name": "Bob Green",
                "email": "bob@email.com", 
                "phone": "098-765-4321",
                "registration_date": "2024-02-20"
            }
        }
        self.next_member_id = 3
    
    def register_member(self, name: str, email: str, phone: str) -> str:
        """Register a new member (simulates slow database operation)"""
        time.sleep(2)  # Simulate database insertion delay
        
        member_id = f"M{self.next_member_id:03d}"
        self.members[member_id] = {
            "name": name,
            "email": email,
            "phone": phone,
            "registration_date": time.strftime("%Y-%m-%d")
        }
        self.next_member_id += 1
        
        print(f"New member registered: {member_id} - {name}")
        return member_id
    
    def list_all_members(self) -> List[Dict]:
        """List all registered members"""
        time.sleep(0.3)  # Simulate database query delay
        members_list = []
        for member_id, member_info in self.members.items():
            member_copy = member_info.copy()
            member_copy['member_id'] = member_id
            members_list.append(member_copy)
        return members_list
    
    def get_member(self, member_id: str) -> Optional[Dict]:
        """Get member details by ID"""
        if member_id in self.members:
            member_copy = self.members[member_id].copy()
            member_copy['member_id'] = member_id
            return member_copy
        return None
    
    def member_exists(self, member_id: str) -> bool:
        """Check if member exists"""
        return member_id in self.members

if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    try:
        ns = Pyro4.locateNS()
        uri = daemon.register(MemberManager())
        ns.register("library.membermanager", uri)
        print(f"MemberManager service ready. URI: {uri}")
    except:
        uri = daemon.register(MemberManager())
        print(f"Name server not found. Direct URI: {uri}")
    
    daemon.requestLoop()