import tkinter as tk


class LicznikKlikniec:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Licznik kliknięć")
        self.root.geometry("320x200")
        self.root.resizable(False, False)

        self.licznik = 0

        self.etykieta = tk.Label(
            root,
            text=self._tekst_licznika(),
            font=("Segoe UI", 24),
        )
        self.etykieta.pack(pady=(30, 20))

        ramka_przyciskow = tk.Frame(root)
        ramka_przyciskow.pack()

        tk.Button(
            ramka_przyciskow,
            text="Kliknij",
            width=12,
            command=self.kliknij,
        ).pack(side=tk.LEFT, padx=8)

        tk.Button(
            ramka_przyciskow,
            text="Resetuj",
            width=12,
            command=self.resetuj,
        ).pack(side=tk.LEFT, padx=8)

    def _tekst_licznika(self) -> str:
        return str(self.licznik)

    def kliknij(self) -> None:
        self.licznik += 1
        self.etykieta.config(text=self._tekst_licznika())

    def resetuj(self) -> None:
        self.licznik = 0
        self.etykieta.config(text=self._tekst_licznika())


def main() -> None:
    root = tk.Tk()
    LicznikKlikniec(root)
    root.mainloop()


if __name__ == "__main__":
    main()
