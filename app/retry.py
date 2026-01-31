import asyncio


async def retry_with_backoff(func, retries=5, base_delay=1):

    attempt = 0

    while attempt < retries:
        try:
            return await func()

        except Exception as e:
            wait_time = base_delay * (2 ** attempt)

            print(f"Retry {attempt + 1} failed. Retrying in {wait_time} seconds...")

            await asyncio.sleep(wait_time)
            attempt += 1

    raise Exception("AI Service Failed After Multiple Retries")
