# -*- coding: utf-8 -*-
from textwrap import dedent
from juicer.operation import Operation
from juicer.operation import ReportOperation
from juicer.scikit_learn.util import get_X_train_data
from juicer.scikit_learn.model_operation import AlgorithmOperation
from gettext import gettext


class ReadAudioFolderOperation(Operation):
    """
    Read Image Folder.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)

        self.folder_name = parameters.get('folder_name', 'None')

        self.has_code = True
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """

            import glob

            storage_folder = "/srv/storage/srv/storage/limonero/data/AudioOpsData/Raw/{folder_name}"
        
            files = []
            files_wav = glob.glob(storage_folder + "/*.wav")
            files_mp3 = glob.glob(storage_folder + "/*.mp3")
            files.extend(files_wav)
            files.extend(files_mp3)
            df = pd.DataFrame(files, columns =['audio'])

            {outp} = df
            
            #MPCE
            """ \
                .format(outp = self.output, 
                        folder_name = self.folder_name)
            return dedent(code)

class ReadEmbeddingFolderOperation(Operation):
    """
    Read Image Folder.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)

        self.folder_name = parameters.get('folder_name', 'None')

        self.has_code = True
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """

            import glob

            storage_folder = "/srv/storage/srv/storage/limonero/data/AudioOpsData/Embedded/{folder_name}"
        
            files = glob.glob(storage_folder + "/*.pt")
            df = pd.DataFrame(files, columns = ["encoding"])

            {outp} = df
            
            #MPCE
            """ \
                .format(outp = self.output, 
                        folder_name = self.folder_name)
            return dedent(code)

class ExtractAudioFeatureOperation(Operation):
    """
    Read Image Folder.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)

        self.input = self.named_inputs['input data']
        self.folder_name = parameters.get('folder_name', 'None')

        self.has_code = True
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """
            import os
            import torch
            import torchaudio
            from speechbrain.pretrained import SpeakerRecognition

            df = {inp}

            save_folder = "/srv/storage/srv/storage/limonero/data/AudioOpsData/Embedded/{folder_name}"

            df["encoding"] = df["audio"].apply(lambda x: save_folder + "/" + x.split("/")[-1].replace(".wav", ".pt"))

            verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", 
                                               savedir="/srv/storage/srv/storage/limonero/data/AudioOpsData/model")

            sample_rates = []

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            for idx, row in df.iterrows():
                signal, fs = torchaudio.load(row.audio)
                embedding = verification.encode_batch(signal)
                sample_rates.append(fs)
                torch.save(embedding, row.encoding)

            df["sample_rate"] = sample_rates
            
            {outp} = df

            #MPCE
            """ \
                .format(outp=self.output, inp=self.input, folder_name = self.folder_name)
            return dedent(code)


class SearchDatabaseOperation(Operation):
    """
    Read Image Folder.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)
        
        self.input_qry = self.named_inputs['query data']
        self.input_db = self.named_inputs['database data']
        self.has_code = True
        self.group = parameters.get('group', '0')
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """
            import torch
            from torch.nn import CosineSimilarity
            from collections import Counter

            cos = lambda x,y: CosineSimilarity(dim=2, eps=1e-6)(x,y).numpy()[0][0]

            database = {inp_db}
            database["PRESO_ID"] = database.encoding.apply(lambda x: x.split("/")[-1].split("_")[1])
            rows = []

            if {group}:
                rows_preso_df = []
                for preso in list(database.PRESO_ID.unique()):
                    sims = []
                    temp_df = database[database.PRESO_ID == preso]
                    for idx_i, row_i in {inp_qry}.iterrows():
                        query_tensor = torch.load(row_i.encoding)
                        for idx_j, row_j in temp_df.iterrows():
                            db_tensor = torch.load(row_j.encoding)
                            sim = cos(query_tensor, db_tensor)
                            sims.append(sim)
                    row_preso = dict()
                    row_preso["PRESO_ID"] = preso
                    row_preso["sim"] = np.mean(sims)
                    rows_preso_df.append(row_preso)
                match_df = pd.DataFrame(rows_preso_df)
                match_df = match_df.sort_values("sim", ascending = False).head(100)
                
                {outp} = match_df                

            else:
                for idx_i, row_i in {inp_qry}.iterrows():
                    query_tensor = torch.load(row_i.encoding)
                    matches = dict()
                    rows_preso_df = []
                    for preso in list(database.PRESO_ID.unique()):
                        temp_df = database[database.PRESO_ID == preso]
                        sims = []
                        for idx_j, row_j in temp_df.iterrows():
                            db_tensor = torch.load(row_j.encoding)
                            sim = cos(query_tensor, db_tensor)
                            sims.append(sim)
                        row_preso = dict()
                        row_preso["PRESO_ID"] = preso
                        row_preso["sim"] = np.mean(sims)
                        rows_preso_df.append(row_preso)

                    match_df = pd.DataFrame(rows_preso_df)
                    match_df = match_df.sort_values("sim", ascending = False)

                    row_i_match = dict()
                    row_i_match["query"] =  row_i.audio
                    count = 1

                    for idx , match in match_df.iterrows():
                        row_i_match["match " + str(count)] = match.PRESO_ID
                        row_i_match["match " + str(count) + " similaridade"] = np.round(match.sim,2)
                        count += 1
                        if count>30:
                            break

                    rows.append(row_i_match)
                        
                {outp} = pd.DataFrame(rows)
            
            #MPCE
            """ \
                .format(outp = self.output, inp_db=self.input_db, inp_qry = self.input_qry, group=self.group)
            return dedent(code)


