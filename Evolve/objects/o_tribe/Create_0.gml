/// @description Insert description here
// You can write your code in this editor

ticks_survived = 0;
tribesmen_count = 0;
image_blend = tribe_color;

/* Spawn Initial Tribesmen */
for (var temp_index = 0; temp_index < global.STARTING_TRIBESMEN_COUNT; temp_index++)
{
	tribesmen_count = tribesmen_count + 1;
	_self = self;
	var inst = instance_create_layer(x, y, "Instances", o_tribesman, {parent: _self});
}





