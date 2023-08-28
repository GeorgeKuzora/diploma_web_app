import aiohttp
import asyncio


class HttpRequestHandler:
    async def send_get_request(
        self,
        url: str,
        session: aiohttp.ClientSession,
        params: dict | None = None,
        headers: dict | None = None,
        *args, **kwargs
    ) -> str:
        resp = await session.get(url=url, params=params, headers=headers, *args, **kwargs)
        resp.raise_for_status()
        html = await resp.text()
        return html
