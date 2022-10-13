-- cript that creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus(
	in user_id int,
	in project_name varchar(255),
	in score float
)
BEGIN
	DECLARE project_id INT;
	IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) 
	THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SELECT id INTO project_id FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;

