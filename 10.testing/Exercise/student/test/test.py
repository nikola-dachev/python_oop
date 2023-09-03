from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Student_1')
        self.student_with_courses = Student('Student_2', {'OOP': ['some notes']})

    def test_correct_init(self):
        self.assertEqual('Student_1', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'OOP': ['some notes']}, self.student_with_courses.courses)

    def test_enroll_method_course_in_courses(self):
        result = self.student_with_courses.enroll('OOP', ['some other notes'])
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(expected_result, result)
        self.assertEqual(['some notes', 'some other notes'], self.student_with_courses.courses['OOP'])

    def test_enroll_method_create_course_without_third_param(self):
        result = self.student.enroll('Python DB', ['python db is cool'])
        expected_result = "Course and course notes have been added."
        self.assertEqual(expected_result, result)
        self.assertEqual({'Python DB': ['python db is cool']}, self.student.courses)

    def test_enroll_method_create_course_with_third_param_y(self):
        result = self.student.enroll('Python Advanced', ['python advanced is cool'], 'Y')
        expected_result = "Course and course notes have been added."
        self.assertEqual(expected_result, result)
        self.assertEqual({'Python Advanced': ['python advanced is cool']}, self.student.courses)

    def test_enroll_method_create_course_with_third_param(self):
        result = self.student.enroll('Python Advanced', ['python advanced is cool'], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses['Python Advanced'])

    def test_add_notes_method_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python DB', 'some notes')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_method_course_name_in_courses(self):
        expected_result = "Notes have been updated"
        result = self.student_with_courses.add_notes('OOP', 'some more notes')
        self.assertEqual(expected_result, result)
        self.assertEqual(['some notes', 'some more notes'], self.student_with_courses.courses['OOP'])

    def test_leave_course_method_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Pythod DB')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_method_course_in_courses(self):
        result = self.student_with_courses.leave_course('OOP')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)


if __name__ == '__main__':
    main()
