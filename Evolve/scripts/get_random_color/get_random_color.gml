// Script assets have changed for v2.3.0 see

function get_random_color()
{
    // Generate random values for red, green, and blue components
    var r = irandom(255); 
    var g = irandom(255);
    var b = irandom(255);
    
    // Combine these into one color value
    var color = make_colour_rgb(r, g, b);
    
    return color;
}