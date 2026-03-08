import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.service import student_service


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        return student_service.add(body)

    return 'Invalid input', 400


def delete_student(student_id):  # noqa: E501
    """deletes a student

    delete a single student # noqa: E501

    :param student_id: the uid
    :type student_id: int

    :rtype: None
    """
    result, status = student_service.delete(student_id)
    if status == 404:
        return 'Student not found', 404
    return 'Student deleted successfully', 200


def get_student(student_id):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    result = student_service.get(student_id)
    if result is None:
        return 'Student not found', 404
    return result


def get_students():  # noqa: E501
    """Get all students

    Returns a list of all students # noqa: E501


    :rtype: List[Student]
    """
    return student_service.get_all()


def get_average_grade(student_id):  # noqa: E501
    """Get average grade of a student

    Returns the average grade of all the student's grade records # noqa: E501

    :param student_id: ID of student
    :type student_id: int

    :rtype: float
    """
    result, status = student_service.get_average_grade(student_id)
    if status == 404:
        return 'Student not found or student has no grades', 404
    return result
