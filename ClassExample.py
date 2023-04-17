# Rank IDs:
# 
# 1 | Owner
# 2 | Admin
# 3 | Moderator
# 4 | Helper

class Staff():
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        if self.ID == 1:
            self.rank = "Owner"
        if self.ID == 2:
            self.rank = "Admin"
        if self.ID == 3:
            self.rank = "Moderator"
        if self.ID == 4:
            self.rank = "Helper"
        if self.ID == 5:
            self.rank = "Trial"
    
    # Check staff info.
    def StaffData(self):
        return "Name: {}, RankID: {}, Rank: {}".format(self.name,self.ID,self.rank)

    # Promote a staff member.
    def StaffPromote(self):
        if self.ID == 1:
            return "Can't promote Owner to higher rank."
        elif self.ID <= 5:
            self.ID = self.ID -1 # Lower ID meaning higher rank.
            if self.ID == 1:
                self.rank = "Owner"
            elif self.ID == 2:
                self.rank = "Admin"
            elif self.ID == 3:
                self.rank = "Moderator"
            elif self.ID == 4:
                self.rank = "Helper"
            elif self.ID == 5:
                self.rank = "Trial"
            return self.ID
        else:
            return "Error"

    # Demote a staff member.
    def StaffDemote(self):
        if self.ID == 5:
            return "Can't demote Trial to lower rank."
        if self.ID <= 5:
            self.ID += 1 # Higher ID meaning lower rank.
            if self.ID == 1:
                self.rank = "Owner"
            if self.ID == 2:
                self.rank = "Admin"
            if self.ID == 3:
                self.rank = "Moderator"
            if self.ID == 4:
                self.rank = "Helper"
            if self.ID == 5:
                self.rank = "Trial"
            return self.ID
    
    # Create a staff member.
    def StaffCreate(self, StaffList):
        # Check if staff with same name already exists.
        for staff in StaffList:
            if self.name == staff.name:
                return "Staff with same name already exists."
        StaffList.append(self)
        return "Staff added successfully."
    
    # Remove a staff member.
    def StaffRemove(self, StaffList):
        # Check if staff exists in the list.
        if self not in StaffList:
            return "Staff not found."
        StaffList.remove(self)
        return "Staff removed successfully."
        
    
# View list of Helpers.
def ShowHelpers(StaffList):
    print("List of Helpers:")
    for staff in StaffList:
        if staff.rank == "Helper":
            print(staff.StaffData())
            
# View list of Moderators.
def ShowModerators(StaffList):
    print("List of Moderators:")
    for staff in StaffList:
        if staff.rank == "Moderator":
            print(staff.StaffData())
            
# View list of Admins.
def ShowAdmins(StaffList):
    print("List of Admins:")
    for staff in StaffList:
        if staff.rank == "Admin":
            print(staff.StaffData())
    


# Testing the code.

# Staff member promotion and demotion.
Omer = Staff("Omer",5)
print(Omer.StaffData()) # Should return: "Name: Omer, RankID: 5, Rank: Trial"
print(Omer.StaffPromote()) # RankID should be 4.
print(Omer.StaffData()) # Should return: "Name: Omer, RankID: 4, Rank: Helper"
print(Omer.StaffDemote()) # RankID should be 5.
print(Omer.StaffData()) # Should return: "Name: Omer, RankID: 5, Rank: Trial

# Staff member creation.
StaffList = []
staff1 = Staff("John", 2)
result1 = staff1.StaffCreate(StaffList)
print(result1)  # Staff added successfully.
staff2 = Staff("Jane", 3)
result2 = staff2.StaffCreate(StaffList)
print(result2)  # Staff added successfully.
staff3 = Staff("John", 4)
result3 = staff3.StaffCreate(StaffList)
print(result3)  # Staff with same name already exists.


# Staff member removal.
print(staff2.StaffRemove(StaffList)) # Should remove the staff from the list.
print(staff2.StaffRemove(StaffList)) # Should say "Staff not found."
            
    