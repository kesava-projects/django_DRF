from rest_framework.exceptions import APIException

class StudentNotFoundException(APIException):
    status_code = 404
    default_detail = "Student data is not found"