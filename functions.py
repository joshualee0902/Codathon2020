from tkinter import *
from DNAToolkit import *
import random
from structures import *


rndDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

DNAStr = validateSeq(rndDNAStr)

sectionInt = 0
codonString = ''

# function for buttons with 2 or more functions


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def create_dna():
    frame = Tk()
    frame.title("Generate DNA")
    frame.geometry("700x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="Sequence: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(70, 250, font=(140), text='', anchor=NW)

    seqButton = Button(frame, text="GENERATE DNA", command=lambda: printer(DNAStr, canvas_1),
                       width=15, height=2, activebackground="#33B5E5")
    seqButton_window = canvas.create_window(
        255, 70, anchor='nw', window=seqButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def menu_frame():
    frame = Tk()
    frame.title("Function Menu")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()

    bg_1 = PhotoImage(file="grid.png")
    canvas.create_image(300, 200, image=bg_1)

    def desFrame():
        frame.destroy()

    seqlengthButton = Button(frame, text="SEQUENCE LENGTH", command=combine_funcs(desFrame, seqlength_frame),
                             width=15, height=2, activebackground="#33B5E5")
    seqlengthButton_window = canvas.create_window(
        40, 50, anchor='nw', window=seqlengthButton)

    nucfreqButton = Button(frame, text="NUCLEOTIDE FREQUENCY", command=combine_funcs(desFrame, nucfreq_frame),
                           width=20, height=2, activebackground="#33B5E5")
    nucfreqButton_window = canvas.create_window(
        225, 50, anchor='nw', window=nucfreqButton)

    transcriptionButton = Button(frame, text="DNA/RNA TRANSCRIPTION", command=combine_funcs(desFrame, transcription_frame),
                                 width=21, height=2, activebackground="#33B5E5")
    transcriptionButton_window = canvas.create_window(
        425, 50, anchor='nw', window=transcriptionButton)

    reverseButton = Button(frame, text="DNA + REVERSE COMPLEMENT", command=combine_funcs(desFrame, reverse_frame),
                           width=24, height=2, activebackground="#33B5E5")
    reverseButton_window = canvas.create_window(
        10, 180, anchor='nw', window=reverseButton)

    gc_contentButton = Button(frame, text="GC CONTENT", command=combine_funcs(desFrame, gc_content_frame),
                              width=15, height=2, activebackground="#33B5E5")
    gc_contentButton_window = canvas.create_window(
        245, 180, anchor='nw', window=gc_contentButton)

    gc_subButton = Button(frame, text="GC CONTENT IN SUBSECTION", command=combine_funcs(desFrame, gc_sub_frame),
                          width=22, height=2, activebackground="#33B5E5")
    gc_subButton_window = canvas.create_window(
        420, 180, anchor='nw', window=gc_subButton)

    aa_seqButton = Button(frame, text="AMINO ACID SEQUENCE", command=combine_funcs(desFrame, aa_seq_frame),
                          width=20, height=2, activebackground="#33B5E5")
    aa_seqButton_window = canvas.create_window(
        25, 315, anchor='nw', window=aa_seqButton)

    codonfreqButton = Button(frame, text="CODON FREQUENCY", command=combine_funcs(desFrame, codonfreq_frame),
                             width=16, height=2, activebackground="#33B5E5")
    codonfreqButton_window = canvas.create_window(
        240, 315, anchor='nw', window=codonfreqButton)

    reportButton = Button(frame, text="REPORT", command=combine_funcs(desFrame, report_frame),
                          width=15, height=2, activebackground="#33B5E5")
    reportButton_window = canvas.create_window(
        445, 315, anchor='nw', window=reportButton)

    frame.mainloop()


def seqlength_frame():
    frame = Tk()
    frame.title("Sequence Length")
    frame.geometry("600x400")
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="Sequence Length: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(140, 220, font=(140), text='', anchor=NW)

    seqlengthButton = Button(frame, text="PRINT", command=lambda: printer(str(len(DNAStr)), canvas_1),
                             width=15, height=2, activebackground="#33B5E5")
    seqlengthButton_window = canvas.create_window(
        255, 70, anchor='nw', window=seqlengthButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def nucfreq_frame():
    frame = Tk()
    frame.title("Nucleotide Frequency")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="Nucleotide Frequency: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(180, 220, font=(140), text='', anchor=NW)

    nucfreqButton = Button(frame, text="PRINT", command=lambda: printer(str(countNucFrequency(DNAStr)), canvas_1),
                           width=20, height=2, activebackground="#33B5E5")
    nucfreqButton_window = canvas.create_window(
        235, 70, anchor='nw', window=nucfreqButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def transcription_frame():
    frame = Tk()
    frame.title("DNA/RNA Transcription")
    frame.geometry("650x400")
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="DNA: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(50, 220, font=(
        120), text=DNAStr, anchor=NW)

    canvas.create_text(10, 260, font=(
        140), text="RNA: ", anchor=NW, width=200)
    canvas_2 = canvas.create_text(50, 260, font=(120), text='', anchor=NW)

    transcriptionButton = Button(frame, text="TRANSCRIBE DNA", command=lambda: printer(transcription(DNAStr), canvas_2),
                                 width=20, height=2, activebackground="#33B5E5")
    transcriptionButton_window = canvas.create_window(
        235, 70, anchor='nw', window=transcriptionButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def reverse_frame():
    frame = Tk()
    frame.title("DNA String + Reverse Complement")
    frame.geometry("750x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(13, 220, font=(
        140), text="5' ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(25, 220, font=(140), text='', anchor=NW)
    canvas.create_text(580, 220, font=(
        140), text=" 3' [Complement]", anchor=NW, width=200)

    canvas.create_text(13, 240, font=(
        140), text="3' ", anchor=NW, width=200)
    canvas_2 = canvas.create_text(25, 240, font=(140), text='', anchor=NW)
    canvas.create_text(580, 240, font=(
        140), text=" 5' [Rev. Complement]", anchor=NW, width=200)

    revButton = Button(frame, text="PRINT SEQUENCE", command=lambda: combine_funcs(printer(reverse_complement(DNAStr)[::-1], canvas_1), printer(reverse_complement(DNAStr), canvas_2)),
                       width=20, height=2, activebackground="#33B5E5")
    revButton_window = canvas.create_window(
        235, 70, anchor='nw', window=revButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def gc_content_frame():
    frame = Tk()
    frame.title("GC Content")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="GC Content of DNA: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(155, 220, font=(140), text='', anchor=NW)

    gc_contentButton = Button(frame, text="PRINT", command=lambda: printer(str(gc_content(DNAStr)), canvas_1),
                              width=20, height=2, activebackground="#33B5E5")
    gc_contentButton_window = canvas.create_window(
        235, 70, anchor='nw', window=gc_contentButton)

    canvas.create_text(174, 220, font=(
        140), text="%", anchor=NW, width=200)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def gc_sub_frame():
    frame = Tk()
    frame.title("GC Content in Subsection")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    sectionVar = IntVar()

    canvas.create_text(10, 50, font=(
        140), text="Subsection (int != 0): ", anchor=NW, width=200)
    sectionEntry = Entry(frame, textvariable=sectionVar).place(x=160, y=50)

    canvas.create_text(10, 220, font=(
        140), text="GC Content in Subsection (%): ", anchor=NW, width=230)
    canvas_1 = canvas.create_text(230, 220, font=(140), text='', anchor=NW)

    def assignValue(var):
        global sectionInt
        sectionInt = var.get()

    gc_subButton = Button(frame, text="CALCULATE", command=lambda: combine_funcs(printer(gc_content_subsec(DNAStr, sectionVar.get()), canvas_1), assignValue(sectionVar)),
                          width=20, height=2, activebackground="#33B5E5")
    gc_subButton_window = canvas.create_window(
        230, 120, anchor='nw', window=gc_subButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def aa_seq_frame():
    frame = Tk()
    frame.title("Aminoacids Sequence from DNA")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    canvas.create_text(10, 220, font=(
        140), text="Amino Acid Sequence: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(180, 220, font=(140), text='', anchor=NW)

    aaseqButton = Button(frame, text="PRINT", command=lambda: printer(translate_seq(DNAStr, 0), canvas_1),
                         width=20, height=2, activebackground="#33B5E5")
    aaseqButton_window = canvas.create_window(
        235, 70, anchor='nw', window=aaseqButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def codonfreq_frame():
    frame = Tk()
    frame.title("Codon Frequency")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def printer(string, canv, delta=300, delay=0):
        for x in range(len(string) + 1):
            s = string[:x]
            def new_text(s=s): return canvas.itemconfigure(canv, text=s)
            canvas.after(delay, new_text)
            delay += delta

    codonVar = StringVar()

    canvas.create_text(10, 50, font=(
        140), text="Codon (A, C, D, E, F, G, H, I , K, L, M, N, P, Q, R, S, T, V, W, Y, _): ", anchor=NW, width=200)
    codonEntry = Entry(frame, textvariable=codonVar).place(x=240, y=50)

    canvas.create_text(10, 220, font=(
        140), text="Codon Frequency: ", anchor=NW, width=200)
    canvas_1 = canvas.create_text(150, 220, font=(140), text='', anchor=NW)

    def assignValue(var):
        global codonString
        codonString = var.get()

    codonfreqButton = Button(frame, text="PRINT", command=lambda: combine_funcs(printer(str(codon_usage(DNAStr, codonVar.get())), canvas_1), assignValue(codonVar)),
                             width=20, height=2, activebackground="#33B5E5")
    codonfreqButton_window = canvas.create_window(
        240, 90, anchor='nw', window=codonfreqButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()


def report_frame():
    frame = Tk()
    frame.title("Nucleotide Frequency")
    frame.geometry("600x400")
    frame.resizable(0, 0)
    canvas = Canvas(frame, width=1400, height=700)
    canvas.pack()
    delta = 300
    delay = 0

    def writeFile(string):
        file = open('final_reoprt.txt', 'a+')
        file.write(string)
        file.close()

    canvas_1 = canvas.create_text(180, 220, font=(140), text='', anchor=NW)

    finalString = ("[1] + Sequence Length: " + str(len(DNAStr)) + "\n" + "[2] + Nucleotide Frequency: "
                   + str(countNucFrequency(DNAStr)) + "\n" +
                   "[3] + DNA/RNA Transcription: "
                   + transcription(DNAStr) + "\n" +
                   "[4] + DNA String + Reverse Complement:\n5' "
                   + DNAStr + " 3'" + "\n" +
                   "3' " + reverse_complement(DNAStr)[::-1]
                   + " 5' [Complement]" + "\n" + "5' " +
                   reverse_complement(DNAStr) +
                   " 3' [Rev. Complement]\n" + "[5] + GC Content: "
                   + str(gc_content(DNAStr)) + "%\n" +
                   "[6] + GC Content in Subsection (" + str(sectionInt) + "): " +
                   str(gc_content_subsec(DNAStr, sectionInt)) + "\n"
                   + "[7] + Aminoacids Sequence from DNA: " + str(translate_seq(DNAStr, 0)) + "\n" + "[8] + Codon frequency (" + codonString + "): " + str(codon_usage(DNAStr, codonString)) + "\n")

    reportButton = Button(frame, text="GENERATE REPORT", command=lambda: writeFile(finalString),
                          width=20, height=2, activebackground="#33B5E5")
    reportButton_window = canvas.create_window(
        235, 70, anchor='nw', window=reportButton)

    def desFrame():
        frame.destroy()

    menuButton = Button(frame, text="MENU", command=combine_funcs(desFrame, menu_frame),
                        width=15, height=2, activebackground="#33B5E5")
    menuButton_window = canvas.create_window(
        255, 350, anchor='nw', window=menuButton)

    frame.mainloop()
