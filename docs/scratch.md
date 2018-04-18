# Scratch Notes and Log

## Wednesday, April 18, 2018 9:37 AM

-------------------------------------

high level

* count down from 60

* play sound file when countdown hits zero

code does

* pause for 1 second in between displaying each number in countdown using `time.sleep()`

* call `subprocess.Popen()` to open sound file with default app

-------------------------------------

Windows version

	subprocess.Popen(['start','alarm.wave',shell=True])

to play audio

need to configure `open` for Mac

[Play audio with Python](https://stackoverflow.com/questions/260738/play-audio-with-python)

	subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])

[VLC Command Line](https://wiki.videolan.org/Command_line/)

[How to open and play mp3 file in python?](https://www.daniweb.com/programming/software-development/threads/491663/how-to-open-and-play-mp3-file-in-python)

	import subprocess

	# pick an external mp3 player you have
	sound_program = "path to player"
	# pick a sound file you have
	sound_file = "path to mp3"
	subprocess.call([sound_program, sound_file])

I tried:

	# subprocess.Popen(['open','-a /Applications/VLC.app/Contents/MacOS/VLC','alarm.wav'],shell=True)
	# subprocess.call(['/Applications/VLC.app/Contents/MacOS/VLC','--intf ncurses', 'alarm.wav'],shell=True)

this one worked:

	subprocess.call(['/Applications/VLC.app/Contents/MacOS/VLC --intf ncurses /Users/sunnyair/Dropbox/python_projects/countdown_041818_1/countdown/alarm.wav'],shell=True)

## Wednesday, April 18, 2018 10:18 AM

Ideas for similar

this is a simple delay before execution

could...

* use `time.sleep()` to give user chance to press Ctrl-C to cancel action like deleting files...  program could print "Print Ctrl-C to cancel" message and then handle any `KeyboardInterrupt` exceptions with `try` and `except` statements

* for long term counts, use `timedelta` objects to measure days, hours, minutes, seconds until some point in the future...

