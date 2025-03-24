class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    # Method to update the staff member's address
    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address
        else:
            raise ValueError("Invalid type for address. Expected a string.")

    # Method to update the staff member's sex
    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            raise ValueError("Invalid type for sex. Expected a string.")

    # Method to compare two Staff instances
    def __eq__(self, other):
        if not isinstance(other, Staff):
            return NotImplemented
        return (self.name == other.name and
                self.DoB == other.DoB and
                self.sex == other.sex and
                self.staffID == other.staffID and
                self.address == other.address)

class Manager(Staff):
    def __init__(self, name, DoB, sex, staffID, address, department, team_size):
        super().__init__(name, DoB, sex, staffID, address)
        self.department = department
        self.team_size = team_size

    # Method to compare two Manager instances
    def __eq__(self, other):
        if not isinstance(other, Manager):
            return NotImplemented
        return (super().__eq__(other) and
                self.department == other.department and
                self.team_size == other.team_size)

    # Method to update the manager's team size
    def update_team_size(self, new_team_size):
        if isinstance(new_team_size, int):
            self.team_size = new_team_size
        else:
            raise ValueError("Invalid type for team size. Expected an integer.")

    # Method to update the manager's department
    def update_department(self, new_department):
        if isinstance(new_department, str):
            self.department = new_department
        else:
            raise ValueError("Invalid type for department. Expected a string.")

    # Method to update the manager's date of birth
    def update_DoB(self, new_DoB):
        if isinstance(new_DoB, str):
            self.DoB = new_DoB
        else:
            raise ValueError("Invalid type for DoB. Expected a string.")

    # Method to update the manager's sex
    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            raise ValueError("Invalid type for sex. Expected a string.")

    # Method to update the manager's staff ID
    def update_staffID(self, new_staffID):
        if isinstance(new_staffID, str):
            self.staffID = new_staffID
        else:
            raise ValueError("Invalid type for staffID. Expected a string.")

    # Method to update the manager's address
    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address
        else:
            raise ValueError("Invalid type for address. Expected a string.")

# Instances of Staff and Manager classes
staff_member = Staff(
    name="Will Smith",
    DoB="1999-07-07",
    sex="Male",
    staffID="S003344",
    address="123 Main St, Small Town, Ireland"
)

# Creating an instance of Manager
manager_member = Manager(
    name="Jade Smith",
    DoB="1983-05-15",
    sex="Female",
    staffID="M002288",
    address="456 Hampton St, Othertown, Ireland",
    department="Sales",
    team_size=10
)

# Perform examples of tasks A4 and A7
# Example 1 for A4: Update the staff member's address
staff_member.update_address("789 New St, Big City, Ireland")
print(f"Updated Staff Member Address: {staff_member.address}")

# Example 2 for A4: Update the staff member's sex
staff_member.update_sex("Non-binary")
print(f"Updated Staff Member Sex: {staff_member.sex}")

# Example 1 for A7: Update the manager's team size
manager_member.update_team_size(12)
print(f"Updated Manager Team Size: {manager_member.team_size}")

# Example 2 for A7: Update the manager's date of birth
manager_member.update_DoB("1983-06-15")
print(f"Updated Manager Date of Birth: {manager_member.DoB}")
