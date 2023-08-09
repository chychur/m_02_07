# DataBase


A database was created, the schema of which contains:

![DB schema](/db/college.png)

of `students`, `groups`, `teachers`, `discipline` (with an indication of the teacher who reads the subject) and `score_log`(a table where each student has grades from subjects with an indication of when the grade was received).
The database was filled with fake data (30 students, 3 groups, 5 subjects and 5 teachers, and up to 20 grades for each student in all subjects). The Faker package was used to create fake data.

Make the following selections from the obtained database:

1. Find the 5 students with the highest average score in all subjects.
2. Find the student with the highest average score in a certain subject.
3. Find the average score in groups for a certain subject.
4. Find the average score on the stream (over the entire score table).
5. Find out what courses a particular teacher teaches.
6. Find a list of students in a certain group.
7. Find the grades of students in a separate group on a certain subject.
8. Find the average score given by a certain teacher in his subjects.
9. Find the list of courses attended by the student.
10. A list of courses taught to a particular student by a particular teacher.

Each request is in a separate file `query_number.sql`, where instead of `number` is the number of the request from the list.