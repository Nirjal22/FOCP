
staff = {"John","Luffy","Trump","Naruto","Roman","Eren"}
directors = {"Casemiro", "Luffy","Trump" , "Ronaldo"}


staff_or_external = staff.union(directors)
print(staff_or_external)


common_members = staff.intersection(directors)
print(common_members)


staff_not_directors = staff.difference(directors)
print(staff_not_directors)


either_staff_or_directors = staff.symmetric_difference(directors)
print(either_staff_or_directors)
