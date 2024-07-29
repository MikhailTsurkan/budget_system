from store.controller import Controller
import os

def main():
    controller = Controller.from_file(os.path.join("data", "data.json"))

    controller.manager.create(1000, "cash")

    controller.create_file("data")


main()
