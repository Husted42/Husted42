// Sort enemies by distance to exit (ascending)
auto insertion_sort_enemy_range(auto arr) {
    for (int i = 1; i < arr.size(); i++) {
        auto key = arr[i]; // Enemy to insert
        int j = i - 1;

        while (j >= 0 && arr[j].distance_to_exit > key.distance_to_exit) {
            arr[j + 1] = arr[j]; // Shift right
            j--;
        }

        arr[j + 1] = key; // Insert enemy
    }
    return arr;
}

// Sort all enemies
auto sorted_list = insertion_sort_enemy_range(me.enemies_in_range);

// Prioritize armored enemies
auto e_armored = sorted_list[0];

for (auto e : sorted_list) {
    if (e.is_armored) {
        e_armored = e;
        break; // Stop at first armored enemy
    }
}

// Shoot compatible enemies in sorted order
for (auto e : sorted_list) {
    if (me.is_tesla && e.is_flying) {
        me.shoot(e);
    }
	else if (me.is_sniper) {
		me.shoot(e_armored)
	}
    else if (me.is_arrow && !e.is_flying) {
        me.shoot(e);
    }
	else {
		me.shoot(e)
	}
}