#include <stdio.h>
#include <math.h>

#include <libfixmath/fix16.h>

#include "display.h"

SDL_Window* window = NULL;
SDL_Renderer* renderer = NULL;
uint16_t* color_buffer = NULL;
fix16_t* z_buffer = NULL;
SDL_Texture* color_buffer_texture = NULL;
int window_width = 640;
int window_height = 480;

bool initialize_window(void) {
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        fprintf(stderr, "Error initializing SDL.\n");
        return false;
    }

    // Use SDL to query what is the fullscreen max. width and height
    SDL_DisplayMode display_mode;
    SDL_GetCurrentDisplayMode(0, &display_mode);
    window_width = display_mode.w;
    window_height = display_mode.h;

    // Create a SDL window
    window = SDL_CreateWindow(
        NULL,
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        window_width,
        window_height,
        SDL_WINDOW_BORDERLESS
    );
    if (!window) {
        fprintf(stderr, "Error creating SDL window.\n");
        return false;
    }

    // Create a SDL renderer
    renderer = SDL_CreateRenderer(window, -1, 0);
    if (!renderer) {
        fprintf(stderr, "Error creating SDL renderer.\n");
        return false;
    }
    SDL_SetWindowFullscreen(window, SDL_WINDOW_FULLSCREEN);

    return true;
}

void draw_grid(void) {
    for (int y = 0; y < window_height; y += 10)
        for (int x = 0; x < window_width; x += 10)
            color_buffer[(window_width * y) + x] = 0xF333;
}

void draw_pixel(int x, int y, uint16_t color) {
    if (x >=0 && x < window_width && y >= 0 && y < window_height)
        color_buffer[(window_width * y) + x] = color;
}

void draw_horiz_line(int x0, int x1, int y, uint16_t color) {
    if (x1 < x0) {
        int t = x0;
        x0 = x1;
        x1 = t;
    }    
    for (int x = x0; x <= x1; x++)
        draw_pixel(x, y, color);
}

void draw_line(int x0, int y0, int x1, int y1, uint16_t color) {
    int delta_x = x1 - x0;
    int delta_y = y1 - y0;

    int longest_side_length = (abs(delta_x) >= abs(delta_y)) ? abs(delta_x) : abs(delta_y);

    fix16_t x_inc = fix16_div(fix16_from_int(delta_x), fix16_from_int(longest_side_length));
    fix16_t y_inc = fix16_div(fix16_from_int(delta_y), fix16_from_int(longest_side_length));

    fix16_t x = fix16_from_int(x0);
    fix16_t y = fix16_from_int(y0);
    for (int i = 0; i <= longest_side_length; i++) {
        draw_pixel(fix16_to_int(x), fix16_to_int(y), color);
        x += x_inc;
        y += y_inc;        
    }
}

void draw_rect(int x, int y, int width, int height, uint16_t color) {
    for (int j = y; j < y + height; j++)
        for (int i = x; i < x + width; i++)
            draw_pixel(i, j, color);
}

void render_color_buffer(void) {
    SDL_UpdateTexture(
        color_buffer_texture,
        NULL,
        color_buffer,
        (int)(window_width * sizeof(uint16_t))
    );
    SDL_RenderCopy(renderer, color_buffer_texture, NULL, NULL);
}

void clear_color_buffer(uint16_t color) {
    for (int y = 0; y < window_height; y++) {
        for (int x = 0; x < window_width; x++) {
            color_buffer[(window_width * y) + x] = color;
        }
    }
}

void clear_z_buffer(void) {
    for (int y = 0; y < window_height; y++) {
        for (int x = 0; x < window_width; x++) {
            z_buffer[(window_width * y) + x] = fix16_from_float(1.0);
        }
    }
}

void destroy_window(void) {
    SDL_DestroyTexture(color_buffer_texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}
