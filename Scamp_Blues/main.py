# ==============================================================================
#  Generate blues form from:
#     - Tone
#     - Bpm  
#     - Quantity of chorus
# ==============================================================================

import os                  # Import operating system funtions
from scamp import *        # Import SCAMP library functions
from pathlib import Path   # Import path library functions

# ==============================================================================
# Global variables and Constants
# ==============================================================================

VOLUME_PIANO   = 0.8
VOLUME_BASS    = 1
VOLUME_DRUM    = 0.5
DURATION       = 2.0                   # seconds
DURATION_8     = ( DURATION / 8 )      # value: 0.25
DURATION_4DOT  = ( DURATION_8 * 3 )    # value: 0.75
DURATION_4     = ( DURATION / 4 )      # value: 0.50

# MIDI drums
DRUM_KICK         = 35
DRUM_SNARE        = 38 
DRUM_HIHAT_CLOSED = 42
DRUM_HIHAT_OPENED = 46
DRUM_CYMBAL_CRASH = 49

# Do Scale  
gdNotes = {
   # musical note: standard MIDI
   'C' : 60,
   'D' : 62,
   'E' : 64,
   'F' : 65,
   'G' : 67,
   'A' : 69,
   'B' : 71
}

# ==============================================================================
# Functions section                            
# ==============================================================================

# ==============================================================================
# Validate tone.
# ==============================================================================
def bValidTone(psTone):
   # ToDo
   return(True)
# end-funtion: bValidTone ===================================================

# ==============================================================================
# Validate tempo.
# ==============================================================================
def bValidTempo(piTempo):
   # ToDo
   return(True)
# end-function: bValidTempo =================================================

# ==============================================================================
# Validate quantity chorus.
# ==============================================================================
def bValidRepeatChorus(piRepeatChorus):
   # ToDo
   return(True)
# end-function: bValidRepeatChorus ==========================================

# ==============================================================================
# Return user tone.
# ==============================================================================
def sEnterTone():
   sTone = ""
   bValid_Tone = False
   while (bValid_Tone == False):
      sTone = input("Ingrese tonalidad (Ej: C/Dm/F#m): ")
      bValid_Tone = bValidTone(sTone)
   return(sTone)
# end-function: sEnterTone =====================================================

# ==============================================================================
# Return user tempo.
# ==============================================================================
def fEnterTempo():
   fTempo = 0
   bValid_Tempo = False
   while (bValid_Tempo == False):
      fTempo = input("Ingrese tempo (50-120): ")
      bValid_Tempo = bValidTempo(fTempo) 
   return ( float(fTempo) )
# end-function: fEnterTempo ====================================================

# ==============================================================================
# Return user quantity chorus.
# ==============================================================================
def iEnterRepeatChorus():
   iRepeatChorus = 0
   bValid_Chorus = False
   while (bValid_Chorus == False):
      iRepeatChorus = input("Ingrese cantidad de vueltas (1-4): ")
      bValid_Chorus = bValidRepeatChorus(iRepeatChorus) 
   return ( int(iRepeatChorus) )
# end-function: iEnterRepeatChorus =============================================

# ==============================================================================
# Get tone.
# ==============================================================================
def iGet_MIDITone(psScaleTone):
   sTone = ""
   iNoteMIDI = 0 
   
   sTone = psScaleTone[0]
   iNoteMIDI = gdNotes[sTone]

   if ("#" in psScaleTone):
      iNoteMIDI = iNoteMIDI + 1
   if ("b" in psScaleTone):
      iNoteMIDI = iNoteMIDI - 1
      
   return ( iNoteMIDI )
# end-function: iGet_MIDITone ==================================================

