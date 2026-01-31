import random
import asyncio


async def mock_ai_service(audio_data: str):

    # Random latency (1 to 3 seconds)
    await asyncio.sleep(random.randint(1, 3))

    # 25% failure chance
    if random.random() < 0.25:
        raise Exception("External AI API Failed (503)")

    return "Transcription successful: Hello from AI"
