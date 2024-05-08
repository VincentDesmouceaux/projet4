# main.py

from controllers.application_controller import ApplicationController


def main():
    app_controller = ApplicationController('src/data/tournaments.json')
    app_controller.start()


if __name__ == '__main__':
    main()
