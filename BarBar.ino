#include <FastLED.h>
#include "image.h"

// Microcontroller specific defines
#define DATA_PIN 2
#define DELAY 4

// LED specific defines
#define COLOR_ORDER GRB
#define CHIPSET WS2812
#define BRIGHTNESS  128

void loop() {
    for (int step=0; step<RESOLUTION; step++){
        for (int position=0; position<NUM_LEDS; position++){
            leds[position] = image[step][position];
        }
        FastLED.show();
        delay(DELAY);
    }
}

void setup() {
    delay(1000); 
    FastLED.addLeds<CHIPSET,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS);   
    FastLED.setBrightness( BRIGHTNESS );
    FastLED.clear();
}
