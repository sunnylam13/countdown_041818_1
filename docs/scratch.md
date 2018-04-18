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

