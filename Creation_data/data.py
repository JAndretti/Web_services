import csv
import datetime
import pymysql
import os

# Define the base directory
base_dir = 'BDD/Data'


sensor_dict = {'ACC':1,'BVP':2,'EDA':3,'HR':4,'IBI':5,'tags':6,'TEMP':7}
student_dict = {'S1':1,'S2':2,'S3':3,'S4':4,'S5':5,'S6':6,'S7':7,'S8':8,'S9':9,'S10':10}
exam_dict = {'Final':3,'Midterm 1':1,'Midterm 2':2}
# Open or create a new text file
with open("output.sql", "w") as out:
    # Iterate over the student directories
    for student_dir in os.listdir(base_dir):
        student_dir_path = os.path.join(base_dir, student_dir)  
        if os.path.isdir(student_dir_path):
            # Get the student id from the directory name
            id_student = student_dir
            # Iterate over the exam directories
            for exam_dir in os.listdir(student_dir_path):
                exam_dir_path = os.path.join(student_dir_path, exam_dir)
                if os.path.isdir(exam_dir_path):
                    # Get the exam id from the directory name
                    id_exam =exam_dir
                    # Iterate over the CSV files
                    for file_name in os.listdir(exam_dir_path):
                        if file_name.endswith('.csv'):
                            file_path = os.path.join(exam_dir_path, file_name)
                            # Open the CSV file
                            with open(file_path, 'r') as file:
                                reader = csv.reader(file)
                                # Read the timestamp and sampling rate
                                try:
                                    timestamp=float(next(reader)[0])
                                    sampling_rate=float(next(reader)[0])
                                    # Get the sensor id from the file name
                                    id_sensor = file_name.split('.')[0]
                                    # Iterate over the rows of data
                                    line = next(reader)
                                    i=0 # itération pour réduire le nbr de données
                                    while line and i<=5:
                                        # Compute the acquisition time
                                        timestamp+=sampling_rate
                                        acquisition_time=datetime.datetime.fromtimestamp(int(str(timestamp).split('.')[0]))
                                        acquisition_time=acquisition_time.strftime("%Y-%m-%d %H:%M:%S")
                                        # Insert the data into the database
                                        query = f"INSERT IGNORE INTO Measurements (Id_Student, Id_Sensor, Id_Exam, Acquisition_time, Measurement_value) VALUES {student_dict.get(id_student), sensor_dict.get(id_sensor), exam_dict.get(id_exam), acquisition_time, float(line[0])};" 
                                        line = next(reader)
                                        #print(query)
                                        out.write(query + "\n")
                                        i=i+1

                                except StopIteration:
                                    pass
