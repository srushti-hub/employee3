from employee import get_employee_info

def test_get_employee_info():
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 6000

    expected_output = (
        " Employee Name : Alice Smith,\n"
        " Employee ID : E202,\n"
        " Department : HR,\n"
        " Salary : 6000 "
    )

    assert get_employee_info(name, emp_id, department, salary) == expected_output
