from psychopy import voicekey, sound
import numpy as np
import sys 
import time
import pyo64 as pyo

# --- VOICE KEY PATCH - ON ---

def _pyo_init_patched(rate = 44100, nchnls = 1, buffersize = 32, duplex = 1):    
    sound.initPyo(rate = rate, stereo = True, buffer = buffersize)
    voicekey.pyo_server = vks = sound.pyoSndServer
    vks.setDuplex(duplex)
    
    # avoid mac issue of losing first 0.5s if no sound played for ~1 minute:
    if sys.platform == 'darwin':
        z2 = np.zeros(2)
        _sndTable = pyo.DataTable(size = 2, init = z2.T.tolist(), chnls = vks.getNchnls())
        _snd = pyo.TableRead(_sndTable, freq = rate, mul=0)
        _snd.play()
        time.sleep(0.510)

__voicekey_pyo_init = voicekey.pyo_init
voicekey.pyo_init = _pyo_init_patched    

'''
def _BaseVoiceKey_set_baseline_patched(self):
    data = np.int16(np.array(self._baselinetable.getTable()) * 2 ** 15) # *2 ** 15 (patch 1)
    
    if self.config['more_processing']: # calculate noise on the seleted band only, if more_processing... (patch 2)
        data = voicekey.vk_tools.bandpass(data, self.config['low'], self.config['high'], self.rate)
    
    tstart = int(voicekey.T_BASELINE_ON * self.rate)
    segment_power = voicekey.vk_tools.rms(data[tstart:])

    # Look for bad baseline period:
    if self.baseline > voicekey.TOO_LOUD:
        self.bad_baseline = True

    # Dubiously quiet is bad too:
    if segment_power < voicekey.TOO_QUIET:
        self.stop()
        msg = ('Baseline period is TOO quiet\nwrong input '
               'channel selected? device-related initial delay?')
        raise ValueError(msg)
        
    self.baseline = max(segment_power, 1)

__voicekey_TOO_LOUD = voicekey.TOO_LOUD
__voicekey_TOO_QUIET = voicekey.TOO_QUIET            
__voicekey__BaseVoiceKey_set_baseline = voicekey._BaseVoiceKey._set_baseline

voicekey.TOO_LOUD  = voicekey.TOO_LOUD * 2 ** 15
voicekey.TOO_QUIET = voicekey.TOO_QUIET * 2 ** 15
voicekey._BaseVoiceKey._set_baseline = _BaseVoiceKey_set_baseline_patched
'''