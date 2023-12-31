from invoke import task

@task
def start(ctx):
    ctx.run('python3 src/index.py', pty=True)

@task
def start_cli(ctx):
    ctx.run('python3 src/index.py --ui cli', pty=True)

@task
def test(ctx):
    ctx.run('pytest src', pty=True)

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html', pty=True)

@task
def unit_test(ctx):
    ctx.run('pytest src/tests/unit_tests', pty=True)

@task
def integration_test(ctx):
    ctx.run('pytest src/tests/integration_tests', pty=True)

@task
def performance_test(ctx):
    ctx.run('python3 src/performance_test.py', pty=True)

@task
def lint(ctx):
    ctx.run('pylint src', pty=True)

@task
def format(ctx):
    ctx.run('autopep8 --in-place --recursive src', pty=True)
