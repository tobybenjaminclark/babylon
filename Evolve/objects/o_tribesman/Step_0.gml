/// @description Insert description here
// You can write your code in this editor

image_blend = parent.tribe_color;

if state == TRIBESMAN_STATES.WANDER
{
	switch (dir) {
	    case 0: // Up
	        y = y - _speed;
	        break;
	    case 1: // Right
	        x = x + _speed;
	        break;
	    case 2: // Down
	        y = y + _speed;
	        break;
	    case 3: // Left
	        x = x - _speed;
	        break;
	}

	// Change direction randomly
	if (irandom_range(0, 30) == 1){ // 5% chance to change direction every step
	    dir = irandom_range(0, 3);
	}
	
	if (irandom(5) == 1) state = TRIBESMAN_STATES.GATHER;
}
else if state == TRIBESMAN_STATES.GATHER
{
	var nearest_bush = instance_nearest(x, y, o_bush);

	// Move towards the nearest o_bush instance
	if (nearest_bush != noone)
	{
	    var bush_dir = point_direction(x, y, nearest_bush.x, nearest_bush.y);
	    var x_move = lengthdir_x(_speed, bush_dir);
	    var y_move = lengthdir_y(_speed, bush_dir);
		
		x += x_move;
		y += y_move;
		if(TELEPORT)
		{
			x = nearest_bush.x;
			y = nearest_bush.y;
		}
		
		// Check if the object has reached the bush
		if (point_distance(x, y, nearest_bush.x, nearest_bush.y) <= distance_threshold || TELEPORT)
		{
			_id = nearest_bush.o_id;
			_chance = get_action(parent.decisions, _id, CONSUME)
			
			if (random(1) < _chance)
			{
				if (_id == BUSH_RED)
				{
					parent.tribesmen_count = parent.tribesmen_count - 1;
					instance_destroy(self);
					return;
				}
				else
				{
					state = TRIBESMAN_STATES.WANDER;
					instance_destroy(nearest_bush);
				}
			}
			else
			{
				state = TRIBESMAN_STATES.WANDER;
			}
		}
	}
	else
	{
		state = TRIBESMAN_STATES.WANDER;
	}
}

// Prevent the walker from going out of bounds
x = clamp(x, 0, room_width);
y = clamp(y, 0, room_height);



