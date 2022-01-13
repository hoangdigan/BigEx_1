
-- BIG EXCERCISE 1 - PYTHON 01 CLASS

DROP DATABASE IF EXISTS StudentScores;
CREATE DATABASE StudentScores;
USE StudentScores;

CREATE TABLE Students (	
	student_id 				SMALLINT AUTO_INCREMENT PRIMARY KEY,  
	full_name 				VARCHAR(50) NOT NULL,
    birthday				DATE NOT NULL,
    sex						ENUM('0', '1'),
    phone					VARCHAR(50) UNIQUE KEY NOT NULL,
    email 					VARCHAR(50) UNIQUE KEY NOT NULL,
    address					VARCHAR(150)    
);

CREATE TABLE Subjects (	
	subject_id				SMALLINT AUTO_INCREMENT PRIMARY KEY, 
	subject_name			VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
);	
	
CREATE TABLE Scores (	
	student_id				SMALLINT,  
	subject_id				SMALLINT,  
	process_scores		    TINYINT,  
    exam_scores				TINYINT,
	final_scores			DOUBLE AS ((process_scores + exam_scores*2)/3),
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON UPDATE CASCADE ON DELETE CASCADE 
);	
