from datetime import date


def main() -> None:
    print(f"Hola, Alejandro García, mando un saludo! Hoy es {date.today().strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    main()
