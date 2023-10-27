USE diploma_web_app;

INSERT INTO skills_skill (skill_name, skill_description)
VALUES 
	("golang", "golang language"),
	("python", "python language"),
    ("java", "java language"),
    ("django", "django framework"),
    ("html", "html markup language"),
    ("spring", "spring framework");
COMMIT;

INSERT INTO companies_address (country, region, city, street, building, room)
VALUES
	("RUS", "saint-petersburg", "saint-petersburg", "nevskiy", "1", "1"),
	("BEL", "minskaya", "minsk", "lenina", "2", "111"),
	("KAZ", "astaninskaya", "astana", "nursultan", "99", "222");
COMMIT;

INSERT INTO companies_company (id, title, description, email, phone, address_id)
VALUES
	(1, "yandex", "yandex software company", "yandex@yandex.ru", "+79313332211", 1),
	(2, "minsk software", "software company in minsk", "minsk@minsk.bel", "+96784333496", 2),
	(3, "kazhah soft", "software company in kazahstan", "kaz@kaz.kz", "+16323432200", 3);
COMMIT;

INSERT INTO jobs_job 
	(job_name, job_description, address_id, company_id, is_archived, max_salary, min_salary, pub_date, required_experience)
VALUES
	("python developer", "Developing in python and django", 1, 1, 1, 200000, 100000, "2023-01-01", "1-3YEARS"),
	("golang developer", "job in belarus", 2, 2, 0, 300000, 200000, "2023-08-30", "3-6YEARS"),
	("java developer", "job in kazahstan", 3, 3, 0, 60000, 50000, CURDATE(), "WITHOUT");
COMMIT;

INSERT INTO jobs_job_skills
	(job_id, skill_id)
VALUES
	(13, 2),
	(13, 4),
	(13, 5),
	(14, 1),
	(14, 5),
	(15, 3),
	(15, 6);
COMMIT;
-- INSERT INTO auth_user (username, first_name, last_name, email, date_joined, is)
-- VALUES
-- 	("georgiy", "georgiy", "ivanov", "georgiy@ivanov.ru", "2023-09-12"),
-- 	("petr", "petr", "ivanov", "petr@ivanov.ru", "2022-09-12")
