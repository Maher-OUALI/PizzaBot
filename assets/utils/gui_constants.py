#root app config
APP_TITLE='PizzaBot'
APP_WIDTH, APP_HEIGHT=400,500
APP_GEOMETRY=str(APP_WIDTH)+'x'+str(APP_HEIGHT)
APP_ICON_PATH='assets/images/pizzabot.ico'
MARGIN=6
TOP_LEVEL_TITLE="Pizza Ready"
TOP_LEVEL_WIDTH, TOP_LEVEL_HEIGHT=256,256
PIZZA_IMG_PATH='assets/images/pizza.png'
PIZZA_IMG_FONT="arial.ttf"
PIZZA_IMG_TEXT="Pizza for "
PIZZA_IMG_TEXT_POS=(5, 5)
PIZZA_IMG_TEXT_COLOR=(0, 255, 255)#cyan

#splash window config
SPLASH_OUTPUT_FIELD_FONT="none 20 bold"
SPLASH_OUTPUT_FIELD_TEXT="What's your name ?"
SPLASH_OUTPUT_FIELD_HEIGHT=40
SPLASH_OUTPUT_FIELD_X=APP_WIDTH//5
SPLASH_OUTPUT_FIELD_Y=APP_HEIGHT//4

SPLASH_INPUT_FIELD_X=SPLASH_OUTPUT_FIELD_X+MARGIN*12
SPLASH_INPUT_FIELD_Y=SPLASH_OUTPUT_FIELD_Y+SPLASH_OUTPUT_FIELD_HEIGHT+MARGIN
SPLASH_INPUT_FIELD_WIDTH, SPLASH_INPUT_FIELD_HEIGHT=80,20

SPLASH_SEND_BUTTON_TEXT="Want Some Pizza!"
SPLASH_SEND_BUTTON_X=SPLASH_OUTPUT_FIELD_X+MARGIN*10
SPLASH_SEND_BUTTON_Y=SPLASH_INPUT_FIELD_Y+SPLASH_INPUT_FIELD_HEIGHT+MARGIN
SPLASH_SEND_BUTTON_WIDTH, SPLASH_SEND_BUTTON_HEIGHT=100,30

DELIVERY_IMG_PATH='assets/images/delivery.gif'
SPLASH_DELIVERY_IMG_X=SPLASH_OUTPUT_FIELD_X+MARGIN*7
SPLASH_DELIVERY_IMG_Y=SPLASH_SEND_BUTTON_Y+SPLASH_SEND_BUTTON_HEIGHT+MARGIN

#main window config
INPUT_FIELD_FONT="Arial"
INPUT_FIELD_HEIGHT, OUTPUT_FIELD_X, OUTPUT_FIELD_Y, SCROLL_WIDTH=70, MARGIN, MARGIN, 20
SEND_BUTTON_HEIGHT=INPUT_FIELD_HEIGHT
SEND_BUTTON_WIDTH=SEND_BUTTON_HEIGHT
INPUT_FIELD_X=OUTPUT_FIELD_X
SCROLL_Y=OUTPUT_FIELD_Y
OUTPUT_FIELD_HEIGHT=APP_HEIGHT-OUTPUT_FIELD_Y*2-INPUT_FIELD_HEIGHT
SCROLL_HEIGHT=OUTPUT_FIELD_HEIGHT
OUTPUT_FIELD_WIDTH=APP_WIDTH-OUTPUT_FIELD_X*2-SCROLL_WIDTH
SCROLL_X=OUTPUT_FIELD_WIDTH+OUTPUT_FIELD_X*2
INPUT_FIELD_Y=OUTPUT_FIELD_HEIGHT+OUTPUT_FIELD_Y*2
SEND_BUTTON_Y=INPUT_FIELD_Y
INPUT_FIELD_WIDTH=APP_WIDTH-INPUT_FIELD_X*2-SEND_BUTTON_WIDTH
SEND_BUTTON_X=INPUT_FIELD_WIDTH+INPUT_FIELD_X*2
SEND_BUTTON_IMG_PATH='assets/images/send.png'

