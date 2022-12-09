import uvicorn
from config import config, AppEnvironment


"""No need of below code as we have changed the flow of env variables."""
# @click.command()
# @click.option(
#     "--env",
#     type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
#     default="local",
# )
# @click.option(
#     "--debug",
#     type=click.BOOL,
#     is_flag=True,
#     default=False,
# )


def main():
    uvicorn.run(
        app="app.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=False if config.ENV == AppEnvironment.Production else True,
        workers=1,
    )


if __name__ == "__main__":
    main()
