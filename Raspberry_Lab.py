import RPi.GPIO as GPIO
import time

# Định nghĩa chân GPIO
LED_PINS = [18, 23, 24, 25]
BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mode = 0  # bắt đầu từ chế độ tắt
last_button = 1  # trạng thái nút trước đó

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)

        # Kiểm tra bấm nút (nhấn từ HIGH -> LOW)
        if button_state == GPIO.LOW and last_button == GPIO.HIGH:
            mode = (mode + 1) % 4
            print("Chế độ:", mode)
            time.sleep(0.3)  # chống dội phím

        last_button = button_state

        # --- Các chế độ ---
        if mode == 0:
            # Tắt hết
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.LOW)

        elif mode == 1:
            # Sáng hết
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)

        elif mode == 2:
            # Nhấp nháy tất cả
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)

        elif mode == 3:
            # Sáng lần lượt
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()