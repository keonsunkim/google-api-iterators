# youtube.api_modules.mixins.py

import re


# third party import
from pytube import YouTube


# local imports
from tools import parse_xml_captions
from mixins import CSVSaveMixin

from .parser import youtube_transcript_data_parser

class YoutubeVideoBase:
    
    root_url = 'https://www.youtube.com/watch?v='
    
    re_language_code_str = '(?<=code=").{0,2}'
    
    def __init__(self, video_id, *args, **kwargs):
        self.yt = YouTube(self.root_url + video_id)
        self.re_dict = dict()
        self.return_data = {'downloaded_files' : dict(), 'transcript' : dict()}
        super(YoutubeVideoBase, self).__init__(*args, **kwargs)
    
    def download(self, directory, video = False, audio = False):
        
        # wipe previous download data and get new data
        self.return_data['downloaded_files'] = dict()
        
        if audio:
            audio_file_name = self.yt.streams.filter(
                adaptive = True
            ).filter(
                only_audio  = True
            ).order_by(
                "abr"
            ).desc().first().download(
                output_path = directory, filename_prefix = video_id
            )
            
            self.return_data['downloaded_files']['audio'] = audio_file_name
            
            
        if video:
            video_file_name = self.yt.streams.filter(
                adaptive = True
            ).filter(
                only_video  = True
            ).order_by(
                "resolution"
            ).desc().first().download(
                output_path = directory, filename_prefix = video_id
            )
            
            self.return_data['downloaded_files']['video'] = video_file_name
            
    def get_transcript(self, languages):
        dict_of_transcripts = dict()
        for ln in languages:
            if ln in self.re_dict:
                pass 
            else:
                self.re_dict[ln] = re.compile(self.re_language_code_str + str(ln))

            try:
                # if transcripts are availible in video, get them
                caption_list_ln = self.re_dict.get(ln).findall(str(self.yt.captions))
                if caption_list_ln:
                    for ln in caption_list_ln:
                        dict_of_transcripts[ln] = parse_xml_captions(
                                                self.yt.captions[ln].xml_captions
                                                )
                else:
                    print(Exception(f'No {ln} caption availible for {self.yt.video_id}'))
            except:
                print(Exception(f'No {ln} caption availible for {self.yt.video_id}'))
        
        self.return_data['transcript'] = dict_of_transcripts
        return self.return_data['transcript']


class YoutubeVideoModule(YoutubeVideoBase, CSVSaveMixin):
    
    _parser_function = youtube_transcript_data_parser
    
    def __init__(self, video_id, *args, **kwargs):
        super(YoutubeVideoModule, self).__init__(video_id, *args, **kwargs)

        
    def save_transcripts(self, languages, *args, **kwargs):
        if kwargs.get('third_party_speech_recognition', None):
            print('third party speech recognition not implemented')
            pass
        
        else:
            self.get_transcript(languages)
            self.save()
            
            
    
    
    
     