import PySimpleGUI as sg
import sys
import Downloader as ad
import get_name as gn




sg.theme('DarkAmber')

layout = [[sg.Text('Enter link'),sg.InputText()]]
layout.append([sg.Button("Download"), sg.CloseButton("Cancel")])
# layout.append([sg.Output(size=(65,20))])

window = sg.Window('Download your song', layout, finalize=True)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
            break
    url = values[0]
    if event == "Download":
        sg.popup('Your Song Name', gn.name_song(url))
        # sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
        # # print(values["inp"])
        ad.audio(url)
