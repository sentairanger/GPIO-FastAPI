from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LEDBoard, Servo, OutputDevice

factory = PiGPIOFactory(host='192.168.0.10')
factory2 = PiGPIOFactory(host='192.168.0.21')

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

traffic_light = LEDBoard(17, 27, 23, pin_factory=factory)
servo = Servo(22, pin_factory=factory)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get("/red", response_class=HTMLResponse)
def red(request: Request):
    traffic_light.value = (1, 0, 0)
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get("/yellow", response_class=HTMLResponse)
def yellow(request: Request):
    traffic_light.value = (0, 1, 0)
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get("/green", response_class=HTMLResponse)
def green(request: Request):
    traffic_light.value = (0, 0, 1)
    return templates.TemplateResponse("gpio.html", { "request" : request })


@app.get('/min', response_class=HTMLResponse)
def servomin(request: Request):
    servo.min()
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get('/mid', response_class=HTMLResponse)
def servomid(request: Request):
    servo.mid()
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get('/max', response_class=HTMLResponse)
def servomax(request: Request):
    servo.max()
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get('/up', response_class=HTMLResponse)
def north(request: Request):
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return templates.TemplateResponse("gpio.html", { "request" : request })


# backwards
@app.get('/down', response_class=HTMLResponse)
def south(request: Request):
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return templates.TemplateResponse("gpio.html", { "request" : request })

#right
@app.get('/right', response_class=HTMLResponse)
def east(request: Request):
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return templates.TemplateResponse("gpio.html", { "request" : request })

#left
@app.get('/left', response_class=HTMLResponse)
def west(request: Request):
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return templates.TemplateResponse("gpio.html", { "request" : request })

@app.get('/stop', response_class=HTMLResponse)
def stop_two(request: Request):
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return templates.TemplateResponse("gpio.html", { "request" : request })