# ==============================================================================
# Set first chord blues: 1º degree
# ==============================================================================
def lSetPiano_ChrdFrst(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_7 = 0
   lChord = []
      
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # Get first note
   # -12: go down on octave the first note 
   iNote_1 = ( iTone - 12 )
   
   # Get third note
   if ("m" in psScaleTone):
      iNote_3 = ( iTone + 3 )   # minor key
   else:
      iNote_3 = ( iTone + 4 )   # major key

   # Get seventh note
   iNote_7 = ( iTone + 10 )
      
   lChord = [iNote_1, iNote_3, iNote_7]
   return ( lChord )
# end-function: lSetPiano_ChrdFrst =============================================

# ==============================================================================
# Set second chord blues: 4º degree
# ==============================================================================
def lSetPiano_ChrdFrth(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_7 = 0
   lChord = []
   
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # Get first note
   # -12: go down on octave the first note
   iNote_1 = ( ( iTone + 5 ) - 12 )
      
   # Get third note
   if ("m" in psScaleTone):
      iNote_3 = ( ( iTone + 5 ) + 3 ) # minor key
   else:
      iNote_3 = ( ( iTone + 5 ) + 4 ) # major key

   # Get seventh note
   iNote_7 = ( ( iTone + 5 ) + 10 )
      
   lChord = [iNote_1, iNote_3, iNote_7]
   return ( lChord )
# end-function: lSetPiano_ChrdFrth =============================================

# ==============================================================================
# Set fifth chord blues: 5º degree
# ==============================================================================
def lSetPiano_ChrdFfth(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_7 = 0
   lChord = []
   
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # Get first note
   # -12: go down on octave the first note
   iNote_1 = ( ( iTone + 7 ) - 12 )
      
   # Get third note
   iNote_3 = ( ( iTone + 7 ) + 4 )
   
   # Get seventh note
   iNote_7 = ( ( iTone + 7 ) + 10 )
      
   lChord = [iNote_1, iNote_3, iNote_7]
   return ( lChord )
# end-function: lSetPiano_ChrdFfth =============================================

# ==============================================================================
# Seteamos el primer acorde: 1º grado para el bajo
# ==============================================================================
def lSetBass_ChrdFrst(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_5 = 0
   lChord = []
      
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # # Get first note
   # -24: go down on two octaves the first note
   iNote_1 = ( iTone - 24 )
   
   # Get third note
   if ("m" in psScaleTone):
      iNote_3 = ( iNote_1 + 3 )   # Tonalidad menor
   else:
      iNote_3 = ( iNote_1 + 4 )   # Tonalidad mayor

   # Get fifth note
   iNote_5 = ( iNote_1 + 7 )
      
   lChord = [iNote_1, iNote_3, iNote_5]
   return ( lChord )
# end-function: lSetBass_ChrdFrst ==============================================

# ==============================================================================
# Seteamos el segundo acorde: 4º grado para el bajo
# ==============================================================================
def lSetBass_ChrdFrth(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_5 = 0
   lChord = []
   
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # Get first note
   # -24: go down on two octaves the first note
   iNote_1 = ( ( iTone + 5 ) - 24 )
      
   # Get third note
   if ("m" in psScaleTone):
      iNote_3 = ( iNote_1 + 3 ) # menor tone
   else:
      iNote_3 = ( iNote_1 + 4 ) # major tone

   # Get fifth note
   iNote_5 = ( iNote_1 + 7 )
      
   lChord = [iNote_1, iNote_3, iNote_5]
   return ( lChord )
# end-function: lSetBass_ChrdFrth ==============================================

# ==============================================================================
# Seteamos el quinto acorde: 5º grado para el bajo
# ==============================================================================
def lSetBass_ChrdFfth(psScaleTone):
   iTone = 0
   iNote_1 = 0
   iNote_3 = 0
   iNote_5 = 0
   lChord = []
   
   # Get tone
   iTone = iGet_MIDITone(psScaleTone)
   
   # Get first note
   # -24: go down on two octaves the first note
   iNote_1 = ( ( iTone + 7 ) - 24 )
      
   # Get third note
   iNote_3 = (  iNote_1 + 4 )
   
   # Get fifth note
   iNote_5 = ( iNote_1 + 7 )
      
   lChord = [iNote_1, iNote_3, iNote_5]
   return ( lChord )
# end-function: lSetBass_ChrdFfth ==============================================

# ==============================================================================
def Drum():
   for idxRepeatChorus in range( iUsr_RepeatChorus ): # Quantityt of chorus
      for idxChorus in range (12):                    # Execute 12 measures of blues form
         if ( idxChorus == 0 ):
            insDrum.play_chord([DRUM_KICK,DRUM_CYMBAL_CRASH],VOLUME_DRUM,DURATION_8)
         else:
            insDrum.play_chord([DRUM_KICK,DRUM_HIHAT_CLOSED],VOLUME_DRUM,DURATION_8)
         
         insDrum.play_note(DRUM_HIHAT_CLOSED,VOLUME_DRUM,DURATION_8)
         insDrum.play_chord([DRUM_SNARE,DRUM_HIHAT_CLOSED],VOLUME_DRUM,DURATION_8)
         insDrum.play_note(DRUM_HIHAT_CLOSED,VOLUME_DRUM,DURATION_8)
         insDrum.play_chord([DRUM_KICK,DRUM_HIHAT_CLOSED],VOLUME_DRUM,DURATION_8)
         insDrum.play_note(DRUM_HIHAT_CLOSED,VOLUME_DRUM,DURATION_8)
         insDrum.play_chord([DRUM_SNARE,DRUM_HIHAT_CLOSED],VOLUME_DRUM,DURATION_8)
         if ( idxChorus == 11 ):
            insDrum.play_note(DRUM_HIHAT_OPENED,VOLUME_DRUM,DURATION_8)   
         else:
            insDrum.play_note(DRUM_HIHAT_CLOSED,VOLUME_DRUM,DURATION_8)
# end-function: Drum =========================================================
            
# ==============================================================================
def Piano():
   for idxChorus in range(iUsr_RepeatChorus):   # Quantity of chorus
      print("Vuelta número:",idxChorus + 1)
      for idxMeasure in range(12):              # Execute 12 measures of blues form 
      
         if ( idxMeasure == 0 
              or 
              idxMeasure == 2 
              or 
              idxMeasure == 3 
              or 
              idxMeasure == 6 
              or 
              idxMeasure == 7 
              or 
              idxMeasure == 10
            ):
            insPiano.play_chord(lPiano_ChrdFrst,VOLUME_PIANO,DURATION)
         
         if ( idxMeasure == 1 
              or 
              idxMeasure == 4 
              or 
              idxMeasure == 5 
              or 
              idxMeasure == 9
            ):
            insPiano.play_chord(lPiano_ChrdFrth,VOLUME_PIANO,DURATION)        
         
         if ( idxMeasure == 8 ):
            insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION)
         
         if ( idxMeasure == 11 ):
            if ( idxChorus == (iUsr_RepeatChorus - 1) ): # Last chorus
               print("Final ....")
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4)
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4)
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4)
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4)
            else:                                        # Backaround, go to the beginning
               print("Volvemos ....")
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4DOT,"staccato")
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4DOT,"staccato")
               insPiano.play_chord(lPiano_ChrdFfth,VOLUME_PIANO,DURATION_4, "staccato")
