import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        yield page

        if request.node.rep_call.failed:
            context.tracing.stop(
                path=f"traces/{request.node.name}.zip"
            )
        else:
            context.tracing.stop()

        context.close()
        browser.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "artifacts/videos/",
    }



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)