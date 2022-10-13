-- script that creates an index inx_name_first_score on the table names and the first letter of the name and the score

CREATE INDEX idx_name_first_score ON names (name(1), score);