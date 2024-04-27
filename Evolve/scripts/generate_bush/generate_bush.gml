// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information

function get_bush_sprite(_bush_id)
{
	switch (_bush_id)
	{
	    case BUSH_HARD:			return spr_bush_hard;
	    case BUSH_HARD_SMALL:	return spr_bush_hard_small;
	    case BUSH_SOFT:			return spr_bush_soft;
	    case BUSH_SOFT_SMALL:	return spr_bush_soft_small;
	    case BUSH_RED:			return spr_bush_red;
	    case BUSH_PINK:			return spr_bush_pink;
	    case BUSH_ORANGE:		return spr_bush_orange;
	    case CACTUS_BIG:		return spr_cactus_big;
	    case CACTUS_SMALL:		return spr_cactus;
	    default:				return noone;
	}
}

function generate_bush(_x_pos, _y_pos)
{
	var bush_id = irandom_range(1, 9);
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_bush);
	inst.sprite_index = get_bush_sprite(bush_id);
}


function generate_grass(_x_pos, _y_pos)
{
	var potential_sprites = [spr_fern_hard, spr_fern_hard_small, spr_fern_soft, spr_fern_soft_small]
	var spr_ref = potential_sprites[irandom(array_length(potential_sprites)-1)];
					
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_grass);
	inst.sprite_index = spr_ref
}