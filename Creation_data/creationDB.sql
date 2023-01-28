DROP TABLE IF EXISTS `Student`;
DROP TABLE IF EXISTS `Measurements`;
DROP TABLE IF EXISTS `Exam`;
DROP TABLE IF EXISTS `Sensor`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `Grade`;




CREATE TABLE Student(
   Id_Student INT AUTO_INCREMENT,
   Number VARCHAR(3) NOT NULL,
   PRIMARY KEY(Id_Student),
   UNIQUE(Number)
);
CREATE TABLE Exam(
   Id_Exam INT AUTO_INCREMENT,
   Name VARCHAR(50) NOT NULL,
   PRIMARY KEY(Id_Exam),
   UNIQUE(Name)
);
CREATE TABLE Sensor(
   Id_Sensor INT AUTO_INCREMENT,
   Short_Name VARCHAR(4) NOT NULL,
   PRIMARY KEY(Id_Sensor),
   UNIQUE(Short_Name)
);
CREATE TABLE Measurements(
   Id_Student INT,
   Id_Exam INT,
   Id_Sensor INT,
   Acquisition_time DATETIME,
   Measurement_value DOUBLE,
   PRIMARY KEY(Id_Student, Id_Exam, Id_Sensor, Acquisition_time),
   FOREIGN KEY(Id_Student) REFERENCES Student(Id_Student),
   FOREIGN KEY(Id_Exam) REFERENCES Exam(Id_Exam),
   FOREIGN KEY(Id_Sensor) REFERENCES Sensor(Id_Sensor)
);
CREATE TABLE Grade(
   Id_Student INT,
   Id_Exam INT,
   Grade_value INT NOT NULL,
   PRIMARY KEY(Id_Student, Id_Exam),
   FOREIGN KEY(Id_Student) REFERENCES Student(Id_Student),
   FOREIGN KEY(Id_Exam) REFERENCES Exam(Id_Exam)
);


CREATE TABLE `users` (
  `idUser` int(11) NOT NULL,
  `loginUser` varchar(50) NOT NULL,
  `pwdUser` varchar(50) NOT NULL,
  `rights` enum('read','all','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`idUser`, `loginUser`, `pwdUser`, `rights`) VALUES
(1, 'Joan', PASSWORD('Andromede432'), 'read'),
(2, 'Mary', PASSWORD('Passiflore812'), 'all');