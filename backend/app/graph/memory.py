import sqlite3
from pathlib import Path

from langgraph.checkpoint.sqlite import SqliteSaver


# backend/
BACKEND_DIR = Path(__file__).resolve().parents[2]

# backend/conversation_memory.db
MEMORY_DB_PATH = (
    BACKEND_DIR / "conversation_memory.db"
)


# Create SQLite connection for LangGraph memory.
#
# check_same_thread=False is required because
# FastAPI may handle requests using different threads.
memory_connection = sqlite3.connect(
    str(MEMORY_DB_PATH),
    check_same_thread=False
)


# LangGraph checkpointer
checkpointer = SqliteSaver(
    memory_connection
)