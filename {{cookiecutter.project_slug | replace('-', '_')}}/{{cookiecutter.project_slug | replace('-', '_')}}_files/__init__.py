from loguru import logger

def run(secret_config, cwd):
    logger.info("Hello {{ cookiecutter.project_slug }}!")

    logger.info("Goodbye.")