# end-function: Piano ========================================================

# ==============================================================================
def Bass():
   for idxChorus in range(iUsr_RepeatChorus):   # Quantity of chorus 
      for idxMeasure in range(12):              # Execute 12 measures of blues form
      
         if ( idxMeasure == 0 
              or 
              idxMeasure == 2 
              or 
              idxMeasure == 3 
              or 
              idxMeasure == 6 
              or 
              idxMeasure == 7 
              or 
              idxMeasure == 10
            ):
            insBass.play_note(lBass_ChrdFrst[0],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrst[1],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrst[2],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrst[1],VOLUME_BASS,DURATION_4)
         
         if ( idxMeasure == 1 
              or 
              idxMeasure == 4 
              or 
              idxMeasure == 5 
              or 
              idxMeasure == 9
            ):
            insBass.play_note(lBass_ChrdFrth[0],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrth[1],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrth[2],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFrth[1],VOLUME_BASS,DURATION_4)
            
         if ( idxMeasure == 8 ):
            insBass.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFfth[1],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFfth[2],VOLUME_BASS,DURATION_4)
            insBass.play_note(lBass_ChrdFfth[1],VOLUME_BASS,DURATION_4)
         
         if ( idxMeasure == 11 ):
            if ( idxChorus == (iUsr_RepeatChorus - 1) ): # Last chorus
               insBass.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4)
               insBass.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4)
               insBass.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4)
               insBass.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4)
            else:                                        # Backaround, go to the beginning
               insPiano.play_note(lBass_ChrdFfth[0],VOLUME_BASS,DURATION_4DOT,"staccato")
               insPiano.play_note(lBass_ChrdFfth[1],VOLUME_BASS,DURATION_4DOT,"staccato")
               insPiano.play_note(lBass_ChrdFfth[2],VOLUME_BASS,DURATION_4, "staccato")
