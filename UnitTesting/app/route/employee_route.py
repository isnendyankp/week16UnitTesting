from flask import Blueprint, request
from app.models.employee import Employees
from app.utils.database import db

employee_blueprint = Blueprint('employee_endpoint', __name__)


# Method GET retrieve all employees in zoo
@employee_blueprint.route("/", methods=["GET"])
def get_employees():
    try:
        # get all employees from the database
        employees = Employees.query.all()
        return [employee.as_dict() for employee in employees], 200
    except Exception as e:
        return e, 500

