# TASK: Write code based on the previous two examples, but use the equivalent method calls
# to achieve the same results.


# Given sets
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members (using issubset())")


if managers <= staff:
    print("All managers are staff members (using <=)")


if staff.issuperset(managers):
    print("All managers are staff members (using issuperset())")


if staff >= managers:
    print("All managers are staff members (using >=)")
