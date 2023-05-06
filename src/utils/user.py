class User:
    def __init__(self, uid: str) -> None:
        self.uid = uid
        self.name = str()
        self.faculty = str()
        self.group = str()
        self.why = str()
        self.other_group = str()
        self.old_group = None
        self.department = list()

    def __str__(self) -> str:
        return f"{self.name}\n{self.faculty}\n{self.group}\n{self.why}\n{self.other_group}\n{self.old_group}\n{self.department}"
    
    def set_name(self, name: str) -> None:
        self.name = name

    def set_faculty(self, faculty: str) -> None:
        self.faculty = faculty

    def set_group(self, group: str) -> None:
        self.group = group

    def set_why(self, why: str) -> None:
        self.why = why

    def set_other_group(self, other_group: str) -> None:
        self.other_group = other_group

    def set_old_group(self, old_group: str) -> None:
        self.old_group = old_group

    def set_department(self, department: str) -> None:
        self.department.append(department)

    def get_name(self) -> str:
        return self.name
    
    def get_faculty(self) -> str:
        return self.faculty
    
    def get_group(self) -> str:
        return self.group
    
    def get_why(self) -> str:
        return self.why
    
    def get_other_group(self) -> str:
        return self.other_group
    
    def get_old_group(self) -> str:
        return self.old_group
    
    def get_department(self) -> str:
        return ', '.join(self.department)
    
    def get_uid(self) -> str:
        return self.uid
    