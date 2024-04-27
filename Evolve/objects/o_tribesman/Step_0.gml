/// @description Insert description here
// You can write your code in this editor

if state == TRIBESMAN_STATES.WANDER
{
	switch (dir) {
	    case 0: // Up
	        y -= speed;
	        break;
	    case 1: // Right
	        x += speed;
	        break;
	    case 2: // Down
	        y += speed;
	        break;
	    case 3: // Left
	        x -= speed;
	        break;
	}

	// Change direction randomly
	if (random(100) < 5) { // 5% chance to change direction every step
	    dir = irandom(3);
	}

	// Prevent the walker from going out of bounds
	x = clamp(x, 0, room_width);
	y = clamp(y, 0, room_height);
	
	if (irandom(100) == 1) state = TRIBESMAN_STATES.GATHER;
}
else if state == TRIBESMAN_STATES.GATHER
{
	/* Gather resources */
	// Find the nearest o_bush instance
	var nearest_bush = instance_nearest(x, y, o_bush);

	// Move towards the nearest o_bush instance
	if (nearest_bush != noone) {
	    var dir2 = point_direction(x, y, nearest_bush.x, nearest_bush.y);
	    var x_move = lengthdir_x(speed, dir2);
	    var y_move = lengthdir_y(speed, dir2);
	    x += x_move;
	    y += y_move;
	}
	// Check if the object has reached the bush
    if (point_distance(x, y, nearest_bush.x, nearest_bush.y) <= distance_threshold) {
        // Your object has reached the bush
		instance_destroy(nearest_bush)
        state = TRIBESMAN_STATES.WANDER;
        // You can add any actions you want to perform when reaching the bush here
    }
}



