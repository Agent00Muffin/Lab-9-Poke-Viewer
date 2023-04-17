from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokémon Info Viewer")
# Additional window configuration
root.resizable(False, False)
# Add frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2,pady=(20, 10))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=(10, 20), pady=(10, 20))

# Add widgets to frames
# Populate widget in the top frame
lbl_name = ttk.Label(frm_top, text='Pokémon name:')
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    # get the Pokémon name entered by the user
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return

    # Get the pokemon info from the API
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        error_msg = f'Unable to fetch information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=error_msg, icon='error')
        return

    # check if pokemon has 2 types
    if len(poke_info['types']) == 2:
        type = poke_info['types'][0]['type']['name']+ ", " + poke_info['types'][1]['type']['name']
    else:
        type = poke_info['types'][0]['type']['name']

    # Populkate the info values
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} hg"
    lbl_type_value['text'] = f"{type}"

    # Populate the stats values
    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defense['value'] = poke_info['stats'][2]['base_stat']
    bar_S_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_S_defense['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

# Populate widget in the Info frame
# Height:
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, sticky=E)
lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1)
# Weight:
lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, sticky=E)
lbl_weight_value = ttk.Label(frm_btm_left, text='TBD')
lbl_weight_value.grid(row=1, column=1)
# Type:
lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, sticky=E)
lbl_type_value = ttk.Label(frm_btm_left, text='TBD')
lbl_type_value.grid(row=2, column=1)


# Populate widget in the stats frame
# Hp:
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1)
# Attack:
lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1)
# Defence:
lbl_defense = ttk.Label(frm_btm_right, text='Deffence:')
lbl_defense.grid(row=2, column=0, sticky=E)
bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1)
# Special Attack:
lbl_S_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_S_attack.grid(row=3, column=0, sticky=E)
bar_S_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_S_attack.grid(row=3, column=1)
# Special Defence:
lbl_S_defense = ttk.Label(frm_btm_right, text='Special Defence:')
lbl_S_defense.grid(row=3, column=0, sticky=E)
bar_S_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_S_defense.grid(row=3, column=1)
# Speed:
lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=4, column=0, sticky=E)
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=4, column=1)




# Loop until window is closed

root.mainloop()