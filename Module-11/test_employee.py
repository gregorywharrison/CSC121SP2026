import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    return Employee('Gregory', 'Harrison', 50000)

def test_give_default_raise(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.salary == 55000

def test_give_custom_raise(employee_instance):
    employee_instance.give_raise(10000)
    assert employee_instance.salary == 60000
