import itertools

from faker import Faker
import pandas as pd
import psycopg2

import db
from models.major import MajorModel
from models.department import DepartmentModel
from models.professor import ProfessorModel
from models.class_ import ClassModel
from models.student import StudentModel
from models.post import PostModel
from models.comment import CommentModel
from models.grade import GradeModel
from models.preclass import PreclassModel
from models.scholarship import ScholarshipModel

fake = Faker()

try:
    db.execute('SELECT 1 FROM major')
except psycopg2.ProgrammingError:
    major_model = MajorModel()
    major_rows = list(itertools.islice(major_model, 30))
    df_major = pd.DataFrame(major_rows, columns=["id", "name"])
    db.execute("DROP TABLE IF EXISTS major")
    db.insert(df_major, "major")

try:
    db.execute('SELECT 1 FROM department')
except psycopg2.ProgrammingError:
    department_model = DepartmentModel(fake)
    department_rows = list(itertools.islice(department_model, 30))
    df_department = pd.DataFrame(department_rows, columns=["id", "name", "place"])
    db.execute("DROP TABLE IF EXISTS department")
    db.insert(df_department, "department")

try:
    db.execute('SELECT 1 FROM professor')
except psycopg2.ProgrammingError:
    professor_model = ProfessorModel(fake, db.fetch("SELECT id FROM department"))
    professor_rows = list(itertools.islice(professor_model, 30))
    df_professor = pd.DataFrame(
        professor_rows, columns=["id", "name", "department"]
    )
    db.execute("DROP TABLE IF EXISTS professor")
    db.insert(df_professor, "professor")

try:
    db.execute('SELECT 1 FROM class')
except psycopg2.ProgrammingError:
    class_model = ClassModel(
        fake,
        db.fetch("SELECT id FROM department"),
        db.fetch("SELECT id FROM professor"),
    )
    class_rows = list(
        itertools.islice(class_model, 30 * 4 * 100)
    )  # 30 years, 100 classes per quarter
    df_class = pd.DataFrame(
        class_rows,
        columns=[
            "id",
            "year",
            "quarter",
            "is_completed",
            "name",
            "place",
            "period",
            "professor",
            "credit",
            "capacity",
            "is_pass",
            "classification",
            "department",
        ],
    )
    db.execute("DROP TABLE IF EXISTS class")
    db.insert(df_class, "class")
    
try:
    db.execute('SELECT 1 FROM student')
except psycopg2.ProgrammingError:
    student_model = StudentModel(
        fake,
        db.fetch("SELECT id FROM major"),
        db.fetch("SELECT id FROM professor"),
    )
    student_rows = list(
        itertools.islice(student_model, 30 * 30 * 50)
    )  # 30 years, 50 students per major
    df_student = pd.DataFrame(
        student_rows,
        columns=[
            "id",
            "name",
            "major_id",
            "year",
            "semester",
            "phone",
            "email",
            "professor_id",
            "pw",
        ],
    )
    db.execute("DROP TABLE IF EXISTS student")
    db.insert(df_student, "student")

try:
    db.execute('SELECT 1 FROM post')
except psycopg2.ProgrammingError:
    post_model = PostModel(
        fake,
        db.fetch("SELECT id, year, quarter FROM class"),
        db.fetch("SELECT id FROM student"),
    )
    post_rows = list(
        itertools.islice(post_model, 30 * 365 * 5)
    )  # 30 years, 5 posts per day
    df_post = pd.DataFrame(
        post_rows,
        columns=[
            "id",
            "title",
            "content",
            "like_",
            "hate",
            "hits",
            "is_notice",
            "class_id",
            "year",
            "quarter",
            "author",
            "created_time",
        ],
    )
    db.execute("DROP TABLE IF EXISTS post")
    db.insert(df_post, "post")

try:
    db.execute('SELECT 1 FROM comment')
except psycopg2.ProgrammingError:
    comment_model = CommentModel(
        fake,
        db.fetch("SELECT id, created_time FROM post"),
        db.fetch("SELECT id FROM student"),
    )
    comment_rows = list(
        itertools.islice(comment_model, 30 * 365 * 10)
    )  # 30 years, 10 comments per day
    df_comment = pd.DataFrame(
        comment_rows,
        columns=[
            "id",
            "comment_id",
            "post_id",
            "content",
            "like_",
            "hate",
            "author",
            "created_time",
        ],
    )
    db.execute("DROP TABLE IF EXISTS comment")
    db.insert(df_comment, "comment")

try:
    db.execute('SELECT 1 FROM grade')
except psycopg2.ProgrammingError:
    grade_model = GradeModel(
        fake,
        db.fetch("SELECT id, year, quarter FROM class"),
        db.fetch("SELECT id FROM student"),
    )
    grade_rows = list(
        itertools.islice(grade_model, 3 * len(df_student))
    )  # 4 years, 15 courses per quarter for each student,
    # but it would be too large so only 3 courses per student
    df_grade = pd.DataFrame(
        grade_rows,
        columns=["student_id", "class_id", "year", "quarter", "retake", "grade"],
    )
    db.execute("DROP TABLE IF EXISTS grade")
    db.insert(df_grade, "grade")

try:
    db.execute('SELECT 1 FROM prerequisite_class')
except psycopg2.ProgrammingError:
    preclass_model = PreclassModel(db.fetch("SELECT id FROM class WHERE year=2020 AND quarter=2"))
    preclass_rows = list(preclass_model)
    df_preclass = pd.DataFrame(
        preclass_rows,
        columns=["pre_class_id", "class_id"],
    )
    db.execute("DROP TABLE IF EXISTS prerequisite_class")
    db.insert(df_preclass, "prerequisite_class")

try:
    db.execute('SELECT 1 FROM scholarship')
except psycopg2.ProgrammingError:
    scholarship_model = ScholarshipModel()
    scholarship_rows = list(itertools.islice(scholarship_model, 30))
    df_scholarship = pd.DataFrame(
        scholarship_rows,
        columns=["year", "semester", "won"],
    )
    db.execute("DROP TABLE IF EXISTS scholarship")
    db.insert(df_scholarship, "scholarship")