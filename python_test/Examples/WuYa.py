#!/usr/bin/python3

import sys
sys.path+=['../']

import ScoreDraft
#from ScoreDraftNotes import *
import Meteor

Freqs=[1.0, 9.0/8.0, 81.0/64.0, 4.0/3.0, 3.0/2.0, 27.0/16.0, 243.0/128.0]

def note(octave, freq, duration):
	return (freq*(2.0**(octave-5.0)), duration)

def do(octave=5, duration=48):
	return note(octave,Freqs[0],duration)

def re(octave=5, duration=48):
	return note(octave,Freqs[1],duration)

def mi(octave=5, duration=48):
	return note(octave,Freqs[2],duration)

def fa(octave=5, duration=48):
	return note(octave,Freqs[3],duration)

def so(octave=5, duration=48):
	return note(octave,Freqs[4],duration)

def la(octave=5, duration=48):
	return note(octave,Freqs[5],duration)

def ti(octave=5, duration=48):
	return note(octave,Freqs[6],duration)

def BL(duration=48):
	return (-1.0, duration)

def BK(duration=48):
	return (-1.0, -duration)

FreqsC=Freqs[:]
# FreqsF=[f*Freqs[5] for f in Freqs]
FreqsF=[f*Freqs[3] for f in Freqs]

Freqs[:]=FreqsF

doc=Meteor.Document()
doc.setTempo(120)

GePing = ScoreDraft.GePing_UTAU()

GuitarMute=ScoreDraft.RockMute()
Guitar=ScoreDraft.AlansGuitar()
Bass=ScoreDraft.Bass()

assDrum=ScoreDraft.BassDrum()
Snare=ScoreDraft.Snare()

BassDrum=ScoreDraft.BassDrum()
Snare=ScoreDraft.Snare()

perc_list=[BassDrum,Snare]

def dong(duration=48):
	return (0,duration)

def cha(duration=48):
	return (1,duration)

def Bl(duration=48):
	return (-1,duration)


track=doc.newBuf()
track_gm=doc.newBuf()
track_g=doc.newBuf()
track_b=doc.newBuf()
track_p=doc.newBuf()

def Chord(elems, duration, delay=0):
	ret=[]
	for elem in elems:
		ret+=[elem[0](elem[1], duration)]
		duration-=delay
		ret+=[BK(duration)]
	ret+=[BL(duration)]
	return ret


def Repeat(x,t):
	ret=[]
	for i in range(t):
		ret+=x
	return ret

seq_gm=Repeat(
	Repeat(Chord([(la,3), (mi,4), (la,4) ], 24),4)+Repeat(Chord([(do,4), (so,4), (do, 5)], 24),4) +
	Repeat(Chord([(re,4), (la,4), (re,5) ], 24),4)+Repeat(Chord([(mi,4), (ti,4), (mi, 5)], 24),4) 
	,2)
seq_b=Repeat([la(2,96), do(3,96), re(3,96), mi(3,96)],2)
seq_p=Repeat([dong(),cha()],8)

seq_gm+=Repeat(Chord([(fa,4), (do,5), (fa,5)],12),4)+[BL(24)]+ Repeat(Chord([(mi,4), (ti,4), (mi,5)],12),4)+[BL(24)]
seq_b+=[BL(144)]
seq_p+=Repeat(Repeat([cha(12)],4)+[Bl(24)],2)