# end-function: Bass ===========================================================

# ==============================================================================  
def Drum_Final():
   insDrum.play_chord([DRUM_KICK,DRUM_CYMBAL_CRASH],VOLUME_DRUM,DURATION * 2)
# end-function: Drum_Final =====================================================

# ==============================================================================  
def Piano_Final():
   insPiano.play_chord(lPiano_ChrdFrst,VOLUME_PIANO,DURATION * 2)
# end-function: Piano_Final ====================================================

# ==============================================================================  
def Bass_Final():
   insBass.play_note(lBass_ChrdFrst[0],VOLUME_BASS,DURATION * 2)
# end-funcion: Bass_Final ======================================================

# ==============================================================================  
#                                   Main
# ==============================================================================
# Clear screen
os.system("cls")

# Initialize variables
sUsr_ScaleTone = ""
iUsr_RepeatChorus = 0
fUsr_Tempo = 0
sPathMainFolder = ""
sPathSoundFont = ""

# Get tone
sUsr_ScaleTone = sEnterTone()

# Get tempo
fUsr_Tempo = fEnterTempo()

# Get quantity chorus
iUsr_RepeatChorus = iEnterRepeatChorus()

# Obtain path to main folder
sPathMainFolder = Path("main.py").parent
sPathSoundFont = sPathMainFolder/"FluidR3_GM.sf2"

# Create session SCAMP:
#  - Define audio driver
#  - Define sounds/instruments
ssMySession = Session(
                  tempo=fUsr_Tempo,
                  default_audio_driver="dsound",
                  default_soundfont=str(sPathSoundFont)
               )

# Create instances of instruments
insPiano = ssMySession.new_part("Bright Piano")
insDrum = ssMySession.new_part("Standard kit")
insBass = ssMySession.new_part("Fingered Bass")

# Set chords depending on the tone
lPiano_ChrdFrst = lSetPiano_ChrdFrst(sUsr_ScaleTone) 
lPiano_ChrdFrth = lSetPiano_ChrdFrth(sUsr_ScaleTone)
lPiano_ChrdFfth = lSetPiano_ChrdFfth(sUsr_ScaleTone)

lBass_ChrdFrst = lSetBass_ChrdFrst(sUsr_ScaleTone)
lBass_ChrdFrth = lSetBass_ChrdFrth(sUsr_ScaleTone)
lBass_ChrdFfth = lSetBass_ChrdFfth(sUsr_ScaleTone)

print("Reproduciendo progresión de Blues en: " + sUsr_ScaleTone)

# Initial measure to hear tempo
print("Intro")
for idxQuarter in range(4):
   insDrum.play_note(DRUM_HIHAT_CLOSED,VOLUME_DRUM,DURATION_4)   

# Start
ssMySession.fork(Drum)
ssMySession.fork(Piano)
ssMySession.fork(Bass)
ssMySession.wait_for_children_to_finish()

# Final measure and chords
ssMySession.fork(Piano_Final)
ssMySession.fork(Drum_Final)
ssMySession.fork(Bass_Final)
ssMySession.wait_for_children_to_finish()