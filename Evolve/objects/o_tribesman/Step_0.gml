/// @description Insert description here
// You can write your code in this editor

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



