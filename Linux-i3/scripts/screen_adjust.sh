#!/usr/bin/env bash

set -euo pipefail

INTERNAL_OUTPUT=$(xrandr --query | awk '$2 == "connected" && $1 ~ /^eDP/ { print $1; exit }')
EXTERNAL_OUTPUT=$(xrandr --query | awk '$2 == "connected" && $1 ~ /^(HDMI|DP)-/ { print $1; exit }')

if [[ -z "$INTERNAL_OUTPUT" ]]; then
	echo "Could not detect the built-in display."
	exit 1
fi

if [[ -z "$EXTERNAL_OUTPUT" ]]; then
	echo "No external display is connected."
	exit 1
fi

get_modes() {
	local output_name=$1

	xrandr --query | awk -v output_name="$output_name" '
		$1 == output_name { in_section = 1; next }
		in_section && $2 ~ /connected|disconnected/ { exit }
		in_section && $1 ~ /^[0-9]+x[0-9]+$/ { print $1 }
	'
}

find_common_mode() {
	local internal_mode

	while read -r internal_mode; do
		[[ -z "$internal_mode" ]] && continue

		if get_modes "$EXTERNAL_OUTPUT" | grep -Fxq "$internal_mode"; then
			printf '%s\n' "$internal_mode"
			return 0
		fi
	done < <(get_modes "$INTERNAL_OUTPUT")

	return 1
}

echo "Pick an option:"
echo "   1 - Extend using the external screen"
echo "   2 - Mirror to the external screen"
read -r conf

case "$conf" in
	1)
		xrandr \
			--output "$INTERNAL_OUTPUT" --primary --auto \
			--output "$EXTERNAL_OUTPUT" --auto --right-of "$INTERNAL_OUTPUT"
		;;
	2)
		COMMON_MODE=$(find_common_mode || true)

		if [[ -z "$COMMON_MODE" ]]; then
			echo "No shared resolution found for $INTERNAL_OUTPUT and $EXTERNAL_OUTPUT."
			exit 1
		fi

		xrandr \
			--output "$INTERNAL_OUTPUT" --mode "$COMMON_MODE" --primary \
			--output "$EXTERNAL_OUTPUT" --mode "$COMMON_MODE" --same-as "$INTERNAL_OUTPUT"
		;;
	*)
		echo "Invalid option: $conf"
		exit 1
		;;
esac