class ProcessOperation(Operation):
    """
    Resample.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)
        
        self.input = self.named_inputs['input data']
        self.has_code = True
        self.resample = parameters.get('resample', '0')
        self.mono = parameters.get('mono', '0')
        self.convert = parameters.get('convert', '0')
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """
            import os
            from pydub import AudioSegment

            df = {inp}
            
            audio_files_final = []
            
            for idx, row in df.iterrows():
                dir_ = "/".join(row.audio.split('/')[:-1]) + "/processed/"

                if not os.path.exists(dir_):
                    os.makedirs(dir_)

                if row.audio.endswith(".mp3"):
                    if {convert}:   
                        output_file  =  dir_ + row.audio.split('/')[-1].replace('.mp3', '_processed.wav')
                    else:
                        output_file  =  dir_ + row.audio.split('/')[-1].replace('.mp3', '_processed.mp3')
                    sound_object = AudioSegment.from_mp3(row.audio)
            
                elif row.audio.endswith(".wav"):
                    if {convert}:   
                        output_file  =  dir_ + row.audio.split('/')[-1].replace('.wav', '_processed.wav')
                    else:
                        output_file  =  dir_ + row.audio.split('/')[-1].replace('.wav', '_processed.wav')
                    sound_object = AudioSegment.from_wav(row.audio)

                else:
                    continue

                if {resample}:
                    sound_object = sound_object.set_frame_rate(16000)
                if {mono}:
                    sound_object = sound_object.set_channels(1)

                file_type = output_file.split(".")[-1]
                sound_object.export(output_file, format=file_type)
                
                audio_files_final.append(output_file)

            df['audio'] =  audio_files_final

            {outp} = df

            #MPCE
            """ \
                .format(outp=self.output, inp=self.input, resample=self.resample, mono=self.mono, convert=self.convert)
            return dedent(code)

class DenoiseOperation(Operation):
    """
    Resample.
    Parameters: 
    """

    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters, named_inputs, named_outputs)
        
        self.input = self.named_inputs['input data']
        self.has_code = True
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        if self.has_code:
            code = """
            import os
            import glob
            import pandas as pd
            from denoiser.enhance import enhance

            df = {inp}
            
            #Sets the arguments
            class Args():
                def __init__(self, input, output):
                    self.noisy_dir = input
                    self.out_dir = output
                    self.model_path = None
                    self.dns32 = None
                    self.dns64 = None
                    self.master64 = None
                    self.device = "cpu"
                    self.noisy_json = None
                    self.sample_rate = 16000
                    self.num_workers = 1
                    self.streaming = None
                    self.dry = 0.
            
            #Gathers a list of unique audio folders
            audio_folders = list(set(["/".join(i.split('/')[:-1]) for i in df['audio'].tolist()]))

            #Creates list for final embeddings file paths
            final_emb = []

            for audio_folder in audio_folders:
                if "processed" in audio_folder:
                    #Avoids nested folders
                    denoised_folder = audio_folder.replace("processed","denoised")
                else:
                    #For in case it does not follows a pre process operation
                    denoised_folder = audio_folder + "/denoised/"

                if not os.path.exists(denoised_folder):
                    #Checks if folder exists
                    #Embeding generation is made per folder so the check is not per file
                    args = Args(audio_folder, denoised_folder)
                    enhance(args)
                
                #Add to the list of files
                enhanced_files = glob.glob(denoised_folder + "/*enhanced.wav")
                final_emb.extend(enhanced_files)

            {outp} = pd.DataFrame(final_emb, columns = ["audio"])

            #MPCE
            """ \
                .format(outp=self.output, inp=self.input)
            return dedent(code)