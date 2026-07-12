from pathlib import Path

# Configuración de la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]

class EduGPT:
    def __init__(self):
        self.name = "EduGPT"
        self.version = "0.0.2"
        self.books_path = BASE_DIR / "data" / "books"
        self.processed_path = BASE_DIR / "data" / "processed"
        self.corpus_path = self.processed_path / "corpus.txt"
        self.corpus = []
        self.vocabulary = set()
        self.total_words = 0

    def show_information(self):
        print("=" * 45)
        print(f"{self.name} v{self.version}")
        print("=" * 45)
        print()
        print(f"Modelo: {self.name}")
        print("Estado: Activo")
        print(f"Corpus cargado: {self.total_words} palabras")
        print(f"Vocabulario: {len(self.vocabulary)} palabras")
        print()
        print("EduGPT:")
        print("Hola, todavía no sé nada.")
        print("Enséñame un libro.")

    def find_books(self):
        books = list(self.books_path.glob("*.txt"))
        return books

    def show_books(self):
        books = self.find_books()
        print("\n========== LIBROS ENCONTRADOS ==========\n")
        if not books:
            print("No se encontró ningún libro.")
            return
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.name}")
        print(f"\nTotal de libros: {len(books)}")

    def read_books(self, books):
        corpus = ""
        print("\nLeyendo libros...\n")
        for book in books:
            print(f"> Leyendo: {book.name}")
            with open(book, "r", encoding="utf-8") as file:
                corpus += file.read()
            corpus += "\n"
        return corpus

    def save_corpus(self, corpus):
        self.processed_path.mkdir(parents=True, exist_ok=True)
        with open(self.corpus_path, "w", encoding="utf-8") as file:
            file.write(corpus)

    def build_corpus(self):
        books = self.find_books()
        print("\n********** CONSTRUCCIÓN DEL CORPUS **********")
        if not books:
            print("\nNo se encontraron libros.")
            return
        print("\nLibros encontrados:\n")
        for book in books:
            print(f"- {book.name}")
        corpus = self.read_books(books)
        self.save_corpus(corpus)
        print("Corpus construido exitosamente.")
        # Mostramos la información tan pronto termina de construirlo
        self.show_corpus_information(books, corpus)

    def show_corpus_information(self, books, corpus):
        total_books = len(books)
        total_characters = len(corpus)
        total_lines = len(corpus.splitlines())
        total_words = len(corpus.split())
        print("\n--- Estadísticas del Corpus ---")
        print(f"Libros procesados: {total_books}")
        print(f"Caracteres: {total_characters}")
        print(f"Líneas: {total_lines}")
        print(f"Palabras: {total_words}")
        print()
        print(f"Archivo generado: {self.corpus_path}")

    def show_menu(self):
        print("\n" + "=" * 45)
        print(f"         MENÚ PRINCIPAL - {self.name}")
        print("=" * 45)
        print("1. Construir corpus")
        print("2. Entrenar modelo")
        print("3. Información del modelo")
        print("0. Salir")
        print()
        return input("Seleccione una opción: ")

    def train(self):
        print()
        print("=" * 45)
        print("ENTRENAMIENTO")
        print("=" * 45)
        print()
        print("Esta función estará disponible próximamente.")