// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information

function generate_bush(_x_pos, _y_pos)
{
	var potential_sprites = [spr_bush_hard, spr_bush_orange, spr_bush_pink, spr_bush_red,
		spr_bush_soft, spr_bush_hard_small, spr_bush_soft_small, spr_bush_hard, spr_bush_soft,
		spr_cactus, spr_cactus_big];
	var spr_ref = potential_sprites[irandom(array_length(potential_sprites)-1)];
					
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_bush);
	inst.sprite_index = spr_ref
}

function generate_grass(_x_pos, _y_pos)
{
	var potential_sprites = [spr_fern_hard, spr_fern_hard_small, spr_fern_soft, spr_fern_soft_small]
	var spr_ref = potential_sprites[irandom(array_length(potential_sprites)-1)];
					
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_grass);
	inst.sprite_index = spr_ref
}