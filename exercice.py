#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mido


NOTES_PER_OCTAVE = 12


def build_note_dictionaries(note_names, add_octave_no=True):
	C0_MIDI_NO = 12 
	def note(note_names, add_octave_no):
		n = 0
		i = 0
		lenNote = len(note_names)
		while True:
			i+=1
			if n == lenNote:
				n = 0
			if add_octave_no:
				yield f'{note_names[n]}{(i -1)//12}'
				n+=1
	
			else:
				yield f'{note_names[n]}'
				n+=1
	def MIDI(midi):
		i = midi
		while True:
			yield i
			i+=1
			if i == 95:
				break

	name_to_midi = dict(zip(note(note_names, add_octave_no), MIDI(C0_MIDI_NO)))	
	midi_to_name = dict(zip(MIDI(C0_MIDI_NO), note(note_names, add_octave_no)))
	
	return midi_to_name, name_to_midi

def build_print_note_name_callback(midi_to_name):
	build_note_dictionaries()
	pass

def build_print_chord_name_callback(chord_names_and_notes, name_to_midi):
	# Construire le dictionnaire d'assocations entre état des notes et accord joué.
	
	# Créez et retourner le callback
	pass


def main():
	PORT_MIDI = "UnPortMIDI 0"

	english_names = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
	solfeggio_names = ["Do", "Réb", "Ré", "Mib", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si"]

	midi_to_name_eng_8va, name_to_midi_eng_8va = build_note_dictionaries(english_names, True)
	midi_to_name_fr, name_to_midi_fr = build_note_dictionaries(solfeggio_names, False)
	print(midi_to_name_eng_8va[64])
	print(name_to_midi_eng_8va["C0"])
	print(midi_to_name_fr[61])
	print(midi_to_name_fr[73])
	print(name_to_midi_fr["Fa#"])

	input("Appuyez sur ENTER pour passer à l'étape suivante...")
	print("- - " * 30)
	
	midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, True)
	print_note_name = build_print_note_name_callback(midi_to_name)
	keyboard = mido.open_input(PORT_MIDI, callback=print_note_name)

	input("Affichage des noms de notes (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
	keyboard.close()

	print("- - " * 30)

	chord_names = {
		"Do majeur" : ("Do", "Mi", "Sol"),
		"Fa majeur" : ("Fa", "La", "Do"),
		"Sol majeur" : ("Sol", "Si", "Ré"),
	}
	
	midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, False)
	print_chord_name = build_print_chord_name_callback(chord_names, name_to_midi)
	keyboard = mido.open_input(PORT_MIDI, callback=print_chord_name)
	
	input("Affichage des noms d'accords (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
	keyboard.close()

if __name__ == "__main__":
	main()
