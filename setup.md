# Desired initial project structure

FocusForgeAI/
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements-dev.txt           # or use pyproject.toml only
├── .env.example
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── focusforge_agent.py
│   │   └── tools.py
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── google_calendar.py
│   │   └── opik_tracing.py
│   └── utils/
│       ├── __init__.py
│       └── logging.py
├── tests/
│   ├── __init__.py
│   └── test_agent_basic.py
└── scripts/
    └── setup_opik.py