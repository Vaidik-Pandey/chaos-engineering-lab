import docker
import time
import random
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

client = docker.from_env()

TARGETS = ['flask-app']
CHAOS_INTERVAL = 30

def kill_container(name):
    try:
        container = client.containers.get(name)
        logger.warning(f"🐒 CHAOS: Killing container {name}!")
        container.stop()
        logger.info(f"💀 Container {name} stopped!")
        return True
    except Exception as e:
        logger.error(f"Error killing {name}: {e}")
        return False

def get_container_status(name):
    try:
        container = client.containers.get(name)
        return container.status
    except:
        return "not found"

def run_chaos():
    logger.info("🐒 Chaos Monkey Started! No container is safe...")
    while True:
        target = random.choice(TARGETS)
        status = get_container_status(target)
        logger.info(f"👀 Checking {target} → Status: {status}")
        if status == 'running':
            kill_container(target)
        else:
            logger.info(f"⚠️ {target} already down, skipping...")
        logger.info(f"😴 Sleeping {CHAOS_INTERVAL} seconds before next attack...")
        time.sleep(CHAOS_INTERVAL)

if __name__ == '__main__':
    run_chaos()
