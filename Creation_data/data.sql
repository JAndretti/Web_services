INSERT IGNORE INTO Student (Number) VALUES ('S1');
INSERT IGNORE INTO Student (Number) VALUES ('S2');
INSERT IGNORE INTO Student (Number) VALUES ('S3');
INSERT IGNORE INTO Student (Number) VALUES ('S4');
INSERT IGNORE INTO Student (Number) VALUES ('S5');
INSERT IGNORE INTO Student (Number) VALUES ('S6');
INSERT IGNORE INTO Student (Number) VALUES ('S7');
INSERT IGNORE INTO Student (Number) VALUES ('S8');
INSERT IGNORE INTO Student (Number) VALUES ('S9');
INSERT IGNORE INTO Student (Number) VALUES ('S10');


INSERT IGNORE INTO Sensor (Short_Name) VALUES ('ACC');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('BVP');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('EDA');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('HR');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('IBI');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('tags');
INSERT IGNORE INTO Sensor (Short_Name) VALUES ('TEMP');

INSERT IGNORE INTO Exam (Name) VALUES ('Midterm 1');
INSERT IGNORE INTO Exam (Name) VALUES ('Midterm 2');
INSERT IGNORE INTO Exam (Name) VALUES ('Final');


INSERT IGNORE INTO Measurements (Id_Student, Id_Sensor, Id_Exam, Acquisition_time, Measurement_value) VALUES (5, 7, 2, '2018-11-10 15:18:22', 22.17);
INSERT IGNORE INTO Measurements (Id_Student, Id_Sensor, Id_Exam, Acquisition_time, Measurement_value) VALUES (5, 7, 2, '2018-11-10 15:18:26', 22.17);
INSERT IGNORE INTO Measurements (Id_Student, Id_Sensor, Id_Exam, Acquisition_time, Measurement_value) VALUES (5, 7, 2, '2018-11-10 15:18:30', 22.17);





