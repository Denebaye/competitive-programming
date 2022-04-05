"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def calcimportance(self,id_emp,id):
        if not id_emp[id].subordinates:
            return id_emp[id].importance
        
        curr = id_emp[id].importance
        
        for emp_subordinate in id_emp[id].subordinates:
            
            curr += self.calcimportance(id_emp,emp_subordinate)
            
        return curr
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_emp = {}
        my_memo = {}
        for employee in employees:
            id_emp[employee.id] = employee
        
        return self.calcimportance(id_emp,id)
    
    
    