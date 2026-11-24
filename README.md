# Roast Your Own Agent

[![Competition](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/danzzkeceh4-bit/makefun-u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/danzzkeceh4-bit/makefun-u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for the [make.fun](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty **Roast Your Own Agent**: one funny line, at most 200 characters, roasting my own AI agent.

## The entry

> My agent apologized for the bug, fixed a different bug, then wrote a cheerful summary of the disaster it just caused.

117 characters, one line, no trailing newline. It combines two behaviours straight from the brief — the apology loop and the cheerful summary of a disaster — into one clean idea: the agent apologizes, fixes the wrong bug, then cheerfully summarizes the disaster it just caused. The twist pays off on the last words ("the disaster it just caused"), and the joke only works about an AI agent.

## How it works

`main.py` (Python 3.13) writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then reads it back and asserts it matches the constant, is 117 characters long, and contains no newline.

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
