from tinydb import TinyDB, Query

# Initialize database
db = TinyDB('students_db.json')
students_table = db.table('students')


def add(student):
    """Add a new student to the database"""
    # Get the next student ID
    all_students = students_table.all()
    if all_students:
        next_id = max([s.get('student_id', 0) for s in all_students]) + 1
    else:
        next_id = 1

    # Add student_id to the student object
    student.student_id = next_id

    # Convert student object to dictionary
    student_dict = student.to_dict()

    # Insert into database
    students_table.insert(student_dict)

    return next_id


def get_all():
    """Get all students from the database"""
    return students_table.all()


def get(student_id):
    """Get a single student by ID"""
    Student = Query()
    result = students_table.search(Student.student_id == student_id)

    if result:
        return result[0]
    else:
        return None


def delete(student_id):
    """Delete a student by ID"""
    Student = Query()
    result = students_table.search(Student.student_id == student_id)

    if not result:
        return None, 404

    students_table.remove(Student.student_id == student_id)
    return None, 200