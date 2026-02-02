"""FocusForge AI entry point."""

from src.config import Settings


def main() -> None:
    """Run the FocusForge AI application."""
    settings = Settings()
    _ = settings  # Config loaded and validated
    print("FocusForge AI starting...")


if __name__ == "__main__":
    main()
