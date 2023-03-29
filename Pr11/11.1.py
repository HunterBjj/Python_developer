"""
2. Деканат.
Дано: n - целое число.
Задание: спроектируйте следующую предметную область, используя объектно-ориентированный подход.
Сотрудники деканата каждый семестр решают проблему формирования отчетных ведомостей студентов,
разных групп и курсов. Цель - получить информацию о среднем балле каждого студента, группы,
а также предмета(например, средний балл по физкультуре в группе 433 составляет 4.1).
Такая информация поможет сформировать список студентов, которых нужно отчислить и стипендиатов,
а также наиболее "проблемные" предметы.
"""


class Academic_performance():
    def __init__(self, ball_student, student_name, ball_group, group_name, ball_course, course_name):
        self.ball_student = ball_student
        self.student_name = student_name
        self.ball_group = ball_group
        self.group_name = group_name
        self.ball_course = ball_course
        self.ball_course = course_name
        self.course_name = course_name

    def student(self):

        result = 0
        count = 0
        for i in range(len(self.ball_student)):
            result += self.ball_student[i]
            count += 1
        result *= count

        return result, self.student_name

    def group(self):

        result = 0
        count = 0
        for i in range(len(self.ball_group)):
            result += self.ball_group[i]
            count += 1
        result *= count

        return result, self.group_name

    def course(self):

        result = 0
        count = 0
        for i in range(len(self.ball_course)):
            result += self.ball_course[i]
            count += 1
        result *= count

        return result, self.course_name
