
#-------------------------------------------------------------------------------
# Name:        Wii Remote - connect to Bluetooth cwiid
# Purpose:
#
# Author:      Brian Hensley
#
# Created:     21/07/2012
# Copyright:   (c) Brian 2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import cwiid
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.output(31,False)
GPIO.setup(33,GPIO.OUT)
GPIO.output(33,False)
GPIO.setup(35,GPIO.OUT)
GPIO.output(35,False)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,False)


def main():

        print 'Press button 1 + 2 on your Wii Remote...'
        time.sleep(1)

        wm=cwiid.Wiimote()
	print 'Wii Remote connected...'
	print '\nPress the PLUS button to disconnect the Wii and end the application'
        time.sleep(1)
	
	Rumble = False
        wm.rpt_mode = cwiid.RPT_BTN
	
	#position = 50
	#print 'starting position: ', position

        while True:
   #         if wm.state['buttons'] == 2048:
	#	if position > 0:
	#		position = position - 10
                	#print 'Left button pressed \n'
	#		print 'Position: ', position
     #           time.sleep(.5)
             
	#	if wm.state['buttons'] == 2048:
		#	if position == 0:
		#		print 'You reached the minimum position'
        #       time.sleep(.5)
                
      #      if wm.state['buttons'] == 1024:
		#if position < 100:
	#	#	position = position + 10
      #          	#print 'Right button pressed \n'
	#		print 'Position: ', position
     #           time.sleep(.5)
                
	#	if wm.state['buttons'] == 1024:
	#		GPIO.output(31,False)
	#		GPIO.output(33,True)
	#		GPIO.output(35,True)
	#		GPIO.output(37,False)
	#		print 'Back'
	#		time.sleep(.5)
                
	#    if wm.state['buttons'] == 1025:
	#	if position < 100:
	#		position = position + 10
	#		print 'Moving Forward, Wheel position: ', position
	#	time.sleep(.5)

	#    if wm.state['buttons'] == 1026:
	#	if position < 100:
	#		position = position + 10
	#		print 'Moving Reverse, Wheel position: ', position
	#	time.sleep(.5) 

	#    if wm.state['buttons'] == 2049:
	#	if position > 0:
	#		position = position - 10
	#		print 'Moving Forward, Wheel position: ', position
	#	time.sleep(.5) 

	#    if wm.state['buttons'] == 2050:
	#	if position > 0:
	#		position = position - 10
	#		print 'Moving Reverse, Wheel position: ', position
	#	time.sleep(.5) 

	    if wm.state['buttons'] == 512:
		GPIO.output(31,False)
		GPIO.output(33,False)
		GPIO.output(35,True)
		GPIO.output(37,True)
		print 'Right'
		time.sleep(.5)

	    if wm.state['buttons'] == 256:
		GPIO.output(31,True)
		GPIO.output(33,True)
		GPIO.output(35,False)
		GPIO.output(37,False)
		print 'Left'
		time.sleep(.5)


            if wm.state['buttons'] == 2:
                print 'Button 1 pressed'
                time.sleep(.5)

            if wm.state['buttons'] == 1:
                print 'Button 2 pressed'
                time.sleep(.5)
                
            if wm.state['buttons'] == 8:
				GPIO.output(31,False)
				GPIO.output(33,False)
				GPIO.output(35,False)
				GPIO.output(37,False)
				print 'Stop'
				time.sleep(.5)

            if wm.state['buttons'] == 4:
                print 'Button B pressed'
                time.sleep(.5)
                
            if wm.state['buttons'] == 12:
                print 'Button A + B pressed'
                time.sleep(.5)
                
            if wm.state['buttons'] == 128:
                print 'Button home pressed'
                time.sleep(.5)
                
            if wm.state['buttons'] == 1024:
				GPIO.output(31,False)
				GPIO.output(33,True)
				GPIO.output(35,True)
				GPIO.output(37,False)
				print 'Back'
				time.sleep(.5)    
                
            if wm.state['buttons'] == 2048:
				GPIO.output(31,True)
				GPIO.output(33,False)
				GPIO.output(35,False)
				GPIO.output(37,True)
				print 'Forward'
				time.sleep(.5)  
                
                
                
                
                
                
	    if wm.state['buttons'] == 16:
		if Rumble == False:
			print 'Rumble is on'		
			wm.rumble = True
			Rumble = True
			time.sleep(1)
		elif Rumble == True:
			wm.rumble = False
			#Rumble = False
			time.sleep(.1)
			wm.rumble = True
			Rumble = True
			time.sleep(.3)
			print 'Rumble is off'
			wm.rumble = False
			Rumble = False
			time.sleep(1)
			
	    if wm.state['buttons'] == 4096:
		if Rumble == False:
				wm.rumble = True
				Rumble = True
				time.sleep(.5)
				wm.rumble = False
				Rumble = False
				time.sleep(.5)
				print 'closing Bluetooth connection. Good Bye!'
				time.sleep(1)
				GPIO.cleanup()
				exit(wm)


if __name__ == '__main__':
    main()

