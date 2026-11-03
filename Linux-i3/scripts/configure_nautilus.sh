#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)

ensure_dbus_session() {
	if [[ -n "${DBUS_SESSION_BUS_ADDRESS:-}" ]]; then
		return
	fi

	if command -v dbus-run-session >/dev/null 2>&1; then
		echo "No DBus session detected; re-running under dbus-run-session."
		exec dbus-run-session -- bash "$0" "$@"
	fi

	if command -v dbus-launch >/dev/null 2>&1; then
		eval "$(dbus-launch --sh-syntax)"
		export DBUS_SESSION_BUS_ADDRESS DBUS_SESSION_BUS_PID
		return
	fi

	echo "No DBus session and no dbus launcher found; gsettings may not persist."
}

if ! command -v gsettings >/dev/null 2>&1; then
	echo "gsettings not found; skipping Nautilus configuration."
	exit 0
fi

ensure_dbus_session "$@"

schema_exists() {
	gsettings list-schemas | grep -qx "$1"
}

key_exists() {
	gsettings list-keys "$1" | grep -qx "$2"
}

set_key_if_available() {
	local schema="$1"
	local key="$2"
	local value="$3"

	if schema_exists "$schema" && key_exists "$schema" "$key"; then
		gsettings set "$schema" "$key" "$value"
		echo "Set $schema::$key"
	else
		echo "Info: optional key not available on this system: $schema::$key"
	fi
}

set_first_valid_enum_value() {
	local schema="$1"
	local key="$2"
	shift 2

	if ! schema_exists "$schema" || ! key_exists "$schema" "$key"; then
		echo "Info: optional key not available on this system: $schema::$key"
		return
	fi

	local range_output
	range_output=$(gsettings range "$schema" "$key" 2>/dev/null || true)

	local candidate
	for candidate in "$@"; do
		if printf '%s\n' "$range_output" | grep -Fxq "'$candidate'"; then
			set_key_if_available "$schema" "$key" "'$candidate'"
			return
		fi
	done

	echo "Info: optional enum setting unavailable for $schema::$key on this system."
}

# Keep behavior predictable without requiring a full GNOME session.
set_key_if_available org.gnome.nautilus.preferences default-folder-viewer "'list-view'"
set_key_if_available org.gnome.nautilus.preferences executable-text-activation "'ask'"
set_key_if_available org.gnome.nautilus.preferences show-delete-permanently true
set_key_if_available org.gnome.nautilus.preferences show-create-link true
set_first_valid_enum_value org.gnome.nautilus.list-view default-zoom-level medium small large
set_first_valid_enum_value org.gnome.nautilus.icon-view default-zoom-level medium small-plus small large extra-large

# Dark appearance settings used by Nautilus and other GTK apps.
set_key_if_available org.gnome.desktop.interface color-scheme "'prefer-dark'"
set_key_if_available org.gnome.desktop.interface gtk-theme "'Adwaita-dark'"
set_key_if_available org.gnome.desktop.interface icon-theme "'Adwaita'"

# Nautilus uses GTK4 on modern distros, so copy matching theme CSS if present.
if [[ -f "$REPO_ROOT/.config/gtk-4.0/gtk.css" ]]; then
	mkdir -p "$HOME/.config/gtk-4.0"
	cp "$REPO_ROOT/.config/gtk-4.0/gtk.css" "$HOME/.config/gtk-4.0/gtk.css"
	echo "Applied GTK4 CSS for Nautilus theme."
fi

echo "Nautilus configuration complete."
