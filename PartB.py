import unittest
from PartA import Staff, Manager

class TestClassInstances(unittest.TestCase):
    def setUp(self):
        # Instances for testing
        self.staff_member = Staff(
            name="Will Smith",
            DoB="1999-07-07",
            sex="Male",
            staffID="S003344",
            address="123 Main St, Small Town, Ireland"
        )
        self.manager_member = Manager(
            name="Jade Smith",
            DoB="1983-05-15",
            sex="Female",
            staffID="M002288",
            address="456 Hampton St, Othertown, Ireland",
            department="Sales",
            team_size=10
        )

    def test_staff_instance(self): 
        # Test if staff_member is an instance of Staff
        self.assertIsInstance(self.staff_member, Staff)

    def test_manager_instance(self): 
        # Test if manager_member is an instance of Manager
        self.assertIsInstance(self.manager_member, Manager)

    def test_not_staff_instance(self): 
        # Test if manager_member is NOT an instance of Staff
        self.assertNotIsInstance(self.manager_member, Staff)

    def test_not_manager_instance(self): 
        # Test if staff_member is NOT an instance of Manager
        self.assertNotIsInstance(self.staff_member, Manager)

    def test_identical_staff_instances(self): 
        # Test if two staff members with the same attributes are identical
        another_staff_member = Staff(
            name="Will Smith",
            DoB="1999-07-07",
            sex="Male",
            staffID="S003344",
            address="123 Main St, Small Town, Ireland"
        )
        self.assertEqual(self.staff_member, another_staff_member)

    def test_identical_manager_instances(self): 
        # Test if two managers with the same attributes are identical
        another_manager_member = Manager(
            name="Jade Smith",
            DoB="1983-05-15",
            sex="Female",
            staffID="M002288",
            address="456 Hampton St, Othertown, Ireland",
            department="Sales",
            team_size=10
        )
        self.assertEqual(self.manager_member, another_manager_member)

    def test_update_staff_address(self):
        # Test updating the staff member's address
        self.staff_member.update_address("789 New St, Big City, Ireland")
        self.assertEqual(self.staff_member.address, "789 New St, Big City, Ireland")

    def test_update_staff_sex(self):
        # Test updating the staff member's sex
        self.staff_member.update_sex("Non-binary")
        self.assertEqual(self.staff_member.sex, "Non-binary")

    def test_update_manager_team_size(self):
        # Test updating the manager's team size
        self.manager_member.update_team_size(12)
        self.assertEqual(self.manager_member.team_size, 12)

    def test_update_manager_department(self):
        # Test updating the manager's department
        self.manager_member.update_department("Marketing")
        self.assertEqual(self.manager_member.department, "Marketing")

def main():
    # Run the unit tests
    unittest.main()

if __name__ == '__main__':
    main()

    unittest.main()
