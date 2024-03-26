#!/usr/bin/env python
import logging

from sqlmodel import Session

from hexon.db.engine import engine
from hexon.db.init_db import init_db, load_cards

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    with Session(engine) as session:  # type: ignore[attr-defined]
        init_db(session)
        load_cards(session)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
