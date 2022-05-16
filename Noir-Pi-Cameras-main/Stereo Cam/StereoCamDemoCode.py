import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

//Setup the stack layer 1 board
gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

// Setup the stack layer 2 board if any
gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)

// Setup the stack layer 3 board if any
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

// Setup the stack layer 4 board if any
gp.setup(23, gp.OUT)
gp.setup(24, gp.OUT)

//Disable stack layer 1 board output
gp.output(11, True)
gp.output(12, True)

//Disable stack layer 2 board output
gp.output(15, True)
gp.output(16, True)

//Disable stack layer 3 board output
gp.output(21, True)
gp.output(22, True)

//Disable stack layer 4 board output
gp.output(23, True)
gp.output(24, True)

def main():
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	capture(1)

	gp.output(7, True)
	gp.output(11, False)
	gp.output(12, True)
	capture(2)

	gp.output(7, False)
	gp.output(11, True)
	gp.output(12, False)
	capture(3)

	gp.output(7, True)
	gp.output(11, True)
	gp.output(12, False)
	capture(4)

def capture(cam):
	cmd = "raspistill -o capture_%d.jpg" % cam
	os.system(cmd)

if __name__ == "__main__":
	main()

	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)