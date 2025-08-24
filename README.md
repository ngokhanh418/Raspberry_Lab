# DEMO điều khiển đèn Led bằng Button

Hệ thống thay đổi các chế độ đèn: Tắt -> Sáng cả 4 đèn -> 4 đèn sáng xen kẽ ->4 đèn sáng theo thứ tự 

## Yêu cầu phần cứng

### Board và linh kiện
- **RASPBERRY PI** 
- **Led** 
- **Button** (SG90 hoặc tương tự)
- **Breadboard, điện trở** và dây jumper
- **Nguồn cấp** 5V 

### Thư viện cần cài:
- **RPi.GPIO**

### Kết nối chân
```
LED1 → GPIO 18
LED2 → GPIO 23
LED3 → GPIO 24
LED4 → GPIO 25
BUTTON → GPIO 17
```
### Sơ đồ lắp mạch:
