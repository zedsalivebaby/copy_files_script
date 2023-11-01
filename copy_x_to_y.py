# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:39:45 2019

@author: edundar
"""
import os, shutil
from pathlib import Path

#%% Fonction copiant des fichiers ou des dossiers
def copy_files_folders(f, src, dest, ls_exclude=''):
    
    # Identification de la classe de f
    if isinstance(f, list):
        ls = f
    elif isinstance(f, str):
        ls = [f]
    for f in ls:
        print(f)
        if f.name not in ls_exclude:
            src_f = src / f
            print(src_f)
            
            # Si src_f est un dossier
            if (os.path.isdir(src_f)):
                src_folder = src_f
                dest_folder = dest / src_folder.name
                
                #%% Logique de l'opération
                # Si le dossier existe, supprimer
                if (os.path.exists(dest_folder)):
                    try:
                        shutil.rmtree(dest_folder)
                    except PermissionError as e:
                        print(e)
                        continue
                # Copier le dossier src.name du répertoire
                # src dans le répertoire dest         
                try:
                    shutil.copytree(src_folder, dest_folder)
                except OSError as err:
                    print('Error: %s' % err)
                    continue
                
            # Si src_f est un fichier
            else:
                src_file = src_f
                dest_file = dest / src_file.name
                try:
                # si c'est un fichier au lieu d'être un dossier
                # on utilise la fonction copy2 au lieu de copytree
                    shutil.copy2(src_file, dest_file)
                except OSError as err:
                    print('Error: %s' % err)
                    continue
            
#%% Initialisation des répertoires
src_path = Path('E:/MSE2020')
dest_path = Path('D:/Nergica/Collineo_windfarms/test/MSE2020')

#%% Dossier, dossiers, fichier, fichiers ou liste à copier 
f = [f for f in src_path.iterdir()]
ls_exclude = ['MSE2020']

#%%  Appel de la fonction copy_files_folders  
copy_files_folders(f, src_path, dest_path, ls_exclude=ls_exclude)
