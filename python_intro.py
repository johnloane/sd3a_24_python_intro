from PIL import Image, ImageFilter, ImageDraw
import face_recognition
import numpy as np
import sys


def main():
    truncation()


def hello_world():
    print("Hello, world!")


def blur(image):
    before = Image.open(image)
    after = before.filter(ImageFilter.BoxBlur(10))
    after.save("blurred.jpg")


def edges(image):
    before = Image.open(image)
    after = before.filter(ImageFilter.FIND_EDGES)
    after.save("edges.jpg")


def find_faces(image):
    image_to_search = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(image_to_search)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image_to_search[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()


def find_individual_face_in_group(individual_face_image, group_image):
    known_face = face_recognition.load_image_file(individual_face_image)
    known_face_encoding = face_recognition.face_encodings(known_face)[0]
    image_to_search = face_recognition.load_image_file(group_image)
    face_locations = face_recognition.face_locations(image_to_search)
    face_encodings = face_recognition.face_encodings(image_to_search, face_locations)
    pil_image = Image.open(group_image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encodings in zip(
        face_locations, face_encodings
    ):
        matches = face_recognition.compare_faces([known_face_encoding], face_encodings)
        face_distances = face_recognition.face_distance(
            [known_face_encoding], face_encodings
        )
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=5)
    del draw
    pil_image.show()


def greet_person():
    name = input("What is your name? ")
    print(f"Hello, {name}!")


# Types
# str, int, float, bool, list, tuple, dict, set, NoneType


def add_two_integers():
    x = get_integer()
    y = get_integer()
    print(f"{x} + {y} is {x+y}")


def get_integer():
    while True:
        try:
            x = int(input("Enter integer: "))
            break
        except ValueError:
            print("Not an integer, please try again")
    return x


def compare_two_integers():
    x = get_integer()
    y = get_integer()
    if x < y:
        print(f"{x} is less than {y}")
    elif x > y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{x} is equal to {y}")


def do_you_agree():
    response = input("Do you agree? ")
    if response.lower() in ["yes", "y"]:
        print("You agree!")
    else:
        print("You do not agree!")


def test_loops():
    for i in range(5):
        print("IoT is my favourite subject!")


def truncation():
    x = 10
    y = 3
    print(f"{x} // {y} is {x//y}")


if __name__ == "__main__":
    main()
