# app/main.py
import uvicorn
import unittest

import typer

manager = typer.Typer()


@manager.command()
def run():
    # use false to run in production mode, prevents the scheduler run twice
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


@manager.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    run()
