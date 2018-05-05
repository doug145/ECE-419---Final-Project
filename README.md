# Covert Communication System Via CPU Fan and Microphone
## Security Lab Group Project, Spring 2018 

The goal of this project is to create a system that could be used to relay information from one computer to another within close physical proximity.

## Message Structure:

Messages are first transcoded using a form of pulse position modulation and are then transduced to audible CPU fan noises by ramping up CPU activity. As one would expect, communication rates are slow, however in many contexts this would be irrelevant.

## Experimental Setup:

Sender computer: Lenovo L440

Microphone: Apple wired headphones

Room Temperature: ~72 Degrees F

## CPU Fan Characteristics:

Assuming 100% CPU activity starting at t = 0 seconds and CPU activity << 100% at t = 3? seconds:
  * Time at which CPU fan speed begins to increase: t = 3 seconds
  * Time at which CPU fan reaches maximum speed: t = 5? seconds
  * Time at which CPU fan returns to normal speed: t = 5? seconds
  
### Spectrograms of two different microphone postions:

Here we see spectrograms of audio recordings at two different microphone locations. The first spectrogram (top) has the microphone approximately an inch away from the CPU fan output and the second (bottom) has the microphone making physical contact with the laptop chassis at the CPU fan output. Notice that while the CPU fan pulses are visible in both spectrograms, they are more pronounced in the second case.

![](https://github.com/doug145/ECE-419---Final-Project/blob/master/readme_images/spectrogram.png?raw=true)



  
## Tools Used:

pyaudio, numpy, scipy
