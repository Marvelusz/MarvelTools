from core.banner import show_banner
from core.menu import show_menu
from core.footer import show_footer

from modules import (
    username,
    email,
    phone,
    ip,
    address,
    coordinate,
    portscan,
    about,
)


def main():
    while True:
        show_banner()
        show_menu()
        show_footer()

        pilihan = input("\n[MARVELUS] Select Menu > ")

        if pilihan == "01":
            username.run()

        elif pilihan == "02":
            email.run()

        elif pilihan == "03":
            phone.run()

        elif pilihan == "04":
            ip.run()

        elif pilihan == "05":
            address.run()

        elif pilihan == "06":
            coordinate.run()

        elif pilihan == "07":
            portscan.run()

        elif pilihan == "08":
            about.run()

        elif pilihan == "00":
            print("\nThank you for using MARVELUS.")
            break

        else:
            input("\nMenu tidak tersedia... (ENTER)")


if __name__ == "__main__":
    main()