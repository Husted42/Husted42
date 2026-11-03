#!/usr/bin/env bash

set -euo pipefail

if ! command -v rofi >/dev/null 2>&1; then
	echo "rofi not found"
	exit 1
fi

if ! command -v notify-send >/dev/null 2>&1; then
	echo "notify-send not found (install libnotify-bin)"
	exit 1
fi

title="Husted42"
message=$(printf "" | rofi -dmenu -p "Send notification" -mesg "Type a message and press Enter")

if [[ -z "${message// }" ]]; then
	exit 0
fi

notify-send --app-name="Rofi Notify" --urgency=normal --icon=dialog-information "$title" "$message"