seq=[BL(ScoreDraft.TellDuration(seq_gm))]
seq+=[('meng',la(4,24),'li',la(4,24),'bu',la(4,24), 'zhi',la(4,24), 'liu',la(4,48), 'zhuan',so(4,24), 'liao', mi(4,24))]
seq_gm+=Repeat(Chord([(la,3), (re,4), (mi,4), (la,4) ], 24),8)
seq_b+=Repeat([la(2,24),la(2,48),la(2,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('duo',la(4,24),'shao',la(4,48),'nian',re(5,96)), BL(24)]
seq_gm+=Repeat(Chord([(re,4), (so,4), (la,4), (re,5) ], 24),8)
seq_b+=Repeat([re(3,24),re(3,48),re(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('wang',mi(5,48), 'que', mi(5,24), re(5,24), 'qing', la(4,24), 'si', la(4,24), mi(5,48) )]
seq_gm+=Repeat(Chord([(mi,4), (la,4), (ti,4), (mi,5) ], 24),8)
seq_b+=Repeat([mi(3,24),mi(3,48),mi(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('chen',re(5,36),mi(5,12),re(5,24),'nian',so(4,72)), BL(48)]
seq_gm+=Repeat(Chord([(re,4), (so,4), (la,4), (re,5) ], 24),8)
seq_b+=Repeat([re(3,24),re(3,48),re(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('hui', la(4,48), 'mou', la(4,24), 'yi', la(4,48), 'pian', la(4,48)), BL(24)]
seq_gm+=Repeat(Chord([(la,3), (re,4), (mi,4), (la,4) ], 24),8)
seq_b+=Repeat([la(2,24),la(2,48),la(2,24)],2)
seq_p+=Repeat([dong(),cha()],2)

Freqs[:]=FreqsC

seq+=[('wang', do(6,48), 'shi', ti(5,24), la(5,24), 'you', la(5,48), 'fu', so(5,24),la(5,24) )]
seq_gm+=Repeat(Chord([(do,5), (so,5), (la,5), (do,6) ], 24),8)
seq_b+=Repeat([do(4,24),do(4,48),do(4,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('xian', la(5,144)), BL(48)]
seq_g=[BL(ScoreDraft.TellDuration(seq_gm))]
seq_g+=Chord([(la,4), (mi,5), (la,5),(re,6)], 96)+Chord([(do,5), (la,5), (do,6), (so,6)], 96)
seq_gm+=Repeat(Chord([(la,4), (re,5), (mi,5), (la,5) ], 24),4)+Repeat(Chord([(do,5), (so,5), (la,5), (do,6) ], 24),4)
seq_b+=[la(3,24),la(3,48),la(3,24),do(4,24),do(4,48),do(4,24)]
seq_p+=Repeat([dong(),cha()],2)

seq+=[BL(192)]
seq_g+=Repeat(Chord([(re,5), (la,5), (re,6), (so,6)], 24),3)+ Chord([(mi,5), (ti,5), (mi,6), (la,6)], 120)
seq_gm+=Repeat(Chord([(re,5), (so,5), (la,5), (re,6) ], 24),4)+Repeat(Chord([(mi,5), (la,5), (ti,5), (mi,6) ], 24),4)
seq_b+=[re(4,24),re(4,48),re(4,24),mi(4,24),mi(4,48),mi(4,24)]
seq_p+=Repeat([dong(),cha()],2)

Freqs[:]=FreqsF
seq+=[('zui',la(5,24), 'yan',la(5,48)), BL(24), ('xiao',la(5,24),'kan',la(5,48), 'chen', so(5,12), la(5,12))]
seq_g+=Repeat(Repeat(Chord([(re,5), (mi,5), (la,5)],24),2)+[so(5,24), BK(12), la(5,12), la(4,24)],2)
seq_gm+=Repeat(Chord([(la,3), (re,4), (mi,4), (la,4) ], 24),8)
seq_b+=Repeat([la(2,24),la(2,48),la(2,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('shi',so(5,12),la(5,36),so(5,24), 'jian', so(5,96)), BL(24)]
seq_g+=Repeat(Chord([(re,5), (mi,5), (so,5)],24),2)+[mi(5,24), so(5,24), do(5,48), re(5,48)]
seq_gm+=Repeat(Chord([(so,3), (re,4), (mi,4), (so,4) ], 24),8)
seq_b+=Repeat([so(2,24),so(2,48),so(2,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('he',so(5,24),la(5,24),'chu',so(5,24), mi(5,24), 'shi', mi(5,48), 'tao', re(5,24),mi(5,24))]
seq_g+=Repeat(Chord([(re,5), (mi,5), (la,5)],24),2)+[so(5,24),la(5,24),mi(5,48),re(5,48)]
seq_gm+=Repeat(Chord([(la,3), (re,4), (mi,4), (la,4) ], 24),8)
seq_b+=[la(2,24),la(2,48),la(2,24), mi(3,48), re(3,48)]
seq_p+=Repeat([dong(),cha()],2)

seq+=[('yuan',re(5,24),mi(5,120)),BL(48)]
seq_g+=[mi(5,96), so(5,48),la(5,48)]
seq_gm+=Repeat(Chord([(mi,4), (la,4), (ti,4), (mi,5) ], 24),8)
seq_b+=Repeat([mi(3,24),mi(3,48),mi(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('qing', re(5,48), 'feng', mi(5,24), 'ji', re(5,48), 'du',mi(5,48)),BL(24)]
seq_g+=[re(5,48),mi(5,48),so(5,48),la(5,48)]
seq_gm+=Repeat(Chord([(re,4), (so,4), (la,4), (re,5) ], 24),8)
seq_b+=Repeat([re(3,24),re(3,48),re(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

seq+=[('shui', mi(5,12), so(5,36), 'yu', mi(5,48), 'wo', re(5,24), ti(4,24), 'liu', ti(4,24),la(4,24))]
seq_g+=[so(5,48),mi(5,48),re(5,48),so(5,48)]
seq_gm+=Repeat(Chord([(mi,4), (la,4), (ti,4), (mi,5) ], 24),8)
seq_b+=Repeat([mi(3,24),mi(3,48),mi(3,24)],2)
seq_p+=Repeat([dong(),cha()],2)

Freqs[:]=FreqsC

seq+=[('lian', re(5,144)), BL(48)]
seq_g+=Chord([(re,4), (la,4), (re,5),(so,5)], 96)+Chord([(mi,4), (ti,4), (mi,5), (la,5)], 96)
seq_gm+=Repeat(Chord([(re,4), (so,4), (la,4), (re,5) ], 24),4)+Repeat(Chord([(mi,4), (la,4), (ti,4), (mi,5) ], 24),4)
seq_b+=[re(3,24),re(3,48),re(3,24),mi(3,24),mi(3,48),mi(3,24)]
seq_p+=Repeat([dong(),cha()],2)

seq+=[BL(192)]
seq_g+=Repeat(Chord([(so,4), (re,5), (so,5), (do,6)], 24),3)+ Chord([(la,4), (mi,5), (la,5), (re,6)], 120)
seq_gm+=Repeat(Chord([(so,4), (do,5), (re,4), (so,5) ], 24),4)+Repeat(Chord([(la,4), (re,5), (mi,5), (la,5) ], 24),4)
seq_b+=[so(3,24),so(3,48),so(3,24),la(3,24),la(3,48),la(3,24)]
seq_p+=Repeat([dong(),cha()],2)

Freqs[:]=FreqsF

seq+=[('yuan', re(5,12), mi(5,36),re(5,24), 'qi',re(5,72)), BL(48) ]

seq_p+=Repeat([dong(),cha()],2)

seq+=[('yuan', re(5,12), mi(5,36),la(4,24), 'mie',la(4,72)), BL(48) ]

seq_p+=Repeat([dong(),cha()],2)

Freqs[:]=FreqsC

seq+=[('yi', so(5,48), 'mu', la(5,48), 'mu', la(5,24), 'chong', la(5,12), ti(5,24), la(5,12))]

seq_p+=Repeat([dong(),cha()],2)

seq+=[('yan', la(5,144)), BL(72)]

seq_p+=Repeat([dong(),cha()],2)

seq+=[('hua', la(5,48),so(5,24), 'xie',so(5,72)), BL(48) ]

seq_p+=Repeat([dong(),cha()],2)

seq+=[('hua', la(5,48),do(6,24), 'kai',do(6,72)), BL(48) ]

seq_p+=Repeat([dong(),cha()],2)


seq+=[('yi', re(6,48), 'nian', re(6,48), 'nian', do(6,24), 'geng', re(6,24), do(6,24))]

seq_p+=Repeat([dong(),cha()],2)

seq+=[('die', re(6,24), mi(6,24), re(6,24), mi(6,24),re(6,24), mi(6,24),re(6,24), mi(6,24)), BL(24)]

seq_p+=Repeat([dong(),cha()],2)

doc.sing(seq, GePing, track)
doc.playNoteSeq(seq_gm, GuitarMute, track_gm)
doc.playNoteSeq(seq_g,Guitar, track_g)
doc.playNoteSeq(seq_b,Bass, track_b)
doc.playBeatSeq(seq_p, perc_list, track_p)

doc.setTrackVolume(track_gm, 0.5)
doc.setTrackVolume(track_g, 0.5)
doc.setTrackVolume(track_b, 0.5)
doc.setTrackVolume(track_p, 0.5)

doc.meteor()
doc.mixDown('WuYa.wav')
