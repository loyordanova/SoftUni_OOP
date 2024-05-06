from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_without_courses = Student('Kalin')
        self.student_with_courses = Student('Lora', {'Python': ['advance is easy', 'OOP --> cry']})

    def test_correct_initialization(self):
        self.assertEqual('Kalin', self.student_without_courses.name)
        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual({'Python': ['advance is easy', 'OOP --> cry']}, self.student_with_courses.courses)

    def test_enroll_adds_notes_to_existing_course(self):
        result = self.student_with_courses.enroll('Python', ['i want to cry', 'i can not do this'])
        self.assertEqual({'Python': ['advance is easy', 'OOP --> cry', 'i want to cry', 'i can not do this']},
                         self.student_with_courses.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_adds_notes_if_add_course_notes_is_Y_to_new_course(self):
        result = self.student_without_courses.enroll('JS',['still learning', 'hard'], 'Y')
        self.assertEqual({'JS': ['still learning', 'hard']}, self.student_without_courses.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_adds_notes_if_add_course_notes_is_empty_string_to_new_course(self):
        result = self.student_without_courses.enroll('Java', ['tbd'], '')
        self.assertEqual({'Java': ['tbd']}, self.student_without_courses.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_adds_notes_and_creates_new_course(self):
        result = self.student_with_courses.enroll('C#', 'i do not know that language', 'add them')
        self.assertEqual({'C#':  [],
                          'Python': ['advance is easy', 'OOP --> cry']}, self.student_with_courses.courses)
        self.assertEqual("Course has been added.", result)

    def test_notes_added_if_course_exists(self):
        result = self.student_with_courses.add_notes('Python', 'yes')
        self.assertEqual({'Python': ['advance is easy', 'OOP --> cry', 'yes']}, self.student_with_courses.courses)
        self.assertEqual("Notes have been updated", result)

    def test_cannot_add_notes_if_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.add_notes('Python', 'yes')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_pop_course_if_course_exists(self):
        result = self.student_with_courses.leave_course('Python')
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test_cannot_remove_course_if_course_does_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.leave_course('Python')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))