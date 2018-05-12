# Covert Communication System Via CPU Fan and Microphone
## Security Lab Group Project, Spring 2018 

The goal of this project is to create a system that could be used to relay information from one computer to another within close physical proximity. The system would be able to transmit small amounts of information without relying on a network, hence a compromise would be more difficult. 

## Message Structure:

Messages are first transcoded using a form of pulse position modulation and are then transduced to audible CPU fan noises by ramping up CPU activity. As one would expect, communication rates are slow, however in many contexts this would be irrelevant.

## Theoretical Dilemnas 
While this may work in a controlled environment, there are many environmental features that could render this attack useless. Examples include:
  * Any computer with its fans on the highest or close to the highest setting
  * Any machine in a loud environment
  * Any machine that physical access to is prohibited

## Experimental Setup:

Sender computer: Lenovo L440

Microphone: Apple wired headphones

Room Temperature: ~72 Degrees F

## CPU Fan Characteristics:

Assuming 100% CPU activity starting at t = 0 seconds and CPU activity << 100% at t = 6 seconds:
  * Time at which CPU fan speed begins to increase: t = 3 seconds
  * Time at which CPU fan reaches maximum speed: t = 5 seconds
  * Time at which CPU fan returns to normal speed: t = 10 seconds
  
### Spectrograms of two different microphone postions:

Here we see spectrograms of audio recordings at two different microphone locations. The first spectrogram (top) has the microphone approximately an inch away from the CPU fan output and the second (bottom) has the microphone making physical contact with the laptop chassis at the CPU fan output. Notice that while the CPU fan pulses are visible in both spectrograms, they are more pronounced in the second case.

![](https://github.com/doug145/ECE-419---Final-Project/blob/master/readme_images/spectrogram.png?raw=true)


## Future Work
For this project, there are many directions that the project could take after this. One route is that the a user could use a shotgun(directional) mic and pick up the audio from the fan from a distance. We didn't have access to one to test this theory but it is a possibliity as these mics specialize in sound in a direction at an angle. 

Another option is after using placing the program on a user's computer, using a microphone hooked up to a small recorder used for storing the messages. If this were small enough and placed close to a desktop computer, such as one in a classroom, it would be easy to conceal. The recorder could then be collected by the attacker (he could even wear a flourescent vest for a social engineering angle to the attack) then the audio played back and the message decoded.

A final possible avenue of attack would be more of a targeted attack for a sepcific type of data. The attacking program could be modified to grab a specific type of data, such as Linux login info or UIUC credentials. It could then only communicate this data whenever it finds it, and not be constantly recording data.

## Tools Used:

pyaudio, numpy, scipy

## Issues:
Although we got the transmission aspect of this project fully functional, we did not manage to get the recieving end fully working. The reciever requires compicated digital signal processing in order to make it robust. Given more time, we may have succeded. The method we experimented involved taking a spectrograph in realtime and from the microphone. We then perform summations across a subset of frequencies for each time step. Next we performed a convolution using a kernel roughly in the shape of what a pulse would look like. We then did a median filter to smooth out any unrelated noise. Finally we performed a sum across the resulting array, which was used for determining where the pulse showed up within a frame.
