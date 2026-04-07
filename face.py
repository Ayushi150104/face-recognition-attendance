import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

Debalina_image = face_recognition.load_image_file("Debalina Jana.jpeg")
Debalina_encoding = face_recognition.face_encodings(Debalina_image)[0]

Ayushi_image = face_recognition.load_image_file("Ayushi Choudhary.jpeg")
Ayushi_encoding = face_recognition.face_encodings(Ayushi_image)[0]

known_face_encodings = [Debalina_encoding, Ayushi_encoding]
known_face_names = ["Debalina", "Ayushi"]

students = known_face_names.copy()

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations
    )

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding
        )

        face_distance = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )

        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            cv2.putText(
                frame,
                name + " Present",
                (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (255, 0, 0),
                3,
                2,
            )

            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
