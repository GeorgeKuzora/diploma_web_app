import aiohttp


class HttpRequestHandler:
    def __init__(self, session=aiohttp.ClientSession()) -> None:
        self.session = session

    async def send_get_request(
        self, url: str, session: aiohttp.ClientSession, **kwargs
    ) -> tuple[int, str]:
        resp = await session.get(url=url, **kwargs)
        resp.raise_for_status()
        status = resp.status
        html = await resp.text()
        return status, html
