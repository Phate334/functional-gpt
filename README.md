# Functonal GPT

This PoC is inspired by Meta Toolformer and LangChain agents.

## Examples

```bash
> poetry run fgpt --help
> poetry run fgpt "How's the weather in NewYork"
The weather in NewYork is rainy.
> poetry run fgpt "How's the weather in NewYork and air quality"
The weather in NewYork is currently cloudy. As for the air quality, the information provided only states that it is normal, but does not provide any specific measurements or ratings.
> poetry run fgpt 今天台灣的天氣狀況
今天台灣的天氣狀況是多雲的。
```

## How to run

- Install dependencies:

```bash
poetry install
```

- create a .env file with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
```

- Run

```bash
poetry run gpt --help
```
