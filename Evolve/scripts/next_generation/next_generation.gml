// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function mutate_consumables_struct(consumables, mutation_range)
{
    var keys = ["CONSUME_BUSH_HARD", "CONSUME_BUSH_SOFT", "CONSUME_BUSH_HARD_SMALL", "CONSUME_BUSH_SOFT_SMALL", "CONSUME_BUSH_RED", "CONSUME_BUSH_PINK", "CONSUME_BUSH_ORANGE", "CONSUME_CACTUS_BIG", "CONSUME_CACTUS_SMALL", "CONSUME_FERN_HARD", "CONSUME_FERN_SOFT", "CONSUME_FERN_HARD_SMALL", "CONSUME_FERN_SOFT_SMALL"];
    
    for (var i = 0; i < array_length(keys); i++) {
        var key = keys[i];
        var old_value = consumables[$ key];
        var mutated_value = old_value + random_range(-mutation_range, mutation_range);
        consumables[$ key] = clamp(mutated_value, -0.1, 1.1);
    }
}

function copyStruct(struct)
{
    var key, value;
    var newCopy = {};
    var keys = variable_struct_get_names(struct);
    for (var i = array_length(keys)-1; i >= 0; --i) {
            key = keys[i];
            value = struct[$ key];
            variable_struct_get(struct, key);
            variable_struct_set(newCopy, key, value)
    }
    return newCopy;
}

function next_generation()
{
	ds_list_destroy(global.color_list);
	global.color_list = undefined;
	
	var mutation_range = 0.2;
	
	var max_ticks = 0;
	var inst = noone;
	with (o_tribe) {
    if (ticks_survived > max_ticks) {
        max_ticks = ticks_survived;
        inst = id; // 'id' is the built-in variable holding the instance's unique identifier
		}
	}

	decisions = copyStruct(inst.decisions)
	
	with (o_tribe) {
		instance_destroy(self);
	}
	with (o_bush) {
		instance_destroy(self);
	}
	generate_environment()
	
	// Parameters
	var num_points = global.NUMBER_OF_TRIBES; // Number of points or tribes
	var radius = room_width div 4;   // Radius of the circle on which points will be placed

	// Center of the room
	var center_x = room_width / 2;
	var center_y = room_height / 2;

	// Angle between each point (in degrees)
	var angle_step = 360 / num_points;

	// Creating points
	for (var i = 0; i < num_points; i++)
	{
	    // Calculate angle in radians
	    var angle = degtorad(i * angle_step);

	    // Calculate x and y coordinates
	    var _x = center_x + radius * cos(angle);
	    var _y = center_y + radius * sin(angle);
    
	    // Generate Tribe at Position
		_struct = copyStruct(decisions);
		mutate_consumables_struct(_struct, mutation_range);
		
		instance_create_layer(_x, _y, "Instances", o_tribe, {
		decisions: _struct,
		tribe_color: get_random_color()});
	}
}