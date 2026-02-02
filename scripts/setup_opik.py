#!/usr/bin/env python3
"""Initialize Opik client for tracing and observability."""

from dotenv import load_dotenv

load_dotenv()  # Load .env before importing opik (OPIK_API_KEY)

from opik import Opik


def init_opik(api_key: str | None = None) -> Opik:
    """Initialize and return an Opik client.

    Args:
        api_key: Opik API key. If None, reads from OPIK_API_KEY env var.

    Returns:
        Configured Opik client instance.
    """
    client = Opik(api_key=api_key)
    return client


if __name__ == "__main__":
    # Example: initialize Opik (loads OPIK_API_KEY from env if not passed)
    client = init_opik()
    print("Opik client initialized successfully.")
