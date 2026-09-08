import asyncio
import logging
from config import PORT, USERS, MODES

logging.basicConfig(level=logging.INFO)

async def main():
    logging.info(f"Starting MTProto proxy on port {PORT}")
    logging.info(f"Users loaded: {list(USERS.keys())}")
    logging.info(f"Modes: {MODES}")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
