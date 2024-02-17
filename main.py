import sys
from bot import Bot

def send(channel: str, *args):
    payload = args[0] if len(args) > 0 else None

    message = "\n<<zilch>>." + channel

    if payload is not None:
        message += "." + payload

    message += "\n"

    print(message, end="", file=sys.stderr)

def parse_payload(payload):
    parts = payload.split(",")

    return [
        {
            "x": float(parts[0]),
            "y": float(parts[1])
        },
        {
            "x": float(parts[2]),
            "y": float(parts[3])
        }
    ]

send("ready")

bot: Bot = None

while True:
    data = sys.stdin.readline().strip()
    channel, payload = data.split(".", 1)

    if channel == "start":
        standard_config, custom_config = payload.split(".", 1)
        game_time_limit, turn_time_limit, player = standard_config.split(",", 2)
        config = {
            "game_time_limit": int(game_time_limit),
            "turn_time_limit": int(turn_time_limit),
            "paddle": "west" if player == "0" else "east"
        }
        bot = Bot(config)
        send("start")
        continue

    if channel == "move":
        move = bot.move(*parse_payload(payload))
        send("move", move)
        continue

    if channel == "end":
        bot.end(*parse_payload(payload))
        continue
