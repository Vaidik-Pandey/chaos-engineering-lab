import docker
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

client = docker.from_env()

WATCHED = ['flask-app']
CHECK_INTERVAL = 5

def heal_container(name):
    try:
        container = client.containers.get(name)
        if container.status != 'running':
            logger.warning(f"🚑 HEALING: {name} is {container.status}! Restarting...")
            container.restart()
            logger.info(f"✅ {name} restarted successfully!")
    except Exception as e:
        logger.error(f"Heal error for {name}: {e}")

def run_healer():
    logger.info("🚑 Auto-Healer Started! Watching containers...")
    while True:
        for name in WATCHED:
            heal_container(name)
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    run_healer